"""The SDK does not explode on values it does not recognize."""

import json


from seam.exceptions import SeamActionAttemptUnknownStatusError
from seam.modules.action_attempts import poll_until_ready
from seam.resources.action_attempt import action_attempt_from_dict
from seam.resources.device import Device
from seam.resources.seam_event import UnrecognizedEvent, seam_event_from_dict


def test_an_unknown_enum_value_reads_as_itself():
    device = Device.from_dict({"device_id": "device_1", "device_type": "future_lock"})

    assert device.device_type == "future_lock"


def test_an_unknown_event_type_falls_back_to_a_generic_event():
    event = seam_event_from_dict(
        {"event_id": "event_1", "event_type": "future.thing", "nested": {"x": 1}}
    )

    assert isinstance(event, UnrecognizedEvent)
    assert event.event_type == "future.thing"
    assert event.workspace_id is None


def test_an_unknown_error_code_keeps_the_rest_of_the_resource():
    device = Device.from_dict(
        {
            "device_id": "device_1",
            "errors": [{"error_code": "brand_new", "message": "m"}],
        }
    )

    assert device.device_id == "device_1"
    assert device.errors[0].error_code == "brand_new"


def test_an_unknown_action_attempt_status_reads_as_itself():
    attempt = action_attempt_from_dict(
        {"action_attempt_id": "aa", "action_type": "LOCK_DOOR", "status": "cancelled"}
    )

    assert attempt.status == "cancelled"


def test_waiting_on_an_unknown_status_raises_rather_than_claiming_success():
    attempt = action_attempt_from_dict(
        {"action_attempt_id": "aa", "action_type": "LOCK_DOOR", "status": "cancelled"}
    )

    try:
        poll_until_ready(None, action_attempt_id="aa", action_attempt=attempt)
    except SeamActionAttemptUnknownStatusError as error:
        assert error.status == "cancelled"
    else:
        raise AssertionError("expected SeamActionAttemptUnknownStatusError")


def test_raw_json_recovers_a_field_the_generated_shape_drops():
    payload = {
        "event_id": "event_1",
        "event_type": "access_code.created",
        "brand_new_field": "kept",
    }

    event = seam_event_from_dict(payload)

    assert not hasattr(event, "brand_new_field")
    assert json.loads(event.raw_json()) == payload


def test_raw_json_round_trips_an_unrecognized_event():
    payload = {"event_id": "event_1", "event_type": "future.thing", "nested": {"x": 1}}

    assert json.loads(seam_event_from_dict(payload).raw_json()) == payload


def test_raw_json_is_scoped_to_events():
    assert not hasattr(Device.from_dict({"device_id": "device_1"}), "raw_json")


def test_an_unrecognized_action_attempt_reads_its_common_fields():
    attempt = action_attempt_from_dict(
        {
            "action_attempt_id": "aa",
            "action_type": "LOCK_DOOR",
            "status": "cancelled",
            "error": {"type": "x", "message": "m"},
        }
    )

    assert attempt.action_attempt_id == "aa"
    assert attempt.status == "cancelled"
    assert attempt.error["message"] == "m"
    assert attempt.result == {}
