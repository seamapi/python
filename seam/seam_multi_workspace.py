from typing import Any, Dict, Optional, Union
import niquests as requests
from typing_extensions import Self

from .auth import get_auth_headers_for_multi_workspace_personal_access_token
from .constants import LTS_VERSION
from .options import get_endpoint
from .request import SeamHttpClient
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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
        client: Optional[requests.Session] = None,
        client_options: Optional[Dict[str, Any]] = None,
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
        client : requests.Session, optional
          A pre-configured requests session to be used for making HTTP requests. If not provided, a new `SeamHttpClient` instance will be created using the `client_options` and other relevant parameters.
        client_options : dict, optional
          A dictionary of options that will be passed to the `SeamHttpClient` constructor when initializing a new requests session client. This allows for customization of the HTTP client, such as setting additional headers or configuring timeouts. For detailed information on available options, refer to the niquests library [repo](https://github.com/jawah/niquests). If client is provided, this parameter will be ignored.
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
        )

        if client_options is None:
            client_options = {}

        self.client = client or SeamHttpClient(
            base_url=endpoint, auth_headers=auth_headers, **client_options
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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ) -> Self:
        return cls(
            personal_access_token=personal_access_token,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
        )
