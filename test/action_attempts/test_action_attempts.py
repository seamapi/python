from seam import Seam


def test_action_attempts(seam: Seam):

    # Create an ActionAttempt
    some_device = seam.devices.list()[0]
    unlock_door = seam.locks.unlock_door(device_id=some_device.device_id)

    # Retrieve the ActionAttempt
    retrieved_action_attempt = seam.action_attempts.get(
        action_attempt_id=unlock_door.action_attempt_id
    )

    # Check that the retrieved ActionAttempt has the expected properties
    assert retrieved_action_attempt.action_attempt_id == unlock_door.action_attempt_id

    # Create multiple ActionAttempts
    some_device = seam.devices.list()[0]
    unlock_door1 = seam.locks.unlock_door(device_id=some_device.device_id)
    unlock_door2 = seam.locks.unlock_door(device_id=some_device.device_id)

    # Retrieve the list of ActionAttempts
    action_attempts = seam.action_attempts.list(
        action_attempt_ids=[
            unlock_door1.action_attempt_id,
            unlock_door2.action_attempt_id,
        ]
    )

    # Check that the retrieved ActionAttempts have the expected properties
    assert len(action_attempts) == 2
    assert action_attempts[0].action_attempt_id == unlock_door1.action_attempt_id
    assert action_attempts[1].action_attempt_id == unlock_door2.action_attempt_id

    # Create an ActionAttempt
    some_device = seam.devices.list()[0]
    unlock_door = seam.locks.unlock_door(device_id=some_device.device_id)

    # Poll until the ActionAttempt is ready
    action_attempt = seam.action_attempts.poll_until_ready(
        action_attempt_id=unlock_door.action_attempt_id
    )

    # Check that the ActionAttempt is not pending
    assert action_attempt.status != "pending"
