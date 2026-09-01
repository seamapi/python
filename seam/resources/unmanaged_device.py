from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


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

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_, `connected account <https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account>`_, or `device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_, enables you to store custom information, like customer details or internal IDs from your application. Keys set to ``null`` or to an empty string are omitted.

    :ivar device_id: ID of the device.

    :ivar device_type: Type of the device.

    :ivar display_name: Display name of the device, defaults to nickname (if it is set) or ``properties.appearance.name``, otherwise. Enables administrators and users to identify the device easily, especially when there are numerous devices.

    :ivar errors: Array of errors associated with the device. Each error object within the array contains two fields: ``error_code`` and ``message``. ``error_code`` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar is_managed: Indicates that Seam does not manage the device.

    :ivar location: Location information for the device.

    :ivar properties: properties of the device.

    :ivar warnings: Array of warnings associated with the device. Each warning object within the array contains two fields: ``warning_code`` and ``message``. ``warning_code`` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the device.
    """

    @dataclass
    class AccountDisconnectedError(ResourceMapping):
        """Indicates that the account is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["account_disconnected"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitExceededError(ResourceMapping):
        """Indicates that the Salto site user limit has been reached.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["salto_ks_subscription_limit_exceeded"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class InsufficientPermissionsError(ResourceMapping):
        """Indicates that Seam's integration user does not have sufficient permissions on the provider's system to which this device belongs, so Seam cannot manage access codes or unlock the device. See the error message for specifics, then either reauthorize the connected account in Seam or grant the integration user the required permissions in the provider's system.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["insufficient_permissions"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DormakabaSitesDisconnectedError(ResourceMapping):
        """Indicates that one or more dormakaba sites associated with the connected account could not be connected. Contact dormakaba support.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["dormakaba_sites_disconnected"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceOfflineError(ResourceMapping):
        """Indicates that the device is offline.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_offline"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceRemovedError(ResourceMapping):
        """Indicates that the device has been removed.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_removed"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class HubDisconnectedError(ResourceMapping):
        """Indicates that the hub is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["hub_disconnected"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceDisconnectedError(ResourceMapping):
        """Indicates that the device is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_disconnected"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class EmptyBackupAccessCodePoolError(ResourceMapping):
        """Indicates that the `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is empty.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["empty_backup_access_code_pool"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class AugustLockNotAuthorizedError(ResourceMapping):
        """Indicates that the user is not authorized to use the August lock.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["august_lock_not_authorized"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class MissingDeviceCredentialsError(ResourceMapping):
        """Indicates that device credentials are missing.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["missing_device_credentials"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class AuxiliaryHeatRunningError(ResourceMapping):
        """Indicates that the auxiliary heat is running.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["auxiliary_heat_running"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class SubscriptionRequiredError(ResourceMapping):
        """Indicates that a subscription is required to connect.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["subscription_required"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class BridgeDisconnectedError(ResourceMapping):
        """Indicates that the Seam API cannot communicate with `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_, for example, if the Seam Bridge executable has stopped or if the computer running the Seam Bridge executable is offline. See also `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-seam_bridge_disconnected>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar is_connected_account_error: Indicates whether the error is related specifically to the connected account.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["bridge_disconnected"]
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class Location(ResourceMapping):
        """Location information for the device.

        :ivar location_name: Name of the device location.

        :ivar room_name: Name of the room within the device location, when the provider reports one.

        :ivar time_zone: Time zone of the device location.

        :ivar timezone: Deprecated: Use ``time_zone`` instead. Time zone of the device location.
        """

        location_name: Optional[str]
        room_name: Optional[str]
        time_zone: Optional[str]
        timezone: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                location_name=d.get("location_name", None),
                room_name=d.get("room_name", None),
                time_zone=d.get("time_zone", None),
                timezone=d.get("timezone", None),
            )

    @dataclass
    class Properties(ResourceMapping):
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

        @dataclass
        class AccessoryKeypad(ResourceMapping):
            """Accessory keypad properties and state.

            :ivar battery: Keypad battery properties.

            :ivar is_connected: Indicates if an accessory keypad is connected to the device.
            """

            @dataclass
            class Battery(ResourceMapping):
                """Keypad battery properties.

                :ivar level:"""

                level: float

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        level=d.get("level", None),
                    )

            battery: Optional[Battery]
            is_connected: bool

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    battery=_object_from_dict(cls.Battery, d.get("battery")),
                    is_connected=d.get("is_connected", None),
                )

        @dataclass
        class Battery(ResourceMapping):
            """Represents the current status of the battery charge level.

            :ivar level: Battery charge level as a value between 0 and 1, inclusive.

            :ivar status: Represents the current status of the battery charge level. Values are ``critical``, which indicates an extremely low level, suggesting imminent shutdown or an urgent need for charging; ``low``, which signifies that the battery is under the preferred threshold and should be charged soon; ``good``, which denotes a satisfactory charge level, adequate for normal use without the immediate need for recharging; and ``full``, which represents a battery that is fully charged, providing the maximum duration of usage.
            """

            level: float
            status: Literal["critical", "low", "good", "full"]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    level=d.get("level", None),
                    status=d.get("status", None),
                )

        @dataclass
        class Model(ResourceMapping):
            """Device model-related properties.

            :ivar accessory_keypad_supported: Deprecated: use device.properties.model.can_connect_accessory_keypad

            :ivar can_connect_accessory_keypad: Indicates whether the device can connect a accessory keypad.

            :ivar display_name: Display name of the device model.

            :ivar has_built_in_keypad: Indicates whether the device has a built in accessory keypad.

            :ivar manufacturer_display_name: Display name that corresponds to the manufacturer-specific terminology for the device.

            :ivar offline_access_codes_supported: Deprecated: use device.can_program_offline_access_codes.

            :ivar online_access_codes_supported: Deprecated: use device.can_program_online_access_codes.
            """

            accessory_keypad_supported: Optional[bool]
            can_connect_accessory_keypad: Optional[bool]
            display_name: str
            has_built_in_keypad: Optional[bool]
            manufacturer_display_name: str
            offline_access_codes_supported: Optional[bool]
            online_access_codes_supported: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    accessory_keypad_supported=d.get(
                        "accessory_keypad_supported", None
                    ),
                    can_connect_accessory_keypad=d.get(
                        "can_connect_accessory_keypad", None
                    ),
                    display_name=d.get("display_name", None),
                    has_built_in_keypad=d.get("has_built_in_keypad", None),
                    manufacturer_display_name=d.get("manufacturer_display_name", None),
                    offline_access_codes_supported=d.get(
                        "offline_access_codes_supported", None
                    ),
                    online_access_codes_supported=d.get(
                        "online_access_codes_supported", None
                    ),
                )

        accessory_keypad: Optional[AccessoryKeypad]
        battery: Optional[Battery]
        battery_level: Optional[float]
        image_alt_text: Optional[str]
        image_url: Optional[str]
        manufacturer: Optional[str]
        model: Optional[Model]
        name: str
        offline_access_codes_enabled: Optional[bool]
        online: bool
        online_access_codes_enabled: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                accessory_keypad=_object_from_dict(
                    cls.AccessoryKeypad, d.get("accessory_keypad")
                ),
                battery=_object_from_dict(cls.Battery, d.get("battery")),
                battery_level=d.get("battery_level", None),
                image_alt_text=d.get("image_alt_text", None),
                image_url=d.get("image_url", None),
                manufacturer=d.get("manufacturer", None),
                model=_object_from_dict(cls.Model, d.get("model")),
                name=d.get("name", None),
                offline_access_codes_enabled=d.get(
                    "offline_access_codes_enabled", None
                ),
                online=d.get("online", None),
                online_access_codes_enabled=d.get("online_access_codes_enabled", None),
            )

    @dataclass
    class PartialBackupAccessCodePoolWarning(ResourceMapping):
        """Indicates that the backup access code is unhealthy.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["partial_backup_access_code_pool"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ManyActiveBackupCodesWarning(ResourceMapping):
        """Indicates that there are too many backup codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["many_active_backup_codes"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ThirdPartyIntegrationDetectedWarning(ResourceMapping):
        """Indicates that a third-party integration has been detected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["third_party_integration_detected"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TtlockLockGatewayUnlockingNotEnabledWarning(ResourceMapping):
        """Indicates that the Remote Unlock feature is not enabled in the settings."

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ttlock_lock_gateway_unlocking_not_enabled"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TtlockWeakGatewaySignalWarning(ResourceMapping):
        """Indicates that the gateway signal is weak.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ttlock_weak_gateway_signal"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class PowerSavingModeWarning(ResourceMapping):
        """Indicates that the device is in power saving mode and may have limited functionality.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["power_saving_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TemperatureThresholdExceededWarning(ResourceMapping):
        """Indicates that the temperature threshold has been exceeded.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["temperature_threshold_exceeded"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceCommunicationDegradedWarning(ResourceMapping):
        """Indicates that the device appears to be unresponsive.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["device_communication_degraded"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ScheduledMaintenanceWindowWarning(ResourceMapping):
        """Indicates that a scheduled maintenance window has been detected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["scheduled_maintenance_window"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceHasFlakyConnectionWarning(ResourceMapping):
        """Indicates that the device has a flaky connection.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["device_has_flaky_connection"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsOfficeModeWarning(ResourceMapping):
        """Indicates that the Salto KS lock is in Office Mode. Access Codes will not unlock doors.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_office_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsPrivacyModeWarning(ResourceMapping):
        """Indicates that the Salto KS lock is in Privacy Mode. Access Codes will not unlock doors.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_privacy_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class PrivacyModeWarning(ResourceMapping):
        """Indicates that the lock is in Privacy Mode. Access codes and remote unlock are blocked until Privacy Mode is disabled.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["privacy_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitAlmostReachedWarning(ResourceMapping):
        """Indicates that the Salto KS site has exceeded 80% of the maximum number of allowed users. Increase your subscription limit or delete some users from your site.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_subscription_limit_almost_reached"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsLockAccessCodeSupportRemovedWarning(ResourceMapping):
        """Indicates that a change in the reported device model has been detected for this Salto KS lock, which may occur after an IQ hub reset. Access code support may be affected. See https://help.getseam.com/articles/5098842588-salto-ks-lock-loses-access-code-support for troubleshooting steps.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_lock_access_code_support_removed"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnknownIssueWithPhoneWarning(ResourceMapping):
        """Indicates that an unknown issue occurred while syncing the state of the phone with the provider. This issue may affect the proper functioning of the phone.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unknown_issue_with_phone"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class LocklyTimeZoneNotConfiguredWarning(ResourceMapping):
        """Indicates that Seam detected that the Lockly device does not have a time zone configured. Time-bound codes may not work as expected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["lockly_time_zone_not_configured"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UltraloqTimeZoneUnknownWarning(ResourceMapping):
        """Indicates that Seam does not know the time zone of the Ultraloq device. Set a time zone to enable time-bound access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ultraloq_time_zone_unknown"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TimeZoneUnknownWarning(ResourceMapping):
        """Indicates that Seam does not know the device's time zone. Set a time zone to enable time-bound access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["time_zone_unknown"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TimeZoneMismatchWarning(ResourceMapping):
        """Indicates that the device's configured time zone does not match its hardware UTC offset. Time-bound access codes may activate at the wrong local time.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["time_zone_mismatch"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TwoNDeviceMissingTimezoneWarning(ResourceMapping):
        """Indicates that the 2N device does not have a time zone configured. Configure a time zone on the device to enable access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["two_n_device_missing_timezone"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class HubRequiredForAdditionalCapabilitiesWarning(ResourceMapping):
        """Indicates that a hub or relay must be connected to unlock additional capabilities such as remote unlock.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["hub_required_for_additional_capabilities"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ProviderIssueWarning(ResourceMapping):
        """Indicates a provider-specific issue that may affect device functionality.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["provider_issue"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class KeynestUnsupportedLockerWarning(ResourceMapping):
        """Indicates that the key is in a locker that does not support the access codes API.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["keynest_unsupported_locker"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AccessoryKeypadSetupRequiredWarning(ResourceMapping):
        """Indicates that the accessory keypad exists, but is not linked to the Igloohome Bridge. Online access code programming will fail until the keypad is linked to the Igloohome Bridge in the Igloohome app.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["accessory_keypad_setup_required"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AccessoryKeypadLowBatteryWarning(ResourceMapping):
        """Indicates that the accessory keypad paired with this lock has a low or critically low battery. Replace its batteries so guests can keep entering their access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["accessory_keypad_low_battery"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnreliableOnlineStatusWarning(ResourceMapping):
        """Indicates that the device may optimistically be reported as online because the provider does not reliably report its online status.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unreliable_online_status"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class MaxAccessCodesReachedWarning(ResourceMapping):
        """Indicates that the device has reached its maximum number of active access codes. Delete existing codes before creating new ones.

        :ivar active_access_code_count: Number of active access codes on the device when the warning was set.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar max_active_access_code_count: Maximum number of active access codes supported by the device.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        active_access_code_count: int
        created_at: str
        max_active_access_code_count: int
        message: str
        warning_code: Literal["max_access_codes_reached"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                active_access_code_count=d.get("active_access_code_count", None),
                created_at=d.get("created_at", None),
                max_active_access_code_count=d.get(
                    "max_active_access_code_count", None
                ),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[
        AccountDisconnectedError,
        SaltoKsSubscriptionLimitExceededError,
        InsufficientPermissionsError,
        DormakabaSitesDisconnectedError,
        DeviceOfflineError,
        DeviceRemovedError,
        HubDisconnectedError,
        DeviceDisconnectedError,
        EmptyBackupAccessCodePoolError,
        AugustLockNotAuthorizedError,
        MissingDeviceCredentialsError,
        AuxiliaryHeatRunningError,
        SubscriptionRequiredError,
        BridgeDisconnectedError,
    ]
    _ErrorsVariants = {
        "account_disconnected": AccountDisconnectedError,
        "salto_ks_subscription_limit_exceeded": SaltoKsSubscriptionLimitExceededError,
        "insufficient_permissions": InsufficientPermissionsError,
        "dormakaba_sites_disconnected": DormakabaSitesDisconnectedError,
        "device_offline": DeviceOfflineError,
        "device_removed": DeviceRemovedError,
        "hub_disconnected": HubDisconnectedError,
        "device_disconnected": DeviceDisconnectedError,
        "empty_backup_access_code_pool": EmptyBackupAccessCodePoolError,
        "august_lock_not_authorized": AugustLockNotAuthorizedError,
        "missing_device_credentials": MissingDeviceCredentialsError,
        "auxiliary_heat_running": AuxiliaryHeatRunningError,
        "subscription_required": SubscriptionRequiredError,
        "bridge_disconnected": BridgeDisconnectedError,
    }

    Warnings = Union[
        PartialBackupAccessCodePoolWarning,
        ManyActiveBackupCodesWarning,
        ThirdPartyIntegrationDetectedWarning,
        TtlockLockGatewayUnlockingNotEnabledWarning,
        TtlockWeakGatewaySignalWarning,
        PowerSavingModeWarning,
        TemperatureThresholdExceededWarning,
        DeviceCommunicationDegradedWarning,
        ScheduledMaintenanceWindowWarning,
        DeviceHasFlakyConnectionWarning,
        SaltoKsOfficeModeWarning,
        SaltoKsPrivacyModeWarning,
        PrivacyModeWarning,
        SaltoKsSubscriptionLimitAlmostReachedWarning,
        SaltoKsLockAccessCodeSupportRemovedWarning,
        UnknownIssueWithPhoneWarning,
        LocklyTimeZoneNotConfiguredWarning,
        UltraloqTimeZoneUnknownWarning,
        TimeZoneUnknownWarning,
        TimeZoneMismatchWarning,
        TwoNDeviceMissingTimezoneWarning,
        HubRequiredForAdditionalCapabilitiesWarning,
        ProviderIssueWarning,
        KeynestUnsupportedLockerWarning,
        AccessoryKeypadSetupRequiredWarning,
        AccessoryKeypadLowBatteryWarning,
        UnreliableOnlineStatusWarning,
        MaxAccessCodesReachedWarning,
    ]
    _WarningsVariants = {
        "partial_backup_access_code_pool": PartialBackupAccessCodePoolWarning,
        "many_active_backup_codes": ManyActiveBackupCodesWarning,
        "third_party_integration_detected": ThirdPartyIntegrationDetectedWarning,
        "ttlock_lock_gateway_unlocking_not_enabled": TtlockLockGatewayUnlockingNotEnabledWarning,
        "ttlock_weak_gateway_signal": TtlockWeakGatewaySignalWarning,
        "power_saving_mode": PowerSavingModeWarning,
        "temperature_threshold_exceeded": TemperatureThresholdExceededWarning,
        "device_communication_degraded": DeviceCommunicationDegradedWarning,
        "scheduled_maintenance_window": ScheduledMaintenanceWindowWarning,
        "device_has_flaky_connection": DeviceHasFlakyConnectionWarning,
        "salto_ks_office_mode": SaltoKsOfficeModeWarning,
        "salto_ks_privacy_mode": SaltoKsPrivacyModeWarning,
        "privacy_mode": PrivacyModeWarning,
        "salto_ks_subscription_limit_almost_reached": SaltoKsSubscriptionLimitAlmostReachedWarning,
        "salto_ks_lock_access_code_support_removed": SaltoKsLockAccessCodeSupportRemovedWarning,
        "unknown_issue_with_phone": UnknownIssueWithPhoneWarning,
        "lockly_time_zone_not_configured": LocklyTimeZoneNotConfiguredWarning,
        "ultraloq_time_zone_unknown": UltraloqTimeZoneUnknownWarning,
        "time_zone_unknown": TimeZoneUnknownWarning,
        "time_zone_mismatch": TimeZoneMismatchWarning,
        "two_n_device_missing_timezone": TwoNDeviceMissingTimezoneWarning,
        "hub_required_for_additional_capabilities": HubRequiredForAdditionalCapabilitiesWarning,
        "provider_issue": ProviderIssueWarning,
        "keynest_unsupported_locker": KeynestUnsupportedLockerWarning,
        "accessory_keypad_setup_required": AccessoryKeypadSetupRequiredWarning,
        "accessory_keypad_low_battery": AccessoryKeypadLowBatteryWarning,
        "unreliable_online_status": UnreliableOnlineStatusWarning,
        "max_access_codes_reached": MaxAccessCodesReachedWarning,
    }

    can_configure_auto_lock: Optional[bool]
    can_hvac_cool: Optional[bool]
    can_hvac_heat: Optional[bool]
    can_hvac_heat_cool: Optional[bool]
    can_program_offline_access_codes: Optional[bool]
    can_program_online_access_codes: Optional[bool]
    can_program_thermostat_programs_as_different_each_day: Optional[bool]
    can_program_thermostat_programs_as_same_each_day: Optional[bool]
    can_program_thermostat_programs_as_weekday_weekend: Optional[bool]
    can_remotely_lock: Optional[bool]
    can_remotely_unlock: Optional[bool]
    can_run_thermostat_programs: Optional[bool]
    can_simulate_connection: Optional[bool]
    can_simulate_disconnection: Optional[bool]
    can_simulate_hub_connection: Optional[bool]
    can_simulate_hub_disconnection: Optional[bool]
    can_simulate_paid_subscription: Optional[bool]
    can_simulate_removal: Optional[bool]
    can_turn_off_hvac: Optional[bool]
    can_unlock_with_code: Optional[bool]
    capabilities_supported: List[
        Literal[
            "access_code", "lock", "noise_detection", "thermostat", "battery", "phone"
        ]
    ]
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Union[str, bool]]
    device_id: str
    device_type: Literal[
        "akuvox_lock",
        "august_lock",
        "brivo_access_point",
        "butterflymx_panel",
        "avigilon_alta_entry",
        "doorking_lock",
        "genie_door",
        "igloo_lock",
        "linear_lock",
        "lockly_lock",
        "kwikset_lock",
        "nuki_lock",
        "salto_lock",
        "schlage_lock",
        "smartthings_lock",
        "wyze_lock",
        "yale_lock",
        "two_n_intercom",
        "controlbyweb_device",
        "ttlock_lock",
        "igloohome_lock",
        "four_suites_door",
        "dormakaba_oracode_door",
        "tedee_lock",
        "akiles_lock",
        "ultraloq_lock",
        "yacan_lock",
        "keyincode_lock",
        "omnitec_lock",
        "kisi_lock",
        "aqara_lock",
        "keynest_key",
        "noiseaware_activity_zone",
        "minut_sensor",
        "ecobee_thermostat",
        "nest_thermostat",
        "honeywell_resideo_thermostat",
        "tado_thermostat",
        "sensi_thermostat",
        "smartthings_thermostat",
        "ios_phone",
        "android_phone",
        "ring_camera",
    ]
    display_name: str
    errors: List[Errors]
    is_managed: Literal[False]
    location: Optional[Location]
    properties: Optional[Properties]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
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
            custom_metadata=_record_from_dict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            is_managed=d.get("is_managed", None),
            location=_object_from_dict(cls.Location, d.get("location")),
            properties=_object_from_dict(cls.Properties, d.get("properties")),
            warnings=_discriminated_list_from_dict(
                d.get("warnings"), cls._WarningsVariants, "warning_code"
            ),
            workspace_id=d.get("workspace_id", None),
        )
