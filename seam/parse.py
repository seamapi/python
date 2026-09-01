"""Total conversion helpers shared by the generated resource dataclasses.

The Seam API grows new event types, action types, and error codes between SDK
releases, so reading a response must never fail on the shape of the payload.
Every helper here degrades instead of raising: an unusable value becomes
``None``, an empty list, or a :class:`DeepAttrDict` carrying the payload
verbatim, so one unexpected field cannot cost the caller the whole response.

The narrow cost is that a genuinely malformed payload is no longer loud. The
payload survives on the returned object, so it stays diagnosable.
"""

from typing import Any, Dict, List

from .deep_attr_dict import DeepAttrDict


def record_from_dict(value: Any) -> Any:
    """Wrap a free-form record for attribute access, passing anything else through.

    A record the API sends as something other than an object degrades to the raw
    value rather than costing the caller the whole surrounding resource.
    """

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
    """Convert a list of nested objects, skipping nothing and raising for nothing.

    A value that is not a list reads as empty, so callers can always iterate.
    """

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
    convert, yields a DeepAttrDict so a newer API stays readable.
    """

    if not isinstance(value, dict):
        # Not an object at all; hand it back untouched rather than lose it.
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
    """Convert a list of discriminated union members, degrading item by item."""

    if not isinstance(value, list):
        return []

    return [discriminated_from_dict(item, variants, discriminator) for item in value]
