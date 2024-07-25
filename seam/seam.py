from typing import Any, Optional, Union, Dict
from typing_extensions import Self
from urllib3.util.retry import Retry

from .constants import LTS_VERSION
from .parse_options import parse_options
from .routes import Routes
from .models import AbstractSeam
from .client import SeamHttpClient


class Seam(AbstractSeam):
    """Main class for interacting with the Seam API.

    This class provides methods to authenticate and interact with various
    Seam API endpoints,
    including devices, access codes, action_attempts, and more. It supports authentication via API key or personal access token.

    :cvar lts_version: The long-term support (LTS) version of the Seam
        Python SDK
    :vartype lts_version: str
    :ivar defaults: Default settings for API requests
    :vartype defaults: Dict[str, Any]
    :ivar client: The HTTP client used for making API requests
    :vartype client: SeamHttpClient
    :ivar wait_for_action_attempt: Controls whether to wait for an action
        attempt to complete
    :vartype wait_for_action_attempt: Union[bool, Dict[str, float]]

    For more information about the Seam API, visit https://docs.seam.co/
    """

    lts_version: str = LTS_VERSION

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
        """Initialize a Seam client instance.

        This method sets up the Seam client with the provided authentication credentials and configuration options.
        It supports two authentication methods: API key or personal access token.

        :param api_key: The API key for authenticating with Seam. Mutually
            exclusive with personal_access_token
        :type api_key: Optional[str]
        :param personal_access_token: A personal access token for
            authenticating with Seam. Mutually exclusive with api_key
        :type personal_access_token: Optional[str]
        :param workspace_id: The ID of the workspace to interact with.
            Required when using a personal access token
        :type workspace_id: Optional[str]
        :param endpoint: The custom API endpoint URL. If not provided, the
            default Seam API endpoint will be used
        :type endpoint: Optional[str]
        :param wait_for_action_attempt: Controls whether to wait for an
            action attempt to complete. Can be a boolean or a dictionary with
            'timeout' and 'poll_interval' keys
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]
        :param retries: Configuration for retry behavior on failed requests
        :type retries: Optional[urllib3.util.Retry]

        :raises SeamInvalidOptionsError: If neither api_key nor
            personal_access_token is provided, or if workspace_id is missing
            when using a personal access token
        :raises SeamInvalidTokenError: If the provided API key or personal
            access token format is invalid
        """

        self.lts_version = Seam.lts_version
        self.wait_for_action_attempt = wait_for_action_attempt
        auth_headers, endpoint = parse_options(
            api_key=api_key,
            personal_access_token=personal_access_token,
            workspace_id=workspace_id,
            endpoint=endpoint,
        )
        self.defaults = {"wait_for_action_attempt": wait_for_action_attempt}

        self.client = SeamHttpClient(
            base_url=endpoint, auth_headers=auth_headers, retries=retries
        )

        Routes.__init__(self, client=self.client, defaults=self.defaults)

    @classmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
        retries: Optional[Retry] = None,
    ) -> Self:
        """Create a Seam instance using an API key.

        This class method is a convenience constructor for creating a Seam instance authenticated with an API key.

        :param api_key: The API key for authenticating with Seam. Mutually
            exclusive with personal_access_token
        :type api_key: str
        :param endpoint: The custom API endpoint URL. If not provided, the
            default Seam API endpoint will be used
        :type endpoint: Optional[str]
        :param wait_for_action_attempt: Controls whether to wait for an
            action attempt to complete. Can be a boolean or a dictionary with
            'timeout' and 'poll_interval' keys
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]
        :return: A new instance of the Seam class authenticated with the
            provided API key
        :rtype: Self

        :Example:

        >>> seam = Seam.from_api_key("your-api-key-here")
        """
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
        """Create a Seam instance using a personal access token.

        This class method is a convenience constructor for creating a Seam
        instance authenticated with a personal access token.

        :param personal_access_token: The personal access token for
            authenticating with Seam
        :type personal_access_token: str
        :param workspace_id: The ID of the workspace to interact with
        :type workspace_id: str
        :param endpoint: The custom API endpoint URL. If not provided, the
            default Seam API endpoint will be used
        :type endpoint: Optional[str]
        :param wait_for_action_attempt: Controls whether to wait for an
            action attempt to complete. Can be a boolean or a dictionary with
            'timeout' and 'poll_interval' keys
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]
        :return: A new instance of the Seam class authenticated with the
            provided personal access token
        :rtype: Self

        :Example:

        >>> seam = Seam.from_personal_access_token("your-token-here", "workspace-id")
        """
        return cls(
            personal_access_token=personal_access_token,
            workspace_id=workspace_id,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
            retries=retries,
        )
