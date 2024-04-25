from typing import Optional

class SeamHttpInvalidOptionsError(Exception):
    def __init__(self, message):
        super().__init__(f"SeamHttp received invalid options: {message}")

def is_seam_http_options_with_api_key(
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    console_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None,
) -> bool:
    if api_key is None:
        return False

    if client_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            "The client_session_token option cannot be used with the api_key option"
        )

    if console_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            "The console_session_token option cannot be used with the api_key option"
        )

    if personal_access_token is not None:
        raise SeamHttpInvalidOptionsError(
            "The personal_access_token option cannot be used with the api_key option"
        )

    return True

def is_seam_http_options_with_client_session_token(
    client_session_token: Optional[str] = None,
    api_key: Optional[str] = None,
    console_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None
) -> bool:
    if client_session_token is None:
        return False

    if api_key is not None:
        raise SeamHttpInvalidOptionsError(
            'The api_key option cannot be used with the client_session_token option'
        )

    if console_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The console_session_token option cannot be used with the client_session_token option'
        )

    if personal_access_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The personal_access_token option cannot be used with the client_session_token option'
        )

    return True

def is_seam_http_multi_workspace_options_with_console_session_token(
    console_session_token: Optional[str] = None,
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None
) -> bool:
    if console_session_token is None:
        return False

    if api_key is not None:
        raise SeamHttpInvalidOptionsError(
            'The api_key option cannot be used with the console_session_token option'
        )

    if client_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The client_session_token option cannot be used with the console_session_token option'
        )

    if personal_access_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The personal_access_token option cannot be used with the console_session_token option'
        )

    return True

def is_seam_http_options_with_console_session_token(
    console_session_token: Optional[str] = None,
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None
) -> bool:
    if not is_seam_http_multi_workspace_options_with_console_session_token(
        console_session_token=console_session_token,
        api_key=api_key,
        client_session_token=client_session_token,
        personal_access_token=personal_access_token
    ):
        return False

    if workspace_id is None:
        raise SeamHttpInvalidOptionsError(
            'Must pass a workspace_id when using a console_session_token'
        )

    return True

def is_seam_http_multi_workspace_options_with_personal_access_token(
    personal_access_token: Optional[str] = None,
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    console_session_token: Optional[str] = None
) -> bool:
    if personal_access_token is None:
        return False

    if api_key is not None:
        raise SeamHttpInvalidOptionsError(
            'The api_key option cannot be used with the personal_access_token option'
        )

    if client_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The client_session_token option cannot be used with the personal_access_token option'
        )

    if console_session_token is not None:
        raise SeamHttpInvalidOptionsError(
            'The console_session_token option cannot be used with the personal_access_token option'
        )

    return True

def is_seam_http_options_with_personal_access_token(
    personal_access_token: Optional[str] = None,
    api_key: Optional[str] = None,
    client_session_token: Optional[str] = None,
    console_session_token: Optional[str] = None,
    workspace_id: Optional[str] = None
) -> bool:
    if not is_seam_http_multi_workspace_options_with_personal_access_token(
        personal_access_token=personal_access_token,
        api_key=api_key,
        client_session_token=client_session_token,
        console_session_token=console_session_token
    ):
        return False

    if workspace_id is None:
        raise SeamHttpInvalidOptionsError(
            'Must pass a workspace_id when using a personal_access_token'
        )

    return True


