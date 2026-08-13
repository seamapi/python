from typing import Any, Dict, List

import pytest

from seam import NULL, Seam, UnserializableParamError

DEVICE = {"device": {"device_id": "device1"}}
DEVICES: Dict[str, List[Any]] = {"devices": []}


def test_client_serializes_search_params(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get(
            "/devices/list",
            params={
                "device_ids": ["device1", "device2"],
                "custom_metadata_has": {"tag": "front", "floor": 2},
                "limit": 20,
            },
        )

    [request] = requests

    assert request["method"] == "GET"
    assert request["path"] == "/devices/list"
    assert request["query"] == (
        "custom_metadata_has.floor=2"
        "&custom_metadata_has.tag=front"
        "&device_ids=device1"
        "&device_ids=device2"
        "&limit=20"
    )


def test_client_does_not_reencode_the_serialized_search_params(recording_server):
    """The serializer and httpx disagree on exactly two characters.

    httpx escapes ``*`` and leaves ``~`` alone, so a query it encodes is not
    the one the serializer produced. Setting the query on the url keeps ours.
    """

    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params={"search": "a *~ b"})

    [request] = requests

    assert request["query"] == "search=a+*%7E+b"


def test_client_omits_search_params_set_to_none(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params={"search": None, "limit": 20})

    [request] = requests

    assert request["query"] == "limit=20"


def test_client_serializes_search_params_set_to_null(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params={"search": NULL, "limit": 20})

    [request] = requests

    assert request["query"] == "limit=20&search="


def test_client_sends_no_query_string_without_search_params(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params={})
        seam.client.get("/devices/list", params={"search": None})
        seam.client.get("/devices/list")

    for request in requests:
        assert request["target"] == "/devices/list"


def test_client_serializes_search_params_of_every_verb(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params={"device_ids": ["device1"]})
        seam.client.delete("/access_codes/delete", params={"sync": True})

    assert [(request["method"], request["query"]) for request in requests] == [
        ("GET", "device_ids=device1"),
        ("DELETE", "sync=true"),
    ]


def test_client_passes_search_params_it_did_not_serialize_to_httpx(recording_server):
    """Params that are not a mapping are left for httpx to encode.

    A caller who serialized the params themselves, e.g. to the pairs of a
    ``UrlSearchParams``, has already chosen how they are represented.
    """

    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.get("/devices/list", params=[("device_ids", "device1")])

    [request] = requests

    assert request["query"] == "device_ids=device1"


def test_client_rejects_a_search_param_it_cannot_serialize(recording_server):
    with recording_server([(200, DEVICES)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        with pytest.raises(UnserializableParamError):
            seam.client.get("/devices/list", params={"search": object()})

    assert requests == []


def test_client_serializes_null_in_a_json_body_to_null(recording_server):
    with recording_server([(200, DEVICE)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.post(
            "/devices/update",
            json={
                "device_id": "device1",
                "name": NULL,
                "properties": {"code": NULL},
                "codes": [NULL, "1234"],
            },
        )

    [request] = requests

    assert request["method"] == "POST"
    assert request["body"] == {
        "device_id": "device1",
        "name": None,
        "properties": {"code": None},
        "codes": [None, "1234"],
    }


def test_client_leaves_a_json_body_without_null_unchanged(recording_server):
    body = {"device_id": "device1", "name": "Front Door", "limit": 20, "sync": True}

    with recording_server([(200, DEVICE)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.post("/devices/update", json=body)

    [request] = requests

    assert request["body"] == body


def test_client_serializes_the_search_params_of_a_generated_route(recording_server):
    with recording_server([(200, DEVICE)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.devices.get(name="Front Door")

    [request] = requests

    assert request["method"] == "GET"
    assert request["path"] == "/devices/get"
    assert request["query"] == "name=Front+Door"
