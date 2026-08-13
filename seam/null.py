"""The explicit null sentinel used by request params.

Python has a single absence value, ``None``, but the Seam API distinguishes
an omitted param from a param explicitly set to null. For example, in an
update request, an omitted param leaves the current value unchanged,
while a null param unsets the current value.

Since sending null is rarely intended and unsetting a value cannot be undone,
``None`` means the safe option of omitting the param.
Sending null is explicit and always spelled :data:`NULL`.
"""

from collections.abc import Mapping, Sequence
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


NULL = Null()
"""Sentinel for a param explicitly set to null.

Params set to this sentinel are serialized to null,
whereas params set to ``None`` are omitted:

.. code-block:: python

  from seam import NULL, serialize_url_search_params

  serialize_url_search_params({"name": NULL, "limit": 20})
  # => 'limit=20&name='

  serialize_url_search_params({"name": None, "limit": 20})
  # => 'limit=20'

Use it wherever the Seam API documents null as a meaningful value, e.g.,
to unset a value in an update request, or to filter by an unset value.
"""


def is_null(value: Any) -> bool:
    """Returns whether a value is the :data:`NULL` sentinel.

    :param value: The value to check
    :type value: Any

    :returns: Whether the value is the ``NULL`` sentinel"""

    return isinstance(value, Null)


def replace_null(value: Any) -> Any:
    """Returns a copy of a value with every :data:`NULL` sentinel replaced by ``None``.

    The sentinel only distinguishes an explicit null from an omitted param
    within this SDK. Once a request body is being serialized, the param is
    known to be present, so the sentinel becomes the null that JSON has.

    :param value: The value to copy
    :type value: Any

    :returns: The value with each ``NULL`` sentinel replaced by ``None``"""

    if is_null(value):
        return None

    if isinstance(value, Mapping):
        return {key: replace_null(item) for key, item in value.items()}

    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [replace_null(item) for item in value]

    return value
