"""Convert response payloads without raising on their shape.

Seam adds event types, action types, and error codes between SDK releases, so a
value in an unexpected shape degrades to None, an empty list, or a DeepAttrDict
rather than costing the caller the whole response.
"""

from typing import Any, Dict, List

from .deep_attr_dict import DeepAttrDict


def record_from_dict(value: Any) -> Any:
    """Wrap a free-form record for attribute access, passing anything else through."""

    return DeepAttrDict(value) if isinstance(value, dict) else value


def object_from_dict(cls: Any, value: Any) -> Any:
    """Convert an optional nested object, or None when it is unusable."""

    if not isinstance(value, dict):
        return None

    try:
        return cls.from_dict(value)
    except Exception:  # pylint: disable=broad-exception-caught
        return DeepAttrDict(value)


def required_object_from_dict(cls: Any, value: Any) -> Any:
    """Convert a nested object the caller may always read, never returning None."""

    source = value if isinstance(value, dict) else {}

    try:
        return cls.from_dict(source)
    except Exception:  # pylint: disable=broad-exception-caught
        return DeepAttrDict(source)


def object_list_from_dict(cls: Any, value: Any) -> List[Any]:
    """Convert a list of nested objects, reading a non-list as empty."""

    if not isinstance(value, list):
        return []

    return [
        object_from_dict(cls, item) if isinstance(item, dict) else item
        for item in value
    ]


def discriminated_from_dict(
    value: Any, variants: Dict[str, Any], discriminator: str
) -> Any:
    """Convert one member of a discriminated union.

    An unrecognized discriminator, or a known one whose payload does not
    convert, yields a DeepAttrDict.
    """

    if not isinstance(value, dict):
        return value

    key = value.get(discriminator)
    variant = variants.get(key) if isinstance(key, str) else None

    if variant is None:
        return DeepAttrDict(value)

    try:
        return variant.from_dict(value)
    except Exception:  # pylint: disable=broad-exception-caught
        return DeepAttrDict(value)


def discriminated_list_from_dict(
    value: Any, variants: Dict[str, Any], discriminator: str
) -> List[Any]:
    """Convert a list of discriminated union members, reading a non-list as empty."""

    if not isinstance(value, list):
        return []

    return [discriminated_from_dict(item, variants, discriminator) for item in value]
