from typing import Any, Dict, List, Optional, Union
from typing_extensions import Self
import abc
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessCode:
    access_code_id: str
    code: str
    common_code_key: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Dict[str, Any]]
    is_backup: bool
    is_backup_access_code_available: bool
    is_external_modification_allowed: bool
    is_managed: bool
    is_offline_access_code: bool
    is_one_time_use: bool
    is_scheduled_on_device: bool
    is_waiting_for_code_assignment: bool
    name: str
    pulled_backup_access_code_id: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessCode(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            common_code_key=d.get("common_code_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_backup=d.get("is_backup", None),
            is_backup_access_code_available=d.get(
                "is_backup_access_code_available", None
            ),
            is_external_modification_allowed=d.get(
                "is_external_modification_allowed", None
            ),
            is_managed=d.get("is_managed", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            is_waiting_for_code_assignment=d.get(
                "is_waiting_for_code_assignment", None
            ),
            name=d.get("name", None),
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
        )


@dataclass
class AcsAccessGroup:
    access_group_type: str
    access_group_type_display_name: str
    acs_access_group_id: str
    acs_system_id: str
    created_at: str
    display_name: str
    external_type: str
    external_type_display_name: str
    is_managed: bool
    name: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsAccessGroup(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsCredential:
    access_method: str
    acs_credential_id: str
    acs_credential_pool_id: str
    acs_system_id: str
    acs_user_id: str
    assa_abloy_vostio_metadata: Dict[str, Any]
    card_number: str
    code: str
    created_at: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    is_issued: bool
    is_latest_desired_state_synced_with_provider: bool
    is_managed: bool
    is_multi_phone_sync_credential: bool
    is_one_time_use: bool
    issued_at: str
    latest_desired_state_synced_with_provider_at: str
    parent_acs_credential_id: str
    starts_at: str
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredential(
            access_method=d.get("access_method", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            card_number=d.get("card_number", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_issued=d.get("is_issued", None),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            is_managed=d.get("is_managed", None),
            is_multi_phone_sync_credential=d.get(
                "is_multi_phone_sync_credential", None
            ),
            is_one_time_use=d.get("is_one_time_use", None),
            issued_at=d.get("issued_at", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            parent_acs_credential_id=d.get("parent_acs_credential_id", None),
            starts_at=d.get("starts_at", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsCredentialPool:
    acs_credential_pool_id: str
    acs_system_id: str
    created_at: str
    display_name: str
    external_type: str
    external_type_display_name: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredentialPool(
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsCredentialProvisioningAutomation:
    acs_credential_provisioning_automation_id: str
    created_at: str
    credential_manager_acs_system_id: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredentialProvisioningAutomation(
            acs_credential_provisioning_automation_id=d.get(
                "acs_credential_provisioning_automation_id", None
            ),
            created_at=d.get("created_at", None),
            credential_manager_acs_system_id=d.get(
                "credential_manager_acs_system_id", None
            ),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsEncoder:
    acs_encoder_id: str
    acs_system_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEncoder(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsEntrance:
    acs_entrance_id: str
    acs_system_id: str
    assa_abloy_vostio_metadata: Dict[str, Any]
    created_at: str
    display_name: str
    dormakaba_community_metadata: Dict[str, Any]
    errors: List[Dict[str, Any]]
    latch_metadata: Dict[str, Any]
    salto_ks_metadata: Dict[str, Any]
    salto_space_metadata: Dict[str, Any]
    visionline_metadata: Dict[str, Any]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEntrance(
            acs_entrance_id=d.get("acs_entrance_id", None),
            acs_system_id=d.get("acs_system_id", None),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            dormakaba_community_metadata=DeepAttrDict(
                d.get("dormakaba_community_metadata", None)
            ),
            errors=d.get("errors", None),
            latch_metadata=DeepAttrDict(d.get("latch_metadata", None)),
            salto_ks_metadata=DeepAttrDict(d.get("salto_ks_metadata", None)),
            salto_space_metadata=DeepAttrDict(d.get("salto_space_metadata", None)),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
        )


@dataclass
class AcsSystem:
    acs_system_id: str
    can_add_acs_users_to_acs_access_groups: bool
    can_automate_enrollment: bool
    can_create_acs_access_groups: bool
    can_remove_acs_users_from_acs_access_groups: bool
    connected_account_id: str
    connected_account_ids: List[str]
    created_at: str
    default_credential_manager_acs_system_id: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    image_alt_text: str
    image_url: str
    is_credential_manager: bool
    location: Dict[str, Any]
    name: str
    system_type: str
    system_type_display_name: str
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsSystem(
            acs_system_id=d.get("acs_system_id", None),
            can_add_acs_users_to_acs_access_groups=d.get(
                "can_add_acs_users_to_acs_access_groups", None
            ),
            can_automate_enrollment=d.get("can_automate_enrollment", None),
            can_create_acs_access_groups=d.get("can_create_acs_access_groups", None),
            can_remove_acs_users_from_acs_access_groups=d.get(
                "can_remove_acs_users_from_acs_access_groups", None
            ),
            connected_account_id=d.get("connected_account_id", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            default_credential_manager_acs_system_id=d.get(
                "default_credential_manager_acs_system_id", None
            ),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            image_alt_text=d.get("image_alt_text", None),
            image_url=d.get("image_url", None),
            is_credential_manager=d.get("is_credential_manager", None),
            location=DeepAttrDict(d.get("location", None)),
            name=d.get("name", None),
            system_type=d.get("system_type", None),
            system_type_display_name=d.get("system_type_display_name", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsUser:
    access_schedule: Dict[str, Any]
    acs_system_id: str
    acs_user_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_latest_desired_state_synced_with_provider: bool
    is_managed: bool
    is_suspended: bool
    latest_desired_state_synced_with_provider_at: str
    phone_number: str
    user_identity_email_address: str
    user_identity_full_name: str
    user_identity_id: str
    user_identity_phone_number: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsUser(
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            phone_number=d.get("phone_number", None),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ActionAttempt:
    action_attempt_id: str
    action_type: str
    error: Dict[str, Any]
    result: Any
    status: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ActionAttempt(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=DeepAttrDict(d.get("error", None)),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ClientSession:
    client_session_id: str
    connect_webview_ids: List[str]
    connected_account_ids: List[str]
    created_at: str
    device_count: float
    expires_at: str
    token: str
    user_identifier_key: str
    user_identity_ids: List[str]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ClientSession(
            client_session_id=d.get("client_session_id", None),
            connect_webview_ids=d.get("connect_webview_ids", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            device_count=d.get("device_count", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
            user_identifier_key=d.get("user_identifier_key", None),
            user_identity_ids=d.get("user_identity_ids", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ConnectWebview:
    accepted_devices: List[str]
    accepted_providers: List[str]
    any_device_allowed: bool
    any_provider_allowed: bool
    authorized_at: str
    automatically_manage_new_devices: bool
    connect_webview_id: str
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    custom_redirect_failure_url: str
    custom_redirect_url: str
    device_selection_mode: str
    login_successful: bool
    selected_provider: str
    status: str
    url: str
    wait_for_device_creation: bool
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectWebview(
            accepted_devices=d.get("accepted_devices", None),
            accepted_providers=d.get("accepted_providers", None),
            any_device_allowed=d.get("any_device_allowed", None),
            any_provider_allowed=d.get("any_provider_allowed", None),
            authorized_at=d.get("authorized_at", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            custom_redirect_failure_url=d.get("custom_redirect_failure_url", None),
            custom_redirect_url=d.get("custom_redirect_url", None),
            device_selection_mode=d.get("device_selection_mode", None),
            login_successful=d.get("login_successful", None),
            selected_provider=d.get("selected_provider", None),
            status=d.get("status", None),
            url=d.get("url", None),
            wait_for_device_creation=d.get("wait_for_device_creation", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ConnectedAccount:
    account_type: str
    account_type_display_name: str
    automatically_manage_new_devices: bool
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    errors: List[Dict[str, Any]]
    user_identifier: Dict[str, Any]
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectedAccount(
            account_type=d.get("account_type", None),
            account_type_display_name=d.get("account_type_display_name", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            errors=d.get("errors", None),
            user_identifier=DeepAttrDict(d.get("user_identifier", None)),
            warnings=d.get("warnings", None),
        )


@dataclass
class Device:
    can_hvac_cool: bool
    can_hvac_heat: bool
    can_hvac_heat_cool: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_remotely_lock: bool
    can_remotely_unlock: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    capabilities_supported: List[str]
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_type: Any
    display_name: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    location: Dict[str, Any]
    nickname: str
    properties: Any
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Device(
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            capabilities_supported=d.get("capabilities_supported", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            location=DeepAttrDict(d.get("location", None)),
            nickname=d.get("nickname", None),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class DeviceProvider:
    can_hvac_cool: bool
    can_hvac_heat: bool
    can_hvac_heat_cool: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_remotely_lock: bool
    can_remotely_unlock: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    device_provider_name: str
    display_name: str
    image_url: str
    provider_categories: List[str]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return DeviceProvider(
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            device_provider_name=d.get("device_provider_name", None),
            display_name=d.get("display_name", None),
            image_url=d.get("image_url", None),
            provider_categories=d.get("provider_categories", None),
        )


@dataclass
class EnrollmentAutomation:
    created_at: str
    credential_manager_acs_system_id: str
    enrollment_automation_id: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return EnrollmentAutomation(
            created_at=d.get("created_at", None),
            credential_manager_acs_system_id=d.get(
                "credential_manager_acs_system_id", None
            ),
            enrollment_automation_id=d.get("enrollment_automation_id", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class SeamEvent:
    access_code_id: str
    connected_account_id: str
    created_at: str
    device_id: str
    event_id: str
    event_type: str
    occurred_at: str
    workspace_id: str
    code: str
    backup_access_code_id: str
    acs_system_id: str
    acs_credential_id: str
    acs_user_id: str
    acs_encoder_id: str
    acs_access_group_id: str
    client_session_id: str
    connect_webview_id: str
    action_attempt_id: str
    action_type: str
    status: str
    error_code: str
    battery_level: float
    battery_status: str
    minut_metadata: Dict[str, Any]
    noise_level_decibels: float
    noise_level_nrs: float
    noise_threshold_id: str
    noise_threshold_name: str
    noiseaware_metadata: Dict[str, Any]
    method: str
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
    enrollment_automation_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return SeamEvent(
            access_code_id=d.get("access_code_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            code=d.get("code", None),
            backup_access_code_id=d.get("backup_access_code_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_access_group_id=d.get("acs_access_group_id", None),
            client_session_id=d.get("client_session_id", None),
            connect_webview_id=d.get("connect_webview_id", None),
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            status=d.get("status", None),
            error_code=d.get("error_code", None),
            battery_level=d.get("battery_level", None),
            battery_status=d.get("battery_status", None),
            minut_metadata=DeepAttrDict(d.get("minut_metadata", None)),
            noise_level_decibels=d.get("noise_level_decibels", None),
            noise_level_nrs=d.get("noise_level_nrs", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_name=d.get("noise_threshold_name", None),
            noiseaware_metadata=DeepAttrDict(d.get("noiseaware_metadata", None)),
            method=d.get("method", None),
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
            enrollment_automation_id=d.get("enrollment_automation_id", None),
        )


@dataclass
class Network:
    created_at: str
    display_name: str
    network_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Network(
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            network_id=d.get("network_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class NoiseThreshold:
    device_id: str
    ends_daily_at: str
    name: str
    noise_threshold_decibels: float
    noise_threshold_id: str
    noise_threshold_nrs: float
    starts_daily_at: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return NoiseThreshold(
            device_id=d.get("device_id", None),
            ends_daily_at=d.get("ends_daily_at", None),
            name=d.get("name", None),
            noise_threshold_decibels=d.get("noise_threshold_decibels", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_nrs=d.get("noise_threshold_nrs", None),
            starts_daily_at=d.get("starts_daily_at", None),
        )


@dataclass
class Phone:
    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_type: str
    display_name: str
    errors: List[Dict[str, Any]]
    nickname: str
    properties: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Phone(
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            nickname=d.get("nickname", None),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ThermostatSchedule:
    climate_preset_key: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Dict[str, Any]]
    max_override_period_minutes: int
    name: str
    starts_at: str
    thermostat_schedule_id: str
    unstable_is_override_allowed: bool

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatSchedule(
            climate_preset_key=d.get("climate_preset_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            max_override_period_minutes=d.get("max_override_period_minutes", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            unstable_is_override_allowed=d.get("unstable_is_override_allowed", None),
        )


@dataclass
class UnmanagedAccessCode:
    access_code_id: str
    code: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    name: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAccessCode(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
        )


@dataclass
class UnmanagedAcsAccessGroup:
    access_group_type: str
    access_group_type_display_name: str
    acs_access_group_id: str
    acs_system_id: str
    created_at: str
    display_name: str
    external_type: str
    external_type_display_name: str
    is_managed: bool
    name: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsAccessGroup(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UnmanagedAcsCredential:
    access_method: str
    acs_credential_id: str
    acs_credential_pool_id: str
    acs_system_id: str
    acs_user_id: str
    assa_abloy_vostio_metadata: Dict[str, Any]
    card_number: str
    code: str
    created_at: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    is_issued: bool
    is_latest_desired_state_synced_with_provider: bool
    is_managed: bool
    is_multi_phone_sync_credential: bool
    is_one_time_use: bool
    issued_at: str
    latest_desired_state_synced_with_provider_at: str
    parent_acs_credential_id: str
    starts_at: str
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsCredential(
            access_method=d.get("access_method", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            card_number=d.get("card_number", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_issued=d.get("is_issued", None),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            is_managed=d.get("is_managed", None),
            is_multi_phone_sync_credential=d.get(
                "is_multi_phone_sync_credential", None
            ),
            is_one_time_use=d.get("is_one_time_use", None),
            issued_at=d.get("issued_at", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            parent_acs_credential_id=d.get("parent_acs_credential_id", None),
            starts_at=d.get("starts_at", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UnmanagedAcsUser:
    access_schedule: Dict[str, Any]
    acs_system_id: str
    acs_user_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_latest_desired_state_synced_with_provider: bool
    is_managed: bool
    is_suspended: bool
    latest_desired_state_synced_with_provider_at: str
    phone_number: str
    user_identity_email_address: str
    user_identity_full_name: str
    user_identity_id: str
    user_identity_phone_number: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAcsUser(
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            phone_number=d.get("phone_number", None),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UnmanagedDevice:
    can_hvac_cool: bool
    can_hvac_heat: bool
    can_hvac_heat_cool: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_remotely_lock: bool
    can_remotely_unlock: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    capabilities_supported: List[str]
    connected_account_id: str
    created_at: str
    device_id: str
    device_type: Any
    errors: List[Dict[str, Any]]
    is_managed: bool
    location: Dict[str, Any]
    properties: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedDevice(
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            capabilities_supported=d.get("capabilities_supported", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            location=DeepAttrDict(d.get("location", None)),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UserIdentity:
    created_at: str
    display_name: str
    email_address: str
    full_name: str
    phone_number: str
    user_identity_id: str
    user_identity_key: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UserIdentity(
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email_address=d.get("email_address", None),
            full_name=d.get("full_name", None),
            phone_number=d.get("phone_number", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_key=d.get("user_identity_key", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Webhook:
    event_types: List[str]
    secret: str
    url: str
    webhook_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Webhook(
            event_types=d.get("event_types", None),
            secret=d.get("secret", None),
            url=d.get("url", None),
            webhook_id=d.get("webhook_id", None),
        )


@dataclass
class Workspace:
    company_name: str
    connect_partner_name: str
    is_sandbox: bool
    name: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Workspace(
            company_name=d.get("company_name", None),
            connect_partner_name=d.get("connect_partner_name", None),
            is_sandbox=d.get("is_sandbox", None),
            name=d.get("name", None),
            workspace_id=d.get("workspace_id", None),
        )


class AbstractAcsAccessGroupsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_access_group_id: str) -> UnmanagedAcsAccessGroup:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self, *, acs_system_id: Optional[str] = None, acs_user_id: Optional[str] = None
    ) -> List[UnmanagedAcsAccessGroup]:
        raise NotImplementedError()


class AbstractAcsCredentialPools(abc.ABC):

    @abc.abstractmethod
    def list(self, *, acs_system_id: str) -> List[AcsCredentialPool]:
        raise NotImplementedError()


class AbstractAcsCredentialProvisioningAutomations(abc.ABC):

    @abc.abstractmethod
    def launch(
        self,
        *,
        credential_manager_acs_system_id: str,
        user_identity_id: str,
        acs_credential_pool_id: Optional[str] = None,
        create_credential_manager_user: Optional[bool] = None,
        credential_manager_acs_user_id: Optional[str] = None
    ) -> AcsCredentialProvisioningAutomation:
        raise NotImplementedError()


class AbstractAcsCredentials(abc.ABC):

    @abc.abstractmethod
    def create_offline_code(
        self,
        *,
        acs_user_id: str,
        allowed_acs_entrance_id: str,
        ends_at: Optional[str] = None,
        is_one_time_use: Optional[bool] = None,
        starts_at: Optional[str] = None
    ) -> AcsCredential:
        raise NotImplementedError()


class AbstractAcsCredentialsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_credential_id: str) -> UnmanagedAcsCredential:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> List[UnmanagedAcsCredential]:
        raise NotImplementedError()


class AbstractAcsUsersUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_user_id: str) -> UnmanagedAcsUser:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None
    ) -> List[UnmanagedAcsUser]:
        raise NotImplementedError()


class AbstractDevices(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, device_id: str) -> None:
        raise NotImplementedError()


class AbstractThermostats(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        raise NotImplementedError()


class AbstractAcs(abc.ABC):

    @property
    @abc.abstractmethod
    def access_groups(self) -> AbstractAcsAccessGroups:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credential_pools(self) -> AbstractAcsCredentialPools:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credential_provisioning_automations(
        self,
    ) -> AbstractAcsCredentialProvisioningAutomations:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credentials(self) -> AbstractAcsCredentials:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def users(self) -> AbstractAcsUsers:
        raise NotImplementedError()


@dataclass
class AbstractRoutes(abc.ABC):
    acs: AbstractAcs
    devices: AbstractDevices
    thermostats: AbstractThermostats
