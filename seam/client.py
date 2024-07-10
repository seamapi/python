from typing import Dict, Optional
from urllib.parse import urljoin
import niquests as requests
from importlib.metadata import version
from urllib3.util import Retry

from .constants import LTS_VERSION
from .exceptions import (
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
)
from .models import AbstractSeamHttpClient

SDK_HEADERS = {
    "seam-sdk-name": "seamapi/python",
    "seam-sdk-version": version("seam"),
    "seam-lts-version": LTS_VERSION,
}

DEFAULT_RETRIES = Retry()


class SeamHttpClient(requests.Session, AbstractSeamHttpClient):
    def __init__(
        self,
        base_url: str,
        auth_headers: Dict[str, str],
        retries: Optional[Retry] = DEFAULT_RETRIES,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.base_url = base_url

        headers = {**auth_headers, **kwargs.get("headers", {}), **SDK_HEADERS}
        self.headers.update(headers)

        if retries:
            self.retries = retries

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        response = super().request(method, url, *args, **kwargs)

        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        if not 200 <= response.status_code < 300:
            self._handle_error_response(response)

        if "application/json" in response.headers.get("content-type", ""):
            return response.json()

        return response.text

    def _handle_error_response(self, response: requests.Response):
        status_code = response.status_code
        request_id = response.headers.get("seam-request-id")

        if status_code == 401:
            raise SeamHttpUnauthorizedError(request_id)

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
