from collections import OrderedDict

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


def sent_request(recording_server, send):
    """Return the single request the given call put on the wire."""

    with recording_server([(200, {})]) as (endpoint, requests):
        send(SeamHttpClient(base_url=endpoint, auth_headers={}))

    [request] = requests

    return request


def test_client_sends_null_params_as_json_null(recording_server):
    request = sent_request(
        recording_server,
        lambda client: client.patch(
            "/devices/update", json={"device_id": "a", "name": NULL}
        ),
    )

    assert request["body"] == {"device_id": "a", "name": None}


def test_client_sends_nested_null_params_as_json_null(recording_server):
    request = sent_request(
        recording_server,
        lambda client: client.patch(
            "/spaces/update", json={"customer_data": {"check_in": NULL}}
        ),
    )

    assert request["body"] == {"customer_data": {"check_in": None}}


def test_client_passes_through_payloads_without_null_params(recording_server):
    request = sent_request(
        recording_server,
        lambda client: client.patch(
            "/devices/update", json={"device_id": "a", "name": "Front Door"}
        ),
    )

    assert request["body"] == {"device_id": "a", "name": "Front Door"}


def test_client_sends_null_search_params_as_an_empty_value(recording_server):
    request = sent_request(
        recording_server,
        lambda client: client.get(
            "/devices/list", params={"device_id": NULL, "limit": 2}
        ),
    )

    assert request["query"] == "device_id=&limit=2"


def test_client_omits_none_search_params(recording_server):
    request = sent_request(
        recording_server,
        lambda client: client.get(
            "/devices/list", params={"device_id": None, "limit": 2}
        ),
    )

    assert request["query"] == "limit=2"
