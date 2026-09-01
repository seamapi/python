"""Regression tests for reading responses that do not match the generated shape."""

from seam.deep_attr_dict import DeepAttrDict
from seam.exceptions import SeamActionAttemptUnknownStatusError
from seam.modules.action_attempts import poll_until_ready
from seam.resources.device import Device
from seam.resources.action_attempt import action_attempt_from_dict
from seam.resources.seam_event import (
    AccessCodeCreatedEvent,
    seam_event_from_dict,
)


def test_a_list_property_sent_as_a_scalar_reads_as_empty():
    device = Device.from_dict({"device_id": "d", "errors": "oops"})

    assert isinstance(device.errors, list)
    assert not device.errors


def test_a_list_item_that_is_not_an_object_is_kept_verbatim():
    device = Device.from_dict({"device_id": "d", "errors": ["nope"]})

    assert device.errors == ["nope"]


def test_an_unknown_error_code_keeps_the_rest_of_the_resource():
    device = Device.from_dict(
        {
            "device_id": "d",
            "errors": [{"error_code": "brand_new", "message": "m"}],
        }
    )

    assert device.device_id == "d"
    assert isinstance(device.errors[0], DeepAttrDict)
    assert device.errors[0].error_code == "brand_new"


def test_a_nested_object_sent_as_a_scalar_reads_as_none():
    device = Device.from_dict({"device_id": "d", "location": "nope"})

    assert device.location is None


def test_a_payload_that_is_not_an_object_still_yields_a_resource():
    device = Device.from_dict("not an object")

    assert device.device_id is None


def test_an_unknown_event_type_stays_readable():
    event = seam_event_from_dict(
        {
            "event_id": "e",
            "event_type": "future.thing",
            "future_field": {"nested": True},
        }
    )

    assert isinstance(event, DeepAttrDict)
    assert event.future_field.nested is True


def test_a_known_event_survives_one_malformed_field():
    event = seam_event_from_dict(
        {
            "event_id": "e",
            "event_type": "access_code.created",
            "access_code_id": "a",
            "device_custom_metadata": "not an object",
        }
    )

    assert isinstance(event, AccessCodeCreatedEvent)
    assert event.access_code_id == "a"
    assert event.device_custom_metadata == "not an object"


def test_an_unknown_action_attempt_status_stays_readable():
    attempt = action_attempt_from_dict(
        {"action_attempt_id": "aa", "action_type": "LOCK_DOOR", "status": "cancelled"}
    )

    assert isinstance(attempt, DeepAttrDict)
    assert attempt.status == "cancelled"


def test_a_discriminator_that_is_not_a_string_does_not_match_a_variant():
    event = seam_event_from_dict({"event_id": "e", "event_type": 42})

    assert isinstance(event, DeepAttrDict)


def test_waiting_on_an_unknown_status_raises_rather_than_claiming_success():
    attempt = action_attempt_from_dict(
        {"action_attempt_id": "aa", "action_type": "LOCK_DOOR", "status": "cancelled"}
    )

    try:
        poll_until_ready(None, action_attempt_id="aa", action_attempt=attempt)
    except SeamActionAttemptUnknownStatusError as error:
        assert error.status == "cancelled"
        assert "cancelled" in str(error)
    else:
        raise AssertionError("expected SeamActionAttemptUnknownStatusError")


def test_waiting_on_an_attempt_with_no_status_does_not_raise_attribute_error():
    attempt = action_attempt_from_dict({"action_attempt_id": "aa"})

    try:
        poll_until_ready(None, action_attempt_id="aa", action_attempt=attempt)
    except SeamActionAttemptUnknownStatusError as error:
        assert error.status == "None"
    else:
        raise AssertionError("expected SeamActionAttemptUnknownStatusError")
