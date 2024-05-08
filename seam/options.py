import os
from typing import Optional


def get_endpoint_from_env():
    seam_api_url = os.getenv("SEAM_API_URL")
    seam_endpoint = os.getenv("SEAM_ENDPOINT")

    if seam_api_url is not None:
        print(
            "\033[93m"
            "Using the SEAM_API_URL environment variable is deprecated. "
            "Support will be removed in a later major version. Use SEAM_ENDPOINT instead."
            "\033[0m"
        )

    if seam_api_url is not None and seam_endpoint is not None:
        print(
            "\033[93m"
            "Detected both the SEAM_API_URL and SEAM_ENDPOINT environment variables. "
            "Using SEAM_ENDPOINT."
            "\033[0m"
        )

    return seam_endpoint or seam_api_url


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
