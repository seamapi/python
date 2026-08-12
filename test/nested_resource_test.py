"""Regression tests for generated nested resource types."""

import dataclasses

import pytest

import seam.resources.device as device_module
from seam.resources.acs_user import AcsUser
from seam.resources.action_attempt import ActionAttempt
from seam.resources.device import Device


def test_nested_objects_are_typed_and_drop_unknown_fields():
    device = Device.from_dict(
        {
            "properties": {"locked": True, "future_api_field": "ignored"},
            "errors": [{"error_code": "offline", "message": "Offline"}],
            "custom_metadata": {"arbitrary": {"future": True}},
        }
    )

    assert isinstance(device.properties, Device.Properties)
    assert device.properties.locked is True
    assert not hasattr(device.properties, "future_api_field")
    assert isinstance(device.errors[0], Device.Errors)
    assert device.errors[0].error_code == "offline"
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


def test_action_attempt_union_hydrates_nested_result_and_error():
    attempt = ActionAttempt.from_dict(
        {
            "result": {"was_confirmed_by_device": True},
            "error": {"message": "failed", "type": "device_error"},
        }
    )

    assert isinstance(attempt.result, ActionAttempt.Result)
    assert attempt.result.was_confirmed_by_device is True
    assert isinstance(attempt.error, ActionAttempt.Error)
    assert attempt.error.message == "failed"


def test_merged_variants_keep_every_variant_field():
    result_fields = {f.name for f in dataclasses.fields(ActionAttempt.Result)}

    # One field from each of several action attempt variants.
    assert "was_confirmed_by_device" in result_fields
    assert "acs_credential_on_encoder" in result_fields
    assert "instant_key_url" in result_fields

    encoded = ActionAttempt.from_dict(
        {
            "action_type": "ENCODE_ACS_CREDENTIAL",
            "result": {
                "acs_credential_on_encoder": {"card_number": "123"},
                "acs_credential_on_seam": {"acs_credential_id": "cred_1"},
            },
        }
    )
    assert encoded.result.acs_credential_on_encoder.card_number == "123"
    assert encoded.result.acs_credential_on_seam.acs_credential_id == "cred_1"

    instant_key = ActionAttempt.from_dict(
        {
            "action_type": "CREATE_INSTANT_KEY",
            "result": {"instant_key_url": "https://x"},
        }
    )
    assert instant_key.result.instant_key_url == "https://x"


def test_merged_variants_recurse_into_nested_objects():
    from_fields = {f.name for f in dataclasses.fields(AcsUser.PendingMutations.From)}

    # Each of these arrives from a different pending mutation variant.
    assert "full_name" in from_fields
    assert "starts_at" in from_fields
    assert "is_suspended" in from_fields
    assert "acs_access_group_id" in from_fields


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

    # Nested shapes stay off the module namespace.
    assert not hasattr(device_module, "DeviceProperties")
