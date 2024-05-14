from typing import Dict
import requests
from importlib.metadata import version

from seam.types import AbstractRequestMixin, SeamApiException


class RequestMixin(AbstractRequestMixin):
    def make_request(self, method: str, path: str, **kwargs):
        """
        Makes a request to the API

        Parameters
        ----------
        method : str
          Request method
        path : str
          Request path
        **kwargs
          Keyword arguments passed to requests.request

        Raises
        ------
        SeamApiException: If the response status code is not successful.
        """

        url = self.endpoint + path
        sdk_version = version("seam")
        headers = {
            **self._auth_headers,
            "Content-Type": "application/json",
            "User-Agent": "Python SDK v"
            + sdk_version
            + " (https://github.com/seamapi/python-next)",
            "seam-sdk-name": "seamapi/python",
            "seam-sdk-version": sdk_version,
            "seam-lts-version": self.lts_version,
        }

        response = requests.request(method, url, headers=headers, **kwargs)

        if response.status_code != 200:
            raise SeamApiException(response)

        if "application/json" in response.headers["content-type"]:
            return response.json()

        return response.text


class HttpRequester:
    def __init__(self, headers: Dict[str, str], **kwargs):
        self.session = requests.Session()
        self.session.headers.update(headers)

        for key, value in kwargs.items():
            setattr(self.session, key, value)

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        return self._handle_response(response)

    def post(self, url, data=None, json=None, **kwargs):
        response = self.session.post(url, data=data, json=json, **kwargs)
        return self._handle_response(response)

    def put(self, url, data=None, **kwargs):
        response = self.session.put(url, data=data, **kwargs)
        return self._handle_response(response)

    def delete(self, url, **kwargs):
        response = self.session.delete(url, **kwargs)
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        if response.status_code != 200:
            raise SeamApiException(response)

        if "application/json" in response.headers["content-type"]:
            return response.json()

        return response.text
