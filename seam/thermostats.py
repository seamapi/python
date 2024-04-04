from seam.types import AbstractThermostats, AbstractSeam as Seam, ActionAttempt, Device
from typing import Optional, Any, List, Dict, Union
from seam.thermostats_climate_setting_schedules import (
    ThermostatsClimateSettingSchedules,
)


class Thermostats(AbstractThermostats):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam
        self._climate_setting_schedules = ThermostatsClimateSettingSchedules(seam=seam)

    @property
    def climate_setting_schedules(self) -> ThermostatsClimateSettingSchedules:
        return self._climate_setting_schedules

    def cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if sync is not None:
            json_payload["sync"] = sync

        res = self.seam.make_request("POST", "/thermostats/cool", json=json_payload)

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.seam.make_request("POST", "/thermostats/get", json=json_payload)

        return Device.from_dict(res["thermostat"])

    def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if sync is not None:
            json_payload["sync"] = sync

        res = self.seam.make_request("POST", "/thermostats/heat", json=json_payload)

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def heat_cool(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if sync is not None:
            json_payload["sync"] = sync

        res = self.seam.make_request(
            "POST", "/thermostats/heat_cool", json=json_payload
        )

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def list(
        self,
        *,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        created_before: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        include_if: Optional[List[str]] = None,
        exclude_if: Optional[List[str]] = None
    ) -> List[Device]:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if limit is not None:
            json_payload["limit"] = limit
        if created_before is not None:
            json_payload["created_before"] = created_before
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if include_if is not None:
            json_payload["include_if"] = include_if
        if exclude_if is not None:
            json_payload["exclude_if"] = exclude_if

        res = self.seam.make_request("POST", "/thermostats/list", json=json_payload)

        return [Device.from_dict(item) for item in res["thermostats"]]

    def off(
        self,
        *,
        device_id: str,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if sync is not None:
            json_payload["sync"] = sync

        res = self.seam.make_request("POST", "/thermostats/off", json=json_payload)

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def set_fan_mode(
        self,
        *,
        device_id: str,
        fan_mode: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if fan_mode is not None:
            json_payload["fan_mode"] = fan_mode
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
        if sync is not None:
            json_payload["sync"] = sync

        res = self.seam.make_request(
            "POST", "/thermostats/set_fan_mode", json=json_payload
        )

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def update(
        self, *, device_id: str, default_climate_setting: Dict[str, Any]
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if default_climate_setting is not None:
            json_payload["default_climate_setting"] = default_climate_setting

        self.seam.make_request("POST", "/thermostats/update", json=json_payload)

        return None
