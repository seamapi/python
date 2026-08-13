import os
from typing import Optional

from .auth import (
    get_auth_headers,
    get_auth_headers_for_without_workspace_personal_access_token,
)
from .options import SeamInvalidOptionsError, get_endpoint


def parse_options(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
    endpoint: Optional[str] = None,
):
    api_key = api_key or get_api_key_from_env(personal_access_token)
    personal_access_token = personal_access_token or get_personal_access_token_from_env(
        api_key
    )
    workspace_id = workspace_id or os.getenv("SEAM_WORKSPACE_ID")

    auth_headers = get_auth_headers(
        api_key=api_key,
        personal_access_token=personal_access_token,
        workspace_id=workspace_id,
    )
    endpoint = get_endpoint(endpoint)

    return auth_headers, endpoint


def parse_without_workspace_options(
    personal_access_token: Optional[str] = None,
    endpoint: Optional[str] = None,
):
    personal_access_token = personal_access_token or os.getenv(
        "SEAM_PERSONAL_ACCESS_TOKEN"
    )

    if personal_access_token is None:
        raise SeamInvalidOptionsError(
            "Must specify a personal_access_token. "
            "Attempted reading configuration from the environment, "
            "but the environment variable SEAM_PERSONAL_ACCESS_TOKEN is not set."
        )

    auth_headers = get_auth_headers_for_without_workspace_personal_access_token(
        personal_access_token
    )
    endpoint = get_endpoint(endpoint)

    return auth_headers, endpoint


def get_api_key_from_env(personal_access_token: Optional[str]) -> Optional[str]:
    """Read the api_key from the environment.

    A personal access token passed as an option takes precedence over the
    environment, so the environment is not consulted when one is given.
    """

    if personal_access_token is not None:
        return None

    api_key = os.getenv("SEAM_API_KEY")

    if api_key is not None and os.getenv("SEAM_PERSONAL_ACCESS_TOKEN") is not None:
        raise SeamInvalidOptionsError(
            "Both SEAM_API_KEY and SEAM_PERSONAL_ACCESS_TOKEN environment variables "
            "are defined. Please use only one authentication method."
        )

    return api_key


def get_personal_access_token_from_env(api_key: Optional[str]) -> Optional[str]:
    """Read the personal_access_token from the environment.

    An api_key, whether passed as an option or read from the environment, takes
    precedence, so the environment is not consulted when one is set.
    """

    if api_key is not None:
        return None

    return os.getenv("SEAM_PERSONAL_ACCESS_TOKEN")
