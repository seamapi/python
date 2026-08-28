from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import ActionAttempt, Device, action_attempt_from_dict
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
from ..response import unwrap
from ..response import unwrap_list


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

        :returns: OK"""
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
                ]
            ]
        ] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "brivo",
                "butterflymx",
                "avigilon_alta",
                "doorking",
                "genie",
                "igloo",
                "linear",
                "kwikset",
                "nuki",
                "salto",
                "schlage",
                "seam",
                "wyze",
                "yale",
                "two_n",
                "controlbyweb",
                "ttlock",
                "igloohome",
                "four_suites",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "korelock",
                "lockly",
                "smartthings",
                "ultraloq",
                "omnitec",
                "kisi",
                "yacan",
            ]
        ] = None,
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

        :returns: OK"""
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

        :returns: OK"""
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

        :returns: OK"""
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
                ]
            ]
        ] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "brivo",
                "butterflymx",
                "avigilon_alta",
                "doorking",
                "genie",
                "igloo",
                "linear",
                "kwikset",
                "nuki",
                "salto",
                "schlage",
                "seam",
                "wyze",
                "yale",
                "two_n",
                "controlbyweb",
                "ttlock",
                "igloohome",
                "four_suites",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "korelock",
                "lockly",
                "smartthings",
                "ultraloq",
                "omnitec",
                "kisi",
                "yacan",
            ]
        ] = None,
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

        :returns: OK"""
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

        :returns: OK"""
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
        at_least_one_parameter_names=(),
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

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
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/configure_auto_lock")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/get",
        at_least_one_parameter_names=(
            "device_id",
            "name",
        ),
        has_pagination=False,
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

        if all(
            param is None
            for param in (
                device_id,
                name,
            )
        ):
            raise ValueError("At least one parameter is required for /locks/get")

        res = self.client.get("/locks/get", params=params)

        return Device.from_dict(unwrap(res, "device", "/locks/get"))

    @route_metadata(
        path="/locks/list", at_least_one_parameter_names=(), has_pagination=False
    )
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
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
                ]
            ]
        ] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "brivo",
                "butterflymx",
                "avigilon_alta",
                "doorking",
                "genie",
                "igloo",
                "linear",
                "kwikset",
                "nuki",
                "salto",
                "schlage",
                "seam",
                "wyze",
                "yale",
                "two_n",
                "controlbyweb",
                "ttlock",
                "igloohome",
                "four_suites",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "korelock",
                "lockly",
                "smartthings",
                "ultraloq",
                "omnitec",
                "kisi",
                "yacan",
            ]
        ] = None,
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

        return [
            Device.from_dict(item)
            for item in unwrap_list(res, "devices", "/locks/list")
        ]

    @route_metadata(
        path="/locks/lock_door", at_least_one_parameter_names=(), has_pagination=False
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

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
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/lock_door")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/unlock_door", at_least_one_parameter_names=(), has_pagination=False
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

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
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/unlock_door")
            ),
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
        at_least_one_parameter_names=(),
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if auto_lock_enabled is not None:
            json_payload["auto_lock_enabled"] = auto_lock_enabled
        if device_id is not None:
            json_payload["device_id"] = device_id
        if auto_lock_delay_seconds is not None:
            json_payload["auto_lock_delay_seconds"] = auto_lock_delay_seconds

        res = await self.client.post("/locks/configure_auto_lock", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/configure_auto_lock")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/get",
        at_least_one_parameter_names=(
            "device_id",
            "name",
        ),
        has_pagination=False,
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

        if all(
            param is None
            for param in (
                device_id,
                name,
            )
        ):
            raise ValueError("At least one parameter is required for /locks/get")

        res = await self.client.get("/locks/get", params=params)

        return Device.from_dict(unwrap(res, "device", "/locks/get"))

    @route_metadata(
        path="/locks/list", at_least_one_parameter_names=(), has_pagination=False
    )
    async def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
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
                ]
            ]
        ] = None,
        manufacturer: Optional[
            Literal[
                "akuvox",
                "august",
                "brivo",
                "butterflymx",
                "avigilon_alta",
                "doorking",
                "genie",
                "igloo",
                "linear",
                "kwikset",
                "nuki",
                "salto",
                "schlage",
                "seam",
                "wyze",
                "yale",
                "two_n",
                "controlbyweb",
                "ttlock",
                "igloohome",
                "four_suites",
                "dormakaba_oracode",
                "tedee",
                "keyincode",
                "akiles",
                "aqara",
                "korelock",
                "lockly",
                "smartthings",
                "ultraloq",
                "omnitec",
                "kisi",
                "yacan",
            ]
        ] = None,
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

        return [
            Device.from_dict(item)
            for item in unwrap_list(res, "devices", "/locks/list")
        ]

    @route_metadata(
        path="/locks/lock_door", at_least_one_parameter_names=(), has_pagination=False
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = await self.client.post("/locks/lock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/lock_door")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/locks/unlock_door", at_least_one_parameter_names=(), has_pagination=False
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

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = await self.client.post("/locks/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/locks/unlock_door")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )
