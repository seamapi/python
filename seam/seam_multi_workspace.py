from typing import Dict, Optional, Union
from typing_extensions import Self

from seam.auth import get_auth_headers_for_multi_workspace_personal_access_token
from seam.constants import LTS_VERSION
from seam.options import get_endpoint
from seam.request import RequestMixin
from seam.types import AbstractSeamMultiWorkspace
from seam.workspaces import Workspaces


class SeamMultiWorkspace(AbstractSeamMultiWorkspace, RequestMixin):
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
        self._auth_headers = get_auth_headers_for_multi_workspace_personal_access_token(
            personal_access_token
        )
        self._endpoint = get_endpoint(endpoint)

        self._workspaces = Workspaces(seam=self)
        self.workspaces = self.WorkspacesProxy(self._workspaces)

    class WorkspacesProxy:
        """Proxy to expose only the 'create' and 'list' methods of Workspaces."""

        def __init__(self, workspaces):
            self._workspaces = workspaces

        def list(self, **kwargs):
            return self._workspaces.list(**kwargs)

        def create(self, **kwargs):
            return self._workspaces.create(**kwargs)

    @classmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ) -> Self:
        return cls(
            personal_access_token=personal_access_token,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
        )
