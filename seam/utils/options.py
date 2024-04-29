from typing import Optional


class SeamHttpInvalidOptionsError(Exception):
    def __init__(self, message):
        super().__init__(f"SeamHttp received invalid options: {message}")


def is_seam_http_options_with_api_key(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
) -> bool:
    if api_key is None:
        return False

    if personal_access_token is not None:
        raise SeamHttpInvalidOptionsError(
            "The personal_access_token option cannot be used with the api_key option"
        )

    return True


def is_seam_http_options_with_personal_access_token(
    personal_access_token: Optional[str] = None,
    api_key: Optional[str] = None,
    workspace_id: Optional[str] = None,
) -> bool:
    if personal_access_token is None:
        return False

    if api_key is not None:
        raise SeamHttpInvalidOptionsError(
            "The api_key option cannot be used with the personal_access_token option"
        )

    if workspace_id is None:
        raise SeamHttpInvalidOptionsError(
            "Must pass a workspace_id when using a personal_access_token"
        )

    return True
