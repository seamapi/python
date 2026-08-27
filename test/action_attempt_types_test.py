# mypy: warn_unused_ignores=True

"""Static and runtime checks for status-discriminated action attempts.

The ``_assert_*`` functions are compile-time tests: mypy checks that
narrowing on ``status`` recovers the per-status classes, and the
``type: ignore`` comments assert that the flagged expressions are type
errors, since an ignore that suppresses nothing fails the mypy run here.
"""

from typing import Any, Literal, assert_type, cast

from seam.client import SeamHttpClient
from seam.modules.action_attempts import poll_until_ready
from seam.resources import (
    ErrorActionAttempt,
    LockDoorActionAttempt,
    LockDoorErrorActionAttempt,
    LockDoorPendingActionAttempt,
    LockDoorSuccessActionAttempt,
    PendingActionAttempt,
    SuccessActionAttempt,
    action_attempt_from_dict,
)


def _assert_unnarrowed_dereference_is_rejected(
    attempt: LockDoorActionAttempt,
) -> None:
    _ = attempt.result.was_confirmed_by_device  # type: ignore[union-attr]
    _ = attempt.error.message  # type: ignore[union-attr]


def _assert_success_narrowing_needs_no_none_check(
    attempt: LockDoorActionAttempt,
) -> None:
    if attempt.status == "success":
        assert_type(attempt, LockDoorSuccessActionAttempt)
        assert_type(attempt.result, LockDoorSuccessActionAttempt.Result)
        assert_type(attempt.result.was_confirmed_by_device, bool | None)
        assert_type(attempt.error, None)


def _assert_error_narrowing_needs_no_none_check(
    attempt: LockDoorActionAttempt,
) -> None:
    if attempt.status == "error":
        assert_type(attempt, LockDoorErrorActionAttempt)
        assert_type(attempt.error, LockDoorErrorActionAttempt.Error)
        assert_type(attempt.error.message, str)
        assert_type(attempt.error.type, str)
        assert_type(attempt.result, None)


def _assert_isinstance_narrowing_needs_no_none_check(
    attempt: LockDoorActionAttempt,
) -> None:
    if isinstance(attempt, LockDoorSuccessActionAttempt):
        assert_type(attempt.result, LockDoorSuccessActionAttempt.Result)
    if isinstance(attempt, LockDoorErrorActionAttempt):
        assert_type(attempt.error, LockDoorErrorActionAttempt.Error)


def _assert_waiting_returns_the_success_union(client: SeamHttpClient) -> None:
    attempt = poll_until_ready(client, action_attempt_id="attempt-id")
    assert_type(attempt, SuccessActionAttempt)
    assert_type(attempt.status, Literal["success"])
    if attempt.action_type == "LOCK_DOOR":
        assert_type(attempt, LockDoorSuccessActionAttempt)
        assert_type(attempt.result, LockDoorSuccessActionAttempt.Result)
        assert_type(attempt.error, None)


def _assert_pending_members_type_dependents_as_none(
    attempt: LockDoorPendingActionAttempt,
) -> None:
    assert_type(attempt.status, Literal["pending"])
    assert_type(attempt.error, None)
    assert_type(attempt.result, None)


def _assert_status_unions_cover_every_action_type(
    pending: PendingActionAttempt,
    failed: ErrorActionAttempt,
) -> None:
    assert_type(pending.status, Literal["pending"])
    assert_type(pending.error, None)
    assert_type(pending.result, None)
    assert_type(failed.status, Literal["error"])
    assert_type(failed.result, None)
    _ = failed.error.message


def test_from_dict_parses_a_pending_action_attempt():
    attempt = action_attempt_from_dict(
        {
            "action_attempt_id": "attempt-id",
            "action_type": "LOCK_DOOR",
            "status": "pending",
        }
    )

    assert isinstance(attempt, LockDoorPendingActionAttempt)
    assert attempt.status == "pending"
    assert attempt.result is None
    assert attempt.error is None


def test_from_dict_parses_a_successful_action_attempt():
    attempt = action_attempt_from_dict(
        {
            "action_attempt_id": "attempt-id",
            "action_type": "LOCK_DOOR",
            "status": "success",
            "result": {"was_confirmed_by_device": True},
        }
    )

    assert isinstance(attempt, LockDoorSuccessActionAttempt)
    assert attempt.status == "success"
    assert isinstance(attempt.result, LockDoorSuccessActionAttempt.Result)
    assert attempt.result.was_confirmed_by_device is True
    assert attempt.error is None


def test_from_dict_parses_a_failed_action_attempt():
    attempt = action_attempt_from_dict(
        {
            "action_attempt_id": "attempt-id",
            "action_type": "LOCK_DOOR",
            "status": "error",
            "error": {"message": "failed", "type": "device_error"},
        }
    )

    assert isinstance(attempt, LockDoorErrorActionAttempt)
    assert attempt.status == "error"
    assert isinstance(attempt.error, LockDoorErrorActionAttempt.Error)
    assert attempt.error.message == "failed"
    assert attempt.error.type == "device_error"
    assert attempt.result is None


def test_from_dict_keeps_unknown_statuses_readable():
    unknown = cast(
        Any,
        action_attempt_from_dict({"action_type": "LOCK_DOOR", "status": "cancelled"}),
    )

    assert unknown.action_type == "LOCK_DOOR"
    assert unknown.status == "cancelled"


def test_action_attempt_types_narrow_on_status():
    assert callable(_assert_unnarrowed_dereference_is_rejected)
    assert callable(_assert_success_narrowing_needs_no_none_check)
    assert callable(_assert_error_narrowing_needs_no_none_check)
    assert callable(_assert_isinstance_narrowing_needs_no_none_check)
    assert callable(_assert_waiting_returns_the_success_union)
    assert callable(_assert_pending_members_type_dependents_as_none)
    assert callable(_assert_status_unions_cover_every_action_type)
