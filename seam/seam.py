from typing import Any, Optional, Union, Dict
from typing_extensions import Self
from urllib3.util.retry import Retry

from .constants import LTS_VERSION
from .parse_options import parse_options
from .routes import Routes
from .models import AbstractSeam
from .client import SeamHttpClient


class Seam(AbstractSeam):
    """
    Initial Seam class used to interact with Seam API
    """

    lts_version: str = LTS_VERSION
    defaults: Dict[str, Any]

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        personal_access_token: Optional[str] = None,
        workspace_id: Optional[str] = None,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
    ):
        """
        Parameters
        ----------
        api_key : str, optional
          API key.
        personal_access_token : str, optional
          Personal access token.
        workspace_id : str, optional
          Workspace id.
        endpoint : str, optional
          The API endpoint to which the request should be sent.
        wait_for_action_attempt : bool or dict, optional
          Controls whether to wait for an action attempt to complete, either as a boolean or as a dictionary specifying `timeout` and `poll_interval`. Defaults to `False`.
        retries : urllib3.util.Retry, optional
          Configuration for retry behavior on failed requests.
        """

        self.lts_version = Seam.lts_version
        self.wait_for_action_attempt = wait_for_action_attempt
        auth_headers, endpoint = parse_options(
            api_key=api_key,
            personal_access_token=personal_access_token,
            workspace_id=workspace_id,
            endpoint=endpoint,
        )
        defaults = {"wait_for_action_attempt": wait_for_action_attempt}

        self.client = SeamHttpClient(
            base_url=endpoint, auth_headers=auth_headers, retries=retries
        )

        Routes.__init__(self, client=self.client, defaults=defaults)

    @classmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
    ) -> Self:
        return cls(
            api_key,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
            retries=retries,
        )

    @classmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        workspace_id: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
    ) -> Self:
        return cls(
            personal_access_token=personal_access_token,
            workspace_id=workspace_id,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
            retries=retries,
        )
