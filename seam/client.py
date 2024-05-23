from typing import Dict
from urllib.parse import urljoin
import niquests as requests
from importlib.metadata import version

from .constants import LTS_VERSION
from .exceptions import SeamHttpApiError
from .models import AbstractSeamHttpClient

SDK_HEADERS = {
    "seam-sdk-name": "seamapi/python",
    "seam-sdk-version": version("seam"),
    "seam-lts-version": LTS_VERSION,
}


class SeamHttpClient(requests.Session, AbstractSeamHttpClient):
    def __init__(self, base_url: str, auth_headers: Dict[str, str], **kwargs):
        super().__init__(**kwargs)

        self.base_url = base_url
        headers = {**auth_headers, **kwargs.get("headers", {}), **SDK_HEADERS}

        self.headers.update(headers)

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.base_url, url)
        response = super().request(method, url, *args, **kwargs)

        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        if response.status_code != 200:
            raise SeamHttpApiError(response)

        if "application/json" in response.headers["content-type"]:
            return response.json()

        return response.text
