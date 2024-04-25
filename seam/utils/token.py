token_prefix = "seam_"

access_token_prefix = "seam_at"

jwt_prefix = "ey"

client_session_token_prefix = "seam_cst"

publishable_key_token_prefix = "seam_pk"


def is_access_token(token: str) -> bool:
    return token.startswith(access_token_prefix)


def is_jwt(token: str) -> bool:
    return token.startswith(jwt_prefix)


def is_seam_token(token: str) -> bool:
    return token.startswith(token_prefix)


def is_api_key(token: str) -> bool:
    return (
        not is_client_session_token(token)
        and not is_jwt(token)
        and not is_access_token(token)
        and not is_publishable_key(token)
        and is_seam_token(token)
    )


def is_client_session_token(token: str) -> bool:
    return token.startswith(client_session_token_prefix)


def is_publishable_key(token: str) -> bool:
    return token.startswith(publishable_key_token_prefix)


def is_console_session_token(token: str) -> bool:
    return is_jwt(token)


def is_personal_access_token(token: str) -> bool:
    return is_access_token(token)
