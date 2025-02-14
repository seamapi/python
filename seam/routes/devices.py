from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractDevices


class Devices(AbstractDevices):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/delete", json=json_payload)

        return None
