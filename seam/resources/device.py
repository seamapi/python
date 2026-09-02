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
class Device:
    """Represents a `device <https://docs.seam.co/core-concepts/devices>`_ that has been connected to Seam.

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

    :ivar device_manufacturer: Manufacturer of the device. Represents the hardware brand, which may differ from the provider.

    :ivar device_provider: Provider of the device. Represents the third-party service through which the device is controlled.

    :ivar device_type: Type of the device.

    :ivar display_name: Display name of the device, defaults to nickname (if it is set) or ``properties.appearance.name``, otherwise. Enables administrators and users to identify the device easily, especially when there are numerous devices.

    :ivar errors: Array of errors associated with the device. Each error object within the array contains two fields: ``error_code`` and ``message``. ``error_code`` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar is_managed: Indicates whether Seam manages the device. See also `Managed and Unmanaged Devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

    :ivar location: Location information for the device.

    :ivar nickname: Optional nickname to describe the device, settable through Seam.

    :ivar properties: Properties of the device.

    :ivar space_ids: IDs of the spaces the device is in.

    :ivar warnings: Array of warnings associated with the device. Each warning object within the array contains two fields: ``warning_code`` and ``message``. ``warning_code`` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the device.
    """

    @dataclass
    class DeviceManufacturer(ResourceMapping):
        """Manufacturer of the device. Represents the hardware brand, which may differ from the provider.

        :ivar display_name: Display name for the manufacturer, such as ``August``, ``Yale``, ``Salto``, and so on.

        :ivar image_url: Image URL for the manufacturer logo.

        :ivar manufacturer: Manufacturer identifier, such as ``august``, ``yale``, ``salto``, and so on.
        """

        display_name: str
        image_url: Optional[str]
        manufacturer: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                display_name=d.get("display_name", None),
                image_url=d.get("image_url", None),
                manufacturer=d.get("manufacturer", None),
            )

    @dataclass
    class DeviceProvider(ResourceMapping):
        """Provider of the device. Represents the third-party service through which the device is controlled.

        :ivar device_provider_name: Device provider name. Corresponds to the integration type, such as ``august``, ``schlage``, ``yale_access``, and so on.

        :ivar display_name: Display name for the device provider type.

        :ivar image_url: Image URL for the device provider.

        :ivar provider_category: Provider category. Indicates the third-party provider type, such as ``stable``, for stable integrations, or ``internal``, for internal integrations.
        """

        device_provider_name: str
        display_name: str
        image_url: Optional[str]
        provider_category: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                device_provider_name=d.get("device_provider_name", None),
                display_name=d.get("display_name", None),
                image_url=d.get("image_url", None),
                provider_category=d.get("provider_category", None),
            )

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
        """Properties of the device.

        :ivar accessory_keypad: Accessory keypad properties and state.

        :ivar appearance: Appearance-related properties, as reported by the device.

        :ivar battery: Represents the current status of the battery charge level.

        :ivar battery_level: Indicates the battery level of the device as a decimal value between 0 and 1, inclusive.

        :ivar currently_triggering_noise_threshold_ids: Array of noise threshold IDs that are currently triggering.

        :ivar has_direct_power: Indicates whether the device has direct power.

        :ivar image_alt_text: Alt text for the device image.

        :ivar image_url: Image URL for the device.

        :ivar manufacturer: Manufacturer of the device. When a device, such as a smart lock, is connected through a smart hub, the manufacturer of the device might be different from that of the smart hub.

        :ivar model: Device model-related properties.

        :ivar name: Deprecated: use device.display_name instead Name of the device.

        :ivar noise_level_decibels: Indicates current noise level in decibels, if the device supports noise detection.

        :ivar offline_access_codes_enabled: Deprecated: use device.can_program_offline_access_codes Indicates whether it is currently possible to use offline access codes for the device.

        :ivar online: Indicates whether the device is online.

        :ivar online_access_codes_enabled: Deprecated: use device.can_program_online_access_codes Indicates whether it is currently possible to use online access codes for the device.

        :ivar serial_number: Serial number of the device.

        :ivar supports_accessory_keypad: Deprecated: use device.properties.model.can_connect_accessory_keypad

        :ivar supports_offline_access_codes: Deprecated: use offline_access_codes_enabled

        :ivar assa_abloy_credential_service_metadata: ASSA ABLOY Credential Service metadata for the phone.

        :ivar salto_space_credential_service_metadata: Salto Space credential service metadata for the phone.

        :ivar akiles_metadata: Metadata for an Akiles device.

        :ivar aqara_metadata: Metadata for an Aqara device.

        :ivar assa_abloy_vostio_metadata: Metadata for an ASSA ABLOY Vostio system.

        :ivar august_metadata: Metadata for an August device.

        :ivar avigilon_alta_metadata: Metadata for an Avigilon Alta system.

        :ivar brivo_metadata: Metadata for a Brivo device.

        :ivar controlbyweb_metadata: Metadata for a ControlByWeb device.

        :ivar dormakaba_oracode_metadata: Metadata for a dormakaba Oracode device.

        :ivar ecobee_metadata: Metadata for an ecobee device.

        :ivar four_suites_metadata: Metadata for a 4SUITES device.

        :ivar genie_metadata: Metadata for a Genie device.

        :ivar honeywell_resideo_metadata: Metadata for a Honeywell Resideo device.

        :ivar igloo_metadata: Metadata for an igloo device.

        :ivar igloohome_metadata: Metadata for an igloohome device.

        :ivar keynest_metadata: Metadata for a KeyNest device.

        :ivar kisi_metadata: Metadata for a Kisi device.

        :ivar korelock_metadata: Metadata for a Korelock device.

        :ivar kwikset_metadata: Metadata for a Kwikset device.

        :ivar lockly_metadata: Metadata for a Lockly device.

        :ivar minut_metadata: Metadata for a Minut device.

        :ivar nest_metadata: Metadata for a Google Nest device.

        :ivar noiseaware_metadata: Metadata for a NoiseAware device.

        :ivar nuki_metadata: Metadata for a Nuki device.

        :ivar omnitec_metadata: Metadata for an Omnitec device.

        :ivar ring_metadata: Metadata for a Ring device.

        :ivar salto_ks_metadata: Metadata for a Salto KS device.

        :ivar salto_metadata: Deprecated: Use ``salto_ks_metadata`` instead. Metada for a Salto device.

        :ivar schlage_metadata: Metadata for a Schlage device.

        :ivar seam_bridge_metadata: Metadata for Seam Bridge.

        :ivar sensi_metadata: Metadata for a Sensi device.

        :ivar smartthings_metadata: Metadata for a SmartThings device.

        :ivar tado_metadata: Metadata for a tado° device.

        :ivar tedee_metadata: Metadata for a Tedee device.

        :ivar ttlock_metadata: Metadata for a TTLock device.

        :ivar two_n_metadata: Metadata for a 2N device.

        :ivar ultraloq_metadata: Metadata for an Ultraloq device.

        :ivar visionline_metadata: Metadata for an ASSA ABLOY Visionline system.

        :ivar wyze_metadata: Metadata for a Wyze device.

        :ivar yacan_metadata: Metadata for a Yacan device.

        :ivar auto_lock_delay_seconds: The delay in seconds before the lock automatically locks after being unlocked.

        :ivar auto_lock_enabled: Indicates whether automatic locking is enabled.

        :ivar backup_access_code_pool_enabled: Indicates whether the `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is currently enabled for the device. To disable it, set this to ``false`` using `/devices/update <https://docs.seam.co/api/devices/update>`_.

        :ivar code_constraints: Constraints on access codes for the device. Seam represents each constraint as an object with a ``constraint_type`` property. Depending on the constraint type, there may also be additional properties. Note that some constraints are manufacturer- or device-specific.

        :ivar door_open: Indicates whether the door is open.

        :ivar has_native_entry_events: Indicates whether the device supports native entry events.

        :ivar keypad_battery: Keypad battery status.

        :ivar locked: Indicates whether the lock is locked.

        :ivar max_active_codes_supported: Maximum number of active access codes that the device supports.

        :ivar offline_time_frame_options: Time frames that may be requested when creating an offline access code, expressed as a list of options. The caller picks one option (by matching the requested duration when the options' duration ranges do not overlap, or by ``display_name`` when they do) and satisfies that one option's rules. When ``undefined``, any time frame works.

        :ivar online_time_frame_options: Time frames that may be requested when creating an online access code, expressed as a list of options. The caller picks one option (by matching the requested duration when the options' duration ranges do not overlap, or by ``display_name`` when they do) and satisfies that one option's rules. When ``undefined``, any time frame works.

        :ivar supported_code_lengths: Supported code lengths for access codes.

        :ivar supports_backup_access_code_pool: Indicates whether the device supports a `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_.

        :ivar active_thermostat_schedule: Deprecated: Use ``active_thermostat_schedule_id`` with ``/thermostats/schedules/get`` instead. Active `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :ivar active_thermostat_schedule_id: ID of the active `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :ivar available_climate_preset_modes: Climate preset modes that the thermostat supports, such as "home", "away", "wake", "sleep", "occupied", and "unoccupied".

        :ivar available_climate_presets: Available `climate presets <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for the thermostat.

        :ivar available_fan_mode_settings: Fan mode settings that the thermostat supports.

        :ivar available_hvac_mode_settings: HVAC mode settings that the thermostat supports.

        :ivar current_climate_setting: Current climate setting.

        :ivar default_climate_setting: Deprecated: use fallback_climate_preset_key to specify a fallback climate preset instead.

        :ivar fallback_climate_preset_key: Key of the `fallback climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets/setting-the-fallback-climate-preset>`_ for the thermostat.

        :ivar fan_mode_setting: Deprecated: Use ``current_climate_setting.fan_mode_setting`` instead.

        :ivar is_cooling: Indicates whether the connected HVAC system is currently cooling, as reported by the thermostat.

        :ivar is_fan_running: Indicates whether the fan in the connected HVAC system is currently running, as reported by the thermostat.

        :ivar is_heating: Indicates whether the connected HVAC system is currently heating, as reported by the thermostat.

        :ivar is_temporary_manual_override_active: Indicates whether the current thermostat settings differ from the most recent active program or schedule that Seam activated. For this condition to occur, ``current_climate_setting.manual_override_allowed`` must also be ``true``.

        :ivar max_cooling_set_point_celsius: Maximum `cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#cooling-set-point>`_ in °C.

        :ivar max_cooling_set_point_fahrenheit: Maximum `cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#cooling-set-point>`_ in °F.

        :ivar max_heating_set_point_celsius: Maximum `heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#heating-set-point>`_ in °C.

        :ivar max_heating_set_point_fahrenheit: Maximum `heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#heating-set-point>`_ in °F.

        :ivar max_thermostat_daily_program_periods_per_day: Maximum number of periods that the thermostat can support per day. For example, if the thermostat supports 4 periods per day, this value is 4.

        :ivar max_unique_climate_presets_per_thermostat_weekly_program: Maximum number of climate presets that the thermostat can support for weekly programming.

        :ivar min_cooling_set_point_celsius: Minimum `cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#cooling-set-point>`_ in °C.

        :ivar min_cooling_set_point_fahrenheit: Minimum `cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#cooling-set-point>`_ in °F.

        :ivar min_heating_cooling_delta_celsius: Minimum `temperature difference <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#minimum-heating-cooling-temperature-delta>`_ in °C between the cooling and heating set points when in heat-cool (auto) mode.

        :ivar min_heating_cooling_delta_fahrenheit: Minimum `temperature difference <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#minimum-heating-cooling-temperature-delta>`_ in °F between the cooling and heating set points when in heat-cool (auto) mode.

        :ivar min_heating_set_point_celsius: Minimum `heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#heating-set-point>`_ in °C.

        :ivar min_heating_set_point_fahrenheit: Minimum `heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points#heating-set-point>`_ in °F.

        :ivar relative_humidity: Reported relative humidity, as a value between 0 and 1, inclusive.

        :ivar temperature_celsius: Reported temperature in °C.

        :ivar temperature_fahrenheit: Reported temperature in °F.

        :ivar temperature_threshold: Current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.

        :ivar thermostat_daily_program_period_precision_minutes: Precision of the thermostat's period in minutes. For example, if the thermostat supports 15-minute periods, this value is 15. All values are relative to the top of the hour, so for 15 minutes, the periods would be 0, 15, 30, and 45 minutes past the hour.

        :ivar thermostat_daily_programs: Configured `daily programs <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-programs>`_ for the thermostat.

        :ivar thermostat_weekly_program: Current `weekly program <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-programs>`_ for the thermostat.
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
        class Appearance(ResourceMapping):
            """Appearance-related properties, as reported by the device.

            :ivar name: Name of the device as seen from the provider API and application, not settable through Seam.
            """

            name: str

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    name=d.get("name", None),
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

        @dataclass
        class AssaAbloyCredentialServiceMetadata(ResourceMapping):
            """ASSA ABLOY Credential Service metadata for the phone.

            :ivar endpoints: Endpoints associated with the phone.

            :ivar has_active_endpoint: Indicates whether the credential service has active endpoints associated with the phone.
            """

            @dataclass
            class Endpoints(ResourceMapping):
                """Endpoints associated with the phone.

                :ivar endpoint_id: ID of the associated endpoint.

                :ivar is_active: Indicated whether the endpoint is active."""

                endpoint_id: Optional[str]
                is_active: Optional[bool]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        endpoint_id=d.get("endpoint_id", None),
                        is_active=d.get("is_active", None),
                    )

            endpoints: Optional[List[Endpoints]]
            has_active_endpoint: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    endpoints=_object_list_from_dict(cls.Endpoints, d.get("endpoints")),
                    has_active_endpoint=d.get("has_active_endpoint", None),
                )

        @dataclass
        class SaltoSpaceCredentialServiceMetadata(ResourceMapping):
            """Salto Space credential service metadata for the phone.

            :ivar has_active_phone: Indicates whether the credential service has an active associated phone.
            """

            has_active_phone: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    has_active_phone=d.get("has_active_phone", None),
                )

        @dataclass
        class AkilesMetadata(ResourceMapping):
            """Metadata for an Akiles device.

            :ivar _member_group_id: Group ID to which to add users for an Akiles device.

            :ivar gadget_id: Gadget ID for an Akiles device.

            :ivar gadget_name: Gadget name for an Akiles device.

            :ivar product_name: Product name for an Akiles device."""

            _member_group_id: Optional[str]
            gadget_id: Optional[str]
            gadget_name: Optional[str]
            product_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    _member_group_id=d.get("_member_group_id", None),
                    gadget_id=d.get("gadget_id", None),
                    gadget_name=d.get("gadget_name", None),
                    product_name=d.get("product_name", None),
                )

        @dataclass
        class AqaraMetadata(ResourceMapping):
            """Metadata for an Aqara device.

            :ivar device_name: Device name for an Aqara device.

            :ivar did: Device ID (did) for an Aqara device.

            :ivar firmware_version: Firmware version for an Aqara device.

            :ivar model: Model identifier for an Aqara device.

            :ivar model_type: Model type for an Aqara device.

            :ivar parent_did: Parent gateway device ID for an Aqara device.

            :ivar position_id: Position (room) ID for an Aqara device.

            :ivar time_zone: Time zone reported for an Aqara device (e.g. GMT-07:00)."""

            device_name: Optional[str]
            did: Optional[str]
            firmware_version: Optional[str]
            model: Optional[str]
            model_type: Optional[float]
            parent_did: Optional[str]
            position_id: Optional[str]
            time_zone: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_name=d.get("device_name", None),
                    did=d.get("did", None),
                    firmware_version=d.get("firmware_version", None),
                    model=d.get("model", None),
                    model_type=d.get("model_type", None),
                    parent_did=d.get("parent_did", None),
                    position_id=d.get("position_id", None),
                    time_zone=d.get("time_zone", None),
                )

        @dataclass
        class AssaAbloyVostioMetadata(ResourceMapping):
            """Metadata for an ASSA ABLOY Vostio system.

            :ivar encoder_name: Encoder name for an ASSA ABLOY Vostio system."""

            encoder_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    encoder_name=d.get("encoder_name", None),
                )

        @dataclass
        class AugustMetadata(ResourceMapping):
            """Metadata for an August device.

            :ivar has_keypad: Indicates whether an August device has a keypad.

            :ivar house_id: House ID for an August device.

            :ivar house_name: House name for an August device.

            :ivar keypad_battery_level: Keypad battery level for an August device.

            :ivar lock_id: Lock ID for an August device.

            :ivar lock_name: Lock name for an August device.

            :ivar model: Model for an August device."""

            has_keypad: Optional[bool]
            house_id: Optional[str]
            house_name: Optional[str]
            keypad_battery_level: Optional[str]
            lock_id: Optional[str]
            lock_name: Optional[str]
            model: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    has_keypad=d.get("has_keypad", None),
                    house_id=d.get("house_id", None),
                    house_name=d.get("house_name", None),
                    keypad_battery_level=d.get("keypad_battery_level", None),
                    lock_id=d.get("lock_id", None),
                    lock_name=d.get("lock_name", None),
                    model=d.get("model", None),
                )

        @dataclass
        class AvigilonAltaMetadata(ResourceMapping):
            """Metadata for an Avigilon Alta system.

            :ivar entry_name: Entry name for an Avigilon Alta system.

            :ivar entry_relays_total_count: Total count of entry relays for an Avigilon Alta system.

            :ivar org_name: Organization name for an Avigilon Alta system.

            :ivar site_id: Site ID for an Avigilon Alta system.

            :ivar site_name: Site name for an Avigilon Alta system.

            :ivar zone_id: Zone ID for an Avigilon Alta system.

            :ivar zone_name: Zone name for an Avigilon Alta system."""

            entry_name: Optional[str]
            entry_relays_total_count: Optional[float]
            org_name: Optional[str]
            site_id: Optional[float]
            site_name: Optional[str]
            zone_id: Optional[float]
            zone_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    entry_name=d.get("entry_name", None),
                    entry_relays_total_count=d.get("entry_relays_total_count", None),
                    org_name=d.get("org_name", None),
                    site_id=d.get("site_id", None),
                    site_name=d.get("site_name", None),
                    zone_id=d.get("zone_id", None),
                    zone_name=d.get("zone_name", None),
                )

        @dataclass
        class BrivoMetadata(ResourceMapping):
            """Metadata for a Brivo device.

            :ivar activation_enabled: Indicates whether the Brivo access point has activation (remote unlock) enabled.

            :ivar device_name: Device name for a Brivo device."""

            activation_enabled: Optional[bool]
            device_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    activation_enabled=d.get("activation_enabled", None),
                    device_name=d.get("device_name", None),
                )

        @dataclass
        class ControlbywebMetadata(ResourceMapping):
            """Metadata for a ControlByWeb device.

            :ivar device_id: Device ID for a ControlByWeb device.

            :ivar device_name: Device name for a ControlByWeb device.

            :ivar relay_name: Relay name for a ControlByWeb device."""

            device_id: Optional[str]
            device_name: Optional[str]
            relay_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    relay_name=d.get("relay_name", None),
                )

        @dataclass
        class DormakabaOracodeMetadata(ResourceMapping):
            """Metadata for a dormakaba Oracode device.

            :ivar device_id: Device ID for a dormakaba Oracode device.

            :ivar door_id: Door ID for a dormakaba Oracode device.

            :ivar door_is_wireless: Indicates whether a door is wireless for a dormakaba Oracode device.

            :ivar door_name: Door name for a dormakaba Oracode device.

            :ivar iana_timezone: IANA time zone for a dormakaba Oracode device.

            :ivar predefined_time_slots: Predefined time slots for a dormakaba Oracode device.

            :ivar site_id: Deprecated: Previously marked as "@DEPRECATED." Site ID for a dormakaba Oracode device.

            :ivar site_name: Site name for a dormakaba Oracode device."""

            @dataclass
            class PredefinedTimeSlots(ResourceMapping):
                """Predefined time slots for a dormakaba Oracode device.

                :ivar check_in_time: Check in time for a time slot for a dormakaba Oracode device.

                :ivar check_out_time: Checkout time for a time slot for a dormakaba Oracode device.

                :ivar dormakaba_oracode_user_level_id: ID of a user level for a dormakaba Oracode device.

                :ivar dormakaba_oracode_user_level_prefix: Prefix for a user level for a dormakaba Oracode device.

                :ivar is_24_hour: Indicates whether a time slot for a dormakaba Oracode device is a 24-hour time slot.

                :ivar is_biweekly_mode: Indicates whether a time slot for a dormakaba Oracode device is in biweekly mode.

                :ivar is_master: Indicates whether a time slot for a dormakaba Oracode device is a master time slot.

                :ivar is_one_shot: Indicates whether a time slot for a dormakaba Oracode device is a one-shot time slot.

                :ivar name: Name of a time slot for a dormakaba Oracode device.

                :ivar prefix: Prefix for a time slot for a dormakaba Oracode device."""

                check_in_time: Optional[str]
                check_out_time: Optional[str]
                dormakaba_oracode_user_level_id: Optional[str]
                dormakaba_oracode_user_level_prefix: Optional[float]
                is_24_hour: Optional[bool]
                is_biweekly_mode: Optional[bool]
                is_master: Optional[bool]
                is_one_shot: Optional[bool]
                name: Optional[str]
                prefix: Optional[float]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        check_in_time=d.get("check_in_time", None),
                        check_out_time=d.get("check_out_time", None),
                        dormakaba_oracode_user_level_id=d.get(
                            "dormakaba_oracode_user_level_id", None
                        ),
                        dormakaba_oracode_user_level_prefix=d.get(
                            "dormakaba_oracode_user_level_prefix", None
                        ),
                        is_24_hour=d.get("is_24_hour", None),
                        is_biweekly_mode=d.get("is_biweekly_mode", None),
                        is_master=d.get("is_master", None),
                        is_one_shot=d.get("is_one_shot", None),
                        name=d.get("name", None),
                        prefix=d.get("prefix", None),
                    )

            device_id: Optional[str]
            door_id: Optional[float]
            door_is_wireless: Optional[bool]
            door_name: Optional[str]
            iana_timezone: Optional[str]
            predefined_time_slots: Optional[List[PredefinedTimeSlots]]
            site_id: Optional[float]
            site_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    door_id=d.get("door_id", None),
                    door_is_wireless=d.get("door_is_wireless", None),
                    door_name=d.get("door_name", None),
                    iana_timezone=d.get("iana_timezone", None),
                    predefined_time_slots=_object_list_from_dict(
                        cls.PredefinedTimeSlots, d.get("predefined_time_slots")
                    ),
                    site_id=d.get("site_id", None),
                    site_name=d.get("site_name", None),
                )

        @dataclass
        class EcobeeMetadata(ResourceMapping):
            """Metadata for an ecobee device.

            :ivar device_name: Device name for an ecobee device.

            :ivar ecobee_device_id: Device ID for an ecobee device."""

            device_name: Optional[str]
            ecobee_device_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_name=d.get("device_name", None),
                    ecobee_device_id=d.get("ecobee_device_id", None),
                )

        @dataclass
        class FourSuitesMetadata(ResourceMapping):
            """Metadata for a 4SUITES device.

            :ivar device_id: Device ID for a 4SUITES device.

            :ivar device_name: Device name for a 4SUITES device.

            :ivar reclose_delay_in_seconds: Reclose delay, in seconds, for a 4SUITES device.
            """

            device_id: Optional[float]
            device_name: Optional[str]
            reclose_delay_in_seconds: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    reclose_delay_in_seconds=d.get("reclose_delay_in_seconds", None),
                )

        @dataclass
        class GenieMetadata(ResourceMapping):
            """Metadata for a Genie device.

            :ivar device_name: Lock name for a Genie device.

            :ivar door_name: Door name for a Genie device."""

            device_name: Optional[str]
            door_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_name=d.get("device_name", None),
                    door_name=d.get("door_name", None),
                )

        @dataclass
        class HoneywellResideoMetadata(ResourceMapping):
            """Metadata for a Honeywell Resideo device.

            :ivar device_name: Device name for a Honeywell Resideo device.

            :ivar honeywell_resideo_device_id: Device ID for a Honeywell Resideo device.
            """

            device_name: Optional[str]
            honeywell_resideo_device_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_name=d.get("device_name", None),
                    honeywell_resideo_device_id=d.get(
                        "honeywell_resideo_device_id", None
                    ),
                )

        @dataclass
        class IglooMetadata(ResourceMapping):
            """Metadata for an igloo device.

            :ivar bridge_id: Bridge ID for an igloo device.

            :ivar device_id: Device ID for an igloo device.

            :ivar model: Model for an igloo device."""

            bridge_id: Optional[str]
            device_id: Optional[str]
            model: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    bridge_id=d.get("bridge_id", None),
                    device_id=d.get("device_id", None),
                    model=d.get("model", None),
                )

        @dataclass
        class IgloohomeMetadata(ResourceMapping):
            """Metadata for an igloohome device.

            :ivar bridge_id: Bridge ID for an igloohome device.

            :ivar bridge_name: Bridge name for an igloohome device.

            :ivar device_id: Device ID for an igloohome device.

            :ivar device_name: Device name for an igloohome device.

            :ivar is_accessory_keypad_linked_to_bridge: Indicates whether a keypad is linked to a bridge for an igloohome device.

            :ivar keypad_id: Keypad ID for an igloohome device."""

            bridge_id: Optional[str]
            bridge_name: Optional[str]
            device_id: Optional[str]
            device_name: Optional[str]
            is_accessory_keypad_linked_to_bridge: Optional[bool]
            keypad_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    bridge_id=d.get("bridge_id", None),
                    bridge_name=d.get("bridge_name", None),
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    is_accessory_keypad_linked_to_bridge=d.get(
                        "is_accessory_keypad_linked_to_bridge", None
                    ),
                    keypad_id=d.get("keypad_id", None),
                )

        @dataclass
        class KeynestMetadata(ResourceMapping):
            """Metadata for a KeyNest device.

            :ivar address: Address for a KeyNest device.

            :ivar current_or_last_store_id: Current or last store ID for a KeyNest device.

            :ivar current_status: Current status for a KeyNest device.

            :ivar current_user_company: Current user company for a KeyNest device.

            :ivar current_user_email: Current user email for a KeyNest device.

            :ivar current_user_name: Current user name for a KeyNest device.

            :ivar current_user_phone_number: Current user phone number for a KeyNest device.

            :ivar default_office_id: Default office ID for a KeyNest device.

            :ivar device_name: Device name for a KeyNest device.

            :ivar fob_id: Fob ID for a KeyNest device.

            :ivar handover_method: Handover method for a KeyNest device.

            :ivar has_photo: Whether the KeyNest device has a photo.

            :ivar is_quadient_locker: Whether the key is in a locker that does not support the access codes API.

            :ivar key_id: Key ID for a KeyNest device.

            :ivar key_notes: Key notes for a KeyNest device.

            :ivar keynest_app_user: KeyNest app user for a KeyNest device.

            :ivar last_movement: Last movement timestamp for a KeyNest device.

            :ivar property_id: Property ID for a KeyNest device.

            :ivar property_postcode: Property postcode for a KeyNest device.

            :ivar status_type: Status type for a KeyNest device.

            :ivar subscription_plan: Subscription plan for a KeyNest device."""

            address: Optional[str]
            current_or_last_store_id: Optional[float]
            current_status: Optional[str]
            current_user_company: Optional[str]
            current_user_email: Optional[str]
            current_user_name: Optional[str]
            current_user_phone_number: Optional[str]
            default_office_id: Optional[float]
            device_name: Optional[str]
            fob_id: Optional[float]
            handover_method: Optional[str]
            has_photo: Optional[bool]
            is_quadient_locker: Optional[bool]
            key_id: Optional[str]
            key_notes: Optional[str]
            keynest_app_user: Optional[str]
            last_movement: Optional[str]
            property_id: Optional[str]
            property_postcode: Optional[str]
            status_type: Optional[str]
            subscription_plan: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    address=d.get("address", None),
                    current_or_last_store_id=d.get("current_or_last_store_id", None),
                    current_status=d.get("current_status", None),
                    current_user_company=d.get("current_user_company", None),
                    current_user_email=d.get("current_user_email", None),
                    current_user_name=d.get("current_user_name", None),
                    current_user_phone_number=d.get("current_user_phone_number", None),
                    default_office_id=d.get("default_office_id", None),
                    device_name=d.get("device_name", None),
                    fob_id=d.get("fob_id", None),
                    handover_method=d.get("handover_method", None),
                    has_photo=d.get("has_photo", None),
                    is_quadient_locker=d.get("is_quadient_locker", None),
                    key_id=d.get("key_id", None),
                    key_notes=d.get("key_notes", None),
                    keynest_app_user=d.get("keynest_app_user", None),
                    last_movement=d.get("last_movement", None),
                    property_id=d.get("property_id", None),
                    property_postcode=d.get("property_postcode", None),
                    status_type=d.get("status_type", None),
                    subscription_plan=d.get("subscription_plan", None),
                )

        @dataclass
        class KisiMetadata(ResourceMapping):
            """Metadata for a Kisi device.

            :ivar description: Description for a Kisi device.

            :ivar lock_id: Lock ID for a Kisi device.

            :ivar lock_name: Lock name for a Kisi device.

            :ivar place_name: Place name for a Kisi device."""

            description: Optional[str]
            lock_id: Optional[float]
            lock_name: Optional[str]
            place_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    description=d.get("description", None),
                    lock_id=d.get("lock_id", None),
                    lock_name=d.get("lock_name", None),
                    place_name=d.get("place_name", None),
                )

        @dataclass
        class KorelockMetadata(ResourceMapping):
            """Metadata for a Korelock device.

            :ivar device_id: Device ID for a Korelock device.

            :ivar device_name: Device name for a Korelock device.

            :ivar firmware_version: Firmware version for a Korelock device.

            :ivar location_id: Location ID for a Korelock device. Required for timebound access codes.

            :ivar model_code: Model code for a Korelock device.

            :ivar serial_number: Serial number for a Korelock device.

            :ivar wifi_signal_strength: WiFi signal strength (0-1) for a Korelock device.
            """

            device_id: Optional[str]
            device_name: Optional[str]
            firmware_version: Optional[str]
            location_id: Optional[str]
            model_code: Optional[str]
            serial_number: Optional[str]
            wifi_signal_strength: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    firmware_version=d.get("firmware_version", None),
                    location_id=d.get("location_id", None),
                    model_code=d.get("model_code", None),
                    serial_number=d.get("serial_number", None),
                    wifi_signal_strength=d.get("wifi_signal_strength", None),
                )

        @dataclass
        class KwiksetMetadata(ResourceMapping):
            """Metadata for a Kwikset device.

            :ivar device_id: Device ID for a Kwikset device.

            :ivar device_name: Device name for a Kwikset device.

            :ivar model_number: Model number for a Kwikset device."""

            device_id: Optional[str]
            device_name: Optional[str]
            model_number: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    model_number=d.get("model_number", None),
                )

        @dataclass
        class LocklyMetadata(ResourceMapping):
            """Metadata for a Lockly device.

            :ivar device_id: Device ID for a Lockly device.

            :ivar device_name: Device name for a Lockly device.

            :ivar model: Model for a Lockly device."""

            device_id: Optional[str]
            device_name: Optional[str]
            model: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    model=d.get("model", None),
                )

        @dataclass
        class MinutMetadata(ResourceMapping):
            """Metadata for a Minut device.

            :ivar device_id: Device ID for a Minut device.

            :ivar device_name: Device name for a Minut device.

            :ivar latest_sensor_values: Latest sensor values for a Minut device."""

            @dataclass
            class LatestSensorValues(ResourceMapping):
                """Latest sensor values for a Minut device.

                :ivar accelerometer_z: Latest accelerometer Z-axis reading for a Minut device.

                :ivar humidity: Latest humidity reading for a Minut device.

                :ivar pressure: Latest pressure reading for a Minut device.

                :ivar sound: Latest sound reading for a Minut device.

                :ivar temperature: Latest temperature reading for a Minut device."""

                @dataclass
                class AccelerometerZ(ResourceMapping):
                    """Latest accelerometer Z-axis reading for a Minut device.

                    :ivar time: Time of latest accelerometer Z-axis reading for a Minut device.

                    :ivar value: Value of latest accelerometer Z-axis reading for a Minut device.
                    """

                    time: Optional[str]
                    value: Optional[float]

                    @classmethod
                    def from_dict(cls, d: Any):
                        if not isinstance(d, dict):
                            d = {}
                        return cls(
                            time=d.get("time", None),
                            value=d.get("value", None),
                        )

                @dataclass
                class Humidity(ResourceMapping):
                    """Latest humidity reading for a Minut device.

                    :ivar time: Time of latest humidity reading for a Minut device.

                    :ivar value: Value of latest humidity reading for a Minut device."""

                    time: Optional[str]
                    value: Optional[float]

                    @classmethod
                    def from_dict(cls, d: Any):
                        if not isinstance(d, dict):
                            d = {}
                        return cls(
                            time=d.get("time", None),
                            value=d.get("value", None),
                        )

                @dataclass
                class Pressure(ResourceMapping):
                    """Latest pressure reading for a Minut device.

                    :ivar time: Time of latest pressure reading for a Minut device.

                    :ivar value: Value of latest pressure reading for a Minut device."""

                    time: Optional[str]
                    value: Optional[float]

                    @classmethod
                    def from_dict(cls, d: Any):
                        if not isinstance(d, dict):
                            d = {}
                        return cls(
                            time=d.get("time", None),
                            value=d.get("value", None),
                        )

                @dataclass
                class Sound(ResourceMapping):
                    """Latest sound reading for a Minut device.

                    :ivar time: Time of latest sound reading for a Minut device.

                    :ivar value: Value of latest sound reading for a Minut device."""

                    time: Optional[str]
                    value: Optional[float]

                    @classmethod
                    def from_dict(cls, d: Any):
                        if not isinstance(d, dict):
                            d = {}
                        return cls(
                            time=d.get("time", None),
                            value=d.get("value", None),
                        )

                @dataclass
                class Temperature(ResourceMapping):
                    """Latest temperature reading for a Minut device.

                    :ivar time: Time of latest temperature reading for a Minut device.

                    :ivar value: Value of latest temperature reading for a Minut device.
                    """

                    time: Optional[str]
                    value: Optional[float]

                    @classmethod
                    def from_dict(cls, d: Any):
                        if not isinstance(d, dict):
                            d = {}
                        return cls(
                            time=d.get("time", None),
                            value=d.get("value", None),
                        )

                accelerometer_z: Optional[AccelerometerZ]
                humidity: Optional[Humidity]
                pressure: Optional[Pressure]
                sound: Optional[Sound]
                temperature: Optional[Temperature]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        accelerometer_z=_object_from_dict(
                            cls.AccelerometerZ, d.get("accelerometer_z")
                        ),
                        humidity=_object_from_dict(cls.Humidity, d.get("humidity")),
                        pressure=_object_from_dict(cls.Pressure, d.get("pressure")),
                        sound=_object_from_dict(cls.Sound, d.get("sound")),
                        temperature=_object_from_dict(
                            cls.Temperature, d.get("temperature")
                        ),
                    )

            device_id: Optional[str]
            device_name: Optional[str]
            latest_sensor_values: Optional[LatestSensorValues]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    latest_sensor_values=_object_from_dict(
                        cls.LatestSensorValues, d.get("latest_sensor_values")
                    ),
                )

        @dataclass
        class NestMetadata(ResourceMapping):
            """Metadata for a Google Nest device.

            :ivar device_custom_name: Custom device name for a Google Nest device. The device owner sets this value.

            :ivar device_name: Device name for a Google Nest device. Google sets this value.

            :ivar display_name: Display name for a Google Nest device.

            :ivar nest_device_id: Device ID for a Google Nest device.

            :ivar nest_structure_id: ID of the Google Nest structure containing the device.

            :ivar structure_name: Name of the Google Nest structure containing the device. The device owner sets this value.
            """

            device_custom_name: Optional[str]
            device_name: Optional[str]
            display_name: Optional[str]
            nest_device_id: Optional[str]
            nest_structure_id: Optional[str]
            structure_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_custom_name=d.get("device_custom_name", None),
                    device_name=d.get("device_name", None),
                    display_name=d.get("display_name", None),
                    nest_device_id=d.get("nest_device_id", None),
                    nest_structure_id=d.get("nest_structure_id", None),
                    structure_name=d.get("structure_name", None),
                )

        @dataclass
        class NoiseawareMetadata(ResourceMapping):
            """Metadata for a NoiseAware device.

            :ivar device_id: Device ID for a NoiseAware device.

            :ivar device_model: Device model for a NoiseAware device.

            :ivar device_name: Device name for a NoiseAware device.

            :ivar noise_level_decibel: Noise level, in decibels, for a NoiseAware device.

            :ivar noise_level_nrs: Noise level, expressed as a Noise Risk Score (NRS), for a NoiseAware device.
            """

            device_id: Optional[str]
            device_model: Optional[Literal["indoor", "outdoor"]]
            device_name: Optional[str]
            noise_level_decibel: Optional[float]
            noise_level_nrs: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_model=d.get("device_model", None),
                    device_name=d.get("device_name", None),
                    noise_level_decibel=d.get("noise_level_decibel", None),
                    noise_level_nrs=d.get("noise_level_nrs", None),
                )

        @dataclass
        class NukiMetadata(ResourceMapping):
            """Metadata for a Nuki device.

            :ivar device_id: Device ID for a Nuki device.

            :ivar device_name: Device name for a Nuki device.

            :ivar keypad_2_paired: Indicates whether keypad 2 is paired for a Nuki device.

            :ivar keypad_battery_critical: Indicates whether the keypad battery is in a critical state for a Nuki device.

            :ivar keypad_paired: Indicates whether the keypad is paired for a Nuki device.
            """

            device_id: Optional[str]
            device_name: Optional[str]
            keypad_2_paired: Optional[bool]
            keypad_battery_critical: Optional[bool]
            keypad_paired: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    keypad_2_paired=d.get("keypad_2_paired", None),
                    keypad_battery_critical=d.get("keypad_battery_critical", None),
                    keypad_paired=d.get("keypad_paired", None),
                )

        @dataclass
        class OmnitecMetadata(ResourceMapping):
            """Metadata for an Omnitec device.

            :ivar has_gateway: Whether the Omnitec lock has a connected gateway for remote operations.

            :ivar lock_alias: Operator-assigned alias for an Omnitec device.

            :ivar lock_id: Lock ID for an Omnitec device.

            :ivar lock_mac: Bluetooth MAC address for an Omnitec device.

            :ivar lock_name: Lock name for an Omnitec device.

            :ivar time_zone: IANA time zone for the Omnitec device, used to schedule time-bound access codes at the correct local time (accounting for DST).

            :ivar timezone_raw_offset_ms: Static UTC offset of the Omnitec lock in milliseconds. Does not account for DST.
            """

            has_gateway: Optional[bool]
            lock_alias: Optional[str]
            lock_id: Optional[float]
            lock_mac: Optional[str]
            lock_name: Optional[str]
            time_zone: Optional[str]
            timezone_raw_offset_ms: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    has_gateway=d.get("has_gateway", None),
                    lock_alias=d.get("lock_alias", None),
                    lock_id=d.get("lock_id", None),
                    lock_mac=d.get("lock_mac", None),
                    lock_name=d.get("lock_name", None),
                    time_zone=d.get("time_zone", None),
                    timezone_raw_offset_ms=d.get("timezone_raw_offset_ms", None),
                )

        @dataclass
        class RingMetadata(ResourceMapping):
            """Metadata for a Ring device.

            :ivar device_id: Device ID for a Ring device.

            :ivar device_name: Device name for a Ring device."""

            device_id: Optional[str]
            device_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                )

        @dataclass
        class SaltoKsMetadata(ResourceMapping):
            """Metadata for a Salto KS device.

            :ivar battery_level: Battery level for a Salto KS device.

            :ivar customer_reference: Customer reference for a Salto KS device.

            :ivar has_custom_pin_subscription: Indicates whether the site has a Salto KS subscription that supports custom PINs.

            :ivar lock_id: Lock ID for a Salto KS device.

            :ivar lock_type: Lock type for a Salto KS device.

            :ivar locked_state: Locked state for a Salto KS device.

            :ivar model: Model for a Salto KS device.

            :ivar site_id: Site ID for the Salto KS site to which the device belongs.

            :ivar site_name: Site name for the Salto KS site to which the device belongs.
            """

            battery_level: Optional[str]
            customer_reference: Optional[str]
            has_custom_pin_subscription: Optional[bool]
            lock_id: Optional[str]
            lock_type: Optional[str]
            locked_state: Optional[str]
            model: Optional[str]
            site_id: Optional[str]
            site_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    battery_level=d.get("battery_level", None),
                    customer_reference=d.get("customer_reference", None),
                    has_custom_pin_subscription=d.get(
                        "has_custom_pin_subscription", None
                    ),
                    lock_id=d.get("lock_id", None),
                    lock_type=d.get("lock_type", None),
                    locked_state=d.get("locked_state", None),
                    model=d.get("model", None),
                    site_id=d.get("site_id", None),
                    site_name=d.get("site_name", None),
                )

        @dataclass
        class SaltoMetadata(ResourceMapping):
            """Metada for a Salto device.

            :ivar battery_level: Battery level for a Salto device.

            :ivar customer_reference: Customer reference for a Salto device.

            :ivar lock_id: Lock ID for a Salto device.

            :ivar lock_type: Lock type for a Salto device.

            :ivar locked_state: Locked state for a Salto device.

            :ivar model: Model for a Salto device.

            :ivar site_id: Site ID for the Salto KS site to which the device belongs.

            :ivar site_name: Site name for the Salto KS site to which the device belongs.
            """

            battery_level: Optional[str]
            customer_reference: Optional[str]
            lock_id: Optional[str]
            lock_type: Optional[str]
            locked_state: Optional[str]
            model: Optional[str]
            site_id: Optional[str]
            site_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    battery_level=d.get("battery_level", None),
                    customer_reference=d.get("customer_reference", None),
                    lock_id=d.get("lock_id", None),
                    lock_type=d.get("lock_type", None),
                    locked_state=d.get("locked_state", None),
                    model=d.get("model", None),
                    site_id=d.get("site_id", None),
                    site_name=d.get("site_name", None),
                )

        @dataclass
        class SchlageMetadata(ResourceMapping):
            """Metadata for a Schlage device.

            :ivar device_id: Device ID for a Schlage device.

            :ivar device_name: Device name for a Schlage device.

            :ivar model: Model for a Schlage device."""

            device_id: Optional[str]
            device_name: Optional[str]
            model: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    model=d.get("model", None),
                )

        @dataclass
        class SeamBridgeMetadata(ResourceMapping):
            """Metadata for Seam Bridge.

            :ivar device_num: Device number for Seam Bridge.

            :ivar name: Name for Seam Bridge.

            :ivar unlock_method: Unlock method for Seam Bridge."""

            device_num: Optional[float]
            name: Optional[str]
            unlock_method: Optional[Literal["bridge", "doorking"]]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_num=d.get("device_num", None),
                    name=d.get("name", None),
                    unlock_method=d.get("unlock_method", None),
                )

        @dataclass
        class SensiMetadata(ResourceMapping):
            """Metadata for a Sensi device.

            :ivar device_id: Device ID for a Sensi device.

            :ivar device_name: Device name for a Sensi device.

            :ivar dual_setpoints_not_supported: Set to true when the device does not support the /dual-setpoints API endpoint.

            :ivar product_type: Product type for a Sensi device."""

            device_id: Optional[str]
            device_name: Optional[str]
            dual_setpoints_not_supported: Optional[bool]
            product_type: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    dual_setpoints_not_supported=d.get(
                        "dual_setpoints_not_supported", None
                    ),
                    product_type=d.get("product_type", None),
                )

        @dataclass
        class SmartthingsMetadata(ResourceMapping):
            """Metadata for a SmartThings device.

            :ivar device_id: Device ID for a SmartThings device.

            :ivar device_name: Device name for a SmartThings device.

            :ivar location_id: Location ID for a SmartThings device.

            :ivar model: Model for a SmartThings device."""

            device_id: Optional[str]
            device_name: Optional[str]
            location_id: Optional[str]
            model: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    location_id=d.get("location_id", None),
                    model=d.get("model", None),
                )

        @dataclass
        class TadoMetadata(ResourceMapping):
            """Metadata for a tado° device.

            :ivar device_type: Device type for a tado° device.

            :ivar serial_no: Serial number for a tado° device."""

            device_type: Optional[str]
            serial_no: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_type=d.get("device_type", None),
                    serial_no=d.get("serial_no", None),
                )

        @dataclass
        class TedeeMetadata(ResourceMapping):
            """Metadata for a Tedee device.

            :ivar bridge_id: Bridge ID for a Tedee device.

            :ivar bridge_name: Bridge name for a Tedee device.

            :ivar device_id: Device ID for a Tedee device.

            :ivar device_model: Device model for a Tedee device.

            :ivar device_name: Device name for a Tedee device.

            :ivar keypad_id: Keypad ID for a Tedee device.

            :ivar serial_number: Serial number for a Tedee device."""

            bridge_id: Optional[float]
            bridge_name: Optional[str]
            device_id: Optional[float]
            device_model: Optional[str]
            device_name: Optional[str]
            keypad_id: Optional[float]
            serial_number: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    bridge_id=d.get("bridge_id", None),
                    bridge_name=d.get("bridge_name", None),
                    device_id=d.get("device_id", None),
                    device_model=d.get("device_model", None),
                    device_name=d.get("device_name", None),
                    keypad_id=d.get("keypad_id", None),
                    serial_number=d.get("serial_number", None),
                )

        @dataclass
        class TtlockMetadata(ResourceMapping):
            """Metadata for a TTLock device.

            :ivar feature_value: Feature value for a TTLock device.

            :ivar features: Features for a TTLock device.

            :ivar has_gateway: Indicates whether a TTLock device has a gateway.

            :ivar lock_alias: Lock alias for a TTLock device.

            :ivar lock_id: Lock ID for a TTLock device.

            :ivar timezone_raw_offset_ms: Lock-side timezone offset in milliseconds east of UTC, as configured in the TTLock app. Source of truth for the lock's wall-clock interpretation of access code start/end times — a misconfigured value here is the typical cause of customer "codes offset by N hours" reports. Diagnostic only; Seam does not convert times based on this value.

            :ivar wireless_keypads: Wireless keypads for a TTLock device."""

            @dataclass
            class Features(ResourceMapping):
                """Features for a TTLock device.

                :ivar auto_lock_time_config: Indicates whether a TTLock device supports auto-lock time configuration.

                :ivar incomplete_keyboard_passcode: Indicates whether a TTLock device supports an incomplete keyboard passcode.

                :ivar lock_command: Indicates whether a TTLock device supports the lock command.

                :ivar passcode: Indicates whether a TTLock device supports a passcode.

                :ivar passcode_management: Indicates whether a TTLock device supports passcode management.

                :ivar unlock_via_gateway: Indicates whether a TTLock device supports unlock via gateway.

                :ivar wifi: Indicates whether a TTLock device supports Wi-Fi."""

                auto_lock_time_config: Optional[bool]
                incomplete_keyboard_passcode: Optional[bool]
                lock_command: Optional[bool]
                passcode: Optional[bool]
                passcode_management: Optional[bool]
                unlock_via_gateway: Optional[bool]
                wifi: Optional[bool]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        auto_lock_time_config=d.get("auto_lock_time_config", None),
                        incomplete_keyboard_passcode=d.get(
                            "incomplete_keyboard_passcode", None
                        ),
                        lock_command=d.get("lock_command", None),
                        passcode=d.get("passcode", None),
                        passcode_management=d.get("passcode_management", None),
                        unlock_via_gateway=d.get("unlock_via_gateway", None),
                        wifi=d.get("wifi", None),
                    )

            @dataclass
            class WirelessKeypads(ResourceMapping):
                """Wireless keypads for a TTLock device.

                :ivar wireless_keypad_id: ID for a wireless keypad for a TTLock device.

                :ivar wireless_keypad_name: Name for a wireless keypad for a TTLock device.
                """

                wireless_keypad_id: Optional[float]
                wireless_keypad_name: Optional[str]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        wireless_keypad_id=d.get("wireless_keypad_id", None),
                        wireless_keypad_name=d.get("wireless_keypad_name", None),
                    )

            feature_value: Optional[str]
            features: Optional[Features]
            has_gateway: Optional[bool]
            lock_alias: Optional[str]
            lock_id: Optional[float]
            timezone_raw_offset_ms: Optional[float]
            wireless_keypads: Optional[List[WirelessKeypads]]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    feature_value=d.get("feature_value", None),
                    features=_object_from_dict(cls.Features, d.get("features")),
                    has_gateway=d.get("has_gateway", None),
                    lock_alias=d.get("lock_alias", None),
                    lock_id=d.get("lock_id", None),
                    timezone_raw_offset_ms=d.get("timezone_raw_offset_ms", None),
                    wireless_keypads=_object_list_from_dict(
                        cls.WirelessKeypads, d.get("wireless_keypads")
                    ),
                )

        @dataclass
        class TwoNMetadata(ResourceMapping):
            """Metadata for a 2N device.

            :ivar device_id: Device ID for a 2N device.

            :ivar device_name: Device name for a 2N device."""

            device_id: Optional[float]
            device_name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                )

        @dataclass
        class UltraloqMetadata(ResourceMapping):
            """Metadata for an Ultraloq device.

            :ivar device_id: Device ID for an Ultraloq device.

            :ivar device_name: Device name for an Ultraloq device.

            :ivar device_type: Device type for an Ultraloq device.

            :ivar time_zone: IANA timezone for the Ultraloq device."""

            device_id: Optional[str]
            device_name: Optional[str]
            device_type: Optional[str]
            time_zone: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    device_type=d.get("device_type", None),
                    time_zone=d.get("time_zone", None),
                )

        @dataclass
        class VisionlineMetadata(ResourceMapping):
            """Metadata for an ASSA ABLOY Visionline system.

            :ivar encoder_id: Encoder ID for an ASSA ABLOY Visionline system."""

            encoder_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    encoder_id=d.get("encoder_id", None),
                )

        @dataclass
        class WyzeMetadata(ResourceMapping):
            """Metadata for a Wyze device.

            :ivar device_id: Device ID for a Wyze device.

            :ivar device_info_model: Device information model for a Wyze device.

            :ivar device_name: Device name for a Wyze device.

            :ivar keypad_uuid: Keypad UUID for a Wyze device.

            :ivar locker_status_hardlock: Locker status (hardlock) for a Wyze device.

            :ivar product_model: Product model for a Wyze device.

            :ivar product_name: Product name for a Wyze device.

            :ivar product_type: Product type for a Wyze device."""

            device_id: Optional[str]
            device_info_model: Optional[str]
            device_name: Optional[str]
            keypad_uuid: Optional[str]
            locker_status_hardlock: Optional[float]
            product_model: Optional[str]
            product_name: Optional[str]
            product_type: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_info_model=d.get("device_info_model", None),
                    device_name=d.get("device_name", None),
                    keypad_uuid=d.get("keypad_uuid", None),
                    locker_status_hardlock=d.get("locker_status_hardlock", None),
                    product_model=d.get("product_model", None),
                    product_name=d.get("product_name", None),
                    product_type=d.get("product_type", None),
                )

        @dataclass
        class YacanMetadata(ResourceMapping):
            """Metadata for a Yacan device.

            :ivar device_id: Device ID for a Yacan device.

            :ivar device_name: Device name for a Yacan device.

            :ivar device_type: Device type for a Yacan device.

            :ivar serial_number: Serial number for a Yacan device."""

            device_id: Optional[str]
            device_name: Optional[str]
            device_type: Optional[str]
            serial_number: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_id=d.get("device_id", None),
                    device_name=d.get("device_name", None),
                    device_type=d.get("device_type", None),
                    serial_number=d.get("serial_number", None),
                )

        @dataclass
        class CodeConstraints(ResourceMapping):
            """Constraints on access codes for the device. Seam represents each constraint as an object with a ``constraint_type`` property. Depending on the constraint type, there may also be additional properties. Note that some constraints are manufacturer- or device-specific.

            :ivar constraint_type:

            :ivar max_length: Maximum name length constraint for access codes.

            :ivar min_length: Minimum name length constraint for access codes."""

            constraint_type: Literal[
                "no_zeros",
                "cannot_start_with_12",
                "no_triple_consecutive_ints",
                "cannot_specify_pin_code",
                "pin_code_matches_existing_set",
                "start_date_in_future",
                "no_ascending_or_descending_sequence",
                "at_least_three_unique_digits",
                "cannot_contain_089",
                "cannot_contain_0789",
                "unique_first_four_digits",
                "no_all_same_digits",
                "name_length",
                "name_must_be_unique",
            ]
            max_length: Optional[float]
            min_length: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    constraint_type=d.get("constraint_type", None),
                    max_length=d.get("max_length", None),
                    min_length=d.get("min_length", None),
                )

        @dataclass
        class KeypadBattery(ResourceMapping):
            """Keypad battery status.

            :ivar level: Keypad battery charge level."""

            level: float

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    level=d.get("level", None),
                )

        @dataclass
        class OfflineTimeFrameOptions(ResourceMapping):
            """Time frames that may be requested when creating an offline access code, expressed as a list of options. The caller picks one option (by matching the requested duration when the options' duration ranges do not overlap, or by ``display_name`` when they do) and satisfies that one option's rules. When ``undefined``, any time frame works.

            :ivar display_name: Label for this option. For a single-option device, the product name (for example, ``algoPIN`` or ``SmartPIN``); for a multi-option device, a label that distinguishes it (for example, ``Hourly`` or ``Fixed start times``).

            :ivar end_date_recurrence_rule: iCalendar recurrence rule (RRULE) that the end date must fall on. Constrains which calendar dates are selectable, independent of the time-of-day rules.

            :ivar matching_start_end_time: When ``true``, the start and end must fall at the same time of day (the caller picks which). Mutually exclusive with ``time_pairs``.

            :ivar max_duration: Maximum duration this option covers, as an ISO 8601 duration (for example, ``PT672H`` or ``P367D``). Omitted when there is no maximum.

            :ivar min_duration: Minimum duration this option covers, as an ISO 8601 duration (for example, ``PT1H`` or ``P29D``). Omitted when there is no minimum.

            :ivar start_date_recurrence_rule: iCalendar recurrence rule (RRULE) that the start date must fall on (for example, ``FREQ=MONTHLY;BYDAY=1MO,3MO``). Constrains which calendar dates are selectable, independent of the time-of-day rules.

            :ivar time_pairs: Fixed start/end time pairings the caller chooses from. Mutually exclusive with ``matching_start_end_time``.

            :ivar time_zone: IANA time zone for interpreting ``time_pairs`` and the date recurrence rules. Present only when the option fixes times or dates.
            """

            @dataclass
            class TimePairs(ResourceMapping):
                """Fixed start/end time pairings the caller chooses from. Mutually exclusive with ``matching_start_end_time``.

                :ivar display_name: Label for the start/end time pairing.

                :ivar end_time: End time of day as a 24-hour ``HH:MM`` value, interpreted in the option's ``time_zone``. An ``end_time`` earlier on the clock than ``start_time`` means the end falls on a later date.

                :ivar start_time: Start time of day as a 24-hour ``HH:MM`` value, interpreted in the option's ``time_zone``.
                """

                display_name: str
                end_time: str
                start_time: str

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        display_name=d.get("display_name", None),
                        end_time=d.get("end_time", None),
                        start_time=d.get("start_time", None),
                    )

            display_name: str
            end_date_recurrence_rule: Optional[str]
            matching_start_end_time: Optional[Literal[True]]
            max_duration: Optional[str]
            min_duration: Optional[str]
            start_date_recurrence_rule: Optional[str]
            time_pairs: Optional[List[TimePairs]]
            time_zone: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    display_name=d.get("display_name", None),
                    end_date_recurrence_rule=d.get("end_date_recurrence_rule", None),
                    matching_start_end_time=d.get("matching_start_end_time", None),
                    max_duration=d.get("max_duration", None),
                    min_duration=d.get("min_duration", None),
                    start_date_recurrence_rule=d.get(
                        "start_date_recurrence_rule", None
                    ),
                    time_pairs=_object_list_from_dict(
                        cls.TimePairs, d.get("time_pairs")
                    ),
                    time_zone=d.get("time_zone", None),
                )

        @dataclass
        class OnlineTimeFrameOptions(ResourceMapping):
            """Time frames that may be requested when creating an online access code, expressed as a list of options. The caller picks one option (by matching the requested duration when the options' duration ranges do not overlap, or by ``display_name`` when they do) and satisfies that one option's rules. When ``undefined``, any time frame works.

            :ivar display_name: Label for this option. For a single-option device, the product name (for example, ``algoPIN`` or ``SmartPIN``); for a multi-option device, a label that distinguishes it (for example, ``Hourly`` or ``Fixed start times``).

            :ivar end_date_recurrence_rule: iCalendar recurrence rule (RRULE) that the end date must fall on. Constrains which calendar dates are selectable, independent of the time-of-day rules.

            :ivar matching_start_end_time: When ``true``, the start and end must fall at the same time of day (the caller picks which). Mutually exclusive with ``time_pairs``.

            :ivar max_duration: Maximum duration this option covers, as an ISO 8601 duration (for example, ``PT672H`` or ``P367D``). Omitted when there is no maximum.

            :ivar min_duration: Minimum duration this option covers, as an ISO 8601 duration (for example, ``PT1H`` or ``P29D``). Omitted when there is no minimum.

            :ivar start_date_recurrence_rule: iCalendar recurrence rule (RRULE) that the start date must fall on (for example, ``FREQ=MONTHLY;BYDAY=1MO,3MO``). Constrains which calendar dates are selectable, independent of the time-of-day rules.

            :ivar time_pairs: Fixed start/end time pairings the caller chooses from. Mutually exclusive with ``matching_start_end_time``.

            :ivar time_zone: IANA time zone for interpreting ``time_pairs`` and the date recurrence rules. Present only when the option fixes times or dates.
            """

            @dataclass
            class TimePairs(ResourceMapping):
                """Fixed start/end time pairings the caller chooses from. Mutually exclusive with ``matching_start_end_time``.

                :ivar display_name: Label for the start/end time pairing.

                :ivar end_time: End time of day as a 24-hour ``HH:MM`` value, interpreted in the option's ``time_zone``. An ``end_time`` earlier on the clock than ``start_time`` means the end falls on a later date.

                :ivar start_time: Start time of day as a 24-hour ``HH:MM`` value, interpreted in the option's ``time_zone``.
                """

                display_name: str
                end_time: str
                start_time: str

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        display_name=d.get("display_name", None),
                        end_time=d.get("end_time", None),
                        start_time=d.get("start_time", None),
                    )

            display_name: str
            end_date_recurrence_rule: Optional[str]
            matching_start_end_time: Optional[Literal[True]]
            max_duration: Optional[str]
            min_duration: Optional[str]
            start_date_recurrence_rule: Optional[str]
            time_pairs: Optional[List[TimePairs]]
            time_zone: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    display_name=d.get("display_name", None),
                    end_date_recurrence_rule=d.get("end_date_recurrence_rule", None),
                    matching_start_end_time=d.get("matching_start_end_time", None),
                    max_duration=d.get("max_duration", None),
                    min_duration=d.get("min_duration", None),
                    start_date_recurrence_rule=d.get(
                        "start_date_recurrence_rule", None
                    ),
                    time_pairs=_object_list_from_dict(
                        cls.TimePairs, d.get("time_pairs")
                    ),
                    time_zone=d.get("time_zone", None),
                )

        @dataclass
        class ActiveThermostatSchedule(ResourceMapping):
            """Active `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

            :ivar climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

            :ivar created_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ was created.

            :ivar device_id: ID of the desired `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ device.

            :ivar ends_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

            :ivar errors: Errors associated with the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

            :ivar is_override_allowed: Indicates whether a person at the thermostat can change the thermostat's settings after the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ starts.

            :ivar max_override_period_minutes: Number of minutes for which a person at the thermostat can change the thermostat's settings after the activation of the scheduled `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

            :ivar name: User-friendly name to identify the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

            :ivar starts_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

            :ivar thermostat_schedule_id: ID of the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

            :ivar workspace_id: ID of the workspace that contains the thermostat schedule.
            """

            @dataclass
            class Errors(ResourceMapping):
                """Errors associated with the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

                :ivar created_at: Date and time at which Seam created the error.

                :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

                :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
                """

                created_at: str
                error_code: str
                message: str

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        created_at=d.get("created_at", None),
                        error_code=d.get("error_code", None),
                        message=d.get("message", None),
                    )

            climate_preset_key: str
            created_at: str
            device_id: str
            ends_at: str
            errors: List[Errors]
            is_override_allowed: Optional[bool]
            max_override_period_minutes: Optional[int]
            name: Optional[str]
            starts_at: str
            thermostat_schedule_id: str
            workspace_id: str

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    climate_preset_key=d.get("climate_preset_key", None),
                    created_at=d.get("created_at", None),
                    device_id=d.get("device_id", None),
                    ends_at=d.get("ends_at", None),
                    errors=_object_list_from_dict(cls.Errors, d.get("errors")),
                    is_override_allowed=d.get("is_override_allowed", None),
                    max_override_period_minutes=d.get(
                        "max_override_period_minutes", None
                    ),
                    name=d.get("name", None),
                    starts_at=d.get("starts_at", None),
                    thermostat_schedule_id=d.get("thermostat_schedule_id", None),
                    workspace_id=d.get("workspace_id", None),
                )

        @dataclass
        class AvailableClimatePresets(ResourceMapping):
            """Available `climate presets <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for the thermostat.

            :ivar can_delete: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be deleted.

            :ivar can_edit: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be edited.

            :ivar can_use_with_thermostat_daily_programs: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be programmed in a thermostat daily program.

            :ivar climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

            :ivar cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar display_name: Display name for the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

            :ivar fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

            :ivar heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

            :ivar manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat can change the thermostat's settings. See `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

            :ivar name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.
            """

            @dataclass
            class EcobeeMetadata(ResourceMapping):
                """Metadata specific to the Ecobee climate, if applicable.

                :ivar climate_ref: Reference to the Ecobee climate, if applicable.

                :ivar is_optimized: Indicates if the climate preset is optimized by Ecobee.

                :ivar owner: Indicates whether the climate preset is owned by the user or the system.
                """

                climate_ref: Optional[str]
                is_optimized: Optional[bool]
                owner: Optional[Literal["user", "system"]]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        climate_ref=d.get("climate_ref", None),
                        is_optimized=d.get("is_optimized", None),
                        owner=d.get("owner", None),
                    )

            can_delete: bool
            can_edit: bool
            can_use_with_thermostat_daily_programs: bool
            climate_preset_key: str
            climate_preset_mode: Optional[
                Literal["home", "away", "wake", "sleep", "occupied", "unoccupied"]
            ]
            cooling_set_point_celsius: Optional[float]
            cooling_set_point_fahrenheit: Optional[float]
            display_name: str
            ecobee_metadata: Optional[EcobeeMetadata]
            fan_mode_setting: Optional[Literal["auto", "on", "circulate"]]
            heating_set_point_celsius: Optional[float]
            heating_set_point_fahrenheit: Optional[float]
            hvac_mode_setting: Optional[
                Literal["off", "heat", "cool", "heat_cool", "eco"]
            ]
            manual_override_allowed: bool
            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    can_delete=d.get("can_delete", None),
                    can_edit=d.get("can_edit", None),
                    can_use_with_thermostat_daily_programs=d.get(
                        "can_use_with_thermostat_daily_programs", None
                    ),
                    climate_preset_key=d.get("climate_preset_key", None),
                    climate_preset_mode=d.get("climate_preset_mode", None),
                    cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
                    cooling_set_point_fahrenheit=d.get(
                        "cooling_set_point_fahrenheit", None
                    ),
                    display_name=d.get("display_name", None),
                    ecobee_metadata=_object_from_dict(
                        cls.EcobeeMetadata, d.get("ecobee_metadata")
                    ),
                    fan_mode_setting=d.get("fan_mode_setting", None),
                    heating_set_point_celsius=d.get("heating_set_point_celsius", None),
                    heating_set_point_fahrenheit=d.get(
                        "heating_set_point_fahrenheit", None
                    ),
                    hvac_mode_setting=d.get("hvac_mode_setting", None),
                    manual_override_allowed=d.get("manual_override_allowed", None),
                    name=d.get("name", None),
                )

        @dataclass
        class CurrentClimateSetting(ResourceMapping):
            """Current climate setting.

            :ivar can_delete: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be deleted.

            :ivar can_edit: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be edited.

            :ivar can_use_with_thermostat_daily_programs: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be programmed in a thermostat daily program.

            :ivar climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

            :ivar cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar display_name: Display name for the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

            :ivar fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

            :ivar heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

            :ivar manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat can change the thermostat's settings. See `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

            :ivar name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.
            """

            @dataclass
            class EcobeeMetadata(ResourceMapping):
                """Metadata specific to the Ecobee climate, if applicable.

                :ivar climate_ref: Reference to the Ecobee climate, if applicable.

                :ivar is_optimized: Indicates if the climate preset is optimized by Ecobee.

                :ivar owner: Indicates whether the climate preset is owned by the user or the system.
                """

                climate_ref: Optional[str]
                is_optimized: Optional[bool]
                owner: Optional[Literal["user", "system"]]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        climate_ref=d.get("climate_ref", None),
                        is_optimized=d.get("is_optimized", None),
                        owner=d.get("owner", None),
                    )

            can_delete: Optional[bool]
            can_edit: Optional[bool]
            can_use_with_thermostat_daily_programs: Optional[bool]
            climate_preset_key: Optional[str]
            climate_preset_mode: Optional[
                Literal["home", "away", "wake", "sleep", "occupied", "unoccupied"]
            ]
            cooling_set_point_celsius: Optional[float]
            cooling_set_point_fahrenheit: Optional[float]
            display_name: Optional[str]
            ecobee_metadata: Optional[EcobeeMetadata]
            fan_mode_setting: Optional[Literal["auto", "on", "circulate"]]
            heating_set_point_celsius: Optional[float]
            heating_set_point_fahrenheit: Optional[float]
            hvac_mode_setting: Optional[
                Literal["off", "heat", "cool", "heat_cool", "eco"]
            ]
            manual_override_allowed: Optional[bool]
            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    can_delete=d.get("can_delete", None),
                    can_edit=d.get("can_edit", None),
                    can_use_with_thermostat_daily_programs=d.get(
                        "can_use_with_thermostat_daily_programs", None
                    ),
                    climate_preset_key=d.get("climate_preset_key", None),
                    climate_preset_mode=d.get("climate_preset_mode", None),
                    cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
                    cooling_set_point_fahrenheit=d.get(
                        "cooling_set_point_fahrenheit", None
                    ),
                    display_name=d.get("display_name", None),
                    ecobee_metadata=_object_from_dict(
                        cls.EcobeeMetadata, d.get("ecobee_metadata")
                    ),
                    fan_mode_setting=d.get("fan_mode_setting", None),
                    heating_set_point_celsius=d.get("heating_set_point_celsius", None),
                    heating_set_point_fahrenheit=d.get(
                        "heating_set_point_fahrenheit", None
                    ),
                    hvac_mode_setting=d.get("hvac_mode_setting", None),
                    manual_override_allowed=d.get("manual_override_allowed", None),
                    name=d.get("name", None),
                )

        @dataclass
        class DefaultClimateSetting(ResourceMapping):
            """

            :ivar can_delete: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be deleted.

            :ivar can_edit: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be edited.

            :ivar can_use_with_thermostat_daily_programs: Indicates whether the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ key can be programmed in a thermostat daily program.

            :ivar climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

            :ivar cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar display_name: Display name for the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

            :ivar ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

            :ivar fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

            :ivar heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

            :ivar hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

            :ivar manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat can change the thermostat's settings. See `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

            :ivar name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.
            """

            @dataclass
            class EcobeeMetadata(ResourceMapping):
                """Metadata specific to the Ecobee climate, if applicable.

                :ivar climate_ref: Reference to the Ecobee climate, if applicable.

                :ivar is_optimized: Indicates if the climate preset is optimized by Ecobee.

                :ivar owner: Indicates whether the climate preset is owned by the user or the system.
                """

                climate_ref: Optional[str]
                is_optimized: Optional[bool]
                owner: Optional[Literal["user", "system"]]

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        climate_ref=d.get("climate_ref", None),
                        is_optimized=d.get("is_optimized", None),
                        owner=d.get("owner", None),
                    )

            can_delete: Optional[bool]
            can_edit: Optional[bool]
            can_use_with_thermostat_daily_programs: Optional[bool]
            climate_preset_key: Optional[str]
            climate_preset_mode: Optional[
                Literal["home", "away", "wake", "sleep", "occupied", "unoccupied"]
            ]
            cooling_set_point_celsius: Optional[float]
            cooling_set_point_fahrenheit: Optional[float]
            display_name: Optional[str]
            ecobee_metadata: Optional[EcobeeMetadata]
            fan_mode_setting: Optional[Literal["auto", "on", "circulate"]]
            heating_set_point_celsius: Optional[float]
            heating_set_point_fahrenheit: Optional[float]
            hvac_mode_setting: Optional[
                Literal["off", "heat", "cool", "heat_cool", "eco"]
            ]
            manual_override_allowed: Optional[bool]
            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    can_delete=d.get("can_delete", None),
                    can_edit=d.get("can_edit", None),
                    can_use_with_thermostat_daily_programs=d.get(
                        "can_use_with_thermostat_daily_programs", None
                    ),
                    climate_preset_key=d.get("climate_preset_key", None),
                    climate_preset_mode=d.get("climate_preset_mode", None),
                    cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
                    cooling_set_point_fahrenheit=d.get(
                        "cooling_set_point_fahrenheit", None
                    ),
                    display_name=d.get("display_name", None),
                    ecobee_metadata=_object_from_dict(
                        cls.EcobeeMetadata, d.get("ecobee_metadata")
                    ),
                    fan_mode_setting=d.get("fan_mode_setting", None),
                    heating_set_point_celsius=d.get("heating_set_point_celsius", None),
                    heating_set_point_fahrenheit=d.get(
                        "heating_set_point_fahrenheit", None
                    ),
                    hvac_mode_setting=d.get("hvac_mode_setting", None),
                    manual_override_allowed=d.get("manual_override_allowed", None),
                    name=d.get("name", None),
                )

        @dataclass
        class TemperatureThreshold(ResourceMapping):
            """Current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.

            :ivar lower_limit_celsius: Lower limit in °C within the current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.

            :ivar lower_limit_fahrenheit: Lower limit in °F within the current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.

            :ivar upper_limit_celsius: Upper limit in °C within the current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.

            :ivar upper_limit_fahrenheit: Upper limit in °F within the current `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ set for the thermostat.
            """

            lower_limit_celsius: Optional[float]
            lower_limit_fahrenheit: Optional[float]
            upper_limit_celsius: Optional[float]
            upper_limit_fahrenheit: Optional[float]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    lower_limit_celsius=d.get("lower_limit_celsius", None),
                    lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
                    upper_limit_celsius=d.get("upper_limit_celsius", None),
                    upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
                )

        @dataclass
        class ThermostatDailyPrograms(ResourceMapping):
            """Configured `daily programs <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-programs>`_ for the thermostat.

            :ivar created_at: Date and time at which the thermostat daily program was created.

            :ivar device_id: ID of the thermostat device on which the thermostat daily program is configured.

            :ivar name: User-friendly name to identify the thermostat daily program.

            :ivar periods: Array of thermostat daily program periods.

            :ivar thermostat_daily_program_id: ID of the thermostat daily program.

            :ivar workspace_id: ID of the workspace that contains the thermostat daily program.
            """

            @dataclass
            class Periods(ResourceMapping):
                """Array of thermostat daily program periods.

                :ivar climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to activate at the ``starts_at_time``.

                :ivar starts_at_time: Time at which the thermostat daily program period starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
                """

                climate_preset_key: str
                starts_at_time: str

                @classmethod
                def from_dict(cls, d: Any):
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        climate_preset_key=d.get("climate_preset_key", None),
                        starts_at_time=d.get("starts_at_time", None),
                    )

            created_at: str
            device_id: str
            name: Optional[str]
            periods: List[Periods]
            thermostat_daily_program_id: str
            workspace_id: str

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    created_at=d.get("created_at", None),
                    device_id=d.get("device_id", None),
                    name=d.get("name", None),
                    periods=_object_list_from_dict(cls.Periods, d.get("periods")),
                    thermostat_daily_program_id=d.get(
                        "thermostat_daily_program_id", None
                    ),
                    workspace_id=d.get("workspace_id", None),
                )

        @dataclass
        class ThermostatWeeklyProgram(ResourceMapping):
            """Current `weekly program <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-programs>`_ for the thermostat.

            :ivar created_at: Date and time at which the thermostat weekly program was created.

            :ivar friday_program_id: ID of the thermostat daily program to run on Fridays.

            :ivar monday_program_id: ID of the thermostat daily program to run on Mondays.

            :ivar saturday_program_id: ID of the thermostat daily program to run on Saturdays.

            :ivar sunday_program_id: ID of the thermostat daily program to run on Sundays.

            :ivar thursday_program_id: ID of the thermostat daily program to run on Thursdays.

            :ivar tuesday_program_id: ID of the thermostat daily program to run on Tuesdays.

            :ivar wednesday_program_id: ID of the thermostat daily program to run on Wednesdays.
            """

            created_at: str
            friday_program_id: Optional[str]
            monday_program_id: Optional[str]
            saturday_program_id: Optional[str]
            sunday_program_id: Optional[str]
            thursday_program_id: Optional[str]
            tuesday_program_id: Optional[str]
            wednesday_program_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    created_at=d.get("created_at", None),
                    friday_program_id=d.get("friday_program_id", None),
                    monday_program_id=d.get("monday_program_id", None),
                    saturday_program_id=d.get("saturday_program_id", None),
                    sunday_program_id=d.get("sunday_program_id", None),
                    thursday_program_id=d.get("thursday_program_id", None),
                    tuesday_program_id=d.get("tuesday_program_id", None),
                    wednesday_program_id=d.get("wednesday_program_id", None),
                )

        accessory_keypad: Optional[AccessoryKeypad]
        appearance: Optional[Appearance]
        battery: Optional[Battery]
        battery_level: Optional[float]
        currently_triggering_noise_threshold_ids: Optional[List[str]]
        has_direct_power: Optional[bool]
        image_alt_text: Optional[str]
        image_url: Optional[str]
        manufacturer: Optional[str]
        model: Optional[Model]
        name: str
        noise_level_decibels: Optional[float]
        offline_access_codes_enabled: Optional[bool]
        online: bool
        online_access_codes_enabled: Optional[bool]
        serial_number: Optional[str]
        supports_accessory_keypad: Optional[bool]
        supports_offline_access_codes: Optional[bool]
        assa_abloy_credential_service_metadata: Optional[
            AssaAbloyCredentialServiceMetadata
        ]
        salto_space_credential_service_metadata: Optional[
            SaltoSpaceCredentialServiceMetadata
        ]
        akiles_metadata: Optional[AkilesMetadata]
        aqara_metadata: Optional[AqaraMetadata]
        assa_abloy_vostio_metadata: Optional[AssaAbloyVostioMetadata]
        august_metadata: Optional[AugustMetadata]
        avigilon_alta_metadata: Optional[AvigilonAltaMetadata]
        brivo_metadata: Optional[BrivoMetadata]
        controlbyweb_metadata: Optional[ControlbywebMetadata]
        dormakaba_oracode_metadata: Optional[DormakabaOracodeMetadata]
        ecobee_metadata: Optional[EcobeeMetadata]
        four_suites_metadata: Optional[FourSuitesMetadata]
        genie_metadata: Optional[GenieMetadata]
        honeywell_resideo_metadata: Optional[HoneywellResideoMetadata]
        igloo_metadata: Optional[IglooMetadata]
        igloohome_metadata: Optional[IgloohomeMetadata]
        keynest_metadata: Optional[KeynestMetadata]
        kisi_metadata: Optional[KisiMetadata]
        korelock_metadata: Optional[KorelockMetadata]
        kwikset_metadata: Optional[KwiksetMetadata]
        lockly_metadata: Optional[LocklyMetadata]
        minut_metadata: Optional[MinutMetadata]
        nest_metadata: Optional[NestMetadata]
        noiseaware_metadata: Optional[NoiseawareMetadata]
        nuki_metadata: Optional[NukiMetadata]
        omnitec_metadata: Optional[OmnitecMetadata]
        ring_metadata: Optional[RingMetadata]
        salto_ks_metadata: Optional[SaltoKsMetadata]
        salto_metadata: Optional[SaltoMetadata]
        schlage_metadata: Optional[SchlageMetadata]
        seam_bridge_metadata: Optional[SeamBridgeMetadata]
        sensi_metadata: Optional[SensiMetadata]
        smartthings_metadata: Optional[SmartthingsMetadata]
        tado_metadata: Optional[TadoMetadata]
        tedee_metadata: Optional[TedeeMetadata]
        ttlock_metadata: Optional[TtlockMetadata]
        two_n_metadata: Optional[TwoNMetadata]
        ultraloq_metadata: Optional[UltraloqMetadata]
        visionline_metadata: Optional[VisionlineMetadata]
        wyze_metadata: Optional[WyzeMetadata]
        yacan_metadata: Optional[YacanMetadata]
        auto_lock_delay_seconds: Optional[float]
        auto_lock_enabled: Optional[bool]
        backup_access_code_pool_enabled: Optional[bool]
        code_constraints: Optional[List[CodeConstraints]]
        door_open: Optional[bool]
        has_native_entry_events: Optional[bool]
        keypad_battery: Optional[KeypadBattery]
        locked: Optional[bool]
        max_active_codes_supported: Optional[float]
        offline_time_frame_options: Optional[List[OfflineTimeFrameOptions]]
        online_time_frame_options: Optional[List[OnlineTimeFrameOptions]]
        supported_code_lengths: Optional[List[float]]
        supports_backup_access_code_pool: Optional[bool]
        active_thermostat_schedule: Optional[ActiveThermostatSchedule]
        active_thermostat_schedule_id: Optional[str]
        available_climate_preset_modes: Optional[
            List[Literal["home", "away", "wake", "sleep", "occupied", "unoccupied"]]
        ]
        available_climate_presets: Optional[List[AvailableClimatePresets]]
        available_fan_mode_settings: Optional[List[Literal["auto", "on", "circulate"]]]
        available_hvac_mode_settings: Optional[
            List[Literal["off", "heat", "cool", "heat_cool", "eco"]]
        ]
        current_climate_setting: Optional[CurrentClimateSetting]
        default_climate_setting: Optional[DefaultClimateSetting]
        fallback_climate_preset_key: Optional[str]
        fan_mode_setting: Optional[Literal["auto", "on", "circulate"]]
        is_cooling: Optional[bool]
        is_fan_running: Optional[bool]
        is_heating: Optional[bool]
        is_temporary_manual_override_active: Optional[bool]
        max_cooling_set_point_celsius: Optional[float]
        max_cooling_set_point_fahrenheit: Optional[float]
        max_heating_set_point_celsius: Optional[float]
        max_heating_set_point_fahrenheit: Optional[float]
        max_thermostat_daily_program_periods_per_day: Optional[float]
        max_unique_climate_presets_per_thermostat_weekly_program: Optional[float]
        min_cooling_set_point_celsius: Optional[float]
        min_cooling_set_point_fahrenheit: Optional[float]
        min_heating_cooling_delta_celsius: Optional[float]
        min_heating_cooling_delta_fahrenheit: Optional[float]
        min_heating_set_point_celsius: Optional[float]
        min_heating_set_point_fahrenheit: Optional[float]
        relative_humidity: Optional[float]
        temperature_celsius: Optional[float]
        temperature_fahrenheit: Optional[float]
        temperature_threshold: Optional[TemperatureThreshold]
        thermostat_daily_program_period_precision_minutes: Optional[float]
        thermostat_daily_programs: Optional[List[ThermostatDailyPrograms]]
        thermostat_weekly_program: Optional[ThermostatWeeklyProgram]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                accessory_keypad=_object_from_dict(
                    cls.AccessoryKeypad, d.get("accessory_keypad")
                ),
                appearance=_object_from_dict(cls.Appearance, d.get("appearance")),
                battery=_object_from_dict(cls.Battery, d.get("battery")),
                battery_level=d.get("battery_level", None),
                currently_triggering_noise_threshold_ids=d.get(
                    "currently_triggering_noise_threshold_ids", None
                ),
                has_direct_power=d.get("has_direct_power", None),
                image_alt_text=d.get("image_alt_text", None),
                image_url=d.get("image_url", None),
                manufacturer=d.get("manufacturer", None),
                model=_object_from_dict(cls.Model, d.get("model")),
                name=d.get("name", None),
                noise_level_decibels=d.get("noise_level_decibels", None),
                offline_access_codes_enabled=d.get(
                    "offline_access_codes_enabled", None
                ),
                online=d.get("online", None),
                online_access_codes_enabled=d.get("online_access_codes_enabled", None),
                serial_number=d.get("serial_number", None),
                supports_accessory_keypad=d.get("supports_accessory_keypad", None),
                supports_offline_access_codes=d.get(
                    "supports_offline_access_codes", None
                ),
                assa_abloy_credential_service_metadata=_object_from_dict(
                    cls.AssaAbloyCredentialServiceMetadata,
                    d.get("assa_abloy_credential_service_metadata"),
                ),
                salto_space_credential_service_metadata=_object_from_dict(
                    cls.SaltoSpaceCredentialServiceMetadata,
                    d.get("salto_space_credential_service_metadata"),
                ),
                akiles_metadata=_object_from_dict(
                    cls.AkilesMetadata, d.get("akiles_metadata")
                ),
                aqara_metadata=_object_from_dict(
                    cls.AqaraMetadata, d.get("aqara_metadata")
                ),
                assa_abloy_vostio_metadata=_object_from_dict(
                    cls.AssaAbloyVostioMetadata, d.get("assa_abloy_vostio_metadata")
                ),
                august_metadata=_object_from_dict(
                    cls.AugustMetadata, d.get("august_metadata")
                ),
                avigilon_alta_metadata=_object_from_dict(
                    cls.AvigilonAltaMetadata, d.get("avigilon_alta_metadata")
                ),
                brivo_metadata=_object_from_dict(
                    cls.BrivoMetadata, d.get("brivo_metadata")
                ),
                controlbyweb_metadata=_object_from_dict(
                    cls.ControlbywebMetadata, d.get("controlbyweb_metadata")
                ),
                dormakaba_oracode_metadata=_object_from_dict(
                    cls.DormakabaOracodeMetadata, d.get("dormakaba_oracode_metadata")
                ),
                ecobee_metadata=_object_from_dict(
                    cls.EcobeeMetadata, d.get("ecobee_metadata")
                ),
                four_suites_metadata=_object_from_dict(
                    cls.FourSuitesMetadata, d.get("four_suites_metadata")
                ),
                genie_metadata=_object_from_dict(
                    cls.GenieMetadata, d.get("genie_metadata")
                ),
                honeywell_resideo_metadata=_object_from_dict(
                    cls.HoneywellResideoMetadata, d.get("honeywell_resideo_metadata")
                ),
                igloo_metadata=_object_from_dict(
                    cls.IglooMetadata, d.get("igloo_metadata")
                ),
                igloohome_metadata=_object_from_dict(
                    cls.IgloohomeMetadata, d.get("igloohome_metadata")
                ),
                keynest_metadata=_object_from_dict(
                    cls.KeynestMetadata, d.get("keynest_metadata")
                ),
                kisi_metadata=_object_from_dict(
                    cls.KisiMetadata, d.get("kisi_metadata")
                ),
                korelock_metadata=_object_from_dict(
                    cls.KorelockMetadata, d.get("korelock_metadata")
                ),
                kwikset_metadata=_object_from_dict(
                    cls.KwiksetMetadata, d.get("kwikset_metadata")
                ),
                lockly_metadata=_object_from_dict(
                    cls.LocklyMetadata, d.get("lockly_metadata")
                ),
                minut_metadata=_object_from_dict(
                    cls.MinutMetadata, d.get("minut_metadata")
                ),
                nest_metadata=_object_from_dict(
                    cls.NestMetadata, d.get("nest_metadata")
                ),
                noiseaware_metadata=_object_from_dict(
                    cls.NoiseawareMetadata, d.get("noiseaware_metadata")
                ),
                nuki_metadata=_object_from_dict(
                    cls.NukiMetadata, d.get("nuki_metadata")
                ),
                omnitec_metadata=_object_from_dict(
                    cls.OmnitecMetadata, d.get("omnitec_metadata")
                ),
                ring_metadata=_object_from_dict(
                    cls.RingMetadata, d.get("ring_metadata")
                ),
                salto_ks_metadata=_object_from_dict(
                    cls.SaltoKsMetadata, d.get("salto_ks_metadata")
                ),
                salto_metadata=_object_from_dict(
                    cls.SaltoMetadata, d.get("salto_metadata")
                ),
                schlage_metadata=_object_from_dict(
                    cls.SchlageMetadata, d.get("schlage_metadata")
                ),
                seam_bridge_metadata=_object_from_dict(
                    cls.SeamBridgeMetadata, d.get("seam_bridge_metadata")
                ),
                sensi_metadata=_object_from_dict(
                    cls.SensiMetadata, d.get("sensi_metadata")
                ),
                smartthings_metadata=_object_from_dict(
                    cls.SmartthingsMetadata, d.get("smartthings_metadata")
                ),
                tado_metadata=_object_from_dict(
                    cls.TadoMetadata, d.get("tado_metadata")
                ),
                tedee_metadata=_object_from_dict(
                    cls.TedeeMetadata, d.get("tedee_metadata")
                ),
                ttlock_metadata=_object_from_dict(
                    cls.TtlockMetadata, d.get("ttlock_metadata")
                ),
                two_n_metadata=_object_from_dict(
                    cls.TwoNMetadata, d.get("two_n_metadata")
                ),
                ultraloq_metadata=_object_from_dict(
                    cls.UltraloqMetadata, d.get("ultraloq_metadata")
                ),
                visionline_metadata=_object_from_dict(
                    cls.VisionlineMetadata, d.get("visionline_metadata")
                ),
                wyze_metadata=_object_from_dict(
                    cls.WyzeMetadata, d.get("wyze_metadata")
                ),
                yacan_metadata=_object_from_dict(
                    cls.YacanMetadata, d.get("yacan_metadata")
                ),
                auto_lock_delay_seconds=d.get("auto_lock_delay_seconds", None),
                auto_lock_enabled=d.get("auto_lock_enabled", None),
                backup_access_code_pool_enabled=d.get(
                    "backup_access_code_pool_enabled", None
                ),
                code_constraints=_object_list_from_dict(
                    cls.CodeConstraints, d.get("code_constraints")
                ),
                door_open=d.get("door_open", None),
                has_native_entry_events=d.get("has_native_entry_events", None),
                keypad_battery=_object_from_dict(
                    cls.KeypadBattery, d.get("keypad_battery")
                ),
                locked=d.get("locked", None),
                max_active_codes_supported=d.get("max_active_codes_supported", None),
                offline_time_frame_options=_object_list_from_dict(
                    cls.OfflineTimeFrameOptions, d.get("offline_time_frame_options")
                ),
                online_time_frame_options=_object_list_from_dict(
                    cls.OnlineTimeFrameOptions, d.get("online_time_frame_options")
                ),
                supported_code_lengths=d.get("supported_code_lengths", None),
                supports_backup_access_code_pool=d.get(
                    "supports_backup_access_code_pool", None
                ),
                active_thermostat_schedule=_object_from_dict(
                    cls.ActiveThermostatSchedule, d.get("active_thermostat_schedule")
                ),
                active_thermostat_schedule_id=d.get(
                    "active_thermostat_schedule_id", None
                ),
                available_climate_preset_modes=d.get(
                    "available_climate_preset_modes", None
                ),
                available_climate_presets=_object_list_from_dict(
                    cls.AvailableClimatePresets, d.get("available_climate_presets")
                ),
                available_fan_mode_settings=d.get("available_fan_mode_settings", None),
                available_hvac_mode_settings=d.get(
                    "available_hvac_mode_settings", None
                ),
                current_climate_setting=_object_from_dict(
                    cls.CurrentClimateSetting, d.get("current_climate_setting")
                ),
                default_climate_setting=_object_from_dict(
                    cls.DefaultClimateSetting, d.get("default_climate_setting")
                ),
                fallback_climate_preset_key=d.get("fallback_climate_preset_key", None),
                fan_mode_setting=d.get("fan_mode_setting", None),
                is_cooling=d.get("is_cooling", None),
                is_fan_running=d.get("is_fan_running", None),
                is_heating=d.get("is_heating", None),
                is_temporary_manual_override_active=d.get(
                    "is_temporary_manual_override_active", None
                ),
                max_cooling_set_point_celsius=d.get(
                    "max_cooling_set_point_celsius", None
                ),
                max_cooling_set_point_fahrenheit=d.get(
                    "max_cooling_set_point_fahrenheit", None
                ),
                max_heating_set_point_celsius=d.get(
                    "max_heating_set_point_celsius", None
                ),
                max_heating_set_point_fahrenheit=d.get(
                    "max_heating_set_point_fahrenheit", None
                ),
                max_thermostat_daily_program_periods_per_day=d.get(
                    "max_thermostat_daily_program_periods_per_day", None
                ),
                max_unique_climate_presets_per_thermostat_weekly_program=d.get(
                    "max_unique_climate_presets_per_thermostat_weekly_program", None
                ),
                min_cooling_set_point_celsius=d.get(
                    "min_cooling_set_point_celsius", None
                ),
                min_cooling_set_point_fahrenheit=d.get(
                    "min_cooling_set_point_fahrenheit", None
                ),
                min_heating_cooling_delta_celsius=d.get(
                    "min_heating_cooling_delta_celsius", None
                ),
                min_heating_cooling_delta_fahrenheit=d.get(
                    "min_heating_cooling_delta_fahrenheit", None
                ),
                min_heating_set_point_celsius=d.get(
                    "min_heating_set_point_celsius", None
                ),
                min_heating_set_point_fahrenheit=d.get(
                    "min_heating_set_point_fahrenheit", None
                ),
                relative_humidity=d.get("relative_humidity", None),
                temperature_celsius=d.get("temperature_celsius", None),
                temperature_fahrenheit=d.get("temperature_fahrenheit", None),
                temperature_threshold=_object_from_dict(
                    cls.TemperatureThreshold, d.get("temperature_threshold")
                ),
                thermostat_daily_program_period_precision_minutes=d.get(
                    "thermostat_daily_program_period_precision_minutes", None
                ),
                thermostat_daily_programs=_object_list_from_dict(
                    cls.ThermostatDailyPrograms, d.get("thermostat_daily_programs")
                ),
                thermostat_weekly_program=_object_from_dict(
                    cls.ThermostatWeeklyProgram, d.get("thermostat_weekly_program")
                ),
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
    device_manufacturer: Optional[DeviceManufacturer]
    device_provider: Optional[DeviceProvider]
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
    is_managed: Literal[True]
    location: Optional[Location]
    nickname: Optional[str]
    properties: Optional[Properties]
    space_ids: List[str]
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
            device_manufacturer=_object_from_dict(
                cls.DeviceManufacturer, d.get("device_manufacturer")
            ),
            device_provider=_object_from_dict(
                cls.DeviceProvider, d.get("device_provider")
            ),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            is_managed=d.get("is_managed", None),
            location=_object_from_dict(cls.Location, d.get("location")),
            nickname=d.get("nickname", None),
            properties=_object_from_dict(cls.Properties, d.get("properties")),
            space_ids=d.get("space_ids", None),
            warnings=_discriminated_list_from_dict(
                d.get("warnings"), cls._WarningsVariants, "warning_code"
            ),
            workspace_id=d.get("workspace_id", None),
        )
