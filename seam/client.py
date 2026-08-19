from collections.abc import Mapping
from typing import Any, Dict, Optional
from importlib.metadata import version
import abc

import httpx
from httpx import Response
from httpx_retries import Retry, RetryTransport

from .constants import DEFAULT_TIMEOUT
from .exceptions import (
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
)
from .null import replace_null
from .strict_url_search_params_serializer import serialize_url_search_params

SDK_HEADERS = {
    "seam-sdk-name": "seamapi/python",
    "seam-sdk-version": version("seam"),
}

DEFAULT_RETRIES = Retry(
    total=2,
    allowed_methods=["GET", "HEAD", "OPTIONS", "PUT", "DELETE"],
    status_forcelist=[429, *range(500, 600)],
    backoff_factor=0.12,
    backoff_jitter=1 / 6,
)


class AbstractSeamHttpClient(abc.ABC):
    @abc.abstractmethod
    def __init__(self, base_url: str, auth_headers: Dict[str, str], **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def request(self, method: str, url: str, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_response(self, response: Response):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_error_response(self, response: Response):
        raise NotImplementedError


def _build_client_options(
    base_url: str,
    timeout: Optional[float],
    httpx_options: Optional[Dict[str, Any]],
    kwargs: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "base_url": base_url,
        "timeout": timeout,
        **kwargs,
        **(httpx_options or {}),
    }


class SeamHttpResponseHandler:
    def _handle_response(self, response: Response):
        if not 200 <= response.status_code < 300:
            self._handle_error_response(response)

        if "application/json" in response.headers.get("content-type", ""):
            return response.json()

        return response.text

    def _handle_error_response(self, response: Response):
        status_code = response.status_code
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
            error_details["validation_errors"] = error.get("validation_errors")
            raise SeamHttpInvalidInputError(error_details, status_code, request_id)

        raise SeamHttpApiError(error_details, status_code, request_id)


class SeamHttpClient(httpx.Client, SeamHttpResponseHandler, AbstractSeamHttpClient):
    def __init__(
        self,
        base_url: str,
        auth_headers: Dict[str, str],
        retries: Optional[Retry] = DEFAULT_RETRIES,
        timeout: Optional[float] = DEFAULT_TIMEOUT,
        httpx_options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        options = _build_client_options(base_url, timeout, httpx_options, kwargs)

        custom_headers = options.pop("headers", {})
        self._retry_policy = DEFAULT_RETRIES if retries is None else retries

        super().__init__(**options)

        headers = {**auth_headers, **custom_headers, **SDK_HEADERS}
        self.headers.update(headers)

    def _init_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        transport = super()._init_transport(*args, **kwargs)

        if kwargs.get("transport") is not None:
            return transport

        return RetryTransport(transport=transport, retry=self._retry_policy)

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.BaseTransport:
        transport = super()._init_proxy_transport(*args, **kwargs)
        return RetryTransport(transport=transport, retry=self._retry_policy)

    # request returns the decoded body rather than the Response that
    # httpx.Client promises, so the verb helpers routed through it have to
    # say so too. Without these overrides callers see the inherited Response
    # type and indexing the returned payload does not type check.
    def get(self, url, **kwargs) -> Any:
        return self.request("GET", url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> Any:
        return self.request("POST", url, data=data, json=json, **kwargs)

    def put(self, url, data=None, json=None, **kwargs) -> Any:
        return self.request("PUT", url, data=data, json=json, **kwargs)

    def patch(self, url, data=None, json=None, **kwargs) -> Any:
        return self.request("PATCH", url, data=data, json=json, **kwargs)

    def delete(self, url, json=None, **kwargs) -> Any:
        return self.request("DELETE", url, json=json, **kwargs)

    def request(self, method, url, *args, **kwargs) -> Any:
        if isinstance(kwargs.get("params"), Mapping):
            url = with_search_params(url, kwargs.pop("params"))

        if "json" in kwargs:
            kwargs["json"] = replace_null(kwargs["json"])

        response = super().request(method, url, *args, **kwargs)

        return self._handle_response(response)


class AsyncSeamHttpClient(
    httpx.AsyncClient, SeamHttpResponseHandler, AbstractSeamHttpClient
):
    def __init__(
        self,
        base_url: str,
        auth_headers: Dict[str, str],
        retries: Optional[Retry] = DEFAULT_RETRIES,
        timeout: Optional[float] = DEFAULT_TIMEOUT,
        httpx_options: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        options = _build_client_options(base_url, timeout, httpx_options, kwargs)

        custom_headers = options.pop("headers", {})
        self._retry_policy = DEFAULT_RETRIES if retries is None else retries

        super().__init__(**options)

        headers = {**auth_headers, **custom_headers, **SDK_HEADERS}
        self.headers.update(headers)

    def _init_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        transport = super()._init_transport(*args, **kwargs)

        if kwargs.get("transport") is not None:
            return transport

        return RetryTransport(transport=transport, retry=self._retry_policy)

    def _init_proxy_transport(self, *args, **kwargs) -> httpx.AsyncBaseTransport:
        transport = super()._init_proxy_transport(*args, **kwargs)
        return RetryTransport(transport=transport, retry=self._retry_policy)

    async def get(self, url, **kwargs) -> Any:
        return await self.request("GET", url, **kwargs)

    async def post(self, url, data=None, json=None, **kwargs) -> Any:
        return await self.request("POST", url, data=data, json=json, **kwargs)

    async def put(self, url, data=None, json=None, **kwargs) -> Any:
        return await self.request("PUT", url, data=data, json=json, **kwargs)

    async def patch(self, url, data=None, json=None, **kwargs) -> Any:
        return await self.request("PATCH", url, data=data, json=json, **kwargs)

    async def delete(self, url, json=None, **kwargs) -> Any:
        return await self.request("DELETE", url, json=json, **kwargs)

    async def request(self, method, url, *args, **kwargs) -> Any:
        if isinstance(kwargs.get("params"), Mapping):
            url = with_search_params(url, kwargs.pop("params"))

        if "json" in kwargs:
            kwargs["json"] = replace_null(kwargs["json"])

        response = await super().request(method, url, *args, **kwargs)

        return self._handle_response(response)


def with_search_params(url: Any, params: Mapping[str, Any]) -> Any:
    query = serialize_url_search_params(params)

    if not query:
        return url

    return httpx.URL(url, query=query.encode())


def is_api_error_response(response: Response) -> bool:
    try:
        content_type = response.headers.get("content-type", "")

        if not isinstance(content_type, str) or not content_type.startswith(
            "application/json"
        ):
            return False

        data = response.json()
    except ValueError:
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
