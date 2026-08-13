from collections import OrderedDict

import niquests
import pytest

from seam.client import SeamHttpClient
from seam.null import NULL, Null, is_null, replace_null


def test_null_is_a_singleton():
    assert Null() is NULL
    assert is_null(NULL)
    assert is_null(Null())


def test_null_is_not_none():
    assert NULL is not None
    assert not is_null(None)
    assert not is_null("")
    assert not is_null(0)


def test_null_is_falsy():
    assert not NULL


def test_null_repr():
    assert repr(NULL) == "NULL"


def test_replace_null():
    assert replace_null(NULL) is None
    assert replace_null(None) is None
    assert replace_null("a") == "a"
    assert replace_null(0) == 0
    assert replace_null(False) is False


def test_replace_null_in_dict():
    assert replace_null({"a": NULL, "b": 1, "c": None}) == {
        "a": None,
        "b": 1,
        "c": None,
    }


def test_replace_null_in_nested_dict():
    assert replace_null({"a": {"b": {"c": NULL}}}) == {"a": {"b": {"c": None}}}


def test_replace_null_in_lists_and_tuples():
    assert replace_null(["a", NULL]) == ["a", None]
    assert replace_null(("a", NULL)) == ("a", None)
    assert replace_null({"a": [{"b": NULL}]}) == {"a": [{"b": None}]}


def test_replace_null_does_not_modify_the_given_value():
    params = {"a": NULL, "b": [NULL]}
    replace_null(params)

    assert params == {"a": NULL, "b": [NULL]}


def test_replace_null_normalizes_mappings_to_dicts():
    result = replace_null(OrderedDict([("a", NULL)]))

    assert result == {"a": None}


class StubResponse:
    status_code = 200
    headers = {"content-type": "application/json"}

    def json(self):
        return {}


@pytest.fixture(name="sent_payloads")
def sent_payloads_fixture(monkeypatch):
    payloads = []

    # pylint: disable=unused-argument
    def request(self, method, url, *args, **kwargs):
        payloads.append(kwargs.get("json"))
        return StubResponse()

    monkeypatch.setattr(niquests.Session, "request", request)

    return payloads


def test_client_sends_null_params_as_json_null(sent_payloads):
    client = SeamHttpClient(base_url="https://example.com", auth_headers={})
    client.patch("/devices/update", json={"device_id": "a", "name": NULL})

    assert sent_payloads == [{"device_id": "a", "name": None}]


def test_client_sends_nested_null_params_as_json_null(sent_payloads):
    client = SeamHttpClient(base_url="https://example.com", auth_headers={})
    client.patch("/spaces/update", json={"customer_data": {"check_in": NULL}})

    assert sent_payloads == [{"customer_data": {"check_in": None}}]


def test_client_passes_through_payloads_without_null_params(sent_payloads):
    client = SeamHttpClient(base_url="https://example.com", auth_headers={})
    client.patch("/devices/update", json={"device_id": "a", "name": "Front Door"})

    assert sent_payloads == [{"device_id": "a", "name": "Front Door"}]
