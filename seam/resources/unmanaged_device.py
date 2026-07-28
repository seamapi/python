from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UnmanagedDevice:
    """Represents an [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices). An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

    :ivar can_configure_auto_lock: Indicates whether the lock supports configuring automatic locking.
    :vartype can_configure_auto_lock: bool

    :ivar can_hvac_cool: Indicates whether the thermostat supports cooling.
    :vartype can_hvac_cool: bool

    :ivar can_hvac_heat: Indicates whether the thermostat supports heating.
    :vartype can_hvac_heat: bool

    :ivar can_hvac_heat_cool: Indicates whether the thermostat supports simultaneous heating and cooling.
    :vartype can_hvac_heat_cool: bool

    :ivar can_program_offline_access_codes: Indicates whether the device supports programming offline access codes.
    :vartype can_program_offline_access_codes: bool

    :ivar can_program_online_access_codes: Indicates whether the device supports programming online access codes.
    :vartype can_program_online_access_codes: bool

    :ivar can_program_thermostat_programs_as_different_each_day: Indicates whether the thermostat supports different climate programs for each day of the week.
    :vartype can_program_thermostat_programs_as_different_each_day: bool

    :ivar can_program_thermostat_programs_as_same_each_day: Indicates whether the thermostat supports a single climate program applied to every day.
    :vartype can_program_thermostat_programs_as_same_each_day: bool

    :ivar can_program_thermostat_programs_as_weekday_weekend: Indicates whether the thermostat supports weekday/weekend climate programs.
    :vartype can_program_thermostat_programs_as_weekday_weekend: bool

    :ivar can_remotely_lock: Indicates whether the device supports remote locking.
    :vartype can_remotely_lock: bool

    :ivar can_remotely_unlock: Indicates whether the device supports remote unlocking.
    :vartype can_remotely_unlock: bool

    :ivar can_run_thermostat_programs: Indicates whether the thermostat supports running climate programs.
    :vartype can_run_thermostat_programs: bool

    :ivar can_simulate_connection: Indicates whether the device supports simulating connection in a sandbox.
    :vartype can_simulate_connection: bool

    :ivar can_simulate_disconnection: Indicates whether the device supports simulating disconnection in a sandbox.
    :vartype can_simulate_disconnection: bool

    :ivar can_simulate_hub_connection: Indicates whether the hub supports simulating connection in a sandbox.
    :vartype can_simulate_hub_connection: bool

    :ivar can_simulate_hub_disconnection: Indicates whether the hub supports simulating disconnection in a sandbox.
    :vartype can_simulate_hub_disconnection: bool

    :ivar can_simulate_paid_subscription: Indicates whether the device supports simulating a paid subscription in a sandbox.
    :vartype can_simulate_paid_subscription: bool

    :ivar can_simulate_removal: Indicates whether the device supports simulating removal in a sandbox.
    :vartype can_simulate_removal: bool

    :ivar can_turn_off_hvac: Indicates whether the thermostat can be turned off.
    :vartype can_turn_off_hvac: bool

    :ivar can_unlock_with_code: Indicates whether the lock supports unlocking with an access code.
    :vartype can_unlock_with_code: bool

    :ivar capabilities_supported: Collection of capabilities that the device supports when connected to Seam. Values are `access_code`, which indicates that the device can manage and utilize digital PIN codes for secure access; `lock`, which indicates that the device controls a door locking mechanism, enabling the remote opening and closing of doors and other entry points; `noise_detection`, which indicates that the device supports monitoring and responding to ambient noise levels; `thermostat`, which indicates that the device can regulate and adjust indoor temperatures; `battery`, which indicates that the device can manage battery life and health; and `phone`, which indicates that the device is a mobile device, such as a smartphone. **Important:** Superseded by [capability flags](https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags).
    :vartype capabilities_supported: List[str]

    :ivar connected_account_id: Unique identifier for the account associated with the device.
    :vartype connected_account_id: str

    :ivar created_at: Date and time at which the device object was created.
    :vartype created_at: str

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview), [connected account](https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account), or [device](https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device), enables you to store custom information, like customer details or internal IDs from your application.
    :vartype custom_metadata: Dict[str, Any]

    :ivar device_id: ID of the device.
    :vartype device_id: str

    :ivar device_type: Type of the device.
    :vartype device_type: str

    :ivar errors: Array of errors associated with the device. Each error object within the array contains two fields: `error_code` and `message`. `error_code` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. `message` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.
    :vartype errors: List[Dict[str, Any]]

    :ivar is_managed: Indicates that Seam does not manage the device.
    :vartype is_managed: bool

    :ivar location: Location information for the device.
    :vartype location: Dict[str, Any]

    :ivar properties: properties of the device.
    :vartype properties: Dict[str, Any]

    :ivar warnings: Array of warnings associated with the device. Each warning object within the array contains two fields: `warning_code` and `message`. `warning_code` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. `message` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.
    :vartype warnings: List[Dict[str, Any]]

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the device.
    :vartype workspace_id: str"""

    can_configure_auto_lock: bool
    can_hvac_cool: bool
    can_hvac_heat: bool
    can_hvac_heat_cool: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_program_thermostat_programs_as_different_each_day: bool
    can_program_thermostat_programs_as_same_each_day: bool
    can_program_thermostat_programs_as_weekday_weekend: bool
    can_remotely_lock: bool
    can_remotely_unlock: bool
    can_run_thermostat_programs: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_hub_connection: bool
    can_simulate_hub_disconnection: bool
    can_simulate_paid_subscription: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    can_unlock_with_code: bool
    capabilities_supported: List[str]
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_type: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    location: Dict[str, Any]
    properties: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedDevice(
            can_configure_auto_lock=d.get("can_configure_auto_lock", None),
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_program_thermostat_programs_as_different_each_day=d.get(
                "can_program_thermostat_programs_as_different_each_day", None
            ),
            can_program_thermostat_programs_as_same_each_day=d.get(
                "can_program_thermostat_programs_as_same_each_day", None
            ),
            can_program_thermostat_programs_as_weekday_weekend=d.get(
                "can_program_thermostat_programs_as_weekday_weekend", None
            ),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_run_thermostat_programs=d.get("can_run_thermostat_programs", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_hub_connection=d.get("can_simulate_hub_connection", None),
            can_simulate_hub_disconnection=d.get(
                "can_simulate_hub_disconnection", None
            ),
            can_simulate_paid_subscription=d.get(
                "can_simulate_paid_subscription", None
            ),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
            capabilities_supported=d.get("capabilities_supported", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            location=DeepAttrDict(d.get("location", None)),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
