from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostatsSimulate


class ThermostatsSimulate(AbstractThermostatsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def temperature_reached(
        self,
        *,
        device_id: str,
        temperature_celsius: Optional[float] = None,
        temperature_fahrenheit: Optional[float] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if temperature_celsius is not None:
            json_payload["temperature_celsius"] = temperature_celsius
        if temperature_fahrenheit is not None:
            json_payload["temperature_fahrenheit"] = temperature_fahrenheit

        self.client.post("/thermostats/simulate/temperature_reached", json=json_payload)

        return None
