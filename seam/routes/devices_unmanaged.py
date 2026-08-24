from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import UnmanagedDevice


class AbstractDevicesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the unmanaged device that you want to get.

        :param name: Name of the unmanaged device that you want to get.

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
    ) -> List[UnmanagedDevice]:
        """Returns a list of all `unmanaged devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[Literal[True]] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. Set this parameter to ``true`` to convert an unmanaged device to managed.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncDevicesUnmanaged(abc.ABC):

    @abc.abstractmethod
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the unmanaged device that you want to get.

        :param name: Name of the unmanaged device that you want to get.

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
    ) -> List[UnmanagedDevice]:
        """Returns a list of all `unmanaged devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[Literal[True]] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. Set this parameter to ``true`` to convert an unmanaged device to managed.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class DevicesUnmanaged(AbstractDevicesUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/devices/unmanaged/get",
        has_required_parameters=True,
        has_pagination=False,
    )
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the unmanaged device that you want to get.

        :param name: Name of the unmanaged device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/get"
            )

        res = self.client.get("/devices/unmanaged/get", params=params)

        return UnmanagedDevice.from_dict(res["device"])

    @route_metadata(
        path="/devices/unmanaged/list",
        has_required_parameters=False,
        has_pagination=True,
    )
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
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
    ) -> List[UnmanagedDevice]:
        """Returns a list of all `unmanaged devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

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

        res = self.client.get("/devices/unmanaged/list", params=params)

        return [UnmanagedDevice.from_dict(item) for item in res["devices"]]

    @route_metadata(
        path="/devices/unmanaged/update",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[Literal[True]] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. Set this parameter to ``true`` to convert an unmanaged device to managed.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/update"
            )

        self.client.patch("/devices/unmanaged/update", json=json_payload)

        return None


class AsyncDevicesUnmanaged(AbstractAsyncDevicesUnmanaged):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/devices/unmanaged/get",
        has_required_parameters=True,
        has_pagination=False,
    )
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        You must specify either ``device_id`` or ``name``.

        :param device_id: ID of the unmanaged device that you want to get.

        :param name: Name of the unmanaged device that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/get"
            )

        res = await self.client.get("/devices/unmanaged/get", params=params)

        return UnmanagedDevice.from_dict(res["device"])

    @route_metadata(
        path="/devices/unmanaged/list",
        has_required_parameters=False,
        has_pagination=True,
    )
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
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
    ) -> List[UnmanagedDevice]:
        """Returns a list of all `unmanaged devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.

        :param customer_key: Customer key for which you want to list devices.

        :param device_ids: Array of device IDs for which you want to list devices.

        :param device_type: Device type for which you want to list devices.

        :param device_types: Array of device types for which you want to list devices.

        :param limit: Numerical limit on the number of devices to return.

        :param manufacturer: Manufacturer for which you want to list devices.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.

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

        res = await self.client.get("/devices/unmanaged/list", params=params)

        return [UnmanagedDevice.from_dict(item) for item in res["devices"]]

    @route_metadata(
        path="/devices/unmanaged/update",
        has_required_parameters=True,
        has_pagination=False,
    )
    async def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Union[str, bool]]] = None,
        is_managed: Optional[Literal[True]] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs, with key names up to 40 characters long that cannot contain a period (.). Set a key to ``null`` or to an empty string to remove that key from the custom metadata.

        :param is_managed: Indicates whether the device is managed. Set this parameter to ``true`` to convert an unmanaged device to managed.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/update"
            )

        await self.client.patch("/devices/unmanaged/update", json=json_payload)

        return None
