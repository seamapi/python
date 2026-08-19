from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import ActionAttempt, Device
from .locks_simulate import (
    AbstractLocksSimulate,
    LocksSimulate,
    AbstractAsyncLocksSimulate,
    AsyncLocksSimulate,
)
from ..modules.action_attempts import (
    resolve_action_attempt,
    resolve_action_attempt_async,
)


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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param auto_lock_enabled: Whether to enable or disable auto-lock.

        :param device_id: ID of the lock for which you want to configure the auto-lock.

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param device_id: ID of the lock that you want to get.

        :param name: Name of the lock that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided.

        .. deprecated::
           Use ``/devices/get`` instead."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `locks <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the locks that you want to list.

        :param device_types: Device types of the locks that you want to list.

        :param manufacturer: Manufacturer of the locks that you want to list.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Locks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to lock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Unlocks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncLocks(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAsyncLocksSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    async def configure_auto_lock(
        self,
        *,
        auto_lock_enabled: bool,
        device_id: str,
        auto_lock_delay_seconds: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param auto_lock_enabled: Whether to enable or disable auto-lock.

        :param device_id: ID of the lock for which you want to configure the auto-lock.

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param device_id: ID of the lock that you want to get.

        :param name: Name of the lock that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided.

        .. deprecated::
           Use ``/devices/get`` instead."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `locks <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the locks that you want to list.

        :param device_types: Device types of the locks that you want to list.

        :param manufacturer: Manufacturer of the locks that you want to list.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Locks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to lock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Unlocks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class Locks(AbstractLocks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = LocksSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> LocksSimulate:
        return self._simulate

    @route_metadata(
        path="/locks/configure_auto_lock",
        has_required_parameters=True,
        has_pagination=False,
    )
    def configure_auto_lock(
        self,
        *,
        auto_lock_enabled: bool,
        device_id: str,
        auto_lock_delay_seconds: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param auto_lock_enabled: Whether to enable or disable auto-lock.

        :param device_id: ID of the lock for which you want to configure the auto-lock.

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if auto_lock_enabled is not None:
            json_payload["auto_lock_enabled"] = auto_lock_enabled
        if device_id is not None:
            json_payload["device_id"] = device_id
        if auto_lock_delay_seconds is not None:
            json_payload["auto_lock_delay_seconds"] = auto_lock_delay_seconds

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /locks/configure_auto_lock"
            )

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

    @route_metadata(
        path="/locks/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param device_id: ID of the lock that you want to get.

        :param name: Name of the lock that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided.

        .. deprecated::
           Use ``/devices/get`` instead."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError("At least one parameter is required for /locks/get")

        res = self.client.get("/locks/get", params=params)

        return Device.from_dict(res["device"])

    @route_metadata(
        path="/locks/list", has_required_parameters=False, has_pagination=False
    )
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `locks <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the locks that you want to list.

        :param device_types: Device types of the locks that you want to list.

        :param manufacturer: Manufacturer of the locks that you want to list.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_type is not None:
            params["device_type"] = device_type
        if device_types is not None:
            params["device_types"] = device_types
        if manufacturer is not None:
            params["manufacturer"] = manufacturer

        res = self.client.get("/locks/list", params=params)

        return [Device.from_dict(item) for item in res["devices"]]

    @route_metadata(
        path="/locks/lock_door", has_required_parameters=True, has_pagination=False
    )
    def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Locks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to lock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /locks/lock_door")

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

    @route_metadata(
        path="/locks/unlock_door", has_required_parameters=True, has_pagination=False
    )
    def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Unlocks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /locks/unlock_door"
            )

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


class AsyncLocks(AbstractAsyncLocks):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AsyncLocksSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> AsyncLocksSimulate:
        return self._simulate

    @route_metadata(
        path="/locks/configure_auto_lock",
        has_required_parameters=True,
        has_pagination=False,
    )
    async def configure_auto_lock(
        self,
        *,
        auto_lock_enabled: bool,
        device_id: str,
        auto_lock_delay_seconds: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Configures the auto-lock setting for a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param auto_lock_enabled: Whether to enable or disable auto-lock.

        :param device_id: ID of the lock for which you want to configure the auto-lock.

        :param auto_lock_delay_seconds: Delay in seconds before the lock automatically locks. Required when enabling auto-lock. Must be between 1 and 60.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if auto_lock_enabled is not None:
            json_payload["auto_lock_enabled"] = auto_lock_enabled
        if device_id is not None:
            json_payload["device_id"] = device_id
        if auto_lock_delay_seconds is not None:
            json_payload["auto_lock_delay_seconds"] = auto_lock_delay_seconds

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /locks/configure_auto_lock"
            )

        res = await self.client.post("/locks/configure_auto_lock", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/get", has_required_parameters=True, has_pagination=False
    )
    async def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        """Returns a specified `lock <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param device_id: ID of the lock that you want to get.

        :param name: Name of the lock that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided.

        .. deprecated::
           Use ``/devices/get`` instead."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if name is not None:
            params["name"] = name

        if not params:
            raise ValueError("At least one parameter is required for /locks/get")

        res = await self.client.get("/locks/get", params=params)

        return Device.from_dict(res["device"])

    @route_metadata(
        path="/locks/list", has_required_parameters=False, has_pagination=False
    )
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `locks <https://docs.seam.co/low-level-apis/smart-locks>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the locks that you want to list.

        :param device_types: Device types of the locks that you want to list.

        :param manufacturer: Manufacturer of the locks that you want to list.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_type is not None:
            params["device_type"] = device_type
        if device_types is not None:
            params["device_types"] = device_types
        if manufacturer is not None:
            params["manufacturer"] = manufacturer

        res = await self.client.get("/locks/list", params=params)

        return [Device.from_dict(item) for item in res["devices"]]

    @route_metadata(
        path="/locks/lock_door", has_required_parameters=True, has_pagination=False
    )
    async def lock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Locks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to lock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /locks/lock_door")

        res = await self.client.post("/locks/lock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/unlock_door", has_required_parameters=True, has_pagination=False
    )
    async def unlock_door(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Unlocks a `lock <https://docs.seam.co/low-level-apis/smart-locks>`_. See also `Locking and Unlocking Smart Locks <https://docs.seam.co/low-level-apis/smart-locks/lock-and-unlock>`_.

        :param device_id: ID of the lock that you want to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /locks/unlock_door"
            )

        res = await self.client.post("/locks/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
