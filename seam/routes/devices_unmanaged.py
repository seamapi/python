from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
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
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        page_cursor: Optional[str] = None,
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
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs.

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
        if not any([device_id is not None, name is not None]):
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/get"
            )
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

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
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        page_cursor: Optional[str] = None,
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
        json_payload: Dict[str, Any] = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            json_payload["created_before"] = created_before
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

        res = self.client.post("/devices/unmanaged/list", json=json_payload)

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
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None,
    ) -> None:
        """Updates a specified `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. To convert an unmanaged device to managed, set ``is_managed`` to ``true``.

        An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ on an unmanaged device are unmanaged. To control an unmanaged device with Seam, `convert it to a managed device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed>`_.

        :param device_id: ID of the unmanaged device that you want to update.

        :param custom_metadata: Custom metadata that you want to associate with the device. Supports up to 50 JSON key:value pairs.

        :param is_managed: Indicates whether the device is managed. Set this parameter to ``true`` to convert an unmanaged device to managed.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [device_id is not None, custom_metadata is not None, is_managed is not None]
        ):
            raise ValueError(
                "At least one parameter is required for /devices/unmanaged/update"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        self.client.patch("/devices/unmanaged/update", json=json_payload)

        return None
