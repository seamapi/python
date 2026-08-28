from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata


class AbstractDevicesSimulate(abc.ABC):

    @abc.abstractmethod
    def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect."""
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect."""
        raise NotImplementedError()

    @abc.abstractmethod
    def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:

        :param is_expired:"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        """
        raise NotImplementedError()


class AbstractAsyncDevicesSimulate(abc.ABC):

    @abc.abstractmethod
    async def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:

        :param is_expired:"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        """
        raise NotImplementedError()


class DevicesSimulate(AbstractDevicesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/devices/simulate/connect",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/connect_to_hub",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect_to_hub", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/disconnect",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/disconnect_from_hub",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect_from_hub", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/paid_subscription",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:

        :param is_expired:"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_expired is not None:
            json_payload["is_expired"] = is_expired

        self.client.post("/devices/simulate/paid_subscription", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/remove",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/remove", json=json_payload)

        return None


class AsyncDevicesSimulate(AbstractAsyncDevicesSimulate):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/devices/simulate/connect",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post("/devices/simulate/connect", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/connect_to_hub",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post("/devices/simulate/connect_to_hub", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/disconnect",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post("/devices/simulate/disconnect", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/disconnect_from_hub",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post(
            "/devices/simulate/disconnect_from_hub", json=json_payload
        )

        return None

    @route_metadata(
        path="/devices/simulate/paid_subscription",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:

        :param is_expired:"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_expired is not None:
            json_payload["is_expired"] = is_expired

        await self.client.post("/devices/simulate/paid_subscription", json=json_payload)

        return None

    @route_metadata(
        path="/devices/simulate/remove",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post("/devices/simulate/remove", json=json_payload)

        return None
