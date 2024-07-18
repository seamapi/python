import pytest
from threading import Timer
from seam.exceptions import SeamActionAttemptTimeoutError
from seam import Seam


def test_wait_for_action_attempt_directly_on_returned_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = seam.locks.unlock_door(
        device_id=seed["august_device_1"], wait_for_action_attempt=True
    )

    assert action_attempt.status == "success"


def test_wait_for_action_attempt_waits_by_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


def test_wait_for_action_attempt_can_set_class_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"


def test_wait_for_action_attempt_can_set_class_default_with_object(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"],
        endpoint=endpoint,
        wait_for_action_attempt={"timeout": 5000},
    )

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


def test_wait_for_action_attempt_waits_for_pending_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

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

    resolved_action_attempt = seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id, wait_for_action_attempt=True
    )

    assert resolved_action_attempt.status == "success"


def test_wait_for_action_attempt_returns_successful_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "success",
        },
    )

    successful_action_attempt = seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id
    )

    assert successful_action_attempt.status == "success"

    resolved_action_attempt = seam.action_attempts.get(
        action_attempt_id=action_attempt.action_attempt_id, wait_for_action_attempt=True
    )

    assert resolved_action_attempt == successful_action_attempt


def test_wait_for_action_attempt_times_out(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"

    seam.client.post(
        "/_fake/update_action_attempt",
        json={
            "action_attempt_id": action_attempt.action_attempt_id,
            "status": "pending",
        },
    )

    with pytest.raises(SeamActionAttemptTimeoutError) as exc_info:
        seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt={"timeout": 100},
        )

    assert exc_info.value.action_attempt == action_attempt
