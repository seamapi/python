import os

from .routes import Routes
import requests
from importlib.metadata import version
from typing import Optional, Union, Dict, cast
from .types import AbstractSeam, SeamApiException


class Seam(AbstractSeam):
    """
    Initial Seam class used to interact with Seam API
    """

    api_key: str
    api_url: str = "https://connect.getseam.com"
    lts_version: str = "1.0.0"

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        workspace_id: Optional[str] = None,
        api_url: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ):
        """
        Parameters
        ----------
        api_key : str, optional
          API key
        workspace_id : str, optional
          Workspace id
        api_url : str, optional
          API url
        """
        Routes.__init__(self)

        if api_key is None:
            api_key = os.environ.get("SEAM_API_KEY", None)
        if api_key is None:
            raise Exception(
                "SEAM_API_KEY not found in environment, and api_key not provided"
            )
        if workspace_id is None:
            workspace_id = os.environ.get("SEAM_WORKSPACE_ID", None)
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.lts_version = Seam.lts_version
        self.wait_for_action_attempt = wait_for_action_attempt

        if os.environ.get("SEAM_API_URL", None) is not None:
            print(
                "\n"
                "\033[93m"
                "Using the SEAM_API_URL environment variable is deprecated. "
                "Support will be removed in a later major version. Use SEAM_ENDPOINT instead."
                "\033[0m"
            )
        api_url = (
            os.environ.get("SEAM_API_URL", None)
            or os.environ.get("SEAM_ENDPOINT", None)
            or api_url
        )
        if api_url is not None:
            self.api_url = cast(str, api_url)

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

        url = self.api_url + path
        sdk_version = version("seam")
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "Python SDK v"
            + sdk_version
            + " (https://github.com/seamapi/python)",
            "seam-sdk-name": "seamapi/python",
            "seam-sdk-version": sdk_version,
            "seam-lts-version": self.lts_version,
        }
        if self.workspace_id is not None:
            headers["seam-workspace"] = self.workspace_id
        response = requests.request(method, url, headers=headers, **kwargs)

        if response.status_code != 200:
            raise SeamApiException(response)

        if "application/json" in response.headers["content-type"]:
            return response.json()

        return response.text
