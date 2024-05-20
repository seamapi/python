from seam import Seam, SeamApiException


def test_devices(seam: Seam):
    devices = seam.devices.list()
    assert len(devices) > 0

    connected_account = seam.connected_accounts.list()[0]
    connected_accounts = seam.connected_accounts.list()
    devices = seam.devices.list(
        connected_account_id=connected_account.connected_account_id
    )
    assert len(devices) > 0
    connected_account_ids = [
        account.connected_account_id for account in connected_accounts
    ]
    devices = seam.devices.list(connected_account_ids=connected_account_ids)
    assert len(devices) > 0

    devices = seam.devices.list(device_types=["august_lock"])
    assert len(devices) > 0
    devices = seam.devices.list(device_types=["august_lock"])
    assert len(devices) > 0

    devices = seam.devices.list(manufacturer="august")
    assert len(devices) > 0

    device_ids = [devices[0].device_id]
    devices = seam.devices.list(device_ids=device_ids)
    assert len(devices) == 1

    locks = seam.locks.list()
    assert len(locks) > 0

    some_device = seam.devices.get(name="Fake August Lock 1")
    assert some_device.properties.name == "Fake August Lock 1"

    some_lock = seam.locks.get(device_id=(some_device.device_id))
    assert some_lock.device_id == some_device.device_id

    assert some_lock.properties.locked == True

    seam.locks.unlock_door(device_id=(some_device.device_id))
    some_unlocked_lock = seam.locks.get(device_id=(some_device.device_id))
    assert some_unlocked_lock.properties.locked == False

    seam.locks.lock_door(device_id=(some_device.device_id))
    some_locked_lock = seam.locks.get(device_id=(some_device.device_id))
    assert some_locked_lock.properties.locked == True

    seam.devices.update(device_id=(some_device.device_id), name="Updated lock")
    some_updated_lock = seam.locks.get(device_id=(some_device.device_id))
    assert some_updated_lock.properties.name == "Updated lock"

    devices = seam.devices.list()
    seam.devices.delete(device_id=(some_updated_lock.device_id))
    assert len(seam.devices.list()) == len(devices) - 1

    # Test custom exception
    try:
        seam.devices.get(name="foo")
        assert False
    except SeamApiException as error:
        assert error.status_code == 404
        assert type(error.request_id) == str
        assert error.metadata["type"] == "device_not_found"

    stable_device_providers = seam.devices.list_device_providers(
        provider_category="stable"
    )
    assert len(stable_device_providers) > 0


def test_unmanaged_devices(seam: Seam):

    devices = seam.devices.list()
    assert len(devices) > 0

    unmanaged_devices = seam.devices.unmanaged.list()
    assert len(unmanaged_devices) == 0

    device = devices[0]

    seam.devices.update(device_id=device.device_id, is_managed=False)
    unmanaged_devices = seam.devices.unmanaged.list()
    assert len(unmanaged_devices) == 1

    unmanaged_device = seam.devices.unmanaged.get(device_id=device.device_id)
    assert unmanaged_device.device_id == device.device_id
    unmanaged_device = seam.devices.unmanaged.get(name=device.properties.name)
    assert unmanaged_device.properties.name == device.properties.name

    connected_account = seam.connected_accounts.list()[0]
    devices = seam.devices.unmanaged.list(
        connected_account_id=connected_account.connected_account_id
    )
    assert len(devices) > 0
    devices = seam.devices.unmanaged.list(
        connected_account_ids=[connected_account.connected_account_id]
    )
    assert len(devices) > 0

    devices = seam.devices.unmanaged.list(device_type="august_lock")
    assert len(devices) > 0
    devices = seam.devices.unmanaged.list(device_types=["august_lock"])
    assert len(devices) > 0

    devices = seam.devices.unmanaged.list(manufacturer="august")
    assert len(devices) > 0

    seam.devices.unmanaged.update(device_id=device.device_id, is_managed=True)
    unmanaged_devices = seam.devices.unmanaged.list()
    assert len(unmanaged_devices) == 0
