from typing import Optional
from seam.options import (
    SeamHttpInvalidOptionsError,
    is_seam_http_options_with_api_key,
    is_seam_http_options_with_personal_access_token,
)
from seam.token import (
    is_jwt,
    is_access_token,
    is_client_session_token,
    is_publishable_key,
    is_seam_token,
    TOKEN_PREFIX,
    ACCESS_TOKEN_PREFIX,
)


class SeamHttpInvalidTokenError(Exception):
    def __init__(self, message):
        super().__init__(f"SeamHttp received an invalid token: {message}")


def get_auth_headers(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
):
    if is_seam_http_options_with_api_key(
        api_key=api_key,
        personal_access_token=personal_access_token,
    ):
        return get_auth_headers_for_api_key(api_key)

    if is_seam_http_options_with_personal_access_token(
        personal_access_token=personal_access_token,
        api_key=api_key,
        workspace_id=workspace_id,
    ):
        return get_auth_headers_for_personal_access_token(
            personal_access_token, workspace_id
        )

    raise SeamHttpInvalidOptionsError(
        "Must specify an api_key or personal_access_token. "
        "Attempted reading configuration from the environment, "
        "but the environment variable SEAM_API_KEY is not set."
    )


def get_auth_headers_for_api_key(api_key: str) -> dict:
    if is_client_session_token(api_key):
        raise SeamHttpInvalidTokenError(
            "A Client Session Token cannot be used as an api_key"
        )

    if is_jwt(api_key):
        raise SeamHttpInvalidTokenError("A JWT cannot be used as an api_key")

    if is_access_token(api_key):
        raise SeamHttpInvalidTokenError("An Access Token cannot be used as an api_key")

    if is_publishable_key(api_key):
        raise SeamHttpInvalidTokenError(
            "A Publishable Key cannot be used as an api_key"
        )

    if not is_seam_token(api_key):
        raise SeamHttpInvalidTokenError(
            f"Unknown or invalid api_key format, expected token to start with {TOKEN_PREFIX}"
        )

    return {"authorization": f"Bearer {api_key}"}


def get_auth_headers_for_personal_access_token(
    personal_access_token: str, workspace_id: str
) -> dict:
    if is_jwt(personal_access_token):
        raise SeamHttpInvalidTokenError(
            "A JWT cannot be used as a personal_access_token"
        )

    if is_client_session_token(personal_access_token):
        raise SeamHttpInvalidTokenError(
            "A Client Session Token cannot be used as a personal_access_token"
        )

    if is_publishable_key(personal_access_token):
        raise SeamHttpInvalidTokenError(
            "A Publishable Key cannot be used as a personal_access_token"
        )

    if not is_access_token(personal_access_token):
        raise SeamHttpInvalidTokenError(
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
        raise SeamHttpInvalidTokenError(
            "A JWT cannot be used as a personal_access_token"
        )

    if is_client_session_token(personal_access_token):
        raise SeamHttpInvalidTokenError(
            "A Client Session Token cannot be used as a personal_access_token"
        )

    if is_publishable_key(personal_access_token):
        raise SeamHttpInvalidTokenError(
            "A Publishable Key cannot be used as a personal_access_token"
        )

    if not is_access_token(personal_access_token):
        raise SeamHttpInvalidTokenError(
            f"Unknown or invalid personal_access_token format, expected token to start with {ACCESS_TOKEN_PREFIX}"
        )

    return {
        "authorization": f"Bearer {personal_access_token}",
    }
