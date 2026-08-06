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

    response = seam.client.post(
        "/devices/list",
        json={"device_ids": [seed["august_device_1"], seed["ecobee_device_1"]]},
    )

    device_ids = [device["device_id"] for device in response["devices"]]

    assert len(device_ids) == 2
    assert seed["august_device_1"] in device_ids
    assert seed["ecobee_device_1"] in device_ids
