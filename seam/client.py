from typing import Any, Dict, Optional
from urllib.parse import urljoin
import niquests as requests
from importlib.metadata import version
from inspect import signature
from urllib3.util import Retry
import abc

from .constants import DEFAULT_TIMEOUT, LTS_VERSION
from .exceptions import (
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
)

SDK_HEADERS = {
    "seam-sdk-name": "seamapi/python",
    "seam-sdk-version": version("seam"),
    "seam-lts-version": LTS_VERSION,
}

DEFAULT_RETRIES = Retry()

NIQUESTS_TIMEOUT_DEFAULT = (
    signature(requests.Session.post).parameters["timeout"].default
)


class AbstractSeamHttpClient(abc.ABC):
    @abc.abstractmethod
    def __init__(self, base_url: str, auth_headers: Dict[str, str], **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def request(self, method: str, url: str, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_response(self, response: requests.Response):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_error_response(self, response: requests.Response, status_code: int):
        raise NotImplementedError


class SeamHttpClient(requests.Session, AbstractSeamHttpClient):
    def __init__(
        self,
        base_url: str,
        auth_headers: Dict[str, str],
        retries: Optional[Retry] = DEFAULT_RETRIES,
        timeout: Optional[float] = DEFAULT_TIMEOUT,
        niquests_options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        # niquests.Session mounts its adapters while initializing, so retries
        # must be passed through here. Assigning self.retries afterwards leaves
        # the mounted adapters on their default and the option has no effect.
        options = {
            "retries": DEFAULT_RETRIES if retries is None else retries,
            **kwargs,
            **(niquests_options or {}),
        }

        custom_headers = options.pop("headers", {})

        super().__init__(**options)

        self.base_url = base_url

        self.timeout = timeout

        headers = {**auth_headers, **custom_headers, **SDK_HEADERS}
        self.headers.update(headers)

    # request returns the decoded body rather than the Response that
    # niquests.Session promises, so the verb helpers routed through it have to
    # say so too. Without these overrides callers see the inherited Response
    # type and indexing the returned payload does not type check.
    def get(self, url, **kwargs) -> Any:
        return self.request("GET", url, **kwargs)

    # data and json are named rather than collected into *args because
    # Session.request takes params in the position Session.post gives data.
    def post(self, url, data=None, json=None, **kwargs) -> Any:
        return self.request("POST", url, data=data, json=json, **kwargs)

    def request(self, method, url, *args, **kwargs) -> Any:
        url = urljoin(self.base_url, url)

        if kwargs.get("timeout", NIQUESTS_TIMEOUT_DEFAULT) == NIQUESTS_TIMEOUT_DEFAULT:
            kwargs["timeout"] = self.timeout

        response = super().request(method, url, *args, **kwargs)

        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        # niquests types status_code as optional because a Response exists
        # before it has one. Anything reaching here has been received, so a
        # missing status is an error the SDK cannot classify itself.
        status_code = response.status_code

        if status_code is None:
            response.raise_for_status()
        elif not 200 <= status_code < 300:
            self._handle_error_response(response, status_code)

        if "application/json" in response.headers.get("content-type", ""):
            return response.json()

        return response.text

    def _handle_error_response(self, response: requests.Response, status_code: int):
        request_id = response.headers.get("seam-request-id")

        if status_code == 401:
            raise SeamHttpUnauthorizedError(request_id)

        if not is_api_error_response(response):
            response.raise_for_status()

        error = response.json().get("error", {})
        error_type = error.get("type", "unknown_error")
        error_message = error.get("message", "Unknown error")
        error_data = error.get("data", None)

        error_details = {
            "type": error_type,
            "message": error_message,
            "data": error_data,
        }

        if error_type == "invalid_input":
            raise SeamHttpInvalidInputError(error_details, status_code, request_id)

        raise SeamHttpApiError(error_details, status_code, request_id)


def is_api_error_response(response: requests.Response) -> bool:
    try:
        content_type = response.headers.get("content-type", "")

        if not isinstance(content_type, str) or not content_type.startswith(
            "application/json"
        ):
            return False

        data = response.json()
    except (ValueError, requests.exceptions.JSONDecodeError):
        return False

    if not isinstance(data, dict):
        return False

    error = data.get("error")

    if not isinstance(error, dict):
        return False

    if not isinstance(error.get("type"), str) or not isinstance(
        error.get("message"), str
    ):
        return False

    return True
