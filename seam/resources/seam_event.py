from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class SeamEvent:
    access_code_id: str
    connected_account_custom_metadata: Dict[str, Any]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Dict[str, Any]
    device_id: str
    event_description: str
    event_id: str
    event_type: str
    occurred_at: str
    workspace_id: str
    change_reason: str
    changed_properties: List[Dict[str, Any]]
    description: str
    from_: Dict[str, Any]
    to: Dict[str, Any]
    requested_mutations: List[Dict[str, Any]]
    code: str
    access_code_errors: List[Dict[str, Any]]
    access_code_warnings: List[Dict[str, Any]]
    connected_account_errors: List[Dict[str, Any]]
    connected_account_warnings: List[Dict[str, Any]]
    device_errors: List[Dict[str, Any]]
    device_warnings: List[Dict[str, Any]]
    backup_access_code_id: str
    access_grant_id: str
    acs_entrance_id: str
    access_grant_key: str
    ends_at: str
    starts_at: str
    error_message: str
    missing_device_ids: List[str]
    access_grant_ids: List[str]
    access_grant_keys: List[str]
    access_method_id: str
    is_backup_code: bool
    acs_system_id: str
    acs_system_errors: List[Dict[str, Any]]
    acs_system_warnings: List[Dict[str, Any]]
    acs_credential_id: str
    acs_user_id: str
    acs_encoder_id: str
    acs_access_group_id: str
    client_session_id: str
    connect_webview_id: str
    customer_key: str
    connected_account_type: str
    action_attempt_id: str
    action_type: str
    status: str
    error_code: str
    battery_level: float
    battery_status: str
    device_name: str
    minut_metadata: Dict[str, Any]
    noise_level_decibels: float
    noise_level_nrs: float
    noise_threshold_id: str
    noise_threshold_name: str
    noiseaware_metadata: Dict[str, Any]
    access_code_is_managed: bool
    is_via_bluetooth: bool
    is_via_nfc: bool
    method: str
    user_identity_id: str
    reason: Dict[str, Any]
    climate_preset_key: str
    is_fallback_climate_preset: bool
    thermostat_schedule_id: str
    cooling_set_point_celsius: float
    cooling_set_point_fahrenheit: float
    fan_mode_setting: str
    heating_set_point_celsius: float
    heating_set_point_fahrenheit: float
    hvac_mode_setting: str
    lower_limit_celsius: float
    lower_limit_fahrenheit: float
    temperature_celsius: float
    temperature_fahrenheit: float
    upper_limit_celsius: float
    upper_limit_fahrenheit: float
    desired_temperature_celsius: float
    desired_temperature_fahrenheit: float
    activation_reason: str
    image_url: str
    motion_sub_type: str
    video_url: str
    acs_entrance_ids: List[str]
    device_ids: List[str]
    space_id: str
    space_key: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return SeamEvent(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            change_reason=d.get("change_reason", None),
            changed_properties=d.get("changed_properties", None),
            description=d.get("description", None),
            from_=DeepAttrDict(d.get("from", None)),
            to=DeepAttrDict(d.get("to", None)),
            requested_mutations=d.get("requested_mutations", None),
            code=d.get("code", None),
            access_code_errors=d.get("access_code_errors", None),
            access_code_warnings=d.get("access_code_warnings", None),
            connected_account_errors=d.get("connected_account_errors", None),
            connected_account_warnings=d.get("connected_account_warnings", None),
            device_errors=d.get("device_errors", None),
            device_warnings=d.get("device_warnings", None),
            backup_access_code_id=d.get("backup_access_code_id", None),
            access_grant_id=d.get("access_grant_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            access_grant_key=d.get("access_grant_key", None),
            ends_at=d.get("ends_at", None),
            starts_at=d.get("starts_at", None),
            error_message=d.get("error_message", None),
            missing_device_ids=d.get("missing_device_ids", None),
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            is_backup_code=d.get("is_backup_code", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_system_errors=d.get("acs_system_errors", None),
            acs_system_warnings=d.get("acs_system_warnings", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_access_group_id=d.get("acs_access_group_id", None),
            client_session_id=d.get("client_session_id", None),
            connect_webview_id=d.get("connect_webview_id", None),
            customer_key=d.get("customer_key", None),
            connected_account_type=d.get("connected_account_type", None),
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            status=d.get("status", None),
            error_code=d.get("error_code", None),
            battery_level=d.get("battery_level", None),
            battery_status=d.get("battery_status", None),
            device_name=d.get("device_name", None),
            minut_metadata=DeepAttrDict(d.get("minut_metadata", None)),
            noise_level_decibels=d.get("noise_level_decibels", None),
            noise_level_nrs=d.get("noise_level_nrs", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_name=d.get("noise_threshold_name", None),
            noiseaware_metadata=DeepAttrDict(d.get("noiseaware_metadata", None)),
            access_code_is_managed=d.get("access_code_is_managed", None),
            is_via_bluetooth=d.get("is_via_bluetooth", None),
            is_via_nfc=d.get("is_via_nfc", None),
            method=d.get("method", None),
            user_identity_id=d.get("user_identity_id", None),
            reason=DeepAttrDict(d.get("reason", None)),
            climate_preset_key=d.get("climate_preset_key", None),
            is_fallback_climate_preset=d.get("is_fallback_climate_preset", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
            cooling_set_point_fahrenheit=d.get("cooling_set_point_fahrenheit", None),
            fan_mode_setting=d.get("fan_mode_setting", None),
            heating_set_point_celsius=d.get("heating_set_point_celsius", None),
            heating_set_point_fahrenheit=d.get("heating_set_point_fahrenheit", None),
            hvac_mode_setting=d.get("hvac_mode_setting", None),
            lower_limit_celsius=d.get("lower_limit_celsius", None),
            lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            upper_limit_celsius=d.get("upper_limit_celsius", None),
            upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
            desired_temperature_celsius=d.get("desired_temperature_celsius", None),
            desired_temperature_fahrenheit=d.get(
                "desired_temperature_fahrenheit", None
            ),
            activation_reason=d.get("activation_reason", None),
            image_url=d.get("image_url", None),
            motion_sub_type=d.get("motion_sub_type", None),
            video_url=d.get("video_url", None),
            acs_entrance_ids=d.get("acs_entrance_ids", None),
            device_ids=d.get("device_ids", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
        )
