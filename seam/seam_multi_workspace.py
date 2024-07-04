from typing import Any, Dict, Optional, Union
import niquests as requests
from typing_extensions import Self
from urllib3.util import Retry

from .auth import get_auth_headers_for_multi_workspace_personal_access_token
from .constants import LTS_VERSION
from .options import get_endpoint
from .client import SeamHttpClient
from .models import AbstractSeamMultiWorkspace
from .routes.workspaces import Workspaces


class WorkspacesProxy:
    """Proxy to expose only the 'create' and 'list' methods of Workspaces."""

    def __init__(self, workspaces):
        self._workspaces = workspaces

    def list(self, **kwargs):
        return self._workspaces.list(**kwargs)

    def create(self, **kwargs):
        return self._workspaces.create(**kwargs)


class SeamMultiWorkspace(AbstractSeamMultiWorkspace):
    """
    Seam class used to interact with Seam API without being scoped to any specific workspace.
    """

    lts_version: str = LTS_VERSION

    def __init__(
        self,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
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
        retries : urllib3.util.Retry, optional
          Configuration for retry behavior on failed requests.
        """

        self.lts_version = SeamMultiWorkspace.lts_version
        self.wait_for_action_attempt = wait_for_action_attempt
        auth_headers = get_auth_headers_for_multi_workspace_personal_access_token(
            personal_access_token
        )
        endpoint = get_endpoint(endpoint)

        self.client = SeamHttpClient(
            base_url=endpoint,
            auth_headers=auth_headers,
            retries=retries,
        )

        defaults = {"wait_for_action_attempt": wait_for_action_attempt}

        self._workspaces = Workspaces(client=self.client, defaults=defaults)
        self.workspaces = WorkspacesProxy(self._workspaces)

    @classmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
    ) -> Self:
        return cls(
            personal_access_token=personal_access_token,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
            retries=retries,
        )
