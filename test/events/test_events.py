import time
from seam import Seam

from seam.types import SeamHttpApiError

SINCE = "2021-01-01T00:00:00.000Z"
EVENT_TYPE = "device.connected"
FAKE_UUID = "00000000-0000-0000-0000-000000000000"


def test_events(seam: Seam):

    events = seam.events.list(since=SINCE)
    event = events[0]

    event_by_id = seam.events.get(event_id=event.event_id)
    assert event_by_id.event_id == event.event_id

    event_by_type = seam.events.get(event_type=event.event_type)
    assert event_by_type.event_type == event.event_type

    event_by_device_id = seam.events.get(device_id=event.device_id)
    assert event_by_device_id.device_id == event.device_id

    try:
        seam.events.get(event_id=FAKE_UUID)
    except SeamHttpApiError as e:
        assert e.metadata["message"] == "Event not found"
