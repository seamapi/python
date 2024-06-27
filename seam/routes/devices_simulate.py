from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractDevicesSimulate


class DevicesSimulate(AbstractDevicesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def connect(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect", json=json_payload)

        return None

    def disconnect(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect", json=json_payload)

        return None

    def remove(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/remove", json=json_payload)

        return None
