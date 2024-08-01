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
    Seam class used to interact with Seam API without being scoped to a specific workspace.

    This class provides methods to authenticate and interact with Seam API endpoints
    that can operate without being tied to a specific workspace. It supports operations such as creating and listing workspaces.

    :cvar lts_version: The long-term support (LTS) version of the Seam
        Python SDK
    :vartype lts_version: str
    :ivar wait_for_action_attempt: Controls whether to wait for an action
        attempt to complete
    :vartype wait_for_action_attempt: Union[bool, Dict[str, float]]
    :ivar client: The HTTP client used for making API requests
    :vartype client: SeamHttpClient
    :ivar workspaces: Proxy to access workspace-related operations
    :vartype workspaces: WorkspacesProxy
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
        Initialize a SeamMultiWorkspace client instance.

        This method sets up the SeamMultiWorkspace client with the provided personal access token
        and configuration options.

        :param personal_access_token: A personal access token for
            authenticating with Seam
        :type personal_access_token: str
        :param endpoint: The custom API endpoint URL. If not provided,
            the default Seam API endpoint will be used
        :type endpoint: Optional[str]
        :param wait_for_action_attempt: Controls whether to wait for an
            action attempt to complete. Can be a boolean or a dictionary with
            'timeout' and 'poll_interval' keys
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]
        :param retries: Configuration for retry behavior on failed requests
        :type retries: Optional[urllib3.util.Retry]

        :raises SeamInvalidTokenError: If the provided personal access token format is invalid
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
        """
        Create a SeamMultiWorkspace instance using a personal access token.

        This class method is a convenience constructor for creating a SeamMultiWorkspace instance
        authenticated with a personal access token.

        :param personal_access_token: The personal access token for authenticating with Seam
        :type personal_access_token: str
        :param endpoint: The custom API endpoint URL. If not provided, the default Seam API endpoint will be used
        :type endpoint: Optional[str]
        :param wait_for_action_attempt: Controls whether to wait for an
            action attempt to complete. Can be a boolean or a dictionary with
            'timeout' and 'poll_interval' keys
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]
        :param retries: Configuration for retry behavior on failed requests
        :type retries: Optional[urllib3.util.Retry]
        :return: A new instance of the SeamMultiWorkspace class
            authenticated with the provided personal access token
        :rtype: Self

        :Example:

        >>> seam = SeamMultiWorkspace.from_personal_access_token("your-personal-access-token-here")
        """

        return cls(
            personal_access_token=personal_access_token,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
            retries=retries,
        )
