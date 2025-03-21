from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractThermostatsSchedules, ThermostatSchedule


class ThermostatsSchedules(AbstractThermostatsSchedules, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        device_id: str,
        climate_preset_key: str,
        starts_at: str,
        ends_at: str,
        name: Optional[str] = None,
        max_override_period_minutes: Optional[int] = None,
        is_override_allowed: Optional[bool] = None
    ) -> ThermostatSchedule:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if name is not None:
            json_payload["name"] = name
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/schedules/create",
                method="POST",
                body=json_payload,
                response_key="thermostat_schedule",
                model_type=ThermostatSchedule,
            ),
        )

    def delete(self, *, thermostat_schedule_id: str) -> None:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id

        return None

    def get(self, *, thermostat_schedule_id: str) -> ThermostatSchedule:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/schedules/get",
                method="POST",
                body=json_payload,
                response_key="thermostat_schedule",
                model_type=ThermostatSchedule,
            ),
        )

    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[ThermostatSchedule]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/schedules/list",
                method="POST",
                body=json_payload,
                response_key="thermostat_schedules",
                model_type=List[ThermostatSchedule],
            ),
        )

    def update(
        self,
        *,
        thermostat_schedule_id: str,
        name: Optional[str] = None,
        climate_preset_key: Optional[str] = None,
        max_override_period_minutes: Optional[int] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_override_allowed: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id
        if name is not None:
            json_payload["name"] = name
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed

        return None
