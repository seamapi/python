"""The explicit null sentinel used by request params.

Python has a single absence value, ``None``, but the Seam API distinguishes
an omitted param from a param explicitly set to null. For example, in an
update request, an omitted param leaves the current value unchanged,
while a null param unsets the current value.

Since sending null is rarely intended and unsetting a value cannot be undone,
``None`` means the safe option of omitting the param.
Sending null is explicit and always spelled :data:`NULL`.
"""

from collections.abc import Mapping
from typing import Any


class Null:
    """Type of the :data:`NULL` sentinel."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return "NULL"

    def __bool__(self):
        return False


NULL: Any = Null()
"""Sentinel for a param explicitly set to null.

Params set to this sentinel are sent as null,
whereas params set to ``None`` are omitted from the request.

Use it wherever the Seam API documents null as a meaningful value, e.g.,
to unset a value in an update request, or to filter by an unset value:

.. code-block:: python

  from seam import NULL, Seam

  seam = Seam()

  # Unsets the name, leaving custom_metadata unchanged.
  seam.devices.update(device_id=device_id, name=NULL)

  # Lists only the Access Grants which have no access_grant_key.
  seam.access_grants.list(access_grant_key=NULL)

This sentinel is typed as ``Any`` so that it may be passed
to any param without a type error.
"""


def is_null(value: Any) -> bool:
    """Returns whether a value is the :data:`NULL` sentinel.

    :param value: The value to check
    :type value: Any

    :returns: Whether the value is the ``NULL`` sentinel"""

    return isinstance(value, Null)


def replace_null(value: Any) -> Any:
    """Recursively replaces the :data:`NULL` sentinel with ``None``.

    Returns a copy, so the given value is never modified.
    Use this to prepare a request payload for JSON serialization,
    where ``None`` is serialized to null.

    :param value: The value to convert
    :type value: Any

    :returns: A copy of the value with every ``NULL`` sentinel replaced"""

    if is_null(value):
        return None

    if isinstance(value, Mapping):
        return {key: replace_null(item) for key, item in value.items()}

    if isinstance(value, list):
        return [replace_null(item) for item in value]

    if isinstance(value, tuple):
        return tuple(replace_null(item) for item in value)

    return value
