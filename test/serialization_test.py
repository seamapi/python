from datetime import datetime, timezone

from seam import Seam


def test_serializes_array_params_when_omitted(seam: Seam):
    devices = seam.devices.list()
    database = seam.client.get("/_fake/database")

    assert len(devices) == len(database["devices"])


def test_serializes_array_params_when_none(seam: Seam):
    devices = seam.devices.list(device_ids=None)
    database = seam.client.get("/_fake/database")

    assert len(devices) == len(database["devices"])


def test_serializes_array_params_when_empty(seam: Seam):
    devices = seam.devices.list(device_ids=[])

    assert len(devices) == 0


def test_serializes_array_params_when_non_empty(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    devices = seam.devices.list(
        device_ids=[seed["august_device_1"], seed["ecobee_device_1"]]
    )

    assert len(devices) == 2

    device_ids = [device.device_id for device in devices]
    assert seed["august_device_1"] in device_ids
    assert seed["ecobee_device_1"] in device_ids


def test_serializes_array_params_when_explicitly_using_client(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    response = seam.client.get(
        "/devices/list",
        params={"device_ids": [seed["august_device_1"], seed["ecobee_device_1"]]},
    )

    device_ids = [device["device_id"] for device in response["devices"]]

    assert len(device_ids) == 2
    assert seed["august_device_1"] in device_ids
    assert seed["ecobee_device_1"] in device_ids


def test_serializes_array_params_when_empty_and_explicitly_using_get(seam: Seam):
    # The empty array is serialized to a single empty value, e.g., device_ids=,
    # which the Seam API parses back to the empty array.
    response = seam.client.get("/devices/list", params={"device_ids": []})

    assert len(response["devices"]) == 0


def test_serializes_array_params_when_none_and_explicitly_using_get(seam: Seam):
    response = seam.client.get("/devices/list", params={"device_ids": None})
    database = seam.client.get("/_fake/database")

    assert len(response["devices"]) == len(database["devices"])


def test_serializes_string_params_when_explicitly_using_get(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    response = seam.client.get(
        "/devices/get", params={"device_id": seed["august_device_1"]}
    )

    assert response["device"]["device_id"] == seed["august_device_1"]


def test_serializes_number_params_when_explicitly_using_get(seam: Seam):
    # A float is serialized as the Seam API expects a number, e.g., limit=2,
    # never as 2.0.
    response = seam.client.get("/devices/list", params={"limit": 2.0})

    assert len(response["devices"]) == 2


def test_serializes_datetime_params_when_explicitly_using_get(seam: Seam):
    created_before = datetime(2999, 1, 1, tzinfo=timezone.utc)

    response = seam.client.get(
        "/devices/list", params={"created_before": created_before}
    )
    database = seam.client.get("/_fake/database")

    assert len(response["devices"]) == len(database["devices"])


def test_serializes_params_for_a_route_using_the_semantic_method(server):
    # /devices/list is a GET, so its params are serialized to the query string.
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    devices = seam.devices.list(device_ids=[seed["august_device_1"]])

    assert [device.device_id for device in devices] == [seed["august_device_1"]]
