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

    def connect_to_hub(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect_to_hub", json=json_payload)

        return None

    def disconnect(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect", json=json_payload)

        return None

    def disconnect_from_hub(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect_from_hub", json=json_payload)

        return None

    def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_expired is not None:
            json_payload["is_expired"] = is_expired

        self.client.post("/devices/simulate/paid_subscription", json=json_payload)

        return None

    def remove(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/remove", json=json_payload)

        return None
