import os
from typing import Optional


def get_api_key_from_env(
    client_session_token: Optional[str] = None,
    console_session_token: Optional[str] = None,
    personal_access_token: Optional[str] = None,
):
    if client_session_token is not None:
        return None

    if console_session_token is not None:
        return None

    if personal_access_token is not None:
        return None

    return os.getenv("SEAM_API_KEY")
