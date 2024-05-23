from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostatsClimateSettingSchedules, ClimateSettingSchedule


class ThermostatsClimateSettingSchedules(AbstractThermostatsClimateSettingSchedules):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        device_id: str,
        schedule_ends_at: str,
        schedule_starts_at: str,
        automatic_cooling_enabled: Optional[bool] = None,
        automatic_heating_enabled: Optional[bool] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
        schedule_type: Optional[str] = None
    ) -> ClimateSettingSchedule:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if schedule_ends_at is not None:
            json_payload["schedule_ends_at"] = schedule_ends_at
        if schedule_starts_at is not None:
            json_payload["schedule_starts_at"] = schedule_starts_at
        if automatic_cooling_enabled is not None:
            json_payload["automatic_cooling_enabled"] = automatic_cooling_enabled
        if automatic_heating_enabled is not None:
            json_payload["automatic_heating_enabled"] = automatic_heating_enabled
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name
        if schedule_type is not None:
            json_payload["schedule_type"] = schedule_type

        res = self.client.post(
            "/thermostats/climate_setting_schedules/create", json=json_payload
        )

        return ClimateSettingSchedule.from_dict(res["climate_setting_schedule"])

    def delete(self, *, climate_setting_schedule_id: str) -> None:
        json_payload = {}

        if climate_setting_schedule_id is not None:
            json_payload["climate_setting_schedule_id"] = climate_setting_schedule_id

        self.client.post(
            "/thermostats/climate_setting_schedules/delete", json=json_payload
        )

        return None

    def get(
        self,
        *,
        climate_setting_schedule_id: Optional[str] = None,
        device_id: Optional[str] = None
    ) -> ClimateSettingSchedule:
        json_payload = {}

        if climate_setting_schedule_id is not None:
            json_payload["climate_setting_schedule_id"] = climate_setting_schedule_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post(
            "/thermostats/climate_setting_schedules/get", json=json_payload
        )

        return ClimateSettingSchedule.from_dict(res["climate_setting_schedule"])

    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[ClimateSettingSchedule]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post(
            "/thermostats/climate_setting_schedules/list", json=json_payload
        )

        return [
            ClimateSettingSchedule.from_dict(item)
            for item in res["climate_setting_schedules"]
        ]

    def update(
        self,
        *,
        climate_setting_schedule_id: str,
        automatic_cooling_enabled: Optional[bool] = None,
        automatic_heating_enabled: Optional[bool] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
        schedule_ends_at: Optional[str] = None,
        schedule_starts_at: Optional[str] = None,
        schedule_type: Optional[str] = None
    ) -> None:
        json_payload = {}

        if climate_setting_schedule_id is not None:
            json_payload["climate_setting_schedule_id"] = climate_setting_schedule_id
        if automatic_cooling_enabled is not None:
            json_payload["automatic_cooling_enabled"] = automatic_cooling_enabled
        if automatic_heating_enabled is not None:
            json_payload["automatic_heating_enabled"] = automatic_heating_enabled
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name
        if schedule_ends_at is not None:
            json_payload["schedule_ends_at"] = schedule_ends_at
        if schedule_starts_at is not None:
            json_payload["schedule_starts_at"] = schedule_starts_at
        if schedule_type is not None:
            json_payload["schedule_type"] = schedule_type

        self.client.post(
            "/thermostats/climate_setting_schedules/update", json=json_payload
        )

        return None
