from collections import OrderedDict
from datetime import date, datetime, timedelta, timezone

import pytest

from seam.null import NULL
from seam.utils.url_search_params_serializer import (
    UnserializableParamError,
    UrlSearchParams,
    serialize_url_search_params,
    update_url_search_params,
)


def test_serializes_empty_object():
    assert serialize_url_search_params({}) == ""


def test_serializes_string():
    assert serialize_url_search_params({"foo": "d"}) == "foo=d"
    assert serialize_url_search_params({"foo": "null"}) == "foo=null"
    assert serialize_url_search_params({"foo": "None"}) == "foo=None"
    assert serialize_url_search_params({"foo": "undefined"}) == "foo=undefined"
    assert serialize_url_search_params({"foo": "0"}) == "foo=0"


def test_removes_the_empty_string():
    # Serializing the empty string would conflict with NULL.
    assert serialize_url_search_params({"foo": ""}) == ""
    assert serialize_url_search_params({"foo": "d", "bar": ""}) == "foo=d"


def test_serializes_int():
    assert serialize_url_search_params({"foo": 1}) == "foo=1"
    assert serialize_url_search_params({"foo": 0}) == "foo=0"
    assert serialize_url_search_params({"foo": -42}) == "foo=-42"


def test_serializes_arbitrary_precision_int():
    assert (
        serialize_url_search_params({"foo": 9007199254740993}) == "foo=9007199254740993"
    )
    assert (
        serialize_url_search_params({"foo": 123456789012345678901234567890})
        == "foo=123456789012345678901234567890"
    )


def test_serializes_float():
    assert serialize_url_search_params({"foo": 23.8}) == "foo=23.8"
    assert serialize_url_search_params({"foo": -23.8}) == "foo=-23.8"
    assert serialize_url_search_params({"foo": 0.30000000000000004}) == (
        "foo=0.30000000000000004"
    )


def test_serializes_float_using_the_ecmascript_number_format():
    # A float is serialized exactly as JavaScript would serialize the number,
    # which is not always the same as the Python repr.
    assert serialize_url_search_params({"foo": 1.0}) == "foo=1"
    assert serialize_url_search_params({"foo": -0.0}) == "foo=0"
    assert serialize_url_search_params({"foo": 100.0}) == "foo=100"
    assert serialize_url_search_params({"foo": 1e16}) == "foo=10000000000000000"
    assert serialize_url_search_params({"foo": 1e20}) == "foo=100000000000000000000"
    assert serialize_url_search_params({"foo": 1e21}) == "foo=1e%2B21"
    assert serialize_url_search_params({"foo": 0.0001}) == "foo=0.0001"
    assert serialize_url_search_params({"foo": 1e-6}) == "foo=0.000001"
    assert serialize_url_search_params({"foo": 1e-7}) == "foo=1e-7"
    assert serialize_url_search_params({"foo": 5e-324}) == "foo=5e-324"
    assert serialize_url_search_params({"foo": 1.7976931348623157e308}) == (
        "foo=1.7976931348623157e%2B308"
    )


def test_serializes_bool():
    assert serialize_url_search_params({"foo": True}) == "foo=true"
    assert serialize_url_search_params({"foo": False}) == "foo=false"
    assert serialize_url_search_params({"foo": True, "bar": False}) == (
        "bar=false&foo=true"
    )


def test_removes_none_params():
    assert serialize_url_search_params({"bar": None}) == ""
    assert serialize_url_search_params({"foo": 1, "bar": None}) == "foo=1"


def test_serializes_null_params():
    assert serialize_url_search_params({"bar": NULL}) == "bar="
    assert serialize_url_search_params({"foo": 1, "bar": NULL}) == "bar=&foo=1"


def test_removes_none_params_at_any_depth():
    assert serialize_url_search_params({"foo": {"bar": None, "baz": 1}}) == "foo.baz=1"
    assert serialize_url_search_params({"foo": {"bar": None}}) == ""


def test_serializes_empty_array_params():
    assert serialize_url_search_params({"bar": []}) == "bar="
    assert serialize_url_search_params({"foo": 1, "bar": []}) == "bar=&foo=1"
    assert serialize_url_search_params({"bar": ()}) == "bar="


def test_serializes_array_params_with_one_value():
    assert serialize_url_search_params({"bar": ["a"]}) == "bar=a"
    assert serialize_url_search_params({"foo": 1, "bar": ["a"]}) == "bar=a&foo=1"


def test_serializes_array_params_with_many_values():
    assert serialize_url_search_params({"foo": 1, "bar": ["a", "2"]}) == (
        "bar=a&bar=2&foo=1"
    )
    assert serialize_url_search_params(
        {"foo": 1, "bar": ["null", "2", "undefined"]}
    ) == ("bar=null&bar=2&bar=undefined&foo=1")


def test_serializes_tuple_params():
    assert serialize_url_search_params({"bar": ("a", "2")}) == "bar=a&bar=2"


def test_serializes_array_params_with_mixed_values():
    assert serialize_url_search_params(
        {"bar": [1, "a", True, datetime(1970, 1, 1, tzinfo=timezone.utc)]}
    ) == ("bar=1&bar=a&bar=true&bar=1970-01-01T00%3A00%3A00.000Z")


def test_serializes_datetime():
    assert serialize_url_search_params(
        {"foo": 1, "now": datetime(2025, 2, 24, 18, 44, 39, tzinfo=timezone.utc)}
    ) == ("foo=1&now=2025-02-24T18%3A44%3A39.000Z")


def test_serializes_datetime_with_milliseconds():
    assert serialize_url_search_params(
        {
            "now": datetime(
                2025, 2, 24, 18, 44, 39, microsecond=123000, tzinfo=timezone.utc
            )
        }
    ) == ("now=2025-02-24T18%3A44%3A39.123Z")


def test_truncates_datetime_microseconds():
    assert serialize_url_search_params(
        {
            "now": datetime(
                2025, 2, 24, 18, 44, 39, microsecond=123999, tzinfo=timezone.utc
            )
        }
    ) == ("now=2025-02-24T18%3A44%3A39.123Z")


def test_serializes_datetime_as_utc():
    assert serialize_url_search_params(
        {"now": datetime(2025, 2, 24, 13, 44, 39, tzinfo=timezone(timedelta(hours=-5)))}
    ) == ("now=2025-02-24T18%3A44%3A39.000Z")


def test_serializes_naive_datetime_as_utc():
    assert serialize_url_search_params({"now": datetime(2025, 2, 24, 18, 44, 39)}) == (
        "now=2025-02-24T18%3A44%3A39.000Z"
    )


def test_serializes_datetime_before_the_epoch():
    assert serialize_url_search_params(
        {"then": datetime(1969, 12, 31, 23, 59, 59, tzinfo=timezone.utc)}
    ) == ("then=1969-12-31T23%3A59%3A59.000Z")


def test_serializes_dicts():
    assert serialize_url_search_params({"foo": 1, "bar": {"baz": "a"}}) == (
        "bar.baz=a&foo=1"
    )

    assert serialize_url_search_params({"foo": 1, "bar": {"baz": {"x": {"z": 1}}}}) == (
        "bar.baz.x.z=1&foo=1"
    )

    assert serialize_url_search_params(
        {"foo": 1, "bar": {"baz": {"x": {"z": NULL}}}}
    ) == ("bar.baz.x.z=&foo=1")

    assert serialize_url_search_params({"foo": 1, "bar": {"baz": [1, "a"]}}) == (
        "bar.baz=1&bar.baz=a&foo=1"
    )

    assert serialize_url_search_params({"foo": {}, "bar": 2}) == "bar=2"

    assert serialize_url_search_params({"foo": {"x": {}}, "bar": 2}) == "bar=2"

    assert serialize_url_search_params(
        {"foo": {}, "bar": {"baz": {"x": {"z": NULL, "t": {}}, "q": {}}}}
    ) == ("bar.baz.x.z=")


def test_serializes_dict_subclasses():
    assert serialize_url_search_params(
        {"foo": OrderedDict([("bar", 1), ("baz", 2)])}
    ) == ("foo.bar=1&foo.baz=2")


def test_sorts_params_by_name():
    assert serialize_url_search_params({"b": 1, "a": 2, "c": 3}) == "a=2&b=1&c=3"
    assert serialize_url_search_params({"b": 1, "A": 2, "a": 3, "B": 4}) == (
        "A=2&B=4&a=3&b=1"
    )
    assert serialize_url_search_params({"a10": 1, "a2": 2, "a1": 3}) == (
        "a1=3&a10=1&a2=2"
    )
    assert serialize_url_search_params({"zz": 1, "a": {"z": 2, "b": 3}}) == (
        "a.b=3&a.z=2&zz=1"
    )
    assert serialize_url_search_params({"ab": 1, "a": {"b": 2}}) == "a.b=2&ab=1"


def test_sorts_params_by_utf_16_code_unit():
    assert serialize_url_search_params({"￿": 1, "\U0001f600": 2}) == (
        "%F0%9F%98%80=2&%EF%BF%BF=1"
    )


def test_sorting_preserves_array_order():
    assert serialize_url_search_params({"b": ["3", "1", "2"], "a": 1}) == (
        "a=1&b=3&b=1&b=2"
    )


def test_encodes_params_as_form_urlencoded():
    assert serialize_url_search_params({"foo": "a b"}) == "foo=a+b"
    assert serialize_url_search_params({"foo": "a+b"}) == "foo=a%2Bb"
    assert serialize_url_search_params({"foo": "a~b"}) == "foo=a%7Eb"
    assert serialize_url_search_params({"foo": "a*b"}) == "foo=a*b"
    assert serialize_url_search_params({"foo": "abcXYZ019*-._"}) == "foo=abcXYZ019*-._"
    assert serialize_url_search_params({"foo": "a&b=c?d#e/f"}) == (
        "foo=a%26b%3Dc%3Fd%23e%2Ff"
    )
    assert serialize_url_search_params({"foo": "100%"}) == "foo=100%25"
    assert serialize_url_search_params({"foo": "a\nb"}) == "foo=a%0Ab"


def test_encodes_unicode_params():
    assert serialize_url_search_params({"foo": "héllo wörld"}) == (
        "foo=h%C3%A9llo+w%C3%B6rld"
    )
    assert serialize_url_search_params({"foo": "日本語"}) == (
        "foo=%E6%97%A5%E6%9C%AC%E8%AA%9E"
    )
    assert serialize_url_search_params({"🔒": "a"}) == "%F0%9F%94%92=a"
    assert serialize_url_search_params({"a b": 1}) == "a+b=1"


def test_cannot_serialize_keys_containing_a_dot():
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo.bar": 1})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": {"bar.baz": 1}})


def test_cannot_serialize_non_string_keys():
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({1: "a"})


def test_cannot_serialize_functions():
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": lambda: None})


def test_cannot_serialize_number_pointers():
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": float("inf")})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": float("-inf")})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": float("nan")})


def test_cannot_serialize_arbitrary_objects():
    class Device:
        def __init__(self):
            self.device_id = "a"

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": Device()})


def test_cannot_serialize_date():
    # A date is not an instant, so it has no unambiguous serialization.
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": date(2025, 2, 24)})


def test_cannot_serialize_sets():
    # A set would not serialize deterministically.
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": {"a", "b"}})


def test_cannot_serialize_array_params_with_unserializable_values():
    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": [""]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", None]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", NULL]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", ["s"]]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", []]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", [""]]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", {}]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", {"x": 2}]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"bar": ["a", lambda: None]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": 1, "bar": ["", "a", ""]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": 1, "bar": ["", "a", "2"]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": 1, "bar": ["", "", ""]})

    with pytest.raises(UnserializableParamError):
        serialize_url_search_params({"foo": [1, float("nan")]})


def test_unserializable_param_error_message():
    with pytest.raises(UnserializableParamError) as error:
        serialize_url_search_params({"foo": {"bar.baz": 1}})

    assert str(error.value) == (
        "Could not serialize parameter: 'bar.baz' contains one or more dots"
        ' "." in its name which is unsupported'
    )
    assert error.value.name == "bar.baz"


def test_unserializable_param_error_message_uses_the_full_path():
    with pytest.raises(UnserializableParamError) as error:
        serialize_url_search_params({"foo": {"bar": float("nan")}})

    assert str(error.value) == "Could not serialize parameter: 'foo.bar' is NaN"


def test_update_url_search_params():
    search_params = UrlSearchParams()
    update_url_search_params(search_params, {"foo": "d", "bar": 2})

    assert search_params.to_string() == "bar=2&foo=d"


def test_update_url_search_params_preserves_existing_params():
    search_params = UrlSearchParams([("foo", "bar")])
    update_url_search_params(
        search_params,
        {"name": "Dax", "age": 27, "is_admin": True, "tags": ["cars", "planes"]},
    )

    assert search_params.to_string() == (
        "age=27&foo=bar&is_admin=true&name=Dax&tags=cars&tags=planes"
    )


def test_update_url_search_params_overwrites_existing_params():
    search_params = UrlSearchParams([("foo", "a"), ("bar", "x"), ("foo", "b")])
    update_url_search_params(search_params, {"foo": "new"})

    assert search_params.to_string() == "bar=x&foo=new"


def test_update_url_search_params_appends_array_params():
    search_params = UrlSearchParams([("foo", "old")])
    update_url_search_params(search_params, {"foo": [1, 2]})

    assert search_params.to_string() == "foo=old&foo=1&foo=2"


def test_update_url_search_params_keeps_existing_params_for_absent_values():
    for value in [None, "", {}]:
        search_params = UrlSearchParams([("foo", "a")])
        update_url_search_params(search_params, {"foo": value})

        assert search_params.to_string() == "foo=a"


def test_url_search_params_from_query_string():
    search_params = UrlSearchParams("?a=1&b=hello+world&c=%F0%9F%94%92&d")

    assert search_params.get("a") == "1"
    assert search_params.get("b") == "hello world"
    assert search_params.get("c") == "🔒"
    assert search_params.get("d") == ""
    assert search_params.to_string() == "a=1&b=hello+world&c=%F0%9F%94%92&d="


def test_url_search_params_from_dict():
    assert UrlSearchParams({"a": "1", "b": "2"}).to_string() == "a=1&b=2"


def test_url_search_params_append_and_get():
    search_params = UrlSearchParams()
    search_params.append("foo", "a")
    search_params.append("foo", "b")

    assert search_params.get("foo") == "a"
    assert search_params.get_all("foo") == ["a", "b"]
    assert search_params.get("bar") is None
    assert search_params.get_all("bar") == []
    assert len(search_params) == 2
    assert list(search_params) == [("foo", "a"), ("foo", "b")]


def test_url_search_params_set():
    search_params = UrlSearchParams([("foo", "a"), ("bar", "x"), ("foo", "b")])
    search_params.set("foo", "c")

    assert list(search_params) == [("foo", "c"), ("bar", "x")]

    search_params.set("baz", "y")

    assert search_params.get("baz") == "y"


def test_url_search_params_has_and_delete():
    search_params = UrlSearchParams([("foo", "a"), ("foo", "b")])

    assert search_params.has("foo")

    search_params.delete("foo")

    assert not search_params.has("foo")
    assert len(search_params) == 0


def test_url_search_params_str():
    assert str(UrlSearchParams([("foo", "a b")])) == "foo=a+b"
