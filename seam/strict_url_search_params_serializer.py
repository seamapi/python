"""Strict URL search parameter serializer used by the Seam SDK."""

from .url_search_params_serializer import (
    Params,
    UrlSearchParams,
    serialize_url_search_params as _serialize_url_search_params,
    update_url_search_params as _update_url_search_params,
)


def serialize_url_search_params(params: Params) -> str:
    """Serialize params with strict API validation enabled."""

    return _serialize_url_search_params(params, strict=True)


def update_url_search_params(search_params: UrlSearchParams, params: Params) -> None:
    """Update params with strict API validation enabled."""

    _update_url_search_params(search_params, params, strict=True)
