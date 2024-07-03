import pytest
from seam import Seam


def test_wait_for_action_attempt_directly_on_returned_action_attempt(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False)

    action_attempt = seam.locks.unlock_door(
        device_id=seed["august_device_1"],
        wait_for_action_attempt=True
    )

    assert action_attempt.status == "success"


def test_wait_for_action_attempt_by_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    action_attempt = seam.locks.unlock_door(
        device_id=seed["august_device_1"]
    )

    assert action_attempt.status == "success"


def test_wait_for_action_attempt_can_set_class_default(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False)

    action_attempt = seam.locks.unlock_door(
        device_id=seed["august_device_1"]
    )

    assert action_attempt.status == "pending"


def test_wait_for_action_attempt_can_set_class_default_with_object(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"],
        endpoint=endpoint,
        wait_for_action_attempt={"timeout": 5000}
    )

    action_attempt = seam.locks.unlock_door(
        device_id=seed["august_device_1"]
    )

    assert action_attempt.status == "success"
