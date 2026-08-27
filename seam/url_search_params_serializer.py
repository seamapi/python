"""Serializes Python objects to URL search params.

This is a Python port of the `@seamapi/url-search-params-serializer
<https://github.com/seamapi/url-search-params-serializer>`_ reference
implementation, which defines the standard for how the Seam SDKs and other
Seam API consumers serialize objects to URL search params in HTTP GET requests.

Output is byte-for-byte identical to the reference implementation:
values are encoded with the ``application/x-www-form-urlencoded`` serializer,
params are sorted by name, and numbers are formatted using the
ECMAScript ``Number::toString`` algorithm.

Type mapping between the reference implementation and this port:

- JavaScript ``undefined`` is ``None``, or simply an absent key.
- JavaScript ``null`` is :data:`seam.NULL <seam.null.NULL>`.
  Python has a single absence value, so ``None`` means the safe option of
  omitting the param and sending null is always explicit.
- JavaScript ``string`` is ``str``.
- JavaScript ``boolean`` is ``bool``.
- JavaScript ``number`` is ``float`` or ``int``.
- JavaScript ``bigint`` is ``int``.
  Python integers are arbitrary precision, so ``int`` covers both cases
  and is always serialized in full without exponent notation.
- JavaScript ``Date`` and ``Temporal.Instant`` are
  :class:`datetime.datetime`.
  A naive ``datetime`` is interpreted as UTC.
  Since ``Date`` has millisecond precision, microseconds are truncated.
- JavaScript ``Array`` is ``list`` or ``tuple``.
  Unordered collections such as ``set`` are unsupported
  because they would not serialize deterministically.
- A JavaScript plain object is any ``Mapping``, e.g., a ``dict``.
"""

import datetime
import math
import string
from collections.abc import Mapping
from decimal import Decimal
from typing import Any, Iterator, List, Optional, Sequence, Tuple, Union
from urllib.parse import parse_qsl

from .exceptions import SeamError
from .null import is_null

Params = Mapping[str, Any]


class UnserializableParamError(SeamError):
    """Exception raised when a param could not be serialized.

    :ivar name: Name of the param that could not be serialized
    :vartype name: str
    """

    def __init__(self, name: str, message: str):
        """
        :param name: Name of the param that could not be serialized
        :type name: str
        :param message: Description of why the param could not be serialized
        :type message: str
        """

        super().__init__(f"Could not serialize parameter: '{name}' {message}")
        self.name = name


class UrlSearchParams:
    """A mutable collection of URL search params.

    Implements the parts of the `URLSearchParams
    <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams>`_
    interface needed to serialize params to a query string.
    Unlike a ``dict``, a name may appear more than once,
    which is how arrays are serialized.
    """

    def __init__(
        self,
        init: Optional[Union[str, Params, Sequence[Tuple[str, str]]]] = None,
    ):
        """
        :param init: A query string, a mapping of names to values,
            or a sequence of name-value pairs
        :type init: Optional[Union[str, Mapping[str, Any], Sequence[Tuple[str, str]]]]
        """

        self._pairs: List[Tuple[str, str]] = []

        if init is None:
            return

        if isinstance(init, str):
            query = init[1:] if init.startswith("?") else init
            self._pairs = list(parse_qsl(query, keep_blank_values=True))
            return

        items = init.items() if isinstance(init, Mapping) else init
        self._pairs = [(str(name), str(value)) for name, value in items]

    def append(self, name: str, value: str) -> None:
        """Appends a name-value pair, keeping any existing pairs with this name.

        :param name: Name of the param
        :type name: str
        :param value: Value of the param
        :type value: str
        """

        self._pairs.append((name, value))

    def set(self, name: str, value: str) -> None:
        """Sets the value associated with a name.

        Replaces the first pair with this name and removes any others.
        Appends a new pair if no pair with this name exists.

        :param name: Name of the param
        :type name: str
        :param value: Value of the param
        :type value: str
        """

        if not self.has(name):
            self.append(name, value)
            return

        pairs: List[Tuple[str, str]] = []
        is_set = False

        for pair in self._pairs:
            if pair[0] != name:
                pairs.append(pair)
            elif not is_set:
                pairs.append((name, value))
                is_set = True

        self._pairs = pairs

    def get(self, name: str) -> Optional[str]:
        """Returns the value of the first pair with this name.

        :param name: Name of the param
        :type name: str

        :returns: The value, or ``None`` if no pair with this name exists
        """

        for existing_name, value in self._pairs:
            if existing_name == name:
                return value

        return None

    def get_all(self, name: str) -> List[str]:
        """Returns the values of all pairs with this name, in insertion order.

        :param name: Name of the param
        :type name: str

        :returns: The values"""

        return [value for existing_name, value in self._pairs if existing_name == name]

    def has(self, name: str) -> bool:
        """Returns whether a pair with this name exists.

        :param name: Name of the param
        :type name: str

        :returns: Whether a pair with this name exists"""

        return any(existing_name == name for existing_name, _ in self._pairs)

    def delete(self, name: str) -> None:
        """Removes all pairs with this name.

        :param name: Name of the param
        :type name: str
        """

        self._pairs = [pair for pair in self._pairs if pair[0] != name]

    def sort(self) -> None:
        """Sorts all pairs by name.

        Sorting is stable, so the relative order of pairs
        with the same name is preserved.
        Names are compared by UTF-16 code units to match the
        `URLSearchParams.sort()
        <https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/sort>`_
        specification.
        """

        self._pairs.sort(key=lambda pair: pair[0].encode("utf-16-be"))

    def to_string(self) -> str:
        """Serializes all pairs to a query string.

        :returns: The query string, without a leading ``?``"""

        return "&".join(
            f"{_encode_form_component(name)}={_encode_form_component(value)}"
            for name, value in self._pairs
        )

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_string()!r})"

    def __len__(self) -> int:
        return len(self._pairs)

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        return iter(self._pairs)


def serialize_url_search_params(params: Params, *, strict: bool = False) -> str:
    """Serializes params to a URL search param query string.

    :param params: The params to serialize
    :type params: Mapping[str, Any]
    :param strict: Whether to add ``_strict=true`` to non-empty query strings
    :type strict: bool

    :returns: The query string, without a leading ``?``

    :raises UnserializableParamError: If any param could not be serialized
    """

    search_params = UrlSearchParams()
    update_url_search_params(search_params, params, strict=strict)

    return search_params.to_string()


def update_url_search_params(
    search_params: UrlSearchParams, params: Params, *, strict: bool = False
) -> None:
    """Updates existing URL search params with serialized params.

    Existing params are preserved unless overwritten by a serialized param.
    All params are sorted by name.

    :param search_params: The URL search params to update
    :type search_params: UrlSearchParams
    :param params: The params to serialize
    :type params: Mapping[str, Any]
    :param strict: Whether to add ``_strict=true`` when the result is non-empty
    :type strict: bool

    :raises UnserializableParamError: If any param could not be serialized
    """

    _nested_update_url_search_params(search_params, params, [])

    search_params.sort()

    if strict and len(search_params) > 0:
        search_params.delete("_strict")
        search_params.append("_strict", "true")


def _nested_update_url_search_params(
    search_params: UrlSearchParams, params: Params, path: List[str]
) -> None:
    for key, value in params.items():
        if not isinstance(key, str):
            raise UnserializableParamError(
                repr(key),
                f"is a {type(key).__name__} which is unsupported as a parameter name",
            )

        if "." in key:
            raise UnserializableParamError(
                key,
                'contains one or more dots "." in its name which is unsupported',
            )

        current_path = [*path, key]

        if isinstance(value, Mapping):
            _nested_update_url_search_params(search_params, value, current_path)
            continue

        name = ".".join(current_path)

        if value is None:
            continue

        if isinstance(value, str) and len(value) == 0:
            continue

        if isinstance(value, (list, tuple)):
            _update_url_search_params_from_array(search_params, name, value)
            continue

        search_params.set(name, _serialize(name, value))


def _update_url_search_params_from_array(
    search_params: UrlSearchParams, name: str, values: Sequence[Any]
) -> None:
    if len(values) == 0:
        search_params.set(name, "")
        return

    if len(values) == 1 and _is_empty_string(values[0]):
        raise UnserializableParamError(
            name,
            "is a single element array containing the empty string which is unsupported",
        )

    if any(_is_empty_string(value) for value in values):
        raise UnserializableParamError(
            name,
            "is an array containing the empty string which is unsupported",
        )

    if any(value is None or is_null(value) for value in values):
        raise UnserializableParamError(
            name,
            "is an array containing null or undefined values which is unsupported",
        )

    for value in values:
        search_params.append(name, _serialize(name, value))


def _serialize(name: str, value: Any) -> str:
    if is_null(value):
        return ""

    if isinstance(value, str):
        return value

    if isinstance(value, bool):
        return "true" if value else "false"

    if isinstance(value, int):
        return str(value)

    if isinstance(value, float):
        return _format_number(name, value)

    if isinstance(value, datetime.datetime):
        return _format_datetime(value)

    raise UnserializableParamError(name, f"is a {type(value).__name__}")


def _is_empty_string(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 0


def _format_datetime(value: datetime.datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=datetime.timezone.utc)

    utc_value = value.astimezone(datetime.timezone.utc)
    milliseconds = utc_value.microsecond // 1000

    return (
        f"{utc_value.year:04d}-{utc_value.month:02d}-{utc_value.day:02d}"
        f"T{utc_value.hour:02d}:{utc_value.minute:02d}:{utc_value.second:02d}"
        f".{milliseconds:03d}Z"
    )


def _format_number(name: str, value: float) -> str:
    if math.isnan(value):
        raise UnserializableParamError(name, "is NaN")

    if math.isinf(value):
        raise UnserializableParamError(
            name, "is Infinity" if value > 0 else "is -Infinity"
        )

    if value == 0:
        return "0"

    sign = "-" if value < 0 else ""
    _, digit_tuple, exponent = Decimal(repr(abs(value))).as_tuple()

    # The shortest digit string that round-trips, and the position of the
    # decimal point relative to it, as required by the ECMAScript
    # Number::toString algorithm.
    digits = "".join(str(digit) for digit in digit_tuple)
    point = int(exponent) + len(digits)
    digits = digits.rstrip("0")

    return sign + _format_digits(digits, point)


def _format_digits(digits: str, point: int) -> str:
    """Formats digits and a decimal point position per ECMAScript Number::toString.

    :param digits: Significant digits, without trailing zeros
    :type digits: str
    :param point: Position of the decimal point relative to the digits
    :type point: int

    :returns: The formatted number"""

    count = len(digits)

    if count <= point <= 21:
        return digits + "0" * (point - count)

    if 0 < point <= 21:
        return f"{digits[:point]}.{digits[point:]}"

    if -6 < point <= 0:
        return f"0.{'0' * -point}{digits}"

    exponent = point - 1
    exponent_sign = "+" if exponent >= 0 else "-"
    mantissa = digits if count == 1 else f"{digits[0]}.{digits[1:]}"

    return f"{mantissa}e{exponent_sign}{abs(exponent)}"


_FORM_SAFE_CHARACTERS = frozenset(f"{string.ascii_letters}{string.digits}*-._")


def _encode_form_component(value: str) -> str:
    """Percent-encodes a string using the ``application/x-www-form-urlencoded`` serializer.

    :param value: The string to encode
    :type value: str

    :returns: The encoded string"""

    encoded = []

    for byte in value.encode("utf-8"):
        character = chr(byte)
        if character in _FORM_SAFE_CHARACTERS:
            encoded.append(character)
        elif character == " ":
            encoded.append("+")
        else:
            encoded.append(f"%{byte:02X}")

    return "".join(encoded)
