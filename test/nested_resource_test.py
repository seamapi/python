"""Regression tests for generated nested resource types."""

import pytest

from seam.resources.action_attempt import (
    ActionAttempt,
    ActionAttemptError,
    ActionAttemptResult,
)
from seam.resources.device import Device, DeviceErrors, DeviceProperties


def test_nested_objects_are_typed_and_drop_unknown_fields():
    device = Device.from_dict(
        {
            "properties": {"locked": True, "future_api_field": "ignored"},
            "errors": [{"error_code": "offline", "message": "Offline"}],
            "custom_metadata": {"arbitrary": {"future": True}},
        }
    )

    assert isinstance(device.properties, DeviceProperties)
    assert device.properties.locked is True
    assert not hasattr(device.properties, "future_api_field")
    assert isinstance(device.errors[0], DeviceErrors)
    assert device.errors[0].error_code == "offline"
    assert device.custom_metadata["arbitrary"]["future"] is True


def test_nested_objects_keep_dictionary_style_reads():
    properties = DeviceProperties.from_dict({"locked": True})

    assert properties["locked"] is True
    assert properties.get("locked") is True
    assert properties.get("missing", "default") == "default"
    assert "locked" in properties
    assert "locked" in properties.keys()
    assert "locked" in list(properties)
    with pytest.raises(AttributeError):
        _ = properties.typo


def test_missing_nested_values_use_stable_defaults():
    device = Device.from_dict({"errors": None})

    assert device.properties is None
    assert device.errors == []


def test_action_attempt_union_hydrates_nested_result_and_error():
    attempt = ActionAttempt.from_dict(
        {
            "result": {"was_confirmed_by_device": True},
            "error": {"message": "failed", "type": "device_error"},
        }
    )

    assert isinstance(attempt.result, ActionAttemptResult)
    assert attempt.result.was_confirmed_by_device is True
    assert isinstance(attempt.error, ActionAttemptError)
    assert attempt.error.message == "failed"
