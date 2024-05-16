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

        url = self._endpoint + path
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
