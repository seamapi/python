from seam import Seam, SeamHttpApiError
import pytest


def test_access_codes(seam: Seam):

    all_devices = seam.devices.list()
    some_device = all_devices[0]

    created_access_code = seam.access_codes.create(
        device_id=some_device.device_id, name="Test code", code="4444"
    )
    assert created_access_code.name == "Test code"
    assert created_access_code.status == "setting"

    seam.access_codes.create(
        device_id=some_device.device_id, name="Test code 2", code="5555"
    )

    access_codes = seam.access_codes.list(device_id=some_device.device_id)
    assert len(access_codes) == 2
    access_codes = seam.access_codes.list(
        device_id=some_device.device_id,
        access_code_ids=[created_access_code.access_code_id],
    )
    assert len(access_codes) == 1

    access_code = seam.access_codes.get(
        access_code_id=created_access_code.access_code_id
    )
    assert access_code.code == "4444"

    with pytest.raises(SeamHttpApiError):
        seam.access_codes.create(
            device_id=some_device.device_id, name="Duplicate Access Code", code="4444"
        )

    delete_action_attempt = seam.access_codes.delete(
        access_code_id=created_access_code.access_code_id
    )
    assert delete_action_attempt == None

    access_codes = seam.access_codes.create_multiple(
        device_ids=[device.device_id for device in all_devices]
    )
    assert len(set([ac.common_code_key for ac in access_codes])) == 1

    # Preferred Code Length Tests
    device_ids = [device.device_id for device in all_devices]

    access_codes_of_preferred_length = seam.access_codes.create_multiple(
        device_ids=device_ids, preferred_code_length=4
    )

    for access_codes in access_codes_of_preferred_length:
        assert len(access_codes.code) == 4

    access_codes_of_longer_length = seam.access_codes.create_multiple(
        device_ids=device_ids, preferred_code_length=6
    )

    for access_codes in access_codes_of_longer_length:
        assert len(access_codes.code) == 6
