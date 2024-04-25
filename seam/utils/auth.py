from typing import Optional
import re
from seam.utils.options import (
    SeamHttpInvalidOptionsError,
    is_seam_http_multi_workspace_options_with_personal_access_token,
    is_seam_http_options_with_api_key,
    is_seam_http_options_with_client_session_token,
    is_seam_http_multi_workspace_options_with_console_session_token,
    is_seam_http_options_with_console_session_token,
    is_seam_http_options_with_personal_access_token,
)
from seam.utils.token import (
    is_jwt,
    is_access_token,
    is_client_session_token,
    is_publishable_key,
    is_seam_token,
    publishable_key_token_prefix,
    token_prefix,
    client_session_token_prefix,
    jwt_prefix,
    access_token_prefix,
)


class SeamHttpInvalidTokenError(Exception):
    def __init__(self, message):
        super().__init__(f"SeamHttp received an invalid token: {message}")


def get_auth_headers(
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    publishable_key: Optional[str] = None,
    console_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
):
    if publishable_key:
        return get_auth_headers_for_publishable_key(publishable_key)

    if is_seam_http_options_with_api_key(
        api_key=api_key,
        client_session_token=client_session_token,
        console_session_token=console_session_token,
        personal_access_token=personal_access_token,
    ):
        return get_auth_headers_for_api_key(api_key)

    if is_seam_http_options_with_client_session_token(
        client_session_token=client_session_token,
        api_key=api_key,
        console_session_token=console_session_token,
        personal_access_token=personal_access_token,
    ):
        return get_auth_headers_for_client_session_token(client_session_token)

    if is_seam_http_multi_workspace_options_with_console_session_token(
        console_session_token=console_session_token,
        api_key=api_key,
        client_session_token=client_session_token,
        personal_access_token=personal_access_token,
    ) or is_seam_http_options_with_console_session_token(
        console_session_token=console_session_token,
        api_key=api_key,
        client_session_token=client_session_token,
        personal_access_token=personal_access_token,
        workspace_id=workspace_id,
    ):
        return get_auth_headers_for_console_session_token(
            console_session_token, workspace_id
        )

    if is_seam_http_multi_workspace_options_with_personal_access_token(
        personal_access_token=personal_access_token,
        api_key=api_key,
        client_session_token=client_session_token,
        console_session_token=console_session_token,
    ) or is_seam_http_options_with_personal_access_token(
        personal_access_token=personal_access_token,
        api_key=api_key,
        client_session_token=client_session_token,
        console_session_token=console_session_token,
        workspace_id=workspace_id,
    ):
        return get_auth_headers_for_personal_access_token(
            personal_access_token, workspace_id
        )

    raise SeamHttpInvalidOptionsError(
        "Must specify an api_key, client_session_token, publishable_key, console_session_token, "
        "or personal_access_token. Attempted reading configuration from the environment, "
        "but the environment variable SEAM_API_KEY is not set."
    )


def get_auth_headers_for_publishable_key(publishable_key: str) -> dict:
    if is_jwt(publishable_key):
        raise SeamHttpInvalidTokenError("A JWT cannot be used as a publishable_key")

    if is_access_token(publishable_key):
        raise SeamHttpInvalidTokenError(
            "An Access Token cannot be used as a publishable_key"
        )

    if is_client_session_token(publishable_key):
        raise SeamHttpInvalidTokenError(
            "A Client Session Token Key cannot be used as a publishable_key"
        )

    if not is_publishable_key(publishable_key):
        raise SeamHttpInvalidTokenError(
            f"Unknown or invalid publishable_key format, expected token to start with {publishable_key_token_prefix}"
        )

    return {"seam-publishable-key": publishable_key}


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
            f"Unknown or invalid api_key format, expected token to start with {token_prefix}"
        )

    return {"authorization": f"Bearer {api_key}"}


def get_auth_headers_for_client_session_token(client_session_token: str) -> dict:
    if is_jwt(client_session_token):
        raise SeamHttpInvalidTokenError(
            "A JWT cannot be used as a client_session_token"
        )

    if is_access_token(client_session_token):
        raise SeamHttpInvalidTokenError(
            "An Access Token cannot be used as a client_session_token"
        )

    if is_publishable_key(client_session_token):
        raise SeamHttpInvalidTokenError(
            "A Publishable Key cannot be used as a client_session_token"
        )

    if not is_client_session_token(client_session_token):
        raise SeamHttpInvalidTokenError(
            f"Unknown or invalid client_session_token format, expected token to start with {client_session_token_prefix}"
        )

    return {
        "authorization": f"Bearer {client_session_token}",
        "client-session-token": client_session_token,
    }


def get_auth_headers_for_console_session_token(
    console_session_token: str, workspace_id: Optional[str] = None
) -> dict:
    if is_access_token(console_session_token):
        raise SeamHttpInvalidTokenError(
            "An Access Token cannot be used as a console_session_token"
        )

    if is_client_session_token(console_session_token):
        raise SeamHttpInvalidTokenError(
            "A Client Session Token cannot be used as a console_session_token"
        )

    if is_publishable_key(console_session_token):
        raise SeamHttpInvalidTokenError(
            "A Publishable Key cannot be used as a console_session_token"
        )

    if not is_jwt(console_session_token):
        raise SeamHttpInvalidTokenError(
            f"Unknown or invalid console_session_token format, expected a JWT which starts with {jwt_prefix}"
        )

    headers = {"authorization": f"Bearer {console_session_token}"}
    if workspace_id is not None:
        headers["seam-workspace"] = workspace_id

    return headers


def get_auth_headers_for_personal_access_token(
    personal_access_token: str, workspace_id: Optional[str] = None
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
            f"Unknown or invalid personal_access_token format, expected token to start with {access_token_prefix}"
        )

    headers = {"authorization": f"Bearer {personal_access_token}"}
    if workspace_id is not None:
        headers["seam-workspace"] = workspace_id

    return headers


def warn_on_insecure_user_identifier_key(user_identifier_key: str):
    if is_email(user_identifier_key):
        warning_message = (
            "\033[93m"
            "Using an email for the userIdentifierKey is insecure and may return an error in the future!\n"
            "This is insecure because an email is common knowledge or easily guessed.\n"
            "Use something with sufficient entropy known only to the owner of the client session.\n"
            "For help choosing a user identifier key see "
            "https://docs.seam.co/latest/seam-components/overview/get-started-with-client-side-components#3-select-a-user-identifier-key"
            "\033[0m"
        )
        print(warning_message)


def is_email(value: str) -> bool:
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", value) is not None
