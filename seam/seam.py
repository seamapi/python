import os

from .routes import Routes
import requests
from importlib.metadata import version
from typing import Optional, Union, Dict, cast
from typing_extensions import Self
from seam.utils.auth import get_auth_headers, warn_on_insecure_user_identifier_key
from seam.utils.parse_options import get_api_key_from_env, get_endpoint_from_env
from .routes import Routes
from .types import AbstractSeam, SeamApiException


DEFAULT_ENDPOINT = "https://connect.getseam.com"


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
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ):
        """
        Parameters
        ----------
        api_key : str, optional
          API key
        workspace_id : str, optional
          Workspace id.
        endpoint : str, optional
          The API endpoint to which the request should be sent.
        wait_for_action_attempt : bool or dict, optional
          Controls whether to wait for an action attempt to complete, either as a boolean or as a dictionary specifying `timeout` and `poll_interval`. Defaults to `False`.
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
        endpoint = endpoint or get_endpoint_from_env() or DEFAULT_ENDPOINT
        if endpoint is not None:
            self.endpoint = cast(str, endpoint)

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
