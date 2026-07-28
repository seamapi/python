from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractNoiseSensorsSimulate(abc.ABC):

    @abc.abstractmethod
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        :type device_id: str"""
        raise NotImplementedError()


class NoiseSensorsSimulate(AbstractNoiseSensorsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        :type device_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post(
            "/noise_sensors/simulate/trigger_noise_threshold", json=json_payload
        )

        return None
