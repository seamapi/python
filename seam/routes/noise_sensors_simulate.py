from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata


class AbstractNoiseSensorsSimulate(abc.ABC):

    @abc.abstractmethod
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        """
        raise NotImplementedError()


class AbstractAsyncNoiseSensorsSimulate(abc.ABC):

    @abc.abstractmethod
    async def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        """
        raise NotImplementedError()


class NoiseSensorsSimulate(AbstractNoiseSensorsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/noise_sensors/simulate/trigger_noise_threshold",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post(
            "/noise_sensors/simulate/trigger_noise_threshold", json=json_payload
        )

        return None


class AsyncNoiseSensorsSimulate(AbstractAsyncNoiseSensorsSimulate):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/noise_sensors/simulate/trigger_noise_threshold",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def trigger_noise_threshold(self, *, device_id: str) -> None:
        """Simulates the triggering of a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param device_id: ID of the device for which you want to simulate the triggering of a noise threshold.
        """
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        await self.client.post(
            "/noise_sensors/simulate/trigger_noise_threshold", json=json_payload
        )

        return None
