TOKEN_PREFIX = "seam_"

ACCESS_TOKEN_PREFIX = "seam_at"

JWT_PREFIX = "ey"

CLIENT_SESSION_TOKEN_PREFIX = "seam_cst"

PUBLISHABLE_KEY_TOKEN_PREFIX = "seam_pk"


def is_access_token(token: str) -> bool:
    return token.startswith(ACCESS_TOKEN_PREFIX)


def is_jwt(token: str) -> bool:
    return token.startswith(JWT_PREFIX)


def is_seam_token(token: str) -> bool:
    return token.startswith(TOKEN_PREFIX)


def is_api_key(token: str) -> bool:
    return (
        not is_client_session_token(token)
        and not is_jwt(token)
        and not is_access_token(token)
        and not is_publishable_key(token)
        and is_seam_token(token)
    )


def is_client_session_token(token: str) -> bool:
    return token.startswith(CLIENT_SESSION_TOKEN_PREFIX)


def is_publishable_key(token: str) -> bool:
    return token.startswith(PUBLISHABLE_KEY_TOKEN_PREFIX)


def is_console_session_token(token: str) -> bool:
    return is_jwt(token)


def is_personal_access_token(token: str) -> bool:
    return is_access_token(token)
