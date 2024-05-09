import os
from typing import Optional

from seam.auth import get_auth_headers
from seam.options import get_endpoint_from_env

DEFAULT_ENDPOINT = "https://connect.getseam.com"


def parse_options(
    api_key: Optional[str] = None,
    personal_access_token: Optional[str] = None,
    workspace_id: Optional[str] = None,
    endpoint: Optional[str] = None,
):
    if personal_access_token is None:
        api_key = api_key or os.getenv("SEAM_API_KEY")

    auth_headers = get_auth_headers(
        api_key=api_key,
        personal_access_token=personal_access_token,
        workspace_id=workspace_id,
    )
    endpoint = endpoint or get_endpoint_from_env() or DEFAULT_ENDPOINT

    return auth_headers, endpoint
