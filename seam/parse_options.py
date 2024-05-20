import os
from typing import Optional

from .auth import get_auth_headers
from .options import get_endpoint


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
    endpoint = get_endpoint(endpoint)

    return auth_headers, endpoint
