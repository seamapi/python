"""Read success response payloads defensively.

A 2xx response with an unexpected shape, e.g., a proxy rewrote the body or
the response key was renamed, raises the SDK's own error instead of leaking
a bare KeyError or TypeError from inside a generated route method.
"""

from typing import Any, Dict, List

from .exceptions import SeamHttpInvalidResponseError


def _read_response_key(res: Any, response_key: str, path: str) -> Any:
    if not isinstance(res, dict):
        raise SeamHttpInvalidResponseError(
            path,
            response_key,
            f"got {type(res).__name__} instead of a response object",
        )

    if response_key not in res:
        raise SeamHttpInvalidResponseError(
            path, response_key, "which the response does not contain"
        )

    return res[response_key]


def unwrap(res: Any, response_key: str, path: str) -> Dict[str, Any]:
    """Read an object under the response key, or raise for a malformed response."""

    value = _read_response_key(res, response_key, path)

    if not isinstance(value, dict):
        raise SeamHttpInvalidResponseError(
            path, response_key, f"got {type(value).__name__} instead of an object"
        )

    return value


def unwrap_list(res: Any, response_key: str, path: str) -> List[Any]:
    """Read a list under the response key, or raise for a malformed response."""

    value = _read_response_key(res, response_key, path)

    if not isinstance(value, list):
        raise SeamHttpInvalidResponseError(
            path, response_key, f"got {type(value).__name__} instead of a list"
        )

    return value
