from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostats, ActionAttempt, Device
from .thermostats_daily_programs import ThermostatsDailyPrograms
from .thermostats_schedules import ThermostatsSchedules
from .thermostats_simulate import ThermostatsSimulate
from ..modules.action_attempts import resolve_action_attempt


class Thermostats(AbstractThermostats):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._daily_programs = ThermostatsDailyPrograms(
            client=client, defaults=defaults
        )
        self._schedules = ThermostatsSchedules(client=client, defaults=defaults)
        self._simulate = ThermostatsSimulate(client=client, defaults=defaults)

    @property
    def daily_programs(self) -> ThermostatsDailyPrograms:
        return self._daily_programs

    @property
    def schedules(self) -> ThermostatsSchedules:
        return self._schedules

    @property
    def simulate(self) -> ThermostatsSimulate:
        return self._simulate

    def activate_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post(
            "/thermostats/activate_climate_preset", json=json_payload
        )

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

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

        res = self.client.post("/thermostats/cool", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def create_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None
    ) -> None:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
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

        self.client.post("/thermostats/create_climate_preset", json=json_payload)

        return None

    def delete_climate_preset(self, *, climate_preset_key: str, device_id: str) -> None:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/thermostats/delete_climate_preset", json=json_payload)

        return None

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

        res = self.client.post("/thermostats/heat", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def heat_cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
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
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if sync is not None:
            json_payload["sync"] = sync

        res = self.client.post("/thermostats/heat_cool", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        exclude_if: Optional[List[str]] = None,
        include_if: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        page_cursor: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[Device]:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            json_payload["created_before"] = created_before
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if customer_ids is not None:
            json_payload["customer_ids"] = customer_ids
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if exclude_if is not None:
            json_payload["exclude_if"] = exclude_if
        if include_if is not None:
            json_payload["include_if"] = include_if
        if limit is not None:
            json_payload["limit"] = limit
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if unstable_location_id is not None:
            json_payload["unstable_location_id"] = unstable_location_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/thermostats/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]

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

        res = self.client.post("/thermostats/off", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def set_fallback_climate_preset(
        self, *, climate_preset_key: str, device_id: str
    ) -> None:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/thermostats/set_fallback_climate_preset", json=json_payload)

        return None

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

        res = self.client.post("/thermostats/set_fan_mode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def set_hvac_mode(
        self,
        *,
        device_id: str,
        hvac_mode_setting: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        res = self.client.post("/thermostats/set_hvac_mode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def set_temperature_threshold(
        self,
        *,
        device_id: str,
        lower_limit_celsius: Optional[float] = None,
        lower_limit_fahrenheit: Optional[float] = None,
        upper_limit_celsius: Optional[float] = None,
        upper_limit_fahrenheit: Optional[float] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if lower_limit_celsius is not None:
            json_payload["lower_limit_celsius"] = lower_limit_celsius
        if lower_limit_fahrenheit is not None:
            json_payload["lower_limit_fahrenheit"] = lower_limit_fahrenheit
        if upper_limit_celsius is not None:
            json_payload["upper_limit_celsius"] = upper_limit_celsius
        if upper_limit_fahrenheit is not None:
            json_payload["upper_limit_fahrenheit"] = upper_limit_fahrenheit

        self.client.post("/thermostats/set_temperature_threshold", json=json_payload)

        return None

    def update_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        manual_override_allowed: bool,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        name: Optional[str] = None
    ) -> None:
        json_payload = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if name is not None:
            json_payload["name"] = name

        self.client.post("/thermostats/update_climate_preset", json=json_payload)

        return None

    def update_weekly_program(
        self,
        *,
        device_id: str,
        friday_program_id: Optional[str] = None,
        monday_program_id: Optional[str] = None,
        saturday_program_id: Optional[str] = None,
        sunday_program_id: Optional[str] = None,
        thursday_program_id: Optional[str] = None,
        tuesday_program_id: Optional[str] = None,
        wednesday_program_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if friday_program_id is not None:
            json_payload["friday_program_id"] = friday_program_id
        if monday_program_id is not None:
            json_payload["monday_program_id"] = monday_program_id
        if saturday_program_id is not None:
            json_payload["saturday_program_id"] = saturday_program_id
        if sunday_program_id is not None:
            json_payload["sunday_program_id"] = sunday_program_id
        if thursday_program_id is not None:
            json_payload["thursday_program_id"] = thursday_program_id
        if tuesday_program_id is not None:
            json_payload["tuesday_program_id"] = tuesday_program_id
        if wednesday_program_id is not None:
            json_payload["wednesday_program_id"] = wednesday_program_id

        res = self.client.post("/thermostats/update_weekly_program", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
