import pytest
from threading import Timer
from seam.exceptions import SeamActionAttemptTimeoutError, SeamActionAttemptFailedError
from seam import Seam


@pytest.mark.asyncio
async def test_wait_for_action_attempt_directly_on_returned_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(
        device_id=seed["august_device_1"], wait_for_action_attempt=True
    )

    assert action_attempt.status == "success"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_waits_by_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_can_set_class_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_can_set_class_default_with_object(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"],
        endpoint=endpoint,
        wait_for_action_attempt={"timeout": 5000},
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_waits_for_pending_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "pending",
        },
    )

    def update_action_attempt():
        seam.client.post(
            "/_fake/update_action_attempt",
            json={
                "action_attempt_id": action_attempt.action_attempt_id,
                "status": "success",
            },
        )

    # Use Timer to schedule the update after 1 second
    t = Timer(1.0, update_action_attempt)
    t.start()

    resolved_action_attempt = await seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id, wait_for_action_attempt=True
    )

    assert resolved_action_attempt.status == "success"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_returns_successful_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "success",
        },
    )

    successful_action_attempt = await seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id
    )

    assert successful_action_attempt.status == "success"

    resolved_action_attempt = await seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id, wait_for_action_attempt=True
    )

    assert resolved_action_attempt == successful_action_attempt


@pytest.mark.asyncio
async def test_wait_for_action_attempt_times_out(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "pending",
        },
    )

    with pytest.raises(SeamActionAttemptTimeoutError) as exc_info:
        await seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt={"timeout": 0.1},
        )

    assert exc_info.value.action_attempt == action_attempt


@pytest.mark.asyncio
async def test_wait_for_action_attempt_rejects_when_action_attempt_fails(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "error",
            "error": {"message": "Failed", "type": "foo"},
        },
    )

    with pytest.raises(SeamActionAttemptFailedError, match="Failed") as exc_info:
        await seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt=True,
        )

    assert (
        exc_info.value.action_attempt.action_attempt_id
        == action_attempt.action_attempt_id
    )
    assert exc_info.value.action_attempt.status == "error"
    assert exc_info.value.code == "foo"


@pytest.mark.asyncio
async def test_wait_for_action_attempt_times_out_if_waiting_for_polling_interval(
    server,
):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "pending",
        },
    )

    with pytest.raises(SeamActionAttemptTimeoutError) as exc_info:
        await seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt={"timeout": 0.5, "polling_interval": 5},
        )

    assert exc_info.value.action_attempt == action_attempt
