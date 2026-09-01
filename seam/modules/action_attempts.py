from typing import Dict, Optional, Union, cast
import asyncio
import time

from ..client import AsyncSeamHttpClient, SeamHttpClient
from ..exceptions import (
    SeamActionAttemptFailedError,
    SeamActionAttemptTimeoutError,
    SeamActionAttemptUnknownStatusError,
)
from ..options import SeamInvalidOptionsError
from ..resources import (
    ActionAttempt,
    ErrorActionAttempt,
    PendingActionAttempt,
    SuccessActionAttempt,
    action_attempt_from_dict,
)
from ..response import unwrap

TIMEOUT = 5.0
POLLING_INTERVAL = 0.5

WAIT_FOR_ACTION_ATTEMPT_OPTION_KEYS = ("timeout", "polling_interval")


def _status_of(action_attempt: ActionAttempt) -> Optional[str]:
    """Read the status without assuming the attempt carries one.

    An attempt from a newer API deserializes to a DeepAttrDict, where a missing
    key raises rather than reading as None.
    """

    return getattr(action_attempt, "status", None)


def validate_wait_for_action_attempt(
    value: Optional[Union[bool, Dict[str, float]]],
) -> None:
    if isinstance(value, bool):
        return

    if isinstance(value, dict):
        for key, option in value.items():
            if key not in WAIT_FOR_ACTION_ATTEMPT_OPTION_KEYS:
                raise SeamInvalidOptionsError(
                    f"The wait_for_action_attempt option got an unknown key {key!r}, "
                    'expected "timeout" or "polling_interval"'
                )

            if isinstance(option, bool) or not isinstance(option, (int, float)):
                raise SeamInvalidOptionsError(
                    f"The wait_for_action_attempt option {key!r} must be a number, "
                    f"got {type(option).__name__}"
                )

        return

    raise SeamInvalidOptionsError(
        "The wait_for_action_attempt option must be a bool or a dict with "
        f'"timeout" and "polling_interval" keys, got {type(value).__name__}'
    )


def normalize_wait_for_action_attempt(
    value: Optional[Union[bool, Dict[str, float]]],
) -> Union[bool, Dict[str, float]]:
    """Resolve None to the default and reject anything but a bool or options dict."""

    if value is None:
        return True

    validate_wait_for_action_attempt(value)

    return value


def validate_poll_options(timeout: float, polling_interval: float) -> None:
    # Written as negated comparisons so NaN fails both checks.
    if not timeout >= 0:
        raise SeamInvalidOptionsError(
            f"The timeout option must not be negative, got {timeout}"
        )

    if not polling_interval > 0:
        raise SeamInvalidOptionsError(
            f"The polling_interval option must be greater than zero, got {polling_interval}"
        )


def get_action_attempt(client: SeamHttpClient, action_attempt_id: str) -> ActionAttempt:
    res = client.get(
        "/action_attempts/get", params={"action_attempt_id": action_attempt_id}
    )

    return action_attempt_from_dict(
        unwrap(res, "action_attempt", "/action_attempts/get")
    )


def poll_until_ready(
    client: SeamHttpClient,
    *,
    action_attempt_id: str,
    timeout: float = TIMEOUT,
    polling_interval: float = POLLING_INTERVAL,
    action_attempt: Optional[ActionAttempt] = None,
) -> SuccessActionAttempt:
    validate_poll_options(timeout, polling_interval)

    deadline = time.monotonic() + timeout

    if action_attempt is None:
        action_attempt = get_action_attempt(client, action_attempt_id)

    while _status_of(action_attempt) == "pending":
        remaining = deadline - time.monotonic()

        if remaining <= 0:
            raise SeamActionAttemptTimeoutError(
                cast(PendingActionAttempt, action_attempt), timeout
            )

        time.sleep(min(polling_interval, remaining))

        action_attempt = get_action_attempt(client, action_attempt_id)

    if _status_of(action_attempt) == "error":
        raise SeamActionAttemptFailedError(cast(ErrorActionAttempt, action_attempt))

    # Neither pending, success, nor error: a status added after this SDK release.
    # Waiting cannot conclude, so say so rather than pass it off as a success.
    status = _status_of(action_attempt)
    if status != "success":
        raise SeamActionAttemptUnknownStatusError(action_attempt, str(status))

    return cast(SuccessActionAttempt, action_attempt)


def resolve_action_attempt(
    client: SeamHttpClient,
    *,
    action_attempt: ActionAttempt,
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]],
) -> ActionAttempt:
    validate_wait_for_action_attempt(wait_for_action_attempt)

    if wait_for_action_attempt is True:
        return poll_until_ready(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            action_attempt=action_attempt,
        )

    if isinstance(wait_for_action_attempt, dict):
        return poll_until_ready(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            timeout=wait_for_action_attempt.get("timeout", TIMEOUT),
            polling_interval=wait_for_action_attempt.get(
                "polling_interval", POLLING_INTERVAL
            ),
            action_attempt=action_attempt,
        )

    return action_attempt


async def get_action_attempt_async(
    client: AsyncSeamHttpClient, action_attempt_id: str
) -> ActionAttempt:
    res = await client.get(
        "/action_attempts/get", params={"action_attempt_id": action_attempt_id}
    )

    return action_attempt_from_dict(
        unwrap(res, "action_attempt", "/action_attempts/get")
    )


async def poll_until_ready_async(
    client: AsyncSeamHttpClient,
    *,
    action_attempt_id: str,
    timeout: float = TIMEOUT,
    polling_interval: float = POLLING_INTERVAL,
    action_attempt: Optional[ActionAttempt] = None,
) -> SuccessActionAttempt:
    validate_poll_options(timeout, polling_interval)

    deadline = time.monotonic() + timeout

    if action_attempt is None:
        action_attempt = await get_action_attempt_async(client, action_attempt_id)

    while _status_of(action_attempt) == "pending":
        remaining = deadline - time.monotonic()

        if remaining <= 0:
            raise SeamActionAttemptTimeoutError(
                cast(PendingActionAttempt, action_attempt), timeout
            )

        await asyncio.sleep(min(polling_interval, remaining))

        action_attempt = await get_action_attempt_async(client, action_attempt_id)

    if _status_of(action_attempt) == "error":
        raise SeamActionAttemptFailedError(cast(ErrorActionAttempt, action_attempt))

    # Neither pending, success, nor error: a status added after this SDK release.
    # Waiting cannot conclude, so say so rather than pass it off as a success.
    status = _status_of(action_attempt)
    if status != "success":
        raise SeamActionAttemptUnknownStatusError(action_attempt, str(status))

    return cast(SuccessActionAttempt, action_attempt)


async def resolve_action_attempt_async(
    client: AsyncSeamHttpClient,
    *,
    action_attempt: ActionAttempt,
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]],
) -> ActionAttempt:
    validate_wait_for_action_attempt(wait_for_action_attempt)

    if wait_for_action_attempt is True:
        return await poll_until_ready_async(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            action_attempt=action_attempt,
        )

    if isinstance(wait_for_action_attempt, dict):
        return await poll_until_ready_async(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            timeout=wait_for_action_attempt.get("timeout", TIMEOUT),
            polling_interval=wait_for_action_attempt.get(
                "polling_interval", POLLING_INTERVAL
            ),
            action_attempt=action_attempt,
        )

    return action_attempt
