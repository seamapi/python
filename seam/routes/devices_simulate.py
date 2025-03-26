from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractDevicesSimulate


class DevicesSimulate(AbstractDevicesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def access_code_lock(self, *, access_code_id: str, device_id: str) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/access_code_lock", json=json_payload)

        return None

    def access_code_unlock(self, *, access_code_id: str, device_id: str) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/access_code_unlock", json=json_payload)

        return None

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
