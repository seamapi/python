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
class AccessGrant:
    access_grant_id: str
    access_grant_key: str
    access_method_ids: List[str]
    client_session_token: str
    created_at: str
    display_name: str
    ends_at: str
    instant_key_url: str
    location_ids: List[str]
    name: str
    requested_access_methods: List[Dict[str, Any]]
    space_ids: List[str]
    starts_at: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessGrant(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            access_method_ids=d.get("access_method_ids", None),
            client_session_token=d.get("client_session_token", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            instant_key_url=d.get("instant_key_url", None),
            location_ids=d.get("location_ids", None),
            name=d.get("name", None),
            requested_access_methods=d.get("requested_access_methods", None),
            space_ids=d.get("space_ids", None),
            starts_at=d.get("starts_at", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AccessMethod:
    access_method_id: str
    client_session_token: str
    code: str
    created_at: str
    display_name: str
    instant_key_url: str
    is_encoding_required: bool
    is_issued: bool
    issued_at: str
    mode: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessMethod(
            access_method_id=d.get("access_method_id", None),
            client_session_token=d.get("client_session_token", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            instant_key_url=d.get("instant_key_url", None),
            is_encoding_required=d.get("is_encoding_required", None),
            is_issued=d.get("is_issued", None),
            issued_at=d.get("issued_at", None),
            mode=d.get("mode", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class AcsAccessGroup:
    access_group_type: str
    access_group_type_display_name: str
    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: str
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
            connected_account_id=d.get("connected_account_id", None),
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
    connected_account_id: str
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
    user_identity_id: str
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
            connected_account_id=d.get("connected_account_id", None),
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
            user_identity_id=d.get("user_identity_id", None),
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
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEncoder(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
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
    can_unlock_with_card: bool
    can_unlock_with_code: bool
    can_unlock_with_mobile_key: bool
    connected_account_id: str
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
            can_unlock_with_card=d.get("can_unlock_with_card", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
            can_unlock_with_mobile_key=d.get("can_unlock_with_mobile_key", None),
            connected_account_id=d.get("connected_account_id", None),
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
    acs_access_group_count: float
    acs_system_id: str
    acs_user_count: float
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
            acs_access_group_count=d.get("acs_access_group_count", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_count=d.get("acs_user_count", None),
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
    connected_account_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_managed: bool
    is_suspended: bool
    last_successful_sync_at: str
    pending_mutations: List[Dict[str, Any]]
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
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            last_successful_sync_at=d.get("last_successful_sync_at", None),
            pending_mutations=d.get("pending_mutations", None),
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
class BridgeClientSession:
    bridge_client_machine_identifier_key: str
    bridge_client_name: str
    bridge_client_session_id: str
    bridge_client_session_token: str
    bridge_client_time_zone: str
    created_at: str
    errors: List[Dict[str, Any]]
    pairing_code: str
    pairing_code_expires_at: str
    tailscale_auth_key: str
    tailscale_hostname: str
    telemetry_token: str
    telemetry_token_expires_at: str
    telemetry_url: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return BridgeClientSession(
            bridge_client_machine_identifier_key=d.get(
                "bridge_client_machine_identifier_key", None
            ),
            bridge_client_name=d.get("bridge_client_name", None),
            bridge_client_session_id=d.get("bridge_client_session_id", None),
            bridge_client_session_token=d.get("bridge_client_session_token", None),
            bridge_client_time_zone=d.get("bridge_client_time_zone", None),
            created_at=d.get("created_at", None),
            errors=d.get("errors", None),
            pairing_code=d.get("pairing_code", None),
            pairing_code_expires_at=d.get("pairing_code_expires_at", None),
            tailscale_auth_key=d.get("tailscale_auth_key", None),
            tailscale_hostname=d.get("tailscale_hostname", None),
            telemetry_token=d.get("telemetry_token", None),
            telemetry_token_expires_at=d.get("telemetry_token_expires_at", None),
            telemetry_url=d.get("telemetry_url", None),
        )


@dataclass
class BridgeConnectedSystems:
    acs_system_display_name: str
    acs_system_id: str
    bridge_created_at: str
    bridge_id: str
    connected_account_created_at: str
    connected_account_id: str
    workspace_display_name: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return BridgeConnectedSystems(
            acs_system_display_name=d.get("acs_system_display_name", None),
            acs_system_id=d.get("acs_system_id", None),
            bridge_created_at=d.get("bridge_created_at", None),
            bridge_id=d.get("bridge_id", None),
            connected_account_created_at=d.get("connected_account_created_at", None),
            connected_account_id=d.get("connected_account_id", None),
            workspace_display_name=d.get("workspace_display_name", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ClientSession:
    client_session_id: str
    connect_webview_ids: List[str]
    connected_account_ids: List[str]
    created_at: str
    customer_id: str
    device_count: float
    expires_at: str
    token: str
    user_identifier_key: str
    user_identity_id: str
    user_identity_ids: List[str]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ClientSession(
            client_session_id=d.get("client_session_id", None),
            connect_webview_ids=d.get("connect_webview_ids", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            customer_id=d.get("customer_id", None),
            device_count=d.get("device_count", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
            user_identifier_key=d.get("user_identifier_key", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_ids=d.get("user_identity_ids", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ConnectWebview:
    accepted_capabilities: List[str]
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
    customer_key: str
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
            accepted_capabilities=d.get("accepted_capabilities", None),
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
            customer_key=d.get("customer_key", None),
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
    accepted_capabilities: List[str]
    account_type: str
    account_type_display_name: str
    automatically_manage_new_devices: bool
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    customer_key: str
    errors: List[Dict[str, Any]]
    user_identifier: Dict[str, Any]
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectedAccount(
            accepted_capabilities=d.get("accepted_capabilities", None),
            account_type=d.get("account_type", None),
            account_type_display_name=d.get("account_type_display_name", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            customer_key=d.get("customer_key", None),
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
    can_run_thermostat_programs: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    can_unlock_with_code: bool
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
            can_run_thermostat_programs=d.get("can_run_thermostat_programs", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
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
    can_run_thermostat_programs: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    can_unlock_with_code: bool
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
            can_run_thermostat_programs=d.get("can_run_thermostat_programs", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
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
    connected_account_custom_metadata: Dict[str, Any]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Dict[str, Any]
    device_id: str
    event_id: str
    event_type: str
    occurred_at: str
    workspace_id: str
    code: str
    backup_access_code_id: str
    access_grant_id: str
    acs_entrance_id: str
    access_method_id: str
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
    device_name: str
    enrollment_automation_id: str

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
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            code=d.get("code", None),
            backup_access_code_id=d.get("backup_access_code_id", None),
            access_grant_id=d.get("access_grant_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            access_method_id=d.get("access_method_id", None),
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
            device_name=d.get("device_name", None),
            enrollment_automation_id=d.get("enrollment_automation_id", None),
        )


@dataclass
class InstantKey:
    client_session_id: str
    created_at: str
    expires_at: str
    instant_key_id: str
    instant_key_url: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return InstantKey(
            client_session_id=d.get("client_session_id", None),
            created_at=d.get("created_at", None),
            expires_at=d.get("expires_at", None),
            instant_key_id=d.get("instant_key_id", None),
            instant_key_url=d.get("instant_key_url", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Location:
    created_at: str
    display_name: str
    geolocation: Dict[str, Any]
    location_id: str
    name: str
    time_zone: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Location(
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            geolocation=DeepAttrDict(d.get("geolocation", None)),
            location_id=d.get("location_id", None),
            name=d.get("name", None),
            time_zone=d.get("time_zone", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class MagicLink:
    building_block_type: str
    created_at: str
    customer_key: str
    expires_at: str
    url: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return MagicLink(
            building_block_type=d.get("building_block_type", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            expires_at=d.get("expires_at", None),
            url=d.get("url", None),
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
class Pagination:
    has_next_page: bool
    next_page_cursor: str
    next_page_url: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Pagination(
            has_next_page=d.get("has_next_page", None),
            next_page_cursor=d.get("next_page_cursor", None),
            next_page_url=d.get("next_page_url", None),
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
class PhoneRegistration:
    is_being_activated: bool
    phone_registration_id: str
    provider_name: str
    provider_state: Any

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return PhoneRegistration(
            is_being_activated=d.get("is_being_activated", None),
            phone_registration_id=d.get("phone_registration_id", None),
            provider_name=d.get("provider_name", None),
            provider_state=d.get("provider_state", None),
        )


@dataclass
class PhoneSession:
    provider_sessions: List[Dict[str, Any]]
    user_identity: Dict[str, Any]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return PhoneSession(
            provider_sessions=d.get("provider_sessions", None),
            user_identity=DeepAttrDict(d.get("user_identity", None)),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class Space:
    acs_entrance_count: float
    created_at: str
    device_count: float
    display_name: str
    name: str
    space_id: str
    space_key: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Space(
            acs_entrance_count=d.get("acs_entrance_count", None),
            created_at=d.get("created_at", None),
            device_count=d.get("device_count", None),
            display_name=d.get("display_name", None),
            name=d.get("name", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ThermostatDailyProgram:
    created_at: str
    device_id: str
    name: str
    periods: List[Dict[str, Any]]
    thermostat_daily_program_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatDailyProgram(
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            periods=d.get("periods", None),
            thermostat_daily_program_id=d.get("thermostat_daily_program_id", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class ThermostatSchedule:
    climate_preset_key: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Dict[str, Any]]
    is_override_allowed: bool
    max_override_period_minutes: int
    name: str
    starts_at: str
    thermostat_schedule_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatSchedule(
            climate_preset_key=d.get("climate_preset_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_override_allowed=d.get("is_override_allowed", None),
            max_override_period_minutes=d.get("max_override_period_minutes", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            workspace_id=d.get("workspace_id", None),
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
    connected_account_id: str
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
            connected_account_id=d.get("connected_account_id", None),
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
    connected_account_id: str
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
    user_identity_id: str
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
            connected_account_id=d.get("connected_account_id", None),
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
            user_identity_id=d.get("user_identity_id", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )


@dataclass
class UnmanagedAcsUser:
    access_schedule: Dict[str, Any]
    acs_system_id: str
    acs_user_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_managed: bool
    is_suspended: bool
    last_successful_sync_at: str
    pending_mutations: List[Dict[str, Any]]
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
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            last_successful_sync_at=d.get("last_successful_sync_at", None),
            pending_mutations=d.get("pending_mutations", None),
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
    can_run_thermostat_programs: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    can_unlock_with_code: bool
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
            can_run_thermostat_programs=d.get("can_run_thermostat_programs", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
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
    acs_user_ids: List[str]
    created_at: str
    display_name: str
    email_address: str
    errors: List[Dict[str, Any]]
    full_name: str
    phone_number: str
    user_identity_id: str
    user_identity_key: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UserIdentity(
            acs_user_ids=d.get("acs_user_ids", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            full_name=d.get("full_name", None),
            phone_number=d.get("phone_number", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_key=d.get("user_identity_key", None),
            warnings=d.get("warnings", None),
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
    connect_webview_customization: Dict[str, Any]
    is_sandbox: bool
    is_suspended: bool
    name: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Workspace(
            company_name=d.get("company_name", None),
            connect_partner_name=d.get("connect_partner_name", None),
            connect_webview_customization=DeepAttrDict(
                d.get("connect_webview_customization", None)
            ),
            is_sandbox=d.get("is_sandbox", None),
            is_suspended=d.get("is_suspended", None),
            name=d.get("name", None),
            workspace_id=d.get("workspace_id", None),
        )


class AbstractAccessCodesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        raise NotImplementedError()


class AbstractAccessCodesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def convert_to_managed(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
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
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None
    ) -> UnmanagedAccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        device_id: str,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedAccessCode]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        is_managed: bool,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAccessGrants(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        requested_access_methods: List[Dict[str, Any]],
        user_identity_id: Optional[str] = None,
        user_identity: Optional[Dict[str, Any]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        ends_at: Optional[str] = None,
        location: Optional[Dict[str, Any]] = None,
        location_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
        starts_at: Optional[str] = None
    ) -> AccessGrant:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, access_grant_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None
    ) -> AccessGrant:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        access_grant_ids: List[str],
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        location_id: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> List[AccessGrant]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_grant_id: str,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAccessMethods(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, access_method_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> AccessMethod:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AccessMethod]:
        raise NotImplementedError()


class AbstractAcsAccessGroups(abc.ABC):

    @abc.abstractmethod
    def add_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
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
    def remove_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAcsCredentials(abc.ABC):

    @abc.abstractmethod
    def assign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        access_method: str,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None
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
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        limit: Optional[float] = None
    ) -> List[AcsCredential]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def unassign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
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
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
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
        acs_credential_id_on_seam: Optional[str] = None,
        scenario: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractAcsEntrances(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        location_id: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None
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
        self, *, acs_access_group_id: str, acs_user_id: str
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        acs_system_id: str,
        full_name: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_access_group_ids: Optional[List[str]] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> AcsUser:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> AcsUser:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None
    ) -> List[AcsUser]:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_from_access_group(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_all_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def suspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def unsuspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


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


class AbstractClientSessions(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        customer_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
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
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> ClientSession:
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        without_user_identifier_key: Optional[bool] = None
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
        accepted_capabilities: Optional[List[str]] = None,
        accepted_providers: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        custom_redirect_failure_url: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_selection_mode: Optional[str] = None,
        provider_category: Optional[str] = None,
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
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        user_identifier_key: Optional[str] = None
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
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[ConnectedAccount]:
        raise NotImplementedError()

    @abc.abstractmethod
    def sync(self, *, connected_account_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        connected_account_id: str,
        accepted_capabilities: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        raise NotImplementedError()


class AbstractCustomers(abc.ABC):

    @abc.abstractmethod
    def create_portal(
        self,
        *,
        features: Optional[Dict[str, Any]] = None,
        is_embedded: Optional[bool] = None,
        customer_data: Optional[Dict[str, Any]] = None
    ) -> MagicLink:
        raise NotImplementedError()

    @abc.abstractmethod
    def push_data(
        self,
        *,
        customer_key: str,
        access_grants: Optional[List[Dict[str, Any]]] = None,
        bookings: Optional[List[Dict[str, Any]]] = None,
        buildings: Optional[List[Dict[str, Any]]] = None,
        common_areas: Optional[List[Dict[str, Any]]] = None,
        facilities: Optional[List[Dict[str, Any]]] = None,
        guests: Optional[List[Dict[str, Any]]] = None,
        listings: Optional[List[Dict[str, Any]]] = None,
        properties: Optional[List[Dict[str, Any]]] = None,
        property_listings: Optional[List[Dict[str, Any]]] = None,
        reservations: Optional[List[Dict[str, Any]]] = None,
        residents: Optional[List[Dict[str, Any]]] = None,
        rooms: Optional[List[Dict[str, Any]]] = None,
        spaces: Optional[List[Dict[str, Any]]] = None,
        tenants: Optional[List[Dict[str, Any]]] = None,
        units: Optional[List[Dict[str, Any]]] = None,
        user_identities: Optional[List[Dict[str, Any]]] = None,
        users: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        raise NotImplementedError()


class AbstractDevicesSimulate(abc.ABC):

    @abc.abstractmethod
    def connect(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def connect_to_hub(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect_from_hub(self, *, device_id: str) -> None:
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
        access_method_id: Optional[str] = None,
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
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedDevice]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, device_id: str, is_managed: bool) -> None:
        raise NotImplementedError()


class AbstractEvents(abc.ABC):

    @abc.abstractmethod
    def get(
        self,
        *,
        device_id: Optional[str] = None,
        event_id: Optional[str] = None,
        event_type: Optional[str] = None
    ) -> SeamEvent:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        unstable_offset: Optional[float] = None
    ) -> List[SeamEvent]:
        raise NotImplementedError()


class AbstractInstantKeys(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, instant_key_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, instant_key_id: str) -> InstantKey:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        raise NotImplementedError()


class AbstractLocksSimulate(abc.ABC):

    @abc.abstractmethod
    def keypad_code_entry(
        self,
        *,
        code: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def manual_lock_via_keypad(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()


class AbstractNoiseSensorsNoiseThresholds(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        ends_daily_at: str,
        starts_daily_at: str,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
        sync: Optional[bool] = None
    ) -> NoiseThreshold:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self, *, device_id: str, noise_threshold_id: str, sync: Optional[bool] = None
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
        device_id: str,
        noise_threshold_id: str,
        ends_daily_at: Optional[str] = None,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
        starts_daily_at: Optional[str] = None,
        sync: Optional[bool] = None
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
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        raise NotImplementedError()


class AbstractSpaces(abc.ABC):

    @abc.abstractmethod
    def add_acs_entrances(self, *, acs_entrance_ids: List[str], space_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_devices(self, *, device_ids: List[str], space_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        name: str,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        space_key: Optional[str] = None
    ) -> Space:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, space_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, space_id: Optional[str] = None, space_key: Optional[str] = None
    ) -> Space:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        space_ids: List[str],
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connected_account_id: Optional[str] = None,
        search: Optional[str] = None,
        space_key: Optional[str] = None
    ) -> List[Space]:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_acs_entrances(
        self, *, acs_entrance_ids: List[str], space_id: str
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_devices(self, *, device_ids: List[str], space_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        space_id: Optional[str] = None,
        space_key: Optional[str] = None
    ) -> Space:
        raise NotImplementedError()


class AbstractThermostatsDailyPrograms(abc.ABC):

    @abc.abstractmethod
    def create(
        self, *, device_id: str, name: str, periods: List[Dict[str, Any]]
    ) -> ThermostatDailyProgram:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, thermostat_daily_program_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        name: str,
        periods: List[Dict[str, Any]],
        thermostat_daily_program_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()


class AbstractThermostatsSchedules(abc.ABC):

    @abc.abstractmethod
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
        climate_preset_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_override_allowed: Optional[bool] = None,
        max_override_period_minutes: Optional[int] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None
    ) -> None:
        raise NotImplementedError()


class AbstractThermostatsSimulate(abc.ABC):

    @abc.abstractmethod
    def hvac_mode_adjusted(
        self,
        *,
        device_id: str,
        hvac_mode: str,
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


class AbstractUserIdentities(abc.ABC):

    @abc.abstractmethod
    def add_acs_user(self, *, acs_user_id: str, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        acs_system_ids: Optional[List[str]] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_instant_key(
        self, *, user_identity_id: str, max_use_count: Optional[float] = None
    ) -> InstantKey:
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
    def grant_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        credential_manager_acs_system_id: Optional[str] = None,
        search: Optional[str] = None
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
    def remove_acs_user(self, *, acs_user_id: str, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        user_identity_id: str,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
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
    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        raise NotImplementedError()


class AbstractWorkspaces(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        name: str,
        company_name: Optional[str] = None,
        connect_partner_name: Optional[str] = None,
        connect_webview_customization: Optional[Dict[str, Any]] = None,
        is_sandbox: Optional[bool] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None,
        webview_success_message: Optional[str] = None
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


class AbstractLocks(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractLocksSimulate:
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
        access_method_id: Optional[str] = None,
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
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
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
        acs_credential_id: Optional[str] = None,
        owner_user_identity_id: Optional[str] = None
    ) -> List[Phone]:
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
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        common_code_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        sync: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None
    ) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_multiple(
        self,
        *,
        device_ids: List[str],
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        behavior_when_code_cannot_be_shared: Optional[str] = None,
        code: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None
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
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None
    ) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_ids: Optional[List[str]] = None,
        customer_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[AccessCode]:
        raise NotImplementedError()

    @abc.abstractmethod
    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCode:
        raise NotImplementedError()

    @abc.abstractmethod
    def report_device_constraints(
        self,
        *,
        device_id: str,
        max_code_length: Optional[int] = None,
        min_code_length: Optional[int] = None,
        supported_code_lengths: Optional[List[int]] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_managed: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        sync: Optional[bool] = None,
        type: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update_multiple(
        self,
        *,
        common_code_key: str,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None
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
        access_method_id: Optional[str] = None,
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
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
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
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[str] = None,
        properties: Optional[Dict[str, Any]] = None
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
        access_method_id: Optional[str] = None,
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
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[Device]:
        raise NotImplementedError()


class AbstractThermostats(abc.ABC):

    @property
    @abc.abstractmethod
    def daily_programs(self) -> AbstractThermostatsDailyPrograms:
        raise NotImplementedError()

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
        climate_preset_key: str,
        device_id: str,
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
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_climate_preset(self, *, climate_preset_key: str, device_id: str) -> None:
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
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        sync: Optional[bool] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_method_id: Optional[str] = None,
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
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
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
        self, *, climate_preset_key: str, device_id: str
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
        device_id: str,
        hvac_mode_setting: str,
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
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None
    ) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
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
    access_grants: AbstractAccessGrants
    access_methods: AbstractAccessMethods
    acs: AbstractAcs
    action_attempts: AbstractActionAttempts
    client_sessions: AbstractClientSessions
    connect_webviews: AbstractConnectWebviews
    connected_accounts: AbstractConnectedAccounts
    customers: AbstractCustomers
    devices: AbstractDevices
    events: AbstractEvents
    instant_keys: AbstractInstantKeys
    locks: AbstractLocks
    noise_sensors: AbstractNoiseSensors
    phones: AbstractPhones
    spaces: AbstractSpaces
    thermostats: AbstractThermostats
    user_identities: AbstractUserIdentities
    webhooks: AbstractWebhooks
    workspaces: AbstractWorkspaces
