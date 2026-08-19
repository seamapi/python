from typing import Dict, Optional, Union
import asyncio
import time

from ..client import AsyncSeamHttpClient, SeamHttpClient
from ..exceptions import SeamActionAttemptFailedError, SeamActionAttemptTimeoutError
from ..resources import ActionAttempt, action_attempt_from_dict

TIMEOUT = 5.0
POLLING_INTERVAL = 0.5


def get_action_attempt(client: SeamHttpClient, action_attempt_id: str) -> ActionAttempt:
    res = client.post(
        "/action_attempts/get", json={"action_attempt_id": action_attempt_id}
    )

    return action_attempt_from_dict(res["action_attempt"])


def poll_until_ready(
    client: SeamHttpClient,
    *,
    action_attempt_id: str,
    timeout: float = TIMEOUT,
    polling_interval: float = POLLING_INTERVAL,
) -> ActionAttempt:
    time_waiting = 0.0

    action_attempt = get_action_attempt(client, action_attempt_id)

    while action_attempt.status == "pending":
        time.sleep(polling_interval)
        time_waiting += polling_interval

        if time_waiting > timeout:
            raise SeamActionAttemptTimeoutError(action_attempt, timeout)

        action_attempt = get_action_attempt(client, action_attempt_id)

    if action_attempt.status == "error":
        raise SeamActionAttemptFailedError(action_attempt)

    return action_attempt


def resolve_action_attempt(
    client: SeamHttpClient,
    *,
    action_attempt: ActionAttempt,
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]],
) -> ActionAttempt:
    if wait_for_action_attempt is True:
        return poll_until_ready(
            client=client, action_attempt_id=action_attempt.action_attempt_id
        )

    if isinstance(wait_for_action_attempt, dict):
        return poll_until_ready(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            timeout=wait_for_action_attempt.get("timeout", TIMEOUT),
            polling_interval=wait_for_action_attempt.get(
                "polling_interval", POLLING_INTERVAL
            ),
        )

    return action_attempt


async def get_action_attempt_async(
    client: AsyncSeamHttpClient, action_attempt_id: str
) -> ActionAttempt:
    res = await client.post(
        "/action_attempts/get", json={"action_attempt_id": action_attempt_id}
    )

    return action_attempt_from_dict(res["action_attempt"])


async def poll_until_ready_async(
    client: AsyncSeamHttpClient,
    *,
    action_attempt_id: str,
    timeout: float = TIMEOUT,
    polling_interval: float = POLLING_INTERVAL,
) -> ActionAttempt:
    time_waiting = 0.0

    action_attempt = await get_action_attempt_async(client, action_attempt_id)

    while action_attempt.status == "pending":
        await asyncio.sleep(polling_interval)
        time_waiting += polling_interval

        if time_waiting > timeout:
            raise SeamActionAttemptTimeoutError(action_attempt, timeout)

        action_attempt = await get_action_attempt_async(client, action_attempt_id)

    if action_attempt.status == "error":
        raise SeamActionAttemptFailedError(action_attempt)

    return action_attempt


async def resolve_action_attempt_async(
    client: AsyncSeamHttpClient,
    *,
    action_attempt: ActionAttempt,
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]],
) -> ActionAttempt:
    if wait_for_action_attempt is True:
        return await poll_until_ready_async(
            client=client, action_attempt_id=action_attempt.action_attempt_id
        )

    if isinstance(wait_for_action_attempt, dict):
        return await poll_until_ready_async(
            client=client,
            action_attempt_id=action_attempt.action_attempt_id,
            timeout=wait_for_action_attempt.get("timeout", TIMEOUT),
            polling_interval=wait_for_action_attempt.get(
                "polling_interval", POLLING_INTERVAL
            ),
        )

    return action_attempt
