import requests
from typing import Dict, Optional, Union
from importlib.metadata import version

from seam.constants import LTS_VERSION
from seam.types import AbstractSeam, SeamApiException
from .workspaces import Workspaces


class SeamMultiWorkspace(AbstractSeam):
    """
    Seam class used to interact with Seam API without being scoped to any specific workspace.
    """

    lts_version: str = LTS_VERSION

    def __init__(
        self,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ):
        """
        Parameters
        ----------
        personal_access_token : str, optional
          Personal access token.
        endpoint : str, optional
          The API endpoint to which the request should be sent.
        wait_for_action_attempt : bool or dict, optional
          Controls whether to wait for an action attempt to complete, either as a boolean or as a dictionary specifying `timeout` and `poll_interval`. Defaults to `False`.
        """

        self.lts_version = SeamMultiWorkspace.lts_version
        self.wait_for_action_attempt = wait_for_action_attempt
        self.__auth_headers = {"Authorization": f"Bearer {personal_access_token}"}
        self.__endpoint = ""  # get_endpoint()

        self._workspaces = Workspaces(seam=self)
        self.workspaces = self.WorkspacesProxy(self._workspaces)

    class WorkspacesProxy:
        """Proxy to expose only the 'create' and 'list' methods of Workspaces."""

        def __init__(self, workspaces):
            self._workspaces = workspaces

        def list(self, *args, **kwargs):
            return self._workspaces.list(*args, **kwargs)

        def create(self, data, *args, **kwargs):
            return self._workspaces.create(data, *args, **kwargs)

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
        """

        url = self.__endpoint + path
        sdk_version = version("seam")
        headers = {
            **self.__auth_headers,
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
