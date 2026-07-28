from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ActionAttempt, Device
from .locks_simulate import AbstractLocksSimulate, LocksSimulate
from ..modules.action_attempts import resolve_action_attempt


class AbstractLocks(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractLocksSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def configure_auto_lock(
        self,
        *,
        auto_lock_enabled: bool,
        device_id: str,
        auto_lock_delay_seconds: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified [lock](https://docs.seam.co/low-level-apis/smart-locks).

        :param auto_lock_enabled: Whether to enable or disable auto-lock.
        :type auto_lock_enabled: bool

        :param device_id: ID of the lock for which you want to configure the auto-lock.
        :type device_id: str

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.
        :type auto_lock_delay_seconds: float

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified [lock](https://docs.seam.co/low-level-apis/smart-locks).

        :param device_id: ID of the lock that you want to get.
        :type device_id: str

        :param name: Name of the lock that you want to get.
        :type name: str

        :returns: OK
        :rtype: Device

        .. deprecated::
           Use `/devices/get` instead."""
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
        """Returns a list of all [locks](https://docs.seam.co/low-level-apis/smart-locks).

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

        :param device_type: Device type of the locks that you want to list.
        :type device_type: str

        :param device_types: Device types of the locks that you want to list.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturer of the locks that you want to list.
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
        :rtype: List[Device]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Locks a [lock](https://docs.seam.co/low-level-apis/smart-locks). See also [Locking and Unlocking Smart Locks](https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock).

        :param device_id: ID of the lock that you want to lock.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Unlocks a [lock](https://docs.seam.co/low-level-apis/smart-locks). See also [Locking and Unlocking Smart Locks](https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock).

        :param device_id: ID of the lock that you want to unlock.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()


class Locks(AbstractLocks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = LocksSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> LocksSimulate:
        return self._simulate

    def configure_auto_lock(
        self,
        *,
        auto_lock_enabled: bool,
        device_id: str,
        auto_lock_delay_seconds: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified [lock](https://docs.seam.co/low-level-apis/smart-locks).

        :param auto_lock_enabled: Whether to enable or disable auto-lock.
        :type auto_lock_enabled: bool

        :param device_id: ID of the lock for which you want to configure the auto-lock.
        :type device_id: str

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.
        :type auto_lock_delay_seconds: float

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        if auto_lock_enabled is not None:
            json_payload["auto_lock_enabled"] = auto_lock_enabled
        if device_id is not None:
            json_payload["device_id"] = device_id
        if auto_lock_delay_seconds is not None:
            json_payload["auto_lock_delay_seconds"] = auto_lock_delay_seconds

        res = self.client.post("/locks/configure_auto_lock", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified [lock](https://docs.seam.co/low-level-apis/smart-locks).

        :param device_id: ID of the lock that you want to get.
        :type device_id: str

        :param name: Name of the lock that you want to get.
        :type name: str

        :returns: OK
        :rtype: Device

        .. deprecated::
           Use `/devices/get` instead."""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post("/locks/get", json=json_payload)

        return Device.from_dict(res["device"])

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
        """Returns a list of all [locks](https://docs.seam.co/low-level-apis/smart-locks).

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

        :param device_type: Device type of the locks that you want to list.
        :type device_type: str

        :param device_types: Device types of the locks that you want to list.
        :type device_types: List[str]

        :param limit: Numerical limit on the number of devices to return.
        :type limit: float

        :param manufacturer: Manufacturer of the locks that you want to list.
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

        res = self.client.post("/locks/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]

    def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Locks a [lock](https://docs.seam.co/low-level-apis/smart-locks). See also [Locking and Unlocking Smart Locks](https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock).

        :param device_id: ID of the lock that you want to lock.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/locks/lock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Unlocks a [lock](https://docs.seam.co/low-level-apis/smart-locks). See also [Locking and Unlocking Smart Locks](https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock).

        :param device_id: ID of the lock that you want to unlock.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/locks/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
