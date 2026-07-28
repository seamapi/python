from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedDevice


class AbstractDevicesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        You must specify either `device_id` or `name`.

        :param device_id: ID of the unmanaged device that you want to get.
        :type device_id: str

        :param name: Name of the unmanaged device that you want to get.
        :type name: str

        :returns: OK
        :rtype: UnmanagedDevice"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedDevice]:
        """Returns a list of all [unmanaged devices](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.
        :type connect_webview_id: str

        :param connected_account_id: ID of the connected account for which you want to list devices.
        :type connected_account_id: str

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.
        :type connected_account_ids: List[str]

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.
        :type created_before: str

        :param custom_metadata_has: Set of key:value [custom metadata](https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device) pairs for which you want to list devices.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key for which you want to list devices.
        :type customer_key: str

        :param device_ids: Array of device IDs for which you want to list devices.
        :type device_ids: List[str]

        :param device_type: Device type for which you want to list devices.
        :type device_type: str

        :param device_types: Array of device types for which you want to list devices.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturer for which you want to list devices.
        :type manufacturer: str

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using `device_id` (full or partial UUID prefix, minimum 4 characters), `connected_account_id`, `display_name`, `custom_metadata` or `location.location_name`.
        :type search: str

        :param space_id: ID of the space for which you want to list devices.
        :type space_id: str

        :param unstable_location_id: Deprecated: Use `space_id`.
        :type unstable_location_id: str

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[UnmanagedDevice]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None
    ) -> None:
        """Updates a specified [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices). To convert an unmanaged device to managed, set `is_managed` to `true`.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        :param device_id: ID of the unmanaged device that you want to update.
        :type device_id: str

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs.
        :type custom_metadata: Dict[str, Any]

        :param is_managed: Indicates whether the device is managed. Set this parameter to `true` to convert an unmanaged device to managed.
        :type is_managed: bool"""
        raise NotImplementedError()


class DevicesUnmanaged(AbstractDevicesUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        """Returns a specified [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        You must specify either `device_id` or `name`.

        :param device_id: ID of the unmanaged device that you want to get.
        :type device_id: str

        :param name: Name of the unmanaged device that you want to get.
        :type name: str

        :returns: OK
        :rtype: UnmanagedDevice"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post("/devices/unmanaged/get", json=json_payload)

        return UnmanagedDevice.from_dict(res["device"])

    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        unstable_location_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedDevice]:
        """Returns a list of all [unmanaged devices](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.
        :type connect_webview_id: str

        :param connected_account_id: ID of the connected account for which you want to list devices.
        :type connected_account_id: str

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.
        :type connected_account_ids: List[str]

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.
        :type created_before: str

        :param custom_metadata_has: Set of key:value [custom metadata](https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device) pairs for which you want to list devices.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key for which you want to list devices.
        :type customer_key: str

        :param device_ids: Array of device IDs for which you want to list devices.
        :type device_ids: List[str]

        :param device_type: Device type for which you want to list devices.
        :type device_type: str

        :param device_types: Array of device types for which you want to list devices.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturer for which you want to list devices.
        :type manufacturer: str

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using `device_id` (full or partial UUID prefix, minimum 4 characters), `connected_account_id`, `display_name`, `custom_metadata` or `location.location_name`.
        :type search: str

        :param space_id: ID of the space for which you want to list devices.
        :type space_id: str

        :param unstable_location_id: Deprecated: Use `space_id`.
        :type unstable_location_id: str

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[UnmanagedDevice]"""
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            json_payload["created_before"] = created_before
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if limit is not None:
            json_payload["limit"] = limit
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if space_id is not None:
            json_payload["space_id"] = space_id
        if unstable_location_id is not None:
            json_payload["unstable_location_id"] = unstable_location_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/devices/unmanaged/list", json=json_payload)

        return [UnmanagedDevice.from_dict(item) for item in res["devices"]]

    def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None
    ) -> None:
        """Updates a specified [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices). To convert an unmanaged device to managed, set `is_managed` to `true`.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).

        :param device_id: ID of the unmanaged device that you want to update.
        :type device_id: str

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs.
        :type custom_metadata: Dict[str, Any]

        :param is_managed: Indicates whether the device is managed. Set this parameter to `true` to convert an unmanaged device to managed.
        :type is_managed: bool"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        self.client.post("/devices/unmanaged/update", json=json_payload)

        return None
