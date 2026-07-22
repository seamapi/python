from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostatsSchedules, ThermostatSchedule


class ThermostatsSchedules(AbstractThermostatsSchedules):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        ends_at: str,
        starts_at: str,
        is_override_allowed: Optional[bool] = None,
        max_override_period_minutes: Optional[int] = None,
        name: Optional[str] = None
    ) -> ThermostatSchedule:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if name is not None:
            json_payload["name"] = name

        res = self.client.post("/thermostats/schedules/create", json=json_payload)

        return ThermostatSchedule.from_dict(res["thermostat_schedule"])

    def delete(self, *, thermostat_schedule_id: str) -> None:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id

        self.client.post("/thermostats/schedules/delete", json=json_payload)

        return None

    def get(self, *, thermostat_schedule_id: str) -> ThermostatSchedule:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id

        res = self.client.post("/thermostats/schedules/get", json=json_payload)

        return ThermostatSchedule.from_dict(res["thermostat_schedule"])

    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[ThermostatSchedule]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/thermostats/schedules/list", json=json_payload)

        return [
            ThermostatSchedule.from_dict(item) for item in res["thermostat_schedules"]
        ]

    def update(
        self,
        *,
        thermostat_schedule_id: str,
        climate_preset_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_override_allowed: Optional[bool] = None,
        max_override_period_minutes: Optional[int] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None
    ) -> None:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        self.client.post("/thermostats/schedules/update", json=json_payload)

        return None
