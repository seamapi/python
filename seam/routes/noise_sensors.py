from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Device
from .noise_sensors_noise_thresholds import (
    AbstractNoiseSensorsNoiseThresholds,
    NoiseSensorsNoiseThresholds,
)
from .noise_sensors_simulate import AbstractNoiseSensorsSimulate, NoiseSensorsSimulate


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
    ) -> List[Device]:
        """Returns a list of all `noise sensors <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.
        :type connect_webview_id: str

        :param connected_account_id: ID of the connected account for which you want to list devices.
        :type connected_account_id: str

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.
        :type connected_account_ids: List[str]

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.
        :type created_before: str

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key for which you want to list devices.
        :type customer_key: str

        :param device_ids: Array of device IDs for which you want to list devices.
        :type device_ids: List[str]

        :param device_type: Device type of the noise sensors that you want to list.
        :type device_type: str

        :param device_types: Device types of the noise sensors that you want to list.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturers of the noise sensors that you want to list.
        :type manufacturer: str

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.
        :type page_cursor: str

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.
        :type search: str

        :param space_id: ID of the space for which you want to list devices.
        :type space_id: str

        :param unstable_location_id: Deprecated: Use ``space_id``.
        :type unstable_location_id: str

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[Device]"""
        raise NotImplementedError()


class NoiseSensors(AbstractNoiseSensors):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._noise_thresholds = NoiseSensorsNoiseThresholds(
            client=client, defaults=defaults
        )
        self._simulate = NoiseSensorsSimulate(client=client, defaults=defaults)

    @property
    def noise_thresholds(self) -> NoiseSensorsNoiseThresholds:
        return self._noise_thresholds

    @property
    def simulate(self) -> NoiseSensorsSimulate:
        return self._simulate

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
    ) -> List[Device]:
        """Returns a list of all `noise sensors <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.
        :type connect_webview_id: str

        :param connected_account_id: ID of the connected account for which you want to list devices.
        :type connected_account_id: str

        :param connected_account_ids: Array of IDs of the connected accounts for which you want to list devices.
        :type connected_account_ids: List[str]

        :param created_before: Timestamp by which to limit returned devices. Returns devices created before this timestamp.
        :type created_before: str

        :param custom_metadata_has: Set of key:value `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ pairs for which you want to list devices.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key for which you want to list devices.
        :type customer_key: str

        :param device_ids: Array of device IDs for which you want to list devices.
        :type device_ids: List[str]

        :param device_type: Device type of the noise sensors that you want to list.
        :type device_type: str

        :param device_types: Device types of the noise sensors that you want to list.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturers of the noise sensors that you want to list.
        :type manufacturer: str

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.
        :type page_cursor: str

        :param search: String for which to search. Filters returned devices to include all records that satisfy a partial match using ``device_id`` (full or partial UUID prefix, minimum 4 characters), ``connected_account_id``, ``display_name``, ``custom_metadata`` or ``location.location_name``.
        :type search: str

        :param space_id: ID of the space for which you want to list devices.
        :type space_id: str

        :param unstable_location_id: Deprecated: Use ``space_id``.
        :type unstable_location_id: str

        :param user_identifier_key: Your own internal user ID for the user for which you want to list devices.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[Device]"""
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

        res = self.client.post("/noise_sensors/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]
