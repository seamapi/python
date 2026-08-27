# mypy: warn_unused_ignores=True

from typing import Any, Dict, Literal, Union, assert_type

from seam.resources import (
    AccessCode,
    AccessCodeCreatedEvent,
    ActionAttempt,
    Device,
    LockDoorActionAttempt,
    LockDoorSuccessActionAttempt,
    NoiseSensorNoiseThresholdTriggeredEvent,
    ScanCredentialSuccessActionAttempt,
    SeamEvent,
    UnmanagedAccessCode,
)


def _assert_access_code_narrowing(
    code: AccessCode | UnmanagedAccessCode,
) -> None:
    if code.is_managed:
        assert_type(code, AccessCode)
    else:
        assert_type(code, UnmanagedAccessCode)


def _assert_boolean_shapes(
    code: AccessCode,
    unmanaged_code: UnmanagedAccessCode,
    credential: ScanCredentialSuccessActionAttempt.Result.AcsCredentialOnSeam,
) -> None:
    assert_type(code.is_backup_access_code_available, bool)
    error = code.errors[0]
    if error.error_code == "failed_to_set_on_device":
        assert_type(error, AccessCode.FailedToSetOnDeviceError)
        assert_type(error.is_access_code_error, Literal[True])

    unmanaged_error = unmanaged_code.errors[0]
    if unmanaged_error.error_code == "account_disconnected":
        assert_type(
            unmanaged_error,
            UnmanagedAccessCode.AccountDisconnectedError,
        )
        assert_type(unmanaged_error.is_connected_account_error, Literal[True])

    assert_type(credential.is_managed, Literal[True, False])


def _assert_event_narrowing(event: SeamEvent) -> None:
    if event.event_type == "access_code.created":
        assert_type(event, AccessCodeCreatedEvent)
        assert_type(
            event.connected_account_custom_metadata,
            Dict[str, Union[str, bool]] | None,
        )
    elif event.event_type == "noise_sensor.noise_threshold_triggered":
        assert_type(event, NoiseSensorNoiseThresholdTriggeredEvent)
        assert_type(event.minut_metadata, Dict[str, Any] | None)


def _assert_action_attempt_narrowing(attempt: ActionAttempt) -> None:
    if attempt.action_type == "LOCK_DOOR":
        assert_type(attempt, LockDoorActionAttempt)
        assert_type(
            attempt.result,
            LockDoorSuccessActionAttempt.Result | None,
        )
        if attempt.status == "success":
            assert_type(attempt, LockDoorSuccessActionAttempt)
            assert_type(attempt.result, LockDoorSuccessActionAttempt.Result)


def _assert_record_value_types(device: Device) -> None:
    assert_type(device.custom_metadata, Dict[str, Union[str, bool]])


def _assert_opposite_literal_is_rejected(code: UnmanagedAccessCode) -> None:
    code.is_managed = True  # type: ignore[assignment]


def test_resource_types_narrow_on_discriminants():
    assert callable(_assert_access_code_narrowing)
    assert callable(_assert_boolean_shapes)
    assert callable(_assert_event_narrowing)
    assert callable(_assert_action_attempt_narrowing)
    assert callable(_assert_record_value_types)
    assert callable(_assert_opposite_literal_is_rejected)
