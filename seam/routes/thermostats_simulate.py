from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostatsSimulate


class ThermostatsSimulate(AbstractThermostatsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def hvac_mode_adjusted(
        self,
        *,
        device_id: str,
        hvac_mode: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if hvac_mode is not None:
            json_payload["hvac_mode"] = hvac_mode
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        self.client.post("/thermostats/simulate/hvac_mode_adjusted", json=json_payload)

        return None

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
