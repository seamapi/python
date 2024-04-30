import os
from typing import Optional

from seam.utils.auth import get_auth_headers

DEFAULT_ENDPOINT = "https://connect.getseam.com"


def parse_options(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
    endpoint: Optional[str] = None,
):
    api_key = api_key or get_api_key_from_env(
        personal_access_token=personal_access_token,
    )
    auth_headers = get_auth_headers(
        api_key=api_key,
        personal_access_token=personal_access_token,
        workspace_id=workspace_id,
    )
    endpoint = endpoint or get_endpoint_from_env() or DEFAULT_ENDPOINT

    return auth_headers, endpoint


def get_api_key_from_env(
    personal_access_token: Optional[str] = None,
):
    if personal_access_token is not None:
        return None

    return os.getenv("SEAM_API_KEY")


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
