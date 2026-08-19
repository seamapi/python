"""Regression tests for generated nested resource types."""

import dataclasses
from typing import Any, cast

import pytest

import seam.resources.device as device_module
from seam.resources.acs_user import AcsUser
from seam.resources.action_attempt import (
    LockDoorActionAttempt,
    ScanCredentialActionAttempt,
    action_attempt_from_dict,
)
from seam.resources.device import Device
from seam.resources.seam_event import (
    AccessCodeCreatedEvent,
    seam_event_from_dict,
)


def test_nested_objects_are_typed_and_drop_unknown_fields():
    device = Device.from_dict(
        {
            "properties": {"locked": True, "future_api_field": "ignored"},
            "errors": [{"error_code": "device_offline", "message": "Offline"}],
            "custom_metadata": {"arbitrary": {"future": True}},
        }
    )

    assert isinstance(device.properties, Device.Properties)
    assert device.properties.locked is True
    assert not hasattr(device.properties, "future_api_field")
    assert isinstance(device.errors[0], Device.DeviceOfflineError)
    assert device.errors[0].error_code == "device_offline"
    assert device.custom_metadata["arbitrary"]["future"] is True


def test_nested_objects_keep_dictionary_style_reads():
    properties = Device.Properties.from_dict({"locked": True})

    assert properties["locked"] is True
    assert properties.get("locked") is True
    assert properties.get("missing", "default") == "default"
    assert "locked" in properties
    assert "locked" in properties.keys()
    assert "locked" in list(properties)
    with pytest.raises(AttributeError):
        _ = properties.typo  # pylint: disable=no-member


def test_missing_nested_values_use_stable_defaults():
    device = Device.from_dict({"errors": None})

    assert device.properties is None
    assert isinstance(device.errors, list)
    assert len(device.errors) == 0


def test_event_union_dispatches_and_keeps_unknown_events_readable():
    event = seam_event_from_dict({"event_type": "access_code.created"})
    unknown = cast(
        Any,
        seam_event_from_dict(
            {"event_type": "future.event", "future_api_field": "kept"}
        ),
    )

    assert isinstance(event, AccessCodeCreatedEvent)
    assert unknown.event_type == "future.event"
    assert unknown.future_api_field == "kept"


def test_action_attempt_union_hydrates_nested_result_and_error():
    attempt = action_attempt_from_dict(
        {
            "action_type": "LOCK_DOOR",
            "result": {"was_confirmed_by_device": True},
            "error": {"message": "failed", "type": "device_error"},
        }
    )

    assert isinstance(attempt, LockDoorActionAttempt)
    assert isinstance(attempt.result, LockDoorActionAttempt.Result)
    assert attempt.result.was_confirmed_by_device is True
    assert isinstance(attempt.error, LockDoorActionAttempt.Error)
    assert attempt.error.message == "failed"

    pending = action_attempt_from_dict(
        {"action_type": "LOCK_DOOR", "status": "pending"}
    )
    assert pending.error is None
    assert pending.result is None


def test_action_attempt_variants_keep_distinct_result_shapes():
    lock_fields = {f.name for f in dataclasses.fields(LockDoorActionAttempt.Result)}
    scan_fields = {
        f.name for f in dataclasses.fields(ScanCredentialActionAttempt.Result)
    }

    assert "was_confirmed_by_device" in lock_fields
    assert "acs_credential_on_encoder" not in lock_fields
    assert "acs_credential_on_encoder" in scan_fields
    assert "was_confirmed_by_device" not in scan_fields


def test_discriminated_list_variants_keep_distinct_nested_objects():
    information_fields = {
        f.name
        for f in dataclasses.fields(AcsUser.UpdatingUserInformationPendingMutation.From)
    }
    schedule_fields = {
        f.name
        for f in dataclasses.fields(AcsUser.UpdatingAccessSchedulePendingMutation.From)
    }

    assert "full_name" in information_fields
    assert "starts_at" not in information_fields
    assert "starts_at" in schedule_fields
    assert "full_name" not in schedule_fields


def test_same_named_nested_objects_keep_distinct_shapes():
    device = Device.from_dict(
        {
            "properties": {
                "battery": {"level": 0.5, "status": "good"},
                "accessory_keypad": {"battery": {"level": 0.25}},
            }
        }
    )

    battery = device.properties.battery
    assert isinstance(battery, Device.Properties.Battery)
    assert battery.status == "good"

    keypad_battery = device.properties.accessory_keypad.battery
    assert isinstance(keypad_battery, Device.Properties.AccessoryKeypad.Battery)
    assert keypad_battery.level == 0.25
    assert not isinstance(keypad_battery, Device.Properties.Battery)


def test_nested_classes_are_scoped_to_their_owner():
    preset_metadata = Device.Properties.AvailableClimatePresets.EcobeeMetadata
    device_metadata = Device.Properties.EcobeeMetadata

    assert preset_metadata is not device_metadata
    assert "climate_ref" in preset_metadata.__dataclass_fields__
    assert "ecobee_device_id" in device_metadata.__dataclass_fields__

    assert not hasattr(device_module, "DeviceProperties")
