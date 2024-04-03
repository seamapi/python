from seam.types import AbstractDevicesSimulate, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union


class DevicesSimulate(AbstractDevicesSimulate):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def remove(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.seam.make_request("POST", "/devices/simulate/remove", json=json_payload)

        return None
