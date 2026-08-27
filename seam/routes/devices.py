from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import Device, DeviceProvider
from .devices_simulate import (
    AbstractDevicesSimulate,
    DevicesSimulate,
    AbstractAsyncDevicesSimulate,
    AsyncDevicesSimulate,
)
from .devices_unmanaged import (
    AbstractDevicesUnmanaged,
    DevicesUnmanaged,
    AbstractAsyncDevicesUnmanaged,
    AsyncDevicesUnmanaged,
)
from ..response import unwrap
from ..response import unwrap_list


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
        """Returns a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the device that you want to get.

        :param name: Name of the device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Union[str, bool]]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[
            Literal[
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
        ] = None,
        device_types: Optional[
            List[
                Literal[
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
            ]
        ] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "avigilon_alta",
                "brivo",
                "butterflymx",
                "doorking",
                "four_suites",
                "genie",
                "igloo",
                "keywe",
                "kwikset",
                "linear",
                "nuki",
                "philia",
                "salto",
                "samsung",
                "schlage",
                "seam",
                "unknown",
                "wyze",
                "yale",
                "two_n",
                "ttlock",
                "igloohome",
                "controlbyweb",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "ecobee",
                "honeywell_resideo",
                "keynest",
                "korelock",
                "lockly",
                "minut",
                "nest",
                "noiseaware",
                "sensi",
                "smartthings",
                "tado",
                "ultraloq",
                "ring",
                "ical",
                "lodgify",
                "hostaway",
                "guesty",
                "acuity_scheduling",
                "omnitec",
                "kisi",
                "slack",
                "yacan",
            ]
        ] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[Union[str, Null]] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices. Key names cannot contain a period (.). Specify ``null`` to match a key that is unset. A key given an empty string is omitted from the filter.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :param space_id: ID of the space for which you want to list devices.

        :param unstable_location_id: Deprecated: Use ``space_id``.

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_device_providers(
        self,
        *,
        provider_category: Optional[
            Literal[
                "stable",
                "consumer_smartlocks",
                "beta",
                "thermostats",
                "noise_sensors",
                "access_control_systems",
                "cameras",
                "connectors",
            ]
        ] = None,
    ) -> List[DeviceProvider]:
        """Returns a list of all device providers.

        The information that this endpoint returns for each provider includes a set of `capability flags <https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags>`_, such as ``device_provider.can_remotely_unlock``. If at least one supported device from a provider has a specific capability, the corresponding capability flag is ``true``.

        When you create a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_, you can customize the providers—that is, the brands—that it displays. In the ``/connect_webviews/create`` request, include the desired set of device provider keys in the ``accepted_providers`` parameter. See also `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

        :param provider_category: Category for which you want to list providers.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def report_provider_metadata(self, *, devices: List[Dict[str, Any]]) -> None:
        """Updates provider-specific metadata for devices.

        :param devices: Array of devices with provider metadata to update

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        device_id: str,
        backup_access_code_pool_enabled: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[Union[str, Null]] = None,
        properties: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Updates a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You can add or change `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for a device, change the device's name, or `convert a managed device to unmanaged <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        :param device_id: ID of the device that you want to update.

        :param backup_access_code_pool_enabled: Indicates whether the device's `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is enabled. Set to ``false`` to disable the pool: Seam stops refilling it and removes any backup codes that have not yet been pulled into active use.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). `Adding custom metadata to a device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ enables you to store custom information, like customer details or internal IDs from your application. Then, you can `filter devices by the desired metadata <https://docs.seam.co/core-concepts/devices/filtering-devices-by-custom-metadata>`_. Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. To unmanage a device, set ``is_managed`` to ``false``.

        :param name: Name for the device.

        :param properties:

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncDevices(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAsyncDevicesSimulate:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAsyncDevicesUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the device that you want to get.

        :param name: Name of the device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Union[str, bool]]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[
            Literal[
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
        ] = None,
        device_types: Optional[
            List[
                Literal[
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
            ]
        ] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "avigilon_alta",
                "brivo",
                "butterflymx",
                "doorking",
                "four_suites",
                "genie",
                "igloo",
                "keywe",
                "kwikset",
                "linear",
                "nuki",
                "philia",
                "salto",
                "samsung",
                "schlage",
                "seam",
                "unknown",
                "wyze",
                "yale",
                "two_n",
                "ttlock",
                "igloohome",
                "controlbyweb",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "ecobee",
                "honeywell_resideo",
                "keynest",
                "korelock",
                "lockly",
                "minut",
                "nest",
                "noiseaware",
                "sensi",
                "smartthings",
                "tado",
                "ultraloq",
                "ring",
                "ical",
                "lodgify",
                "hostaway",
                "guesty",
                "acuity_scheduling",
                "omnitec",
                "kisi",
                "slack",
                "yacan",
            ]
        ] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[Union[str, Null]] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices. Key names cannot contain a period (.). Specify ``null`` to match a key that is unset. A key given an empty string is omitted from the filter.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :param space_id: ID of the space for which you want to list devices.

        :param unstable_location_id: Deprecated: Use ``space_id``.

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list_device_providers(
        self,
        *,
        provider_category: Optional[
            Literal[
                "stable",
                "consumer_smartlocks",
                "beta",
                "thermostats",
                "noise_sensors",
                "access_control_systems",
                "cameras",
                "connectors",
            ]
        ] = None,
    ) -> List[DeviceProvider]:
        """Returns a list of all device providers.

        The information that this endpoint returns for each provider includes a set of `capability flags <https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags>`_, such as ``device_provider.can_remotely_unlock``. If at least one supported device from a provider has a specific capability, the corresponding capability flag is ``true``.

        When you create a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_, you can customize the providers—that is, the brands—that it displays. In the ``/connect_webviews/create`` request, include the desired set of device provider keys in the ``accepted_providers`` parameter. See also `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

        :param provider_category: Category for which you want to list providers.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def report_provider_metadata(self, *, devices: List[Dict[str, Any]]) -> None:
        """Updates provider-specific metadata for devices.

        :param devices: Array of devices with provider metadata to update

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def update(
        self,
        *,
        device_id: str,
        backup_access_code_pool_enabled: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[Union[str, Null]] = None,
        properties: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Updates a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You can add or change `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for a device, change the device's name, or `convert a managed device to unmanaged <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        :param device_id: ID of the device that you want to update.

        :param backup_access_code_pool_enabled: Indicates whether the device's `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is enabled. Set to ``false`` to disable the pool: Seam stops refilling it and removes any backup codes that have not yet been pulled into active use.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). `Adding custom metadata to a device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ enables you to store custom information, like customer details or internal IDs from your application. Then, you can `filter devices by the desired metadata <https://docs.seam.co/core-concepts/devices/filtering-devices-by-custom-metadata>`_. Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. To unmanage a device, set ``is_managed`` to ``false``.

        :param name: Name for the device.

        :param properties:

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class Devices(AbstractDevices):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = DevicesSimulate(client=client, defaults=defaults)
        self._unmanaged = DevicesUnmanaged(client=client, defaults=defaults)

    @property
    def simulate(self) -> DevicesSimulate:
        return self._simulate

    @property
    def unmanaged(self) -> DevicesUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/devices/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the device that you want to get.

        :param name: Name of the device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError("At least one parameter is required for /devices/get")

        res = self.client.get("/devices/get", params=params)

        return Device.from_dict(unwrap(res, "device", "/devices/get"))

    @route_metadata(
        path="/devices/list", has_required_parameters=False, has_pagination=True
    )
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Union[str, bool]]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[
            Literal[
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
        ] = None,
        device_types: Optional[
            List[
                Literal[
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
            ]
        ] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "avigilon_alta",
                "brivo",
                "butterflymx",
                "doorking",
                "four_suites",
                "genie",
                "igloo",
                "keywe",
                "kwikset",
                "linear",
                "nuki",
                "philia",
                "salto",
                "samsung",
                "schlage",
                "seam",
                "unknown",
                "wyze",
                "yale",
                "two_n",
                "ttlock",
                "igloohome",
                "controlbyweb",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "ecobee",
                "honeywell_resideo",
                "keynest",
                "korelock",
                "lockly",
                "minut",
                "nest",
                "noiseaware",
                "sensi",
                "smartthings",
                "tado",
                "ultraloq",
                "ring",
                "ical",
                "lodgify",
                "hostaway",
                "guesty",
                "acuity_scheduling",
                "omnitec",
                "kisi",
                "slack",
                "yacan",
            ]
        ] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[Union[str, Null]] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices. Key names cannot contain a period (.). Specify ``null`` to match a key that is unset. A key given an empty string is omitted from the filter.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :param space_id: ID of the space for which you want to list devices.

        :param unstable_location_id: Deprecated: Use ``space_id``.

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            params["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            params["created_before"] = created_before
        if custom_metadata_has is not None:
            params["custom_metadata_has"] = custom_metadata_has
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_ids is not None:
            params["device_ids"] = device_ids
        if device_type is not None:
            params["device_type"] = device_type
        if device_types is not None:
            params["device_types"] = device_types
        if limit is not None:
            params["limit"] = limit
        if manufacturer is not None:
            params["manufacturer"] = manufacturer
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if space_id is not None:
            params["space_id"] = space_id
        if unstable_location_id is not None:
            params["unstable_location_id"] = unstable_location_id
        if user_identifier_key is not None:
            params["user_identifier_key"] = user_identifier_key

        res = self.client.get("/devices/list", params=params)

        return [
            Device.from_dict(item)
            for item in unwrap_list(res, "devices", "/devices/list")
        ]

    @route_metadata(
        path="/devices/list_device_providers",
        has_required_parameters=False,
        has_pagination=False,
    )
    def list_device_providers(
        self,
        *,
        provider_category: Optional[
            Literal[
                "stable",
                "consumer_smartlocks",
                "beta",
                "thermostats",
                "noise_sensors",
                "access_control_systems",
                "cameras",
                "connectors",
            ]
        ] = None,
    ) -> List[DeviceProvider]:
        """Returns a list of all device providers.

        The information that this endpoint returns for each provider includes a set of `capability flags <https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags>`_, such as ``device_provider.can_remotely_unlock``. If at least one supported device from a provider has a specific capability, the corresponding capability flag is ``true``.

        When you create a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_, you can customize the providers—that is, the brands—that it displays. In the ``/connect_webviews/create`` request, include the desired set of device provider keys in the ``accepted_providers`` parameter. See also `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

        :param provider_category: Category for which you want to list providers.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if provider_category is not None:
            params["provider_category"] = provider_category

        res = self.client.get("/devices/list_device_providers", params=params)

        return [
            DeviceProvider.from_dict(item)
            for item in unwrap_list(
                res, "device_providers", "/devices/list_device_providers"
            )
        ]

    @route_metadata(
        path="/devices/report_provider_metadata",
        has_required_parameters=True,
        has_pagination=False,
    )
    def report_provider_metadata(self, *, devices: List[Dict[str, Any]]) -> None:
        """Updates provider-specific metadata for devices.

        :param devices: Array of devices with provider metadata to update

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if devices is not None:
            json_payload["devices"] = devices

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /devices/report_provider_metadata"
            )

        self.client.post("/devices/report_provider_metadata", json=json_payload)

        return None

    @route_metadata(
        path="/devices/update", has_required_parameters=True, has_pagination=False
    )
    def update(
        self,
        *,
        device_id: str,
        backup_access_code_pool_enabled: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[Union[str, Null]] = None,
        properties: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Updates a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You can add or change `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for a device, change the device's name, or `convert a managed device to unmanaged <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        :param device_id: ID of the device that you want to update.

        :param backup_access_code_pool_enabled: Indicates whether the device's `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is enabled. Set to ``false`` to disable the pool: Seam stops refilling it and removes any backup codes that have not yet been pulled into active use.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). `Adding custom metadata to a device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ enables you to store custom information, like customer details or internal IDs from your application. Then, you can `filter devices by the desired metadata <https://docs.seam.co/core-concepts/devices/filtering-devices-by-custom-metadata>`_. Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. To unmanage a device, set ``is_managed`` to ``false``.

        :param name: Name for the device.

        :param properties:

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if backup_access_code_pool_enabled is not None:
            json_payload["backup_access_code_pool_enabled"] = (
                backup_access_code_pool_enabled
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if name is not None:
            json_payload["name"] = name
        if properties is not None:
            json_payload["properties"] = properties

        if not json_payload:
            raise ValueError("At least one parameter is required for /devices/update")

        self.client.patch("/devices/update", json=json_payload)

        return None


class AsyncDevices(AbstractAsyncDevices):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AsyncDevicesSimulate(client=client, defaults=defaults)
        self._unmanaged = AsyncDevicesUnmanaged(client=client, defaults=defaults)

    @property
    def simulate(self) -> AsyncDevicesSimulate:
        return self._simulate

    @property
    def unmanaged(self) -> AsyncDevicesUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/devices/get", has_required_parameters=True, has_pagination=False
    )
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the device that you want to get.

        :param name: Name of the device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError("At least one parameter is required for /devices/get")

        res = await self.client.get("/devices/get", params=params)

        return Device.from_dict(unwrap(res, "device", "/devices/get"))

    @route_metadata(
        path="/devices/list", has_required_parameters=False, has_pagination=True
    )
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Union[str, bool]]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[
            Literal[
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
        ] = None,
        device_types: Optional[
            List[
                Literal[
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
            ]
        ] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "avigilon_alta",
                "brivo",
                "butterflymx",
                "doorking",
                "four_suites",
                "genie",
                "igloo",
                "keywe",
                "kwikset",
                "linear",
                "nuki",
                "philia",
                "salto",
                "samsung",
                "schlage",
                "seam",
                "unknown",
                "wyze",
                "yale",
                "two_n",
                "ttlock",
                "igloohome",
                "controlbyweb",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "ecobee",
                "honeywell_resideo",
                "keynest",
                "korelock",
                "lockly",
                "minut",
                "nest",
                "noiseaware",
                "sensi",
                "smartthings",
                "tado",
                "ultraloq",
                "ring",
                "ical",
                "lodgify",
                "hostaway",
                "guesty",
                "acuity_scheduling",
                "omnitec",
                "kisi",
                "slack",
                "yacan",
            ]
        ] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[Union[str, Null]] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices. Key names cannot contain a period (.). Specify ``null`` to match a key that is unset. A key given an empty string is omitted from the filter.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :param space_id: ID of the space for which you want to list devices.

        :param unstable_location_id: Deprecated: Use ``space_id``.

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            params["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            params["created_before"] = created_before
        if custom_metadata_has is not None:
            params["custom_metadata_has"] = custom_metadata_has
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_ids is not None:
            params["device_ids"] = device_ids
        if device_type is not None:
            params["device_type"] = device_type
        if device_types is not None:
            params["device_types"] = device_types
        if limit is not None:
            params["limit"] = limit
        if manufacturer is not None:
            params["manufacturer"] = manufacturer
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if space_id is not None:
            params["space_id"] = space_id
        if unstable_location_id is not None:
            params["unstable_location_id"] = unstable_location_id
        if user_identifier_key is not None:
            params["user_identifier_key"] = user_identifier_key

        res = await self.client.get("/devices/list", params=params)

        return [
            Device.from_dict(item)
            for item in unwrap_list(res, "devices", "/devices/list")
        ]

    @route_metadata(
        path="/devices/list_device_providers",
        has_required_parameters=False,
        has_pagination=False,
    )
    async def list_device_providers(
        self,
        *,
        provider_category: Optional[
            Literal[
                "stable",
                "consumer_smartlocks",
                "beta",
                "thermostats",
                "noise_sensors",
                "access_control_systems",
                "cameras",
                "connectors",
            ]
        ] = None,
    ) -> List[DeviceProvider]:
        """Returns a list of all device providers.

        The information that this endpoint returns for each provider includes a set of `capability flags <https://docs.seam.co/capability-guides/device-and-system-capabilities#capability-flags>`_, such as ``device_provider.can_remotely_unlock``. If at least one supported device from a provider has a specific capability, the corresponding capability flag is ``true``.

        When you create a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_, you can customize the providers—that is, the brands—that it displays. In the ``/connect_webviews/create`` request, include the desired set of device provider keys in the ``accepted_providers`` parameter. See also `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

        :param provider_category: Category for which you want to list providers.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if provider_category is not None:
            params["provider_category"] = provider_category

        res = await self.client.get("/devices/list_device_providers", params=params)

        return [
            DeviceProvider.from_dict(item)
            for item in unwrap_list(
                res, "device_providers", "/devices/list_device_providers"
            )
        ]

    @route_metadata(
        path="/devices/report_provider_metadata",
        has_required_parameters=True,
        has_pagination=False,
    )
    async def report_provider_metadata(self, *, devices: List[Dict[str, Any]]) -> None:
        """Updates provider-specific metadata for devices.

        :param devices: Array of devices with provider metadata to update

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if devices is not None:
            json_payload["devices"] = devices

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /devices/report_provider_metadata"
            )

        await self.client.post("/devices/report_provider_metadata", json=json_payload)

        return None

    @route_metadata(
        path="/devices/update", has_required_parameters=True, has_pagination=False
    )
    async def update(
        self,
        *,
        device_id: str,
        backup_access_code_pool_enabled: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[Union[str, Null]] = None,
        properties: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Updates a specified `device <https://docs.seam.co/core-concepts/devices>`_.

        You can add or change `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for a device, change the device's name, or `convert a managed device to unmanaged <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        :param device_id: ID of the device that you want to update.

        :param backup_access_code_pool_enabled: Indicates whether the device's `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is enabled. Set to ``false`` to disable the pool: Seam stops refilling it and removes any backup codes that have not yet been pulled into active use.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). `Adding custom metadata to a device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ enables you to store custom information, like customer details or internal IDs from your application. Then, you can `filter devices by the desired metadata <https://docs.seam.co/core-concepts/devices/filtering-devices-by-custom-metadata>`_. Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. To unmanage a device, set ``is_managed`` to ``false``.

        :param name: Name for the device.

        :param properties:

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if backup_access_code_pool_enabled is not None:
            json_payload["backup_access_code_pool_enabled"] = (
                backup_access_code_pool_enabled
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if name is not None:
            json_payload["name"] = name
        if properties is not None:
            json_payload["properties"] = properties

        if not json_payload:
            raise ValueError("At least one parameter is required for /devices/update")

        await self.client.patch("/devices/update", json=json_payload)

        return None
