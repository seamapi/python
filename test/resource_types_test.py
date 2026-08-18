# mypy: warn_unused_ignores=True

from typing import Literal, assert_type

from seam.resources import AccessCode, ActionAttempt, UnmanagedAccessCode


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
    credential: ActionAttempt.Result.AcsCredentialOnSeam,
) -> None:
    assert_type(code.is_backup_access_code_available, bool)
    assert_type(code.errors[0].is_access_code_error, Literal[True] | None)
    assert_type(unmanaged_code.errors[0].is_connected_account_error, bool | None)
    assert_type(credential.is_managed, Literal[True, False])


def _assert_opposite_literal_is_rejected(code: UnmanagedAccessCode) -> None:
    code.is_managed = True  # type: ignore[assignment]


def test_access_code_resources_narrow_on_is_managed():
    assert callable(_assert_access_code_narrowing)
    assert callable(_assert_boolean_shapes)
    assert callable(_assert_opposite_literal_is_rejected)
