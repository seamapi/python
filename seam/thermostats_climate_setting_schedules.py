from seam.types import (
    AbstractThermostatsClimateSettingSchedules,
    AbstractSeam as Seam,
    ClimateSettingSchedule,
)
from typing import Optional, Any, List, Dict, Union


class ThermostatsClimateSettingSchedules(AbstractThermostatsClimateSettingSchedules):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def create(
        self,
        *,
        device_id: str,
        schedule_starts_at: str,
        schedule_ends_at: str,
        schedule_type: Optional[str] = None,
        name: Optional[str] = None,
        automatic_heating_enabled: Optional[bool] = None,
        automatic_cooling_enabled: Optional[bool] = None,
        hvac_mode_setting: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        manual_override_allowed: Optional[bool] = None
    ) -> ClimateSettingSchedule:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if schedule_starts_at is not None:
            json_payload["schedule_starts_at"] = schedule_starts_at
        if schedule_ends_at is not None:
            json_payload["schedule_ends_at"] = schedule_ends_at
        if schedule_type is not None:
            json_payload["schedule_type"] = schedule_type
        if name is not None:
            json_payload["name"] = name
        if automatic_heating_enabled is not None:
            json_payload["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not None:
            json_payload["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed

        res = self.seam.make_request(
            "POST", "/thermostats/climate_setting_schedules/create", json=json_payload
        )

        return ClimateSettingSchedule.from_dict(res["climate_setting_schedule"])

    def delete(self, *, climate_setting_schedule_id: str) -> None:
        json_payload = {}

        if climate_setting_schedule_id is not None:
            json_payload["climate_setting_schedule_id"] = climate_setting_schedule_id

        self.seam.make_request(
            "POST", "/thermostats/climate_setting_schedules/delete", json=json_payload
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

        res = self.seam.make_request(
            "POST", "/thermostats/climate_setting_schedules/get", json=json_payload
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

        res = self.seam.make_request(
            "POST", "/thermostats/climate_setting_schedules/list", json=json_payload
        )

        return [
            ClimateSettingSchedule.from_dict(item)
            for item in res["climate_setting_schedules"]
        ]

    def update(
        self,
        *,
        climate_setting_schedule_id: str,
        schedule_type: Optional[str] = None,
        name: Optional[str] = None,
        schedule_starts_at: Optional[str] = None,
        schedule_ends_at: Optional[str] = None,
        automatic_heating_enabled: Optional[bool] = None,
        automatic_cooling_enabled: Optional[bool] = None,
        hvac_mode_setting: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        manual_override_allowed: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if climate_setting_schedule_id is not None:
            json_payload["climate_setting_schedule_id"] = climate_setting_schedule_id
        if schedule_type is not None:
            json_payload["schedule_type"] = schedule_type
        if name is not None:
            json_payload["name"] = name
        if schedule_starts_at is not None:
            json_payload["schedule_starts_at"] = schedule_starts_at
        if schedule_ends_at is not None:
            json_payload["schedule_ends_at"] = schedule_ends_at
        if automatic_heating_enabled is not None:
            json_payload["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not None:
            json_payload["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed

        self.seam.make_request(
            "POST", "/thermostats/climate_setting_schedules/update", json=json_payload
        )

        return None
