from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractDevicesSimulate(abc.ABC):

    @abc.abstractmethod
    def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        :type device_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect.
        :type device_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        :type device_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect.
        :type device_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:
        :type device_id: str

        :param is_expired:
        :type is_expired: bool"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        :type device_id: str"""
        raise NotImplementedError()


class DevicesSimulate(AbstractDevicesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def connect(self, *, device_id: str) -> None:
        """Simulates connecting a device to Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate connecting to Seam.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect", json=json_payload)

        return None

    def connect_to_hub(self, *, device_id: str) -> None:
        """Simulates bringing the Wi‑Fi hub (bridge) back online for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August and TTLock locks.
        This will clear the ``hub_disconnected`` error on the device.

        :param device_id: ID of the device whose hub you want to reconnect.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/connect_to_hub", json=json_payload)

        return None

    def disconnect(self, *, device_id: str) -> None:
        """Simulates disconnecting a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate disconnecting from Seam.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect", json=json_payload)

        return None

    def disconnect_from_hub(self, *, device_id: str) -> None:
        """Simulates taking the Wi‑Fi hub (bridge) offline for a device.
        Only applicable for sandbox workspaces and currently
        implemented for August, TTLock, and IglooHome devices.
        This will set the ``hub_disconnected`` error on the device, or mark the
        IglooHome bridge offline in sandbox.

        :param device_id: ID of the device whose hub you want to disconnect.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/disconnect_from_hub", json=json_payload)

        return None

    def paid_subscription(self, *, device_id: str, is_expired: bool) -> None:
        """Toggle the simulated Nuki Smart Hosting subscription for a device (sandbox only).
        Send ``is_expired: true`` to simulate an expired subscription, or ``false`` to simulate an active subscription.
        The actual device error is created/cleared by the poller after this state change.

        :param device_id:
        :type device_id: str

        :param is_expired:
        :type is_expired: bool"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_expired is not None:
            json_payload["is_expired"] = is_expired

        self.client.post("/devices/simulate/paid_subscription", json=json_payload)

        return None

    def remove(self, *, device_id: str) -> None:
        """Simulates removing a device from Seam. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your App Against Device Disconnection and Removal <https://docs.seam.co/core-concepts/devices/testing-your-app-against-device-disconnection-and-removal>`_.

        :param device_id: ID of the device that you want to simulate removing from Seam.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/simulate/remove", json=json_payload)

        return None
