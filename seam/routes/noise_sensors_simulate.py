from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractNoiseSensorsSimulate


class NoiseSensorsSimulate(AbstractNoiseSensorsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def trigger_noise_threshold(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post(
            "/noise_sensors/simulate/trigger_noise_threshold", json=json_payload
        )

        return None
