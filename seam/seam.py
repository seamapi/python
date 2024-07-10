from typing import Any, Optional, Union, Dict
from typing_extensions import Self

from .constants import LTS_VERSION
from .parse_options import parse_options
from .routes import Routes
from .models import AbstractSeam
from .client import SeamHttpClient


class Seam(AbstractSeam):
    """
    Main class for interacting with the Seam API.

    This class provides methods to authenticate and interact with various Seam API endpoints,
    including devices, access codes, action_attempts, and more.

    Attributes:
    ----------
        lts_version (str): The long-term support (LTS) version of the Seam Python SDK.
        defaults (Dict[str, Any]): Default settings for API requests.
        client (SeamHttpClient): The HTTP client used for making API requests.

    For more information about the Seam API, visit https://docs.seam.co/
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
    ):
        """
        Initialize a Seam client instance.

        This method sets up the Seam client with the provided authentication credentials and configuration options. It supports two authentication methods: API key or personal access token.

        Parameters:
        ----------
            api_key (Optional[str]): The API key for authenticating with Seam. Mutually exclusive with personal_access_token.
            personal_access_token (Optional[str]): A personal access token for authenticating with Seam. Mutually exclusive with api_key.
            workspace_id (Optional[str]): The ID of the workspace to interact with. Required when using a personal access token.
            endpoint (Optional[str]): The custom API endpoint URL. If not provided, the default Seam API endpoint will be used.
            wait_for_action_attempt (Optional[Union[bool, Dict[str, float]]]): Controls whether to wait for an action attempt to complete. Can be a boolean or a dictionary with 'timeout' and 'poll_interval' keys. Defaults to True.

        Raises:
        ------
            SeamInvalidOptionsError: If neither api_key nor personal_access_token is provided, or if workspace_id is missing when using a personal access token.
            SeamInvalidTokenError: If the provided API key or personal access token format is invalid.
            SeamHttpApiError: For general API errors, including unexpected server responses.
            SeamHttpUnauthorizedError: When the provided authentication credentials (api_key or personal_access_token) are invalid.
            SeamHttpInvalidInputError: When the API request contains invalid input data.
            SeamActionAttemptFailedError: When an action attempt fails to complete successfully (only when wait_for_action_attempt is enabled).
            SeamActionAttemptTimeoutError: When an action attempt exceeds the specified timeout duration (only when wait_for_action_attempt is enabled).

        Note:
        -----
            The authentication method (api_key or personal_access_token) is
            automatically determined based on which parameter is provided.
            If neither api_key nor personal_access_token is provided, the client
            will attempt to read the SEAM_API_KEY environment variable.
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

        self.client = SeamHttpClient(base_url=endpoint, auth_headers=auth_headers)

        Routes.__init__(self, client=self.client, defaults=defaults)

    @classmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
    ) -> Self:
        """
        Create a Seam instance using an API key.

        This class method is a convenience constructor for creating a Seam instance authenticated with an API key.

        Parameters:
        ----------
            api_key (str): The API key for authenticating with Seam. Mutually exclusive with personal_access_token.
            endpoint (Optional[str]): The custom API endpoint URL. If not provided, the default Seam API endpoint will be used.
            wait_for_action_attempt (Optional[Union[bool, Dict[str, float]]]): Controls whether to wait for an action attempt to complete. Can be a boolean or a dictionary with 'timeout' and 'poll_interval' keys. Defaults to True.

        Returns:
        --------
            Self: A new instance of the Seam class authenticated with the provided API key.

        Example:
        --------
            seam = Seam.from_api_key("your-api-key-here")
        """
        return cls(
            api_key, endpoint=endpoint, wait_for_action_attempt=wait_for_action_attempt
        )

    @classmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        workspace_id: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
    ) -> Self:
        """
        Create a Seam instance using a personal access token.

        This class method is a convenience constructor for creating a Seam
        instance authenticated with a personal access token.

        Parameters:
        ----------
            personal_access_token (str): The personal access token for authenticating with Seam.
            workspace_id (str): The ID of the workspace to interact with.
            endpoint (Optional[str]): The custom API endpoint URL. If not provided, the default Seam API endpoint will be used.
            wait_for_action_attempt (Optional[Union[bool, Dict[str, float]]]): Controls whether to wait for an action attempt to complete. Can be a boolean or a dictionary with 'timeout' and 'poll_interval' keys. Defaults to True.

        Returns:
        --------
            Self: A new instance of the Seam class authenticated with the provided personal access token.

        Example:
        --------
            seam = Seam.from_personal_access_token("your-token-here", "workspace-id")
        """
        return cls(
            personal_access_token=personal_access_token,
            workspace_id=workspace_id,
            endpoint=endpoint,
            wait_for_action_attempt=wait_for_action_attempt,
        )
