import time
from threading import Timer

import pytest

from seam.exceptions import SeamActionAttemptTimeoutError, SeamActionAttemptFailedError
from seam import AsyncSeam, Seam, SeamInvalidOptionsError

PENDING_ACTION_ATTEMPT_ID = "11111111-1111-1111-1111-111111111111"

PENDING_ACTION_ATTEMPT_RESPONSE = {
    "action_attempt": {
        "action_attempt_id": PENDING_ACTION_ATTEMPT_ID,
        "action_type": "UNLOCK_DOOR",
        "status": "pending",
        "result": None,
        "error": None,
    }
}


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
            wait_for_action_attempt={"timeout": 0.1},
        )

    assert exc_info.value.action_attempt == action_attempt


def test_wait_for_action_attempt_rejects_when_action_attempt_fails(server):
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
            "status": "error",
            "error": {"message": "Failed", "type": "foo"},
        },
    )

    with pytest.raises(SeamActionAttemptFailedError, match="Failed") as exc_info:
        seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt=True,
        )

    assert (
        exc_info.value.action_attempt.action_attempt_id
        == action_attempt.action_attempt_id
    )
    assert exc_info.value.action_attempt.status == "error"
    assert exc_info.value.code == "foo"


def test_wait_for_action_attempt_times_out_if_waiting_for_polling_interval(server):
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

    start = time.monotonic()

    with pytest.raises(SeamActionAttemptTimeoutError) as exc_info:
        seam.action_attempts.get(
            action_attempt_id=action_attempt.action_attempt_id,
            wait_for_action_attempt={"timeout": 0.5, "polling_interval": 5},
        )

    # The wait sleeps only the time remaining until the deadline, never a
    # full polling_interval past it.
    assert time.monotonic() - start < 2.5

    assert exc_info.value.action_attempt == action_attempt


def test_wait_for_action_attempt_rejects_a_zero_polling_interval(recording_server):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (
        endpoint,
        requests,
    ):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        with pytest.raises(
            SeamInvalidOptionsError,
            match="The polling_interval option must be greater than zero, got 0",
        ):
            seam.action_attempts.get(
                action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                wait_for_action_attempt={"timeout": 1, "polling_interval": 0},
            )

        assert len(requests) == 1


def test_wait_for_action_attempt_rejects_a_negative_polling_interval(recording_server):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        with pytest.raises(
            SeamInvalidOptionsError,
            match="The polling_interval option must be greater than zero, got -1",
        ):
            seam.action_attempts.get(
                action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                wait_for_action_attempt={"timeout": 1, "polling_interval": -1},
            )


def test_wait_for_action_attempt_rejects_a_negative_timeout(recording_server):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        with pytest.raises(
            SeamInvalidOptionsError,
            match="The timeout option must not be negative, got -1",
        ):
            seam.action_attempts.get(
                action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                wait_for_action_attempt={"timeout": -1},
            )


def test_wait_for_action_attempt_polls_at_least_once_before_timing_out(
    recording_server,
):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (
        endpoint,
        requests,
    ):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        start = time.monotonic()

        with pytest.raises(SeamActionAttemptTimeoutError):
            seam.action_attempts.get(
                action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                wait_for_action_attempt={"timeout": 0.1, "polling_interval": 60},
            )

        # One request resolves the route, and the wait still polls once
        # before the deadline passes instead of sleeping a full interval.
        assert len(requests) == 2
        assert time.monotonic() - start < 5


def test_wait_for_action_attempt_polls_with_the_generated_route_shape(
    recording_server,
):
    success_response = {
        "action_attempt": {
            **PENDING_ACTION_ATTEMPT_RESPONSE["action_attempt"],
            "status": "success",
            "result": {},
        }
    }

    with recording_server(
        [(200, PENDING_ACTION_ATTEMPT_RESPONSE), (200, success_response)]
    ) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        action_attempt = seam.action_attempts.get(
            action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
            wait_for_action_attempt={"timeout": 5, "polling_interval": 0.05},
        )

        assert action_attempt.status == "success"

        # The poll goes through the same wire shape as the generated route:
        # a GET with the id and _strict in the query, and no request body.
        poll_request = requests[1]
        assert poll_request["method"] == "GET"
        assert poll_request["path"] == "/action_attempts/get"
        assert f"action_attempt_id={PENDING_ACTION_ATTEMPT_ID}" in poll_request["query"]
        assert "_strict=true" in poll_request["query"]
        assert poll_request["body"] is None


def test_wait_for_action_attempt_retries_a_failed_poll(recording_server):
    success_response = {
        "action_attempt": {
            **PENDING_ACTION_ATTEMPT_RESPONSE["action_attempt"],
            "status": "success",
            "result": {},
        }
    }

    with recording_server(
        [
            (200, PENDING_ACTION_ATTEMPT_RESPONSE),
            (503, {"error": {"type": "service_unavailable", "message": "Down"}}),
            (200, success_response),
        ]
    ) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        action_attempt = seam.action_attempts.get(
            action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
            wait_for_action_attempt={"timeout": 5, "polling_interval": 0.05},
        )

        # A transient 503 mid-wait is retried instead of aborting the wait.
        assert action_attempt.status == "success"
        assert len(requests) == 3


async def test_wait_for_action_attempt_rejects_a_zero_polling_interval_async(
    recording_server,
):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (
        endpoint,
        requests,
    ):
        async with AsyncSeam(api_key="seam_apikey_token", endpoint=endpoint) as seam:
            with pytest.raises(
                SeamInvalidOptionsError,
                match="The polling_interval option must be greater than zero, got 0",
            ):
                await seam.action_attempts.get(
                    action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                    wait_for_action_attempt={"timeout": 1, "polling_interval": 0},
                )

            assert len(requests) == 1


async def test_wait_for_action_attempt_polls_at_least_once_before_timing_out_async(
    recording_server,
):
    with recording_server([(200, PENDING_ACTION_ATTEMPT_RESPONSE)]) as (
        endpoint,
        requests,
    ):
        async with AsyncSeam(api_key="seam_apikey_token", endpoint=endpoint) as seam:
            start = time.monotonic()

            with pytest.raises(SeamActionAttemptTimeoutError):
                await seam.action_attempts.get(
                    action_attempt_id=PENDING_ACTION_ATTEMPT_ID,
                    wait_for_action_attempt={"timeout": 0.1, "polling_interval": 60},
                )

            assert len(requests) == 2
            assert time.monotonic() - start < 5
