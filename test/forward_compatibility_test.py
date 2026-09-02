"""The SDK does not explode on values it does not recognize.

Seam adds event types, action types, error codes, and enum values between SDK
releases. Reading them must not raise; writing logic against them is what an
upgrade is for.
"""

from seam.deep_attr_dict import DeepAttrDict
from seam.exceptions import SeamActionAttemptUnknownStatusError
from seam.modules.action_attempts import poll_until_ready
from seam.resources.action_attempt import action_attempt_from_dict
from seam.resources.device import Device
from seam.resources.seam_event import seam_event_from_dict


def test_an_unknown_enum_value_reads_as_itself():
    device = Device.from_dict({"device_id": "device_1", "device_type": "future_lock"})

    assert device.device_type == "future_lock"


def test_an_unknown_event_type_falls_back_to_a_generic_event():
    event = seam_event_from_dict(
        {"event_id": "event_1", "event_type": "future.thing", "nested": {"x": 1}}
    )

    assert isinstance(event, DeepAttrDict)
    assert event.event_type == "future.thing"


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


# Waiting promises a succeeded attempt or a raise, so an unrecognized status is
# the one place the SDK must not stay quiet: returning it would report a success
# the SDK cannot vouch for.
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
