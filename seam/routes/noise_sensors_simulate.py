from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..null import Null


class AbstractNoiseSensorsSimulate(abc.ABC):

    @abc.abstractmethod
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class NoiseSensorsSimulate(AbstractNoiseSensorsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(path="/noise_sensors/simulate/trigger_noise_threshold", has_required_parameters=True, has_pagination=False)
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /noise_sensors/simulate/trigger_noise_threshold")

        self.client.post("/noise_sensors/simulate/trigger_noise_threshold", json=json_payload)

        return None
