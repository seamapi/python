from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class UnmanagedDeviceErrors(ResourceMapping):
    """Array of errors associated with the device. Each error object within the array contains two fields: ``error_code`` and ``message``. ``error_code`` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar created_at: Date and time at which Seam created the error.

    :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

    :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

    :ivar is_device_error: Indicates that the error is not a device error.

    :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

    :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.
    """

    created_at: str
    error_code: str
    is_connected_account_error: bool
    is_device_error: bool
    message: str
    is_bridge_error: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            error_code=d.get("error_code", None),
            is_connected_account_error=d.get("is_connected_account_error", None),
            is_device_error=d.get("is_device_error", None),
            message=d.get("message", None),
            is_bridge_error=d.get("is_bridge_error", None),
        )


@dataclass
class UnmanagedDeviceLocation(ResourceMapping):
    """Location information for the device.

    :ivar location_name: Name of the device location.

    :ivar time_zone: Time zone of the device location.

    :ivar timezone: Deprecated: Use ``time_zone`` instead. Time zone of the device location.
    """

    location_name: str
    time_zone: str
    timezone: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            location_name=d.get("location_name", None),
            time_zone=d.get("time_zone", None),
            timezone=d.get("timezone", None),
        )


@dataclass
class UnmanagedDeviceBattery(ResourceMapping):
    """Keypad battery properties.

    :ivar level:"""

    level: float

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            level=d.get("level", None),
        )


@dataclass
class UnmanagedDeviceAccessoryKeypad(ResourceMapping):
    """Accessory keypad properties and state.

    :ivar battery: Keypad battery properties.

    :ivar is_connected: Indicates if an accessory keypad is connected to the device."""

    battery: UnmanagedDeviceBattery
    is_connected: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            battery=(
                UnmanagedDeviceBattery.from_dict(d.get("battery"))
                if d.get("battery") is not None
                else None
            ),
            is_connected=d.get("is_connected", None),
        )


@dataclass
class UnmanagedDeviceModel(ResourceMapping):
    """Device model-related properties.

    :ivar accessory_keypad_supported: Deprecated: use device.properties.model.can_connect_accessory_keypad

    :ivar can_connect_accessory_keypad: Indicates whether the device can connect a accessory keypad.

    :ivar display_name: Display name of the device model.

    :ivar has_built_in_keypad: Indicates whether the device has a built in accessory keypad.

    :ivar manufacturer_display_name: Display name that corresponds to the manufacturer-specific terminology for the device.

    :ivar offline_access_codes_supported: Deprecated: use device.can_program_offline_access_codes.

    :ivar online_access_codes_supported: Deprecated: use device.can_program_online_access_codes.
    """

    accessory_keypad_supported: bool
    can_connect_accessory_keypad: bool
    display_name: str
    has_built_in_keypad: bool
    manufacturer_display_name: str
    offline_access_codes_supported: bool
    online_access_codes_supported: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            accessory_keypad_supported=d.get("accessory_keypad_supported", None),
            can_connect_accessory_keypad=d.get("can_connect_accessory_keypad", None),
            display_name=d.get("display_name", None),
            has_built_in_keypad=d.get("has_built_in_keypad", None),
            manufacturer_display_name=d.get("manufacturer_display_name", None),
            offline_access_codes_supported=d.get(
                "offline_access_codes_supported", None
            ),
            online_access_codes_supported=d.get("online_access_codes_supported", None),
        )


@dataclass
class UnmanagedDeviceProperties(ResourceMapping):
    """properties of the device.

    :ivar accessory_keypad: Accessory keypad properties and state.

    :ivar battery: Represents the current status of the battery charge level.

    :ivar battery_level: Indicates the battery level of the device as a decimal value between 0 and 1, inclusive.

    :ivar image_alt_text: Alt text for the device image.

    :ivar image_url: Image URL for the device.

    :ivar manufacturer: Manufacturer of the device. When a device, such as a smart lock, is connected through a smart hub, the manufacturer of the device might be different from that of the smart hub.

    :ivar model: Device model-related properties.

    :ivar name: Deprecated: use device.display_name instead Name of the device.

    :ivar offline_access_codes_enabled: Deprecated: use device.can_program_offline_access_codes Indicates whether it is currently possible to use offline access codes for the device.

    :ivar online: Indicates whether the device is online.

    :ivar online_access_codes_enabled: Deprecated: use device.can_program_online_access_codes Indicates whether it is currently possible to use online access codes for the device.
    """

    accessory_keypad: UnmanagedDeviceAccessoryKeypad
    battery: UnmanagedDeviceBattery
    battery_level: float
    image_alt_text: str
    image_url: str
    manufacturer: str
    model: UnmanagedDeviceModel
    name: str
    offline_access_codes_enabled: bool
    online: bool
    online_access_codes_enabled: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            accessory_keypad=(
                UnmanagedDeviceAccessoryKeypad.from_dict(d.get("accessory_keypad"))
                if d.get("accessory_keypad") is not None
                else None
            ),
            battery=(
                UnmanagedDeviceBattery.from_dict(d.get("battery"))
                if d.get("battery") is not None
                else None
            ),
            battery_level=d.get("battery_level", None),
            image_alt_text=d.get("image_alt_text", None),
            image_url=d.get("image_url", None),
            manufacturer=d.get("manufacturer", None),
            model=(
                UnmanagedDeviceModel.from_dict(d.get("model"))
                if d.get("model") is not None
                else None
            ),
            name=d.get("name", None),
            offline_access_codes_enabled=d.get("offline_access_codes_enabled", None),
            online=d.get("online", None),
            online_access_codes_enabled=d.get("online_access_codes_enabled", None),
        )


@dataclass
class UnmanagedDeviceWarnings(ResourceMapping):
    """Array of warnings associated with the device. Each warning object within the array contains two fields: ``warning_code`` and ``message``. ``warning_code`` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar created_at: Date and time at which Seam created the warning.

    :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

    :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

    :ivar active_access_code_count: Number of active access codes on the device when the warning was set.

    :ivar max_active_access_code_count: Maximum number of active access codes supported by the device.
    """

    created_at: str
    message: str
    warning_code: str
    active_access_code_count: int
    max_active_access_code_count: int

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            message=d.get("message", None),
            warning_code=d.get("warning_code", None),
            active_access_code_count=d.get("active_access_code_count", None),
            max_active_access_code_count=d.get("max_active_access_code_count", None),
        )


@dataclass
class UnmanagedDevice:
    """Represents an `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

    :ivar can_configure_auto_lock: Indicates whether the lock supports configuring automatic locking.

    :ivar can_hvac_cool: Indicates whether the thermostat supports cooling.

    :ivar can_hvac_heat: Indicates whether the thermostat supports heating.

    :ivar can_hvac_heat_cool: Indicates whether the thermostat supports simultaneous heating and cooling.

    :ivar can_program_offline_access_codes: Indicates whether the device supports programming offline access codes.

    :ivar can_program_online_access_codes: Indicates whether the device supports programming online access codes.

    :ivar can_program_thermostat_programs_as_different_each_day: Indicates whether the thermostat supports different climate programs for each day of the week.

    :ivar can_program_thermostat_programs_as_same_each_day: Indicates whether the thermostat supports a single climate program applied to every day.

    :ivar can_program_thermostat_programs_as_weekday_weekend: Indicates whether the thermostat supports weekday/weekend climate programs.

    :ivar can_remotely_lock: Indicates whether the device supports remote locking.

    :ivar can_remotely_unlock: Indicates whether the device supports remote unlocking.

    :ivar can_run_thermostat_programs: Indicates whether the thermostat supports running climate programs.

    :ivar can_simulate_connection: Indicates whether the device supports simulating connection in a sandbox.

    :ivar can_simulate_disconnection: Indicates whether the device supports simulating disconnection in a sandbox.

    :ivar can_simulate_hub_connection: Indicates whether the hub supports simulating connection in a sandbox.

    :ivar can_simulate_hub_disconnection: Indicates whether the hub supports simulating disconnection in a sandbox.

    :ivar can_simulate_paid_subscription: Indicates whether the device supports simulating a paid subscription in a sandbox.

    :ivar can_simulate_removal: Indicates whether the device supports simulating removal in a sandbox.

    :ivar can_turn_off_hvac: Indicates whether the thermostat can be turned off.

    :ivar can_unlock_with_code: Indicates whether the lock supports unlocking with an access code.

    :ivar capabilities_supported: Collection of capabilities that the device supports when connected to Seam. Values are ``access_code``, which indicates that the device can manage and utilize digital PIN codes for secure access; ``lock``, which indicates that the device controls a door locking mechanism, enabling the remote opening and closing of doors and other entry points; ``noise_detection``, which indicates that the device supports monitoring and responding to ambient noise levels; ``thermostat``, which indicates that the device can regulate and adjust indoor temperatures; ``battery``, which indicates that the device can manage battery life and health; and ``phone``, which indicates that the device is a mobile device, such as a smartphone. **Important:** Superseded by `capability flags <https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags>`_.

    :ivar connected_account_id: Unique identifier for the account associated with the device.

    :ivar created_at: Date and time at which the device object was created.

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_, `connected account <https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account>`_, or `device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_, enables you to store custom information, like customer details or internal IDs from your application.

    :ivar device_id: ID of the device.

    :ivar device_type: Type of the device.

    :ivar errors: Array of errors associated with the device. Each error object within the array contains two fields: ``error_code`` and ``message``. ``error_code`` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar is_managed: Indicates that Seam does not manage the device.

    :ivar location: Location information for the device.

    :ivar properties: properties of the device.

    :ivar warnings: Array of warnings associated with the device. Each warning object within the array contains two fields: ``warning_code`` and ``message``. ``warning_code`` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the device.
    """

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
    errors: List[UnmanagedDeviceErrors]
    is_managed: bool
    location: UnmanagedDeviceLocation
    properties: UnmanagedDeviceProperties
    warnings: List[UnmanagedDeviceWarnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
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
            errors=[UnmanagedDeviceErrors.from_dict(i) for i in d.get("errors") or []],
            is_managed=d.get("is_managed", None),
            location=(
                UnmanagedDeviceLocation.from_dict(d.get("location"))
                if d.get("location") is not None
                else None
            ),
            properties=(
                UnmanagedDeviceProperties.from_dict(d.get("properties"))
                if d.get("properties") is not None
                else None
            ),
            warnings=[
                UnmanagedDeviceWarnings.from_dict(i) for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
