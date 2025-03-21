from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractThermostats, ActionAttempt, Device
from .thermostats_schedules import ThermostatsSchedules
from .thermostats_simulate import ThermostatsSimulate
from ..modules.action_attempts import resolve_action_attempt


class Thermostats(AbstractThermostats, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._schedules = ThermostatsSchedules(client=client, defaults=defaults)
        self._simulate = ThermostatsSimulate(client=client, defaults=defaults)

    @property
    def schedules(self) -> ThermostatsSchedules:
        return self._schedules

    @property
    def simulate(self) -> ThermostatsSimulate:
        return self._simulate

    def activate_climate_preset(
        self,
        *,
        device_id: str,
        climate_preset_key: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/activate_climate_preset",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/cool",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )

    def create_climate_preset(
        self,
        *,
        device_id: str,
        climate_preset_key: str,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        hvac_mode_setting: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
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

        return None

    def delete_climate_preset(self, *, device_id: str, climate_preset_key: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key

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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/heat",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/heat_cool",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
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
        exclude_if: Optional[List[str]] = None,
        unstable_location_id: Optional[str] = None
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
        if unstable_location_id is not None:
            json_payload["unstable_location_id"] = unstable_location_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/list",
                method="POST",
                body=json_payload,
                response_key="devices",
                model_type=List[Device],
            ),
        )

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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/off",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )

    def set_fallback_climate_preset(
        self, *, device_id: str, climate_preset_key: str
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key

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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/set_fan_mode",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )

    def set_hvac_mode(
        self,
        *,
        hvac_mode_setting: str,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/thermostats/set_hvac_mode",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
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

        return None

    def update_climate_preset(
        self,
        *,
        device_id: str,
        climate_preset_key: str,
        manual_override_allowed: bool,
        name: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        hvac_mode_setting: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
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

        return None
