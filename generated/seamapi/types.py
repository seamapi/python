from typing import Any, Dict, List, Optional, Union
import abc
from dataclasses import dataclass
from seamapi.utils.deep_attr_dict import DeepAttrDict


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
  errors: Any
  warnings: Any
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
      is_waiting_for_code_assignment=d.get("is_waiting_for_code_assignment", None),
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
      is_backup_access_code_available=d.get("is_backup_access_code_available", None),
      is_backup=d.get("is_backup", None),
      pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
      is_external_modification_allowed=d.get("is_external_modification_allowed", None),
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
  errors: Any
  warnings: Any
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
  status: str
  action_type: str
  action_attempt_id: str
  result: str
  error: Dict[str, Any]

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return ActionAttempt(
      status=d.get("status", None),
      action_type=d.get("action_type", None),
      action_attempt_id=d.get("action_attempt_id", None),
      result=d.get("result", None),
      error=d.get("error", None),
      )
@dataclass
class ClientSession:
  client_session_id: str
  user_identifier_key: str
  created_at: str
  token: str
  device_count: float
  connected_account_ids: List[Any]
  connect_webview_ids: List[Any]
  user_identity_ids: List[Any]
  workspace_id: str

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return ClientSession(
      client_session_id=d.get("client_session_id", None),
      user_identifier_key=d.get("user_identifier_key", None),
      created_at=d.get("created_at", None),
      token=d.get("token", None),
      device_count=d.get("device_count", None),
      connected_account_ids=d.get("connected_account_ids", None),
      connect_webview_ids=d.get("connect_webview_ids", None),
      user_identity_ids=d.get("user_identity_ids", None),
      workspace_id=d.get("workspace_id", None),
      )
@dataclass
class ClimateSettingSchedule:
  climate_setting_schedule_id: str
  schedule_type: str
  device_id: str
  name: str
  schedule_starts_at: str
  schedule_ends_at: str
  created_at: str
  automatic_heating_enabled: bool
  automatic_cooling_enabled: bool
  hvac_mode_setting: str
  cooling_set_point_celsius: float
  heating_set_point_celsius: float
  cooling_set_point_fahrenheit: float
  heating_set_point_fahrenheit: float
  manual_override_allowed: bool

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return ClimateSettingSchedule(
      climate_setting_schedule_id=d.get("climate_setting_schedule_id", None),
      schedule_type=d.get("schedule_type", None),
      device_id=d.get("device_id", None),
      name=d.get("name", None),
      schedule_starts_at=d.get("schedule_starts_at", None),
      schedule_ends_at=d.get("schedule_ends_at", None),
      created_at=d.get("created_at", None),
      automatic_heating_enabled=d.get("automatic_heating_enabled", None),
      automatic_cooling_enabled=d.get("automatic_cooling_enabled", None),
      hvac_mode_setting=d.get("hvac_mode_setting", None),
      cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
      heating_set_point_celsius=d.get("heating_set_point_celsius", None),
      cooling_set_point_fahrenheit=d.get("cooling_set_point_fahrenheit", None),
      heating_set_point_fahrenheit=d.get("heating_set_point_fahrenheit", None),
      manual_override_allowed=d.get("manual_override_allowed", None),
      )
@dataclass
class ConnectWebview:
  connect_webview_id: str
  connected_account_id: str
  url: str
  workspace_id: str
  device_selection_mode: str
  accepted_providers: List[Any]
  accepted_devices: List[Any]
  any_provider_allowed: bool
  any_device_allowed: bool
  created_at: str
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
      connected_account_id=d.get("connected_account_id", None),
      url=d.get("url", None),
      workspace_id=d.get("workspace_id", None),
      device_selection_mode=d.get("device_selection_mode", None),
      accepted_providers=d.get("accepted_providers", None),
      accepted_devices=d.get("accepted_devices", None),
      any_provider_allowed=d.get("any_provider_allowed", None),
      any_device_allowed=d.get("any_device_allowed", None),
      created_at=d.get("created_at", None),
      login_successful=d.get("login_successful", None),
      status=d.get("status", None),
      custom_redirect_url=d.get("custom_redirect_url", None),
      custom_redirect_failure_url=d.get("custom_redirect_failure_url", None),
      custom_metadata=d.get("custom_metadata", None),
      automatically_manage_new_devices=d.get("automatically_manage_new_devices", None),
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
  errors: Any
  warnings: Any
  custom_metadata: Dict[str, Any]

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return ConnectedAccount(
      connected_account_id=d.get("connected_account_id", None),
      created_at=d.get("created_at", None),
      user_identifier=d.get("user_identifier", None),
      account_type=d.get("account_type", None),
      account_type_display_name=d.get("account_type_display_name", None),
      errors=d.get("errors", None),
      warnings=d.get("warnings", None),
      custom_metadata=d.get("custom_metadata", None),
      )
@dataclass
class Device:
  device_id: str
  device_type: Any
  capabilities_supported: List[Any]
  properties: Any
  location: Dict[str, Any]
  connected_account_id: str
  workspace_id: str
  errors: List[Any]
  warnings: List[Any]
  created_at: str
  is_managed: bool

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return Device(
      device_id=d.get("device_id", None),
      device_type=d.get("device_type", None),
      capabilities_supported=d.get("capabilities_supported", None),
      properties=d.get("properties", None),
      location=d.get("location", None),
      connected_account_id=d.get("connected_account_id", None),
      workspace_id=d.get("workspace_id", None),
      errors=d.get("errors", None),
      warnings=d.get("warnings", None),
      created_at=d.get("created_at", None),
      is_managed=d.get("is_managed", None),
      )
@dataclass
class UnmanagedDevice:
  device_id: str
  device_type: Any
  connected_account_id: str
  capabilities_supported: List[Any]
  workspace_id: str
  errors: List[Any]
  warnings: List[Any]
  created_at: str
  is_managed: bool
  properties: Dict[str, Any]

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return UnmanagedDevice(
      device_id=d.get("device_id", None),
      device_type=d.get("device_type", None),
      connected_account_id=d.get("connected_account_id", None),
      capabilities_supported=d.get("capabilities_supported", None),
      workspace_id=d.get("workspace_id", None),
      errors=d.get("errors", None),
      warnings=d.get("warnings", None),
      created_at=d.get("created_at", None),
      is_managed=d.get("is_managed", None),
      properties=d.get("properties", None),
      )
@dataclass
class DeviceProvider:
  device_provider_name: str
  display_name: str
  image_url: str
  provider_categories: List[Any]

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return DeviceProvider(
      device_provider_name=d.get("device_provider_name", None),
      display_name=d.get("display_name", None),
      image_url=d.get("image_url", None),
      provider_categories=d.get("provider_categories", None),
      )
@dataclass
class Event:
  event_id: str
  device_id: str
  event_type: str
  workspace_id: str
  created_at: str
  occurred_at: str

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return Event(
      event_id=d.get("event_id", None),
      device_id=d.get("device_id", None),
      event_type=d.get("event_type", None),
      workspace_id=d.get("workspace_id", None),
      created_at=d.get("created_at", None),
      occurred_at=d.get("occurred_at", None),
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
class ServiceHealth:
  service: str
  status: str
  description: str

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return ServiceHealth(
      service=d.get("service", None),
      status=d.get("status", None),
      description=d.get("description", None),
      )
@dataclass
class Webhook:
  webhook_id: str
  url: str
  event_types: List[Any]
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
  is_sandbox: bool
  connect_partner_name: str

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return Workspace(
      workspace_id=d.get("workspace_id", None),
      name=d.get("name", None),
      is_sandbox=d.get("is_sandbox", None),
      connect_partner_name=d.get("connect_partner_name", None),
      )
@dataclass
class AcsSystem:
  acs_system_id: str
  external_type: str
  external_type_display_name: str
  system_type: str
  system_type_display_name: str
  name: str
  created_at: str
  workspace_id: str
  connected_account_ids: List[Any]

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return AcsSystem(
      acs_system_id=d.get("acs_system_id", None),
      external_type=d.get("external_type", None),
      external_type_display_name=d.get("external_type_display_name", None),
      system_type=d.get("system_type", None),
      system_type_display_name=d.get("system_type_display_name", None),
      name=d.get("name", None),
      created_at=d.get("created_at", None),
      workspace_id=d.get("workspace_id", None),
      connected_account_ids=d.get("connected_account_ids", None),
      )
@dataclass
class AcsAccessGroup:
  acs_access_group_id: str
  acs_system_id: str
  workspace_id: str
  name: str
  access_group_type: str
  access_group_type_display_name: str
  external_type: str
  external_type_display_name: str
  created_at: str

  @staticmethod
  def from_dict(d: Dict[str, Any]):
    return AcsAccessGroup(
      acs_access_group_id=d.get("acs_access_group_id", None),
      acs_system_id=d.get("acs_system_id", None),
      workspace_id=d.get("workspace_id", None),
      name=d.get("name", None),
      access_group_type=d.get("access_group_type", None),
      access_group_type_display_name=d.get("access_group_type_display_name", None),
      external_type=d.get("external_type", None),
      external_type_display_name=d.get("external_type_display_name", None),
      created_at=d.get("created_at", None),
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
  full_name: str
  email: str
  email_address: str
  phone_number: str

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
      full_name=d.get("full_name", None),
      email=d.get("email", None),
      email_address=d.get("email_address", None),
      phone_number=d.get("phone_number", None),
      )


class SeamAPIException(Exception):
  pass


class AbstractAccessCodes(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, device_id: Optional[Any] = None, name: Optional[Any] = None, starts_at: Optional[Any] = None, ends_at: Optional[Any] = None, code: Optional[Any] = None, sync: Optional[Any] = None, attempt_for_offline_device: Optional[Any] = None, common_code_key: Optional[Any] = None, prefer_native_scheduling: Optional[Any] = None, use_backup_access_code_pool: Optional[Any] = None, allow_external_modification: Optional[Any] = None, is_external_modification_allowed: Optional[Any] = None, use_offline_access_code: Optional[Any] = None, is_offline_access_code: Optional[Any] = None, is_one_time_use: Optional[Any] = None, max_time_rounding: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def create_multiple(self, device_ids: Optional[Any] = None, behavior_when_code_cannot_be_shared: Optional[Any] = None, name: Optional[Any] = None, starts_at: Optional[Any] = None, ends_at: Optional[Any] = None, code: Optional[Any] = None, attempt_for_offline_device: Optional[Any] = None, prefer_native_scheduling: Optional[Any] = None, use_backup_access_code_pool: Optional[Any] = None, allow_external_modification: Optional[Any] = None, is_external_modification_allowed: Optional[Any] = None, use_offline_access_code: Optional[Any] = None, is_offline_access_code: Optional[Any] = None, is_one_time_use: Optional[Any] = None, max_time_rounding: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def delete(self, device_id: Optional[Any] = None, access_code_id: Optional[Any] = None, sync: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def generate_code(self, device_id: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, access_code_id: Any, device_id: Optional[Any] = None, code: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, device_id: Optional[Any] = None, access_code_ids: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def pull_backup_access_code(self, access_code_id: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def update(self, name: Optional[Any] = None, starts_at: Optional[Any] = None, ends_at: Optional[Any] = None, code: Optional[Any] = None, sync: Optional[Any] = None, attempt_for_offline_device: Optional[Any] = None, prefer_native_scheduling: Optional[Any] = None, use_backup_access_code_pool: Optional[Any] = None, allow_external_modification: Optional[Any] = None, is_external_modification_allowed: Optional[Any] = None, use_offline_access_code: Optional[Any] = None, is_offline_access_code: Optional[Any] = None, is_one_time_use: Optional[Any] = None, max_time_rounding: Optional[Any] = None, access_code_id: Optional[Any] = None, device_id: Optional[Any] = None, type: Optional[Any] = None, is_managed: Optional[Any] = None):
    raise NotImplementedError()
class AbstractActionAttempts(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, action_attempt_id: Any):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, action_attempt_ids: Optional[Any] = None):
    raise NotImplementedError()
class AbstractClientSessions(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, user_identifier_key: Optional[Any] = None, connect_webview_ids: Optional[Any] = None, connected_account_ids: Optional[Any] = None, user_identity_ids: Optional[Any] = None, expires_at: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, client_session_id: Any, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get_or_create(self, user_identifier_key: Optional[Any] = None, connect_webview_ids: Optional[Any] = None, connected_account_ids: Optional[Any] = None, user_identity_ids: Optional[Any] = None, expires_at: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, client_session_id: Optional[Any] = None, user_identifier_key: Optional[Any] = None, connect_webview_id: Optional[Any] = None, without_user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
class AbstractConnectWebviews(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, device_selection_mode: Optional[Any] = None, custom_redirect_url: Optional[Any] = None, custom_redirect_failure_url: Optional[Any] = None, accepted_providers: Optional[Any] = None, provider_category: Optional[Any] = None, custom_metadata: Optional[Any] = None, automatically_manage_new_devices: Optional[Any] = None, wait_for_device_creation: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, connect_webview_id: Any):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
class AbstractConnectedAccounts(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, connected_account_id: Any, email: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, ):
    raise NotImplementedError()
class AbstractDevices(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, device_id: Any, name: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, connected_account_id: Optional[Any] = None, connected_account_ids: Optional[Any] = None, connect_webview_id: Optional[Any] = None, device_types: Optional[Any] = None, manufacturer: Optional[Any] = None, device_ids: Optional[Any] = None, limit: Optional[Any] = None, created_before: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list_device_providers(self, provider_category: Optional[Any] = None):
    raise NotImplementedError()
class AbstractEvents(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, event_id: Any, event_type: Optional[Any] = None, device_id: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, since: Optional[Any] = None, between: Optional[Any] = None, device_id: Optional[Any] = None, device_ids: Optional[Any] = None, access_code_id: Optional[Any] = None, access_code_ids: Optional[Any] = None, event_type: Optional[Any] = None, event_types: Optional[Any] = None, connected_account_id: Optional[Any] = None):
    raise NotImplementedError()
class AbstractLocks(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, device_id: Any, name: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, connected_account_id: Optional[Any] = None, connected_account_ids: Optional[Any] = None, connect_webview_id: Optional[Any] = None, device_types: Optional[Any] = None, manufacturer: Optional[Any] = None, device_ids: Optional[Any] = None, limit: Optional[Any] = None, created_before: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def lock_door(self, device_id: Optional[Any] = None, sync: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def unlock_door(self, device_id: Optional[Any] = None, sync: Optional[Any] = None):
    raise NotImplementedError()
class AbstractHealth(abc.ABC):
  pass
class AbstractThermostats(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, device_id: Optional[Any] = None, name: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, connected_account_id: Optional[Any] = None, connected_account_ids: Optional[Any] = None, connect_webview_id: Optional[Any] = None, device_types: Optional[Any] = None, manufacturer: Optional[Any] = None, device_ids: Optional[Any] = None, limit: Optional[Any] = None, created_before: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
class AbstractUserIdentities(abc.ABC):
  pass
class AbstractWebhooks(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, url: Optional[Any] = None, event_types: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, webhook_id: Any):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, ):
    raise NotImplementedError()
class AbstractWorkspaces(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, ):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, ):
    raise NotImplementedError()
class AbstractSimulateAccessCodes(abc.ABC):

  
  
  @abc.abstractmethod
  def create_unmanaged_access_code(self, device_id: Optional[Any] = None, name: Optional[Any] = None, code: Optional[Any] = None):
    raise NotImplementedError()
class AbstractUnmanagedAccessCodes(abc.ABC):

  
  
  @abc.abstractmethod
  def delete(self, access_code_id: Optional[Any] = None, sync: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, access_code_id: Any, device_id: Optional[Any] = None, code: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, device_id: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
class AbstractAccessGroupsAcs(abc.ABC):
  pass
class AbstractCredentialPoolsAcs(abc.ABC):
  pass
class AbstractCredentialProvisioningAutomationsAcs(abc.ABC):
  pass
class AbstractCredentialsAcs(abc.ABC):
  pass
class AbstractEntrancesAcs(abc.ABC):
  pass
class AbstractSystemsAcs(abc.ABC):
  pass
class AbstractUsersAcs(abc.ABC):
  pass
class AbstractUnmanagedDevices(abc.ABC):

  
  
  @abc.abstractmethod
  def get(self, device_id: Any, name: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, connected_account_id: Optional[Any] = None, connected_account_ids: Optional[Any] = None, connect_webview_id: Optional[Any] = None, device_types: Optional[Any] = None, manufacturer: Optional[Any] = None, device_ids: Optional[Any] = None, limit: Optional[Any] = None, created_before: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
class AbstractServiceHealth(abc.ABC):
  pass
class AbstractNoiseThresholdsNoiseSensors(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, device_id: Optional[Any] = None, sync: Optional[Any] = None, name: Optional[Any] = None, starts_daily_at: Optional[Any] = None, ends_daily_at: Optional[Any] = None, noise_threshold_decibels: Optional[Any] = None, noise_threshold_nrs: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def delete(self, noise_threshold_id: Optional[Any] = None, device_id: Optional[Any] = None, sync: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, noise_threshold_id: Any):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, device_id: Optional[Any] = None, is_programmed: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def update(self, noise_threshold_id: Optional[Any] = None, device_id: Optional[Any] = None, sync: Optional[Any] = None, name: Optional[Any] = None, starts_daily_at: Optional[Any] = None, ends_daily_at: Optional[Any] = None, noise_threshold_decibels: Optional[Any] = None, noise_threshold_nrs: Optional[Any] = None):
    raise NotImplementedError()
class AbstractSimulateNoiseSensors(abc.ABC):
  pass
class AbstractClimateSettingSchedulesThermostats(abc.ABC):

  
  
  @abc.abstractmethod
  def create(self, schedule_type: Optional[Any] = None, device_id: Optional[Any] = None, name: Optional[Any] = None, schedule_starts_at: Optional[Any] = None, schedule_ends_at: Optional[Any] = None, automatic_heating_enabled: Optional[Any] = None, automatic_cooling_enabled: Optional[Any] = None, hvac_mode_setting: Optional[Any] = None, cooling_set_point_celsius: Optional[Any] = None, heating_set_point_celsius: Optional[Any] = None, cooling_set_point_fahrenheit: Optional[Any] = None, heating_set_point_fahrenheit: Optional[Any] = None, manual_override_allowed: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def get(self, climate_setting_schedule_id: Any, device_id: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def list(self, device_id: Optional[Any] = None, user_identifier_key: Optional[Any] = None):
    raise NotImplementedError()
  
  
  @abc.abstractmethod
  def update(self, climate_setting_schedule_id: Optional[Any] = None, schedule_type: Optional[Any] = None, name: Optional[Any] = None, schedule_starts_at: Optional[Any] = None, schedule_ends_at: Optional[Any] = None, automatic_heating_enabled: Optional[Any] = None, automatic_cooling_enabled: Optional[Any] = None, hvac_mode_setting: Optional[Any] = None, cooling_set_point_celsius: Optional[Any] = None, heating_set_point_celsius: Optional[Any] = None, cooling_set_point_fahrenheit: Optional[Any] = None, heating_set_point_fahrenheit: Optional[Any] = None, manual_override_allowed: Optional[Any] = None):
    raise NotImplementedError()


@dataclass
class AbstractRoutes(abc.ABC):
  access_codes: AbstractAccessCodes
  action_attempts: AbstractActionAttempts
  client_sessions: AbstractClientSessions
  connect_webviews: AbstractConnectWebviews
  connected_accounts: AbstractConnectedAccounts
  devices: AbstractDevices
  events: AbstractEvents
  locks: AbstractLocks
  health: AbstractHealth
  thermostats: AbstractThermostats
  user_identities: AbstractUserIdentities
  webhooks: AbstractWebhooks
  workspaces: AbstractWorkspaces

  @abc.abstractmethod
  def make_request(self, method: str, path: str, **kwargs) -> Any:
    raise NotImplementedError

@dataclass
class AbstractSeam(AbstractRoutes):
  api_key: str
  api_url: str

  @abc.abstractmethod
  def __init__(self, api_key: Optional[str] = None):
    raise NotImplementedError