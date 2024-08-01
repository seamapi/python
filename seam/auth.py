from typing import Optional
from .options import (
    SeamInvalidOptionsError,
    is_seam_options_with_api_key,
    is_seam_options_with_personal_access_token,
)
from .token import (
    is_jwt,
    is_access_token,
    is_client_session_token,
    is_publishable_key,
    is_seam_token,
    TOKEN_PREFIX,
    ACCESS_TOKEN_PREFIX,
)


class SeamInvalidTokenError(Exception):
    """
    Exception raised when an invalid token is provided to the Seam client.

    This error occurs when a token of incorrect type or format is used for
    authentication. It can be raised in various scenarios, such as using a
    client session token as an API key, or providing a token with an incorrect
    prefix.
    """

    def __init__(self, message):
        """
        :param message: Detailed description of the invalid token
        :type message: str
        """

        super().__init__(f"Seam received an invalid token: {message}")


def get_auth_headers(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
):
    if is_seam_options_with_api_key(
        api_key=api_key,
        personal_access_token=personal_access_token,
    ):
        return get_auth_headers_for_api_key(api_key)

    if is_seam_options_with_personal_access_token(
        personal_access_token=personal_access_token,
        api_key=api_key,
        workspace_id=workspace_id,
    ):
        return get_auth_headers_for_personal_access_token(
            personal_access_token, workspace_id
        )

    raise SeamInvalidOptionsError(
        "Must specify an api_key or personal_access_token. "
        "Attempted reading configuration from the environment, "
        "but the environment variable SEAM_API_KEY is not set."
    )


def get_auth_headers_for_api_key(api_key: str) -> dict:
    if is_client_session_token(api_key):
        raise SeamInvalidTokenError(
            "A Client Session Token cannot be used as an api_key"
        )

    if is_jwt(api_key):
        raise SeamInvalidTokenError("A JWT cannot be used as an api_key")

    if is_access_token(api_key):
        raise SeamInvalidTokenError("An Access Token cannot be used as an api_key")

    if is_publishable_key(api_key):
        raise SeamInvalidTokenError("A Publishable Key cannot be used as an api_key")

    if not is_seam_token(api_key):
        raise SeamInvalidTokenError(
            f"Unknown or invalid api_key format, expected token to start with {TOKEN_PREFIX}"
        )

    return {"authorization": f"Bearer {api_key}"}


def get_auth_headers_for_personal_access_token(
    personal_access_token: str, workspace_id: str
) -> dict:
    if is_jwt(personal_access_token):
        raise SeamInvalidTokenError("A JWT cannot be used as a personal_access_token")

    if is_client_session_token(personal_access_token):
        raise SeamInvalidTokenError(
            "A Client Session Token cannot be used as a personal_access_token"
        )

    if is_publishable_key(personal_access_token):
        raise SeamInvalidTokenError(
            "A Publishable Key cannot be used as a personal_access_token"
        )

    if not is_access_token(personal_access_token):
        raise SeamInvalidTokenError(
            f"Unknown or invalid personal_access_token format, expected token to start with {ACCESS_TOKEN_PREFIX}"
        )

    return {
        "authorization": f"Bearer {personal_access_token}",
        "seam-workspace": workspace_id,
    }


def get_auth_headers_for_multi_workspace_personal_access_token(
    personal_access_token: str,
) -> dict:
    if is_jwt(personal_access_token):
        raise SeamInvalidTokenError("A JWT cannot be used as a personal_access_token")

    if is_client_session_token(personal_access_token):
        raise SeamInvalidTokenError(
            "A Client Session Token cannot be used as a personal_access_token"
        )

    if is_publishable_key(personal_access_token):
        raise SeamInvalidTokenError(
            "A Publishable Key cannot be used as a personal_access_token"
        )

    if not is_access_token(personal_access_token):
        raise SeamInvalidTokenError(
            f"Unknown or invalid personal_access_token format, expected token to start with {ACCESS_TOKEN_PREFIX}"
        )

    return {
        "authorization": f"Bearer {personal_access_token}",
    }
