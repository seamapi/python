from typing import Any, Dict, List, Optional, Union
from typing_extensions import Self
import abc
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessCode:
    common_code_key: str
    is_scheduled_on_device: bool
    type: str
    is_waiting_for_code_assignment: bool
    access_code_id: str
    device_id: str
    name: str
    code: str
    created_at: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    is_managed: bool
    starts_at: str
    ends_at: str
    status: str
    is_backup_access_code_available: bool
    is_backup: bool
    pulled_backup_access_code_id: str
    is_external_modification_allowed: bool
    is_one_time_use: bool
    is_offline_access_code: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessCode(
            common_code_key=d.get("common_code_key", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            type=d.get("type", None),
            is_waiting_for_code_assignment=d.get(
                "is_waiting_for_code_assignment", None
            ),
            access_code_id=d.get("access_code_id", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            is_managed=d.get("is_managed", None),
            starts_at=d.get("starts_at", None),
            ends_at=d.get("ends_at", None),
            status=d.get("status", None),
            is_backup_access_code_available=d.get(
                "is_backup_access_code_available", None
            ),
            is_backup=d.get("is_backup", None),
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            is_external_modification_allowed=d.get(
                "is_external_modification_allowed", None
            ),
            is_one_time_use=d.get("is_one_time_use", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
        )


@dataclass
class UnmanagedAccessCode:
    type: str
    access_code_id: str
    device_id: str
    name: str
    code: str
    created_at: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    is_managed: bool
    starts_at: str
    ends_at: str
    status: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAccessCode(
            type=d.get("type", None),
            access_code_id=d.get("access_code_id", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            is_managed=d.get("is_managed", None),
            starts_at=d.get("starts_at", None),
            ends_at=d.get("ends_at", None),
            status=d.get("status", None),
        )


@dataclass
class ActionAttempt:
    action_attempt_id: str
    status: str
    result: Any
    error: Dict[str, Any]
    action_type: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ActionAttempt(
            action_attempt_id=d.get("action_attempt_id", None),
            status=d.get("status", None),
            result=d.get("result", None),
            error=DeepAttrDict(d.get("error", None)),
            action_type=d.get("action_type", None),
        )


@dataclass
class ClientSession:
    client_session_id: str
    workspace_id: str
    created_at: str
    expires_at: str
    token: str
    user_identifier_key: str
    device_count: float
    connected_account_ids: List[str]
    connect_webview_ids: List[str]
    user_identity_ids: List[str]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ClientSession(
            client_session_id=d.get("client_session_id", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
            user_identifier_key=d.get("user_identifier_key", None),
            device_count=d.get("device_count", None),
            connected_account_ids=d.get("connected_account_ids", None),
            connect_webview_ids=d.get("connect_webview_ids", None),
            user_identity_ids=d.get("user_identity_ids", None),
        )


@dataclass
class ThermostatSchedule:
    thermostat_schedule_id: str
    device_id: str
    name: str
    climate_preset_key: str
    max_override_period_minutes: int
    starts_at: str
    unstable_is_override_allowed: bool
    ends_at: str
    created_at: str
    errors: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatSchedule(
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            climate_preset_key=d.get("climate_preset_key", None),
            max_override_period_minutes=d.get("max_override_period_minutes", None),
            starts_at=d.get("starts_at", None),
            unstable_is_override_allowed=d.get("unstable_is_override_allowed", None),
            ends_at=d.get("ends_at", None),
            created_at=d.get("created_at", None),
            errors=d.get("errors", None),
        )


@dataclass
class ConnectWebview:
    connect_webview_id: str
    workspace_id: str
    created_at: str
    connected_account_id: str
    url: str
    device_selection_mode: str
    accepted_providers: List[str]
    accepted_devices: List[str]
    any_device_allowed: bool
    any_provider_allowed: bool
    login_successful: bool
    status: str
    custom_redirect_url: str
    custom_redirect_failure_url: str
    custom_metadata: Dict[str, Any]
    automatically_manage_new_devices: bool
    wait_for_device_creation: bool
    authorized_at: str
    selected_provider: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectWebview(
            connect_webview_id=d.get("connect_webview_id", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            connected_account_id=d.get("connected_account_id", None),
            url=d.get("url", None),
            device_selection_mode=d.get("device_selection_mode", None),
            accepted_providers=d.get("accepted_providers", None),
            accepted_devices=d.get("accepted_devices", None),
            any_device_allowed=d.get("any_device_allowed", None),
            any_provider_allowed=d.get("any_provider_allowed", None),
            login_successful=d.get("login_successful", None),
            status=d.get("status", None),
            custom_redirect_url=d.get("custom_redirect_url", None),
            custom_redirect_failure_url=d.get("custom_redirect_failure_url", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            wait_for_device_creation=d.get("wait_for_device_creation", None),
            authorized_at=d.get("authorized_at", None),
            selected_provider=d.get("selected_provider", None),
        )


@dataclass
class ConnectedAccount:
    connected_account_id: str
    created_at: str
    user_identifier: Dict[str, Any]
    account_type: str
    account_type_display_name: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    custom_metadata: Dict[str, Any]
    automatically_manage_new_devices: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectedAccount(
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            user_identifier=DeepAttrDict(d.get("user_identifier", None)),
            account_type=d.get("account_type", None),
            account_type_display_name=d.get("account_type_display_name", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
        )


@dataclass
class Device:
    device_id: str
    device_type: Any
    nickname: str
    display_name: str
    capabilities_supported: List[str]
    properties: Any
    location: Dict[str, Any]
    connected_account_id: str
    workspace_id: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    created_at: str
    is_managed: bool
    custom_metadata: Dict[str, Any]
    can_remotely_unlock: bool
    can_remotely_lock: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_hvac_heat: bool
    can_hvac_cool: bool
    can_hvac_heat_cool: bool
    can_turn_off_hvac: bool
    can_simulate_removal: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Device(
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            nickname=d.get("nickname", None),
            display_name=d.get("display_name", None),
            capabilities_supported=d.get("capabilities_supported", None),
            properties=DeepAttrDict(d.get("properties", None)),
            location=DeepAttrDict(d.get("location", None)),
            connected_account_id=d.get("connected_account_id", None),
            workspace_id=d.get("workspace_id", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            created_at=d.get("created_at", None),
            is_managed=d.get("is_managed", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
        )


@dataclass
class UnmanagedDevice:
    device_id: str
    device_type: Any
    connected_account_id: str
    location: Dict[str, Any]
    capabilities_supported: List[str]
    workspace_id: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    created_at: str
    is_managed: bool
    properties: Dict[str, Any]
    can_remotely_unlock: bool
    can_remotely_lock: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_hvac_heat: bool
    can_hvac_cool: bool
    can_hvac_heat_cool: bool
    can_turn_off_hvac: bool
    can_simulate_removal: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedDevice(
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            connected_account_id=d.get("connected_account_id", None),
            location=DeepAttrDict(d.get("location", None)),
            capabilities_supported=d.get("capabilities_supported", None),
            workspace_id=d.get("workspace_id", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            created_at=d.get("created_at", None),
            is_managed=d.get("is_managed", None),
            properties=DeepAttrDict(d.get("properties", None)),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
        )


@dataclass
class DeviceProvider:
    device_provider_name: str
    display_name: str
    image_url: str
    provider_categories: List[str]
    can_remotely_unlock: bool
    can_remotely_lock: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_hvac_heat: bool
    can_hvac_cool: bool
    can_hvac_heat_cool: bool
    can_turn_off_hvac: bool
    can_simulate_removal: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return DeviceProvider(
            device_provider_name=d.get("device_provider_name", None),
            display_name=d.get("display_name", None),
            image_url=d.get("image_url", None),
            provider_categories=d.get("provider_categories", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
        )


@dataclass
class SeamEvent:
    event_id: str
    workspace_id: str
    created_at: str
    occurred_at: str
    access_code_id: str
    device_id: str
    connected_account_id: str
    event_type: str
    code: str
    backup_access_code_id: str
    acs_system_id: str
    acs_credential_id: str
    acs_user_id: str
    acs_encoder_id: str
    acs_access_group_id: str
    acs_entrance_id: str
    client_session_id: str
    connect_webview_id: str
    action_attempt_id: str
    action_type: str
    status: str
    error_code: str
    battery_level: float
    battery_status: str
    noise_level_decibels: float
    noise_level_nrs: float
    noise_threshold_id: str
    noise_threshold_name: str
    noiseaware_metadata: Dict[str, Any]
    minut_metadata: Dict[str, Any]
    method: str
    thermostat_schedule_id: str
    climate_preset_key: str
    is_fallback_climate_preset: bool
    fan_mode_setting: str
    hvac_mode_setting: str
    cooling_set_point_celsius: float
    heating_set_point_celsius: float
    cooling_set_point_fahrenheit: float
    heating_set_point_fahrenheit: float
    temperature_celsius: float
    temperature_fahrenheit: float
    upper_limit_celsius: float
    upper_limit_fahrenheit: float
    lower_limit_celsius: float
    lower_limit_fahrenheit: float
    desired_temperature_celsius: float
    desired_temperature_fahrenheit: float
    device_name: str
    enrollment_automation_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return SeamEvent(
            event_id=d.get("event_id", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            occurred_at=d.get("occurred_at", None),
            access_code_id=d.get("access_code_id", None),
            device_id=d.get("device_id", None),
            connected_account_id=d.get("connected_account_id", None),
            event_type=d.get("event_type", None),
            code=d.get("code", None),
            backup_access_code_id=d.get("backup_access_code_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            client_session_id=d.get("client_session_id", None),
            connect_webview_id=d.get("connect_webview_id", None),
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            status=d.get("status", None),
            error_code=d.get("error_code", None),
            battery_level=d.get("battery_level", None),
            battery_status=d.get("battery_status", None),
            noise_level_decibels=d.get("noise_level_decibels", None),
            noise_level_nrs=d.get("noise_level_nrs", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_name=d.get("noise_threshold_name", None),
            noiseaware_metadata=DeepAttrDict(d.get("noiseaware_metadata", None)),
            minut_metadata=DeepAttrDict(d.get("minut_metadata", None)),
            method=d.get("method", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            climate_preset_key=d.get("climate_preset_key", None),
            is_fallback_climate_preset=d.get("is_fallback_climate_preset", None),
            fan_mode_setting=d.get("fan_mode_setting", None),
            hvac_mode_setting=d.get("hvac_mode_setting", None),
            cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
            heating_set_point_celsius=d.get("heating_set_point_celsius", None),
            cooling_set_point_fahrenheit=d.get("cooling_set_point_fahrenheit", None),
            heating_set_point_fahrenheit=d.get("heating_set_point_fahrenheit", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            upper_limit_celsius=d.get("upper_limit_celsius", None),
            upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
            lower_limit_celsius=d.get("lower_limit_celsius", None),
            lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
            desired_temperature_celsius=d.get("desired_temperature_celsius", None),
            desired_temperature_fahrenheit=d.get(
                "desired_temperature_fahrenheit", None
            ),
            device_name=d.get("device_name", None),
            enrollment_automation_id=d.get("enrollment_automation_id", None),
        )


@dataclass
class NoiseThreshold:
    noise_threshold_id: str
    device_id: str
    name: str
    noise_threshold_nrs: float
    starts_daily_at: str
    ends_daily_at: str
    noise_threshold_decibels: float

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return NoiseThreshold(
            noise_threshold_id=d.get("noise_threshold_id", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            noise_threshold_nrs=d.get("noise_threshold_nrs", None),
            starts_daily_at=d.get("starts_daily_at", None),
            ends_daily_at=d.get("ends_daily_at", None),
            noise_threshold_decibels=d.get("noise_threshold_decibels", None),
        )


@dataclass
class Webhook:
    webhook_id: str
    url: str
    event_types: List[str]
    secret: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Webhook(
            webhook_id=d.get("webhook_id", None),
            url=d.get("url", None),
            event_types=d.get("event_types", None),
            secret=d.get("secret", None),
        )


@dataclass
class Workspace:
    workspace_id: str
    name: str
    company_name: str
    is_sandbox: bool
    is_suspended: bool
    connect_partner_name: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Workspace(
            workspace_id=d.get("workspace_id", None),
            name=d.get("name", None),
            company_name=d.get("company_name", None),
            is_sandbox=d.get("is_sandbox", None),
            is_suspended=d.get("is_suspended", None),
            connect_partner_name=d.get("connect_partner_name", None),
        )


@dataclass
class AcsSystem:
    default_credential_manager_acs_system_id: str
    acs_system_id: str
    external_type: str
    external_type_display_name: str
    is_credential_manager: bool
    visionline_metadata: Dict[str, Any]
    system_type: str
    system_type_display_name: str
    location: Dict[str, Any]
    name: str
    created_at: str
    workspace_id: str
    connected_account_ids: List[str]
    connected_account_id: str
    image_url: str
    image_alt_text: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    can_automate_enrollment: bool
    can_create_acs_access_groups: bool
    can_remove_acs_users_from_acs_access_groups: bool
    can_add_acs_users_to_acs_access_groups: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsSystem(
            default_credential_manager_acs_system_id=d.get(
                "default_credential_manager_acs_system_id", None
            ),
            acs_system_id=d.get("acs_system_id", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_credential_manager=d.get("is_credential_manager", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            system_type=d.get("system_type", None),
            system_type_display_name=d.get("system_type_display_name", None),
            location=DeepAttrDict(d.get("location", None)),
            name=d.get("name", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
            connected_account_ids=d.get("connected_account_ids", None),
            connected_account_id=d.get("connected_account_id", None),
            image_url=d.get("image_url", None),
            image_alt_text=d.get("image_alt_text", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            can_automate_enrollment=d.get("can_automate_enrollment", None),
            can_create_acs_access_groups=d.get("can_create_acs_access_groups", None),
            can_remove_acs_users_from_acs_access_groups=d.get(
                "can_remove_acs_users_from_acs_access_groups", None
            ),
            can_add_acs_users_to_acs_access_groups=d.get(
                "can_add_acs_users_to_acs_access_groups", None
            ),
        )


@dataclass
class AcsAccessGroup:
    acs_access_group_id: str
    acs_system_id: str
    workspace_id: str
    name: str
    access_group_type: str
    access_group_type_display_name: str
    display_name: str
    external_type: str
    external_type_display_name: str
    created_at: str
    warnings: List[Dict[str, Any]]
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsAccessGroup(
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            workspace_id=d.get("workspace_id", None),
            name=d.get("name", None),
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            created_at=d.get("created_at", None),
            warnings=d.get("warnings", None),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class UnmanagedAcsAccessGroup:
    acs_access_group_id: str
    acs_system_id: str
    workspace_id: str
    name: str
    access_group_type: str
    access_group_type_display_name: str
    display_name: str
    external_type: str
    external_type_display_name: str
    created_at: str
    warnings: List[Dict[str, Any]]
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsAccessGroup(
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            workspace_id=d.get("workspace_id", None),
            name=d.get("name", None),
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            created_at=d.get("created_at", None),
            warnings=d.get("warnings", None),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class AcsUser:
    acs_user_id: str
    acs_system_id: str
    hid_acs_system_id: str
    workspace_id: str
    created_at: str
    display_name: str
    external_type: str
    external_type_display_name: str
    is_suspended: bool
    access_schedule: Dict[str, Any]
    user_identity_id: str
    user_identity_full_name: str
    user_identity_email_address: str
    user_identity_phone_number: str
    latest_desired_state_synced_with_provider_at: str
    is_latest_desired_state_synced_with_provider: bool
    warnings: List[Dict[str, Any]]
    errors: List[Dict[str, Any]]
    pending_modifications: List[Dict[str, Any]]
    full_name: str
    email: str
    email_address: str
    phone_number: str
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsUser(
            acs_user_id=d.get("acs_user_id", None),
            acs_system_id=d.get("acs_system_id", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_suspended=d.get("is_suspended", None),
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            warnings=d.get("warnings", None),
            errors=d.get("errors", None),
            pending_modifications=d.get("pending_modifications", None),
            full_name=d.get("full_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            phone_number=d.get("phone_number", None),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class UnmanagedAcsUser:
    acs_user_id: str
    acs_system_id: str
    hid_acs_system_id: str
    workspace_id: str
    created_at: str
    display_name: str
    external_type: str
    external_type_display_name: str
    is_suspended: bool
    access_schedule: Dict[str, Any]
    user_identity_id: str
    user_identity_full_name: str
    user_identity_email_address: str
    user_identity_phone_number: str
    latest_desired_state_synced_with_provider_at: str
    is_latest_desired_state_synced_with_provider: bool
    warnings: List[Dict[str, Any]]
    errors: List[Dict[str, Any]]
    pending_modifications: List[Dict[str, Any]]
    full_name: str
    email: str
    email_address: str
    phone_number: str
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsUser(
            acs_user_id=d.get("acs_user_id", None),
            acs_system_id=d.get("acs_system_id", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_suspended=d.get("is_suspended", None),
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            warnings=d.get("warnings", None),
            errors=d.get("errors", None),
            pending_modifications=d.get("pending_modifications", None),
            full_name=d.get("full_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            phone_number=d.get("phone_number", None),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class AcsEntrance:
    acs_system_id: str
    acs_entrance_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    latch_metadata: Dict[str, Any]
    visionline_metadata: Dict[str, Any]
    salto_ks_metadata: Dict[str, Any]
    dormakaba_community_metadata: Dict[str, Any]
    assa_abloy_vostio_metadata: Dict[str, Any]
    salto_space_metadata: Dict[str, Any]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEntrance(
            acs_system_id=d.get("acs_system_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            latch_metadata=DeepAttrDict(d.get("latch_metadata", None)),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            salto_ks_metadata=DeepAttrDict(d.get("salto_ks_metadata", None)),
            dormakaba_community_metadata=DeepAttrDict(
                d.get("dormakaba_community_metadata", None)
            ),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            salto_space_metadata=DeepAttrDict(d.get("salto_space_metadata", None)),
        )


@dataclass
class AcsCredentialProvisioningAutomation:
    acs_credential_provisioning_automation_id: str
    credential_manager_acs_system_id: str
    user_identity_id: str
    created_at: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredentialProvisioningAutomation(
            acs_credential_provisioning_automation_id=d.get(
                "acs_credential_provisioning_automation_id", None
            ),
            credential_manager_acs_system_id=d.get(
                "credential_manager_acs_system_id", None
            ),
            user_identity_id=d.get("user_identity_id", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsCredentialPool:
    acs_credential_pool_id: str
    acs_system_id: str
    display_name: str
    external_type: str
    external_type_display_name: str
    created_at: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredentialPool(
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsCredential:
    acs_credential_id: str
    acs_user_id: str
    acs_credential_pool_id: str
    acs_system_id: str
    parent_acs_credential_id: str
    display_name: str
    code: str
    is_one_time_use: bool
    card_number: str
    is_issued: bool
    issued_at: str
    access_method: str
    external_type: str
    external_type_display_name: str
    created_at: str
    workspace_id: str
    starts_at: str
    ends_at: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    is_multi_phone_sync_credential: bool
    is_latest_desired_state_synced_with_provider: bool
    latest_desired_state_synced_with_provider_at: str
    visionline_metadata: Dict[str, Any]
    assa_abloy_vostio_metadata: Dict[str, Any]
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredential(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            parent_acs_credential_id=d.get("parent_acs_credential_id", None),
            display_name=d.get("display_name", None),
            code=d.get("code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            card_number=d.get("card_number", None),
            is_issued=d.get("is_issued", None),
            issued_at=d.get("issued_at", None),
            access_method=d.get("access_method", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
            starts_at=d.get("starts_at", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            is_multi_phone_sync_credential=d.get(
                "is_multi_phone_sync_credential", None
            ),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class UnmanagedAcsCredential:
    acs_credential_id: str
    acs_user_id: str
    acs_credential_pool_id: str
    acs_system_id: str
    parent_acs_credential_id: str
    display_name: str
    code: str
    is_one_time_use: bool
    card_number: str
    is_issued: bool
    issued_at: str
    access_method: str
    external_type: str
    external_type_display_name: str
    created_at: str
    workspace_id: str
    starts_at: str
    ends_at: str
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    is_multi_phone_sync_credential: bool
    is_latest_desired_state_synced_with_provider: bool
    latest_desired_state_synced_with_provider_at: str
    visionline_metadata: Dict[str, Any]
    assa_abloy_vostio_metadata: Dict[str, Any]
    is_managed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsCredential(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            parent_acs_credential_id=d.get("parent_acs_credential_id", None),
            display_name=d.get("display_name", None),
            code=d.get("code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            card_number=d.get("card_number", None),
            is_issued=d.get("is_issued", None),
            issued_at=d.get("issued_at", None),
            access_method=d.get("access_method", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
            starts_at=d.get("starts_at", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            is_multi_phone_sync_credential=d.get(
                "is_multi_phone_sync_credential", None
            ),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            is_managed=d.get("is_managed", None),
        )


@dataclass
class AcsEncoder:
    acs_encoder_id: str
    acs_system_id: str
    workspace_id: str
    errors: List[Dict[str, Any]]
    created_at: str
    display_name: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEncoder(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            workspace_id=d.get("workspace_id", None),
            errors=d.get("errors", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
        )


@dataclass
class EnrollmentAutomation:
    enrollment_automation_id: str
    credential_manager_acs_system_id: str
    user_identity_id: str
    created_at: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return EnrollmentAutomation(
            enrollment_automation_id=d.get("enrollment_automation_id", None),
            credential_manager_acs_system_id=d.get(
                "credential_manager_acs_system_id", None
            ),
            user_identity_id=d.get("user_identity_id", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Phone:
    device_id: str
    nickname: str
    display_name: str
    workspace_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    device_type: str
    properties: Dict[str, Any]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Phone(
            device_id=d.get("device_id", None),
            nickname=d.get("nickname", None),
            display_name=d.get("display_name", None),
            workspace_id=d.get("workspace_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            errors=d.get("errors", None),
            warnings=d.get("warnings", None),
            device_type=d.get("device_type", None),
            properties=DeepAttrDict(d.get("properties", None)),
        )


@dataclass
class UserIdentity:
    user_identity_id: str
    user_identity_key: str
    email_address: str
    phone_number: str
    display_name: str
    full_name: str
    created_at: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UserIdentity(
            user_identity_id=d.get("user_identity_id", None),
            user_identity_key=d.get("user_identity_key", None),
            email_address=d.get("email_address", None),
            phone_number=d.get("phone_number", None),
            display_name=d.get("display_name", None),
            full_name=d.get("full_name", None),
            created_at=d.get("created_at", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Network:
    network_id: str
    workspace_id: str
    display_name: str
    created_at: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Network(
            network_id=d.get("network_id", None),
            workspace_id=d.get("workspace_id", None),
            display_name=d.get("display_name", None),
            created_at=d.get("created_at", None),
        )


@dataclass
class Pagination:
    next_page_cursor: str
    has_next_page: bool
    next_page_url: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Pagination(
            next_page_cursor=d.get("next_page_cursor", None),
            has_next_page=d.get("has_next_page", None),
            next_page_url=d.get("next_page_url", None),
        )


class AbstractActionAttempts(abc.ABC):

    @abc.abstractmethod
    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, action_attempt_ids: List[str]) -> List[ActionAttempt]:
        raise NotImplementedError()


class AbstractBridges(abc.ABC):

    @abc.abstractmethod
    def get(self, *, bridge_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> None:
        raise NotImplementedError()


class AbstractClientSessions(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        user_identity_ids: Optional[List[str]] = None,
        expires_at: Optional[str] = None
    ) -> ClientSession:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, client_session_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        client_session_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> ClientSession:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_or_create(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        user_identity_ids: Optional[List[str]] = None,
        expires_at: Optional[str] = None
    ) -> ClientSession:
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        client_session_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        connect_webview_ids: Optional[List[str]] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        client_session_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        connect_webview_id: Optional[str] = None,
        without_user_identifier_key: Optional[bool] = None,
        user_identity_id: Optional[str] = None
    ) -> List[ClientSession]:
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke(self, *, client_session_id: str) -> None:
        raise NotImplementedError()


class AbstractConnectWebviews(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        device_selection_mode: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        custom_redirect_failure_url: Optional[str] = None,
        accepted_providers: Optional[List[str]] = None,
        provider_category: Optional[str] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        wait_for_device_creation: Optional[bool] = None
    ) -> ConnectWebview:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, connect_webview_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        limit: Optional[float] = None
    ) -> List[ConnectWebview]:
        raise NotImplementedError()


class AbstractConnectedAccounts(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, connected_account_id: str, sync: Optional[bool] = None) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, connected_account_id: Optional[str] = None, email: Optional[str] = None
    ) -> ConnectedAccount:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None
    ) -> List[ConnectedAccount]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        connected_account_id: str,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        raise NotImplementedError()


class AbstractEvents(abc.ABC):

    @abc.abstractmethod
    def get(
        self,
        *,
        event_id: Optional[str] = None,
        event_type: Optional[str] = None,
        device_id: Optional[str] = None
    ) -> SeamEvent:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        unstable_offset: Optional[float] = None,
        since: Optional[str] = None,
        between: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
        connected_account_id: Optional[str] = None,
        connect_webview_id: Optional[str] = None,
        limit: Optional[float] = None,
        event_ids: Optional[List[str]] = None
    ) -> List[SeamEvent]:
        raise NotImplementedError()


class AbstractLocks(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def lock_door(
        self,
        *,
        device_id: str,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock_door(
        self,
        *,
        device_id: str,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()


class AbstractNetworks(abc.ABC):

    @abc.abstractmethod
    def get(self, *, network_id: str) -> Network:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Network]:
        raise NotImplementedError()


class AbstractWebhooks(abc.ABC):

    @abc.abstractmethod
    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, webhook_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, webhook_id: str) -> Webhook:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Webhook]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, webhook_id: str, event_types: List[str]) -> None:
        raise NotImplementedError()


class AbstractWorkspaces(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        name: str,
        company_name: Optional[str] = None,
        connect_partner_name: Optional[str] = None,
        is_sandbox: Optional[bool] = None,
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None,
        webview_logo_shape: Optional[str] = None
    ) -> Workspace:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
    ) -> Workspace:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Workspace]:
        raise NotImplementedError()

    @abc.abstractmethod
    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()


class AbstractAccessCodesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_unmanaged_access_code(
        self, *, device_id: str, name: str, code: str
    ) -> UnmanagedAccessCode:
        raise NotImplementedError()


class AbstractAccessCodesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def convert_to_managed(
        self,
        *,
        access_code_id: str,
        is_external_modification_allowed: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        sync: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, access_code_id: str, sync: Optional[bool] = None) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> UnmanagedAccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedAccessCode]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        is_managed: bool,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        force: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAcsAccessGroups(abc.ABC):

    @abc.abstractmethod
    def add_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, acs_system_id: Optional[str] = None, acs_user_id: Optional[str] = None
    ) -> List[AcsAccessGroup]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(
        self, *, acs_access_group_id: str
    ) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_users(self, *, acs_access_group_id: str) -> List[AcsUser]:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        raise NotImplementedError()


class AbstractAcsCredentials(abc.ABC):

    @abc.abstractmethod
    def assign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        acs_user_id: str,
        access_method: str,
        credential_manager_acs_system_id: Optional[str] = None,
        code: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None,
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None
    ) -> AcsCredential:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, acs_credential_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_credential_id: str) -> AcsCredential:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        limit: Optional[float] = None,
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None
    ) -> List[AcsCredential]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def unassign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        acs_credential_id: str,
        code: Optional[str] = None,
        ends_at: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAcsEncoders(abc.ABC):

    @abc.abstractmethod
    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_credential_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None
    ) -> List[AcsEncoder]:
        raise NotImplementedError()

    @abc.abstractmethod
    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()


class AbstractAcsEntrances(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(self, *, acs_entrance_id: str, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_credentials_with_access(
        self, *, acs_entrance_id: str, include_if: Optional[List[str]] = None
    ) -> List[AcsCredential]:
        raise NotImplementedError()


class AbstractAcsSystems(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_system_id: str) -> AcsSystem:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, connected_account_id: Optional[str] = None) -> List[AcsSystem]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_compatible_credential_manager_acs_systems(
        self, *, acs_system_id: str
    ) -> List[AcsSystem]:
        raise NotImplementedError()


class AbstractAcsUsers(abc.ABC):

    @abc.abstractmethod
    def add_to_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        full_name: str,
        acs_system_id: str,
        acs_access_group_ids: Optional[List[str]] = None,
        user_identity_id: Optional[str] = None,
        access_schedule: Optional[Dict[str, Any]] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None
    ) -> AcsUser:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_user_id: str) -> AcsUser:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        created_before: Optional[str] = None,
        page_cursor: Optional[str] = None
    ) -> List[AcsUser]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(self, *, acs_user_id: str) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_from_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_all_entrances(self, *, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def suspend(self, *, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def unsuspend(self, *, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        acs_user_id: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractDevicesSimulate(abc.ABC):

    @abc.abstractmethod
    def connect(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, *, device_id: str) -> None:
        raise NotImplementedError()


class AbstractDevicesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        raise NotImplementedError()

    @abc.abstractmethod
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
    ) -> List[UnmanagedDevice]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, device_id: str, is_managed: bool) -> None:
        raise NotImplementedError()


class AbstractNoiseSensorsNoiseThresholds(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        starts_daily_at: str,
        ends_daily_at: str,
        sync: Optional[bool] = None,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None
    ) -> NoiseThreshold:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self, *, noise_threshold_id: str, device_id: str, sync: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, noise_threshold_id: str) -> NoiseThreshold:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, device_id: str, is_programmed: Optional[bool] = None
    ) -> List[NoiseThreshold]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        noise_threshold_id: str,
        device_id: str,
        sync: Optional[bool] = None,
        name: Optional[str] = None,
        starts_daily_at: Optional[str] = None,
        ends_daily_at: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None
    ) -> None:
        raise NotImplementedError()


class AbstractNoiseSensorsSimulate(abc.ABC):

    @abc.abstractmethod
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        raise NotImplementedError()


class AbstractPhonesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        raise NotImplementedError()


class AbstractThermostatsSchedules(abc.ABC):

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, thermostat_schedule_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, thermostat_schedule_id: str) -> ThermostatSchedule:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[ThermostatSchedule]:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()


class AbstractThermostatsSimulate(abc.ABC):

    @abc.abstractmethod
    def hvac_mode_adjusted(
        self,
        *,
        hvac_mode: str,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def temperature_reached(
        self,
        *,
        device_id: str,
        temperature_celsius: Optional[float] = None,
        temperature_fahrenheit: Optional[float] = None
    ) -> None:
        raise NotImplementedError()


class AbstractUserIdentitiesEnrollmentAutomations(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, enrollment_automation_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, enrollment_automation_id: str) -> EnrollmentAutomation:
        raise NotImplementedError()

    @abc.abstractmethod
    def launch(
        self,
        *,
        user_identity_id: str,
        credential_manager_acs_system_id: str,
        acs_credential_pool_id: Optional[str] = None,
        create_credential_manager_user: Optional[bool] = None,
        credential_manager_acs_user_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, user_identity_id: str) -> List[EnrollmentAutomation]:
        raise NotImplementedError()


class AbstractAcsEncodersSimulate(abc.ABC):

    @abc.abstractmethod
    def next_credential_encode_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_encode_will_succeed(
        self, *, acs_encoder_id: str, scenario: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_scan_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id_on_seam: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_scan_will_succeed(
        self,
        *,
        acs_encoder_id: str,
        scenario: Optional[str] = None,
        acs_credential_id_on_seam: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractPhones(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractPhonesSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def deactivate(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, device_id: str) -> Phone:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        owner_user_identity_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> List[Phone]:
        raise NotImplementedError()


class AbstractUserIdentities(abc.ABC):

    @property
    @abc.abstractmethod
    def enrollment_automations(self) -> AbstractUserIdentitiesEnrollmentAutomations:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        user_identity_key: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        full_name: Optional[str] = None
    ) -> UserIdentity:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, credential_manager_acs_system_id: Optional[str] = None
    ) -> List[UserIdentity]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_devices(self, *, user_identity_id: str) -> List[Device]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_acs_systems(self, *, user_identity_id: str) -> List[AcsSystem]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_acs_users(self, *, user_identity_id: str) -> List[AcsUser]:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        user_identity_id: str,
        user_identity_key: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        full_name: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAccessCodes(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAccessCodesSimulate:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAccessCodesUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        sync: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        common_code_key: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None
    ) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_multiple(
        self,
        *,
        device_ids: List[str],
        behavior_when_code_cannot_be_shared: Optional[str] = None,
        preferred_code_length: Optional[float] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        attempt_for_offline_device: Optional[bool] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None
    ) -> List[AccessCode]:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self,
        *,
        access_code_id: str,
        device_id: Optional[str] = None,
        sync: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_code(self, *, device_id: str) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[AccessCode]:
        raise NotImplementedError()

    @abc.abstractmethod
    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        sync: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        device_id: Optional[str] = None,
        type: Optional[str] = None,
        is_managed: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update_multiple(
        self,
        *,
        common_code_key: str,
        ends_at: Optional[str] = None,
        starts_at: Optional[str] = None,
        name: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractDevices(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractDevicesSimulate:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractDevicesUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def list_device_providers(
        self, *, provider_category: Optional[str] = None
    ) -> List[DeviceProvider]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        device_id: str,
        properties: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        is_managed: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        raise NotImplementedError()


class AbstractNoiseSensors(abc.ABC):

    @property
    @abc.abstractmethod
    def noise_thresholds(self) -> AbstractNoiseSensorsNoiseThresholds:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractNoiseSensorsSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()


class AbstractThermostats(abc.ABC):

    @property
    @abc.abstractmethod
    def schedules(self) -> AbstractThermostatsSchedules:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractThermostatsSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def activate_climate_preset(
        self,
        *,
        device_id: str,
        climate_preset_key: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_climate_preset(self, *, device_id: str, climate_preset_key: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def off(
        self,
        *,
        device_id: str,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def set_fallback_climate_preset(
        self, *, device_id: str, climate_preset_key: str
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def set_fan_mode(
        self,
        *,
        device_id: str,
        fan_mode: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()

    @abc.abstractmethod
    def set_temperature_threshold(
        self,
        *,
        device_id: str,
        lower_limit_celsius: Optional[float] = None,
        lower_limit_fahrenheit: Optional[float] = None,
        upper_limit_celsius: Optional[float] = None,
        upper_limit_fahrenheit: Optional[float] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
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
        raise NotImplementedError()


class AbstractAcs(abc.ABC):

    @property
    @abc.abstractmethod
    def access_groups(self) -> AbstractAcsAccessGroups:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credentials(self) -> AbstractAcsCredentials:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def encoders(self) -> AbstractAcsEncoders:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def entrances(self) -> AbstractAcsEntrances:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def systems(self) -> AbstractAcsSystems:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def users(self) -> AbstractAcsUsers:
        raise NotImplementedError()


@dataclass
class AbstractRoutes(abc.ABC):
    access_codes: AbstractAccessCodes
    action_attempts: AbstractActionAttempts
    bridges: AbstractBridges
    client_sessions: AbstractClientSessions
    connect_webviews: AbstractConnectWebviews
    connected_accounts: AbstractConnectedAccounts
    devices: AbstractDevices
    events: AbstractEvents
    locks: AbstractLocks
    networks: AbstractNetworks
    noise_sensors: AbstractNoiseSensors
    phones: AbstractPhones
    thermostats: AbstractThermostats
    user_identities: AbstractUserIdentities
    webhooks: AbstractWebhooks
    workspaces: AbstractWorkspaces
    acs: AbstractAcs
