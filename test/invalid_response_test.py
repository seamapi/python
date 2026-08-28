import pytest

from seam import AsyncSeam, Seam, SeamError, SeamHttpInvalidResponseError

DEVICE_ID = "22222222-2222-2222-2222-222222222222"


def make_seam(endpoint):
    return Seam.from_api_key("seam_apikey_token", endpoint=endpoint)


def test_a_response_missing_the_expected_key_raises(recording_server):
    with recording_server([(200, {"wrong_key": {}})]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match="Seam returned an invalid response for /devices/get: "
            'expected "device", which the response does not contain',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_null_response_body_raises(recording_server):
    with recording_server([(200, None)]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "device", got NoneType instead of a response object',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_string_response_body_raises(recording_server):
    with recording_server([(200, '"a json string"', "application/json")]) as (
        endpoint,
        _,
    ):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "device", got str instead of a response object',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_non_json_gateway_page_raises(recording_server):
    with recording_server(
        [(200, "<html>Scheduled maintenance</html>", "application/json")]
    ) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "device", got str instead of a response object',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_plain_text_response_raises(recording_server):
    with recording_server([(200, "ok")]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "device", got str instead of a response object',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_non_object_value_under_the_response_key_raises(recording_server):
    with recording_server([(200, {"device": "not-an-object"})]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "device", got str instead of an object',
        ):
            seam.devices.get(device_id=DEVICE_ID)


def test_a_non_list_value_under_a_list_response_key_raises(recording_server):
    with recording_server([(200, {"devices": {"not": "a list"}})]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match="Seam returned an invalid response for /devices/list: "
            'expected "devices", got dict instead of a list',
        ):
            seam.devices.list()


def test_a_malformed_poll_response_raises_mid_wait(recording_server):
    pending_response = {
        "action_attempt": {
            "action_attempt_id": "11111111-1111-1111-1111-111111111111",
            "action_type": "UNLOCK_DOOR",
            "status": "pending",
            "result": None,
            "error": None,
        }
    }

    with recording_server([(200, pending_response), (200, {"nonsense": True})]) as (
        endpoint,
        _,
    ):
        seam = make_seam(endpoint)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match="Seam returned an invalid response for /action_attempts/get: "
            'expected "action_attempt", which the response does not contain',
        ):
            seam.action_attempts.get(
                action_attempt_id="11111111-1111-1111-1111-111111111111",
                wait_for_action_attempt={"timeout": 5, "polling_interval": 0.05},
            )


def test_the_invalid_response_error_is_a_seam_error(recording_server):
    with recording_server([(200, {"wrong_key": {}})]) as (endpoint, _):
        seam = make_seam(endpoint)

        with pytest.raises(SeamError) as exc_info:
            seam.devices.get(device_id=DEVICE_ID)

    assert isinstance(exc_info.value, SeamHttpInvalidResponseError)
    assert exc_info.value.path == "/devices/get"
    assert exc_info.value.response_key == "device"


async def test_a_response_missing_the_expected_key_raises_async(recording_server):
    with recording_server([(200, {"wrong_key": {}})]) as (endpoint, _):
        async with AsyncSeam(api_key="seam_apikey_token", endpoint=endpoint) as seam:
            with pytest.raises(
                SeamHttpInvalidResponseError,
                match='expected "device", which the response does not contain',
            ):
                await seam.devices.get(device_id=DEVICE_ID)


async def test_a_non_list_value_under_a_list_response_key_raises_async(
    recording_server,
):
    with recording_server([(200, {"devices": None})]) as (endpoint, _):
        async with AsyncSeam(api_key="seam_apikey_token", endpoint=endpoint) as seam:
            with pytest.raises(
                SeamHttpInvalidResponseError,
                match='expected "devices", got NoneType instead of a list',
            ):
                await seam.devices.list()
