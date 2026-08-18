from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
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
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `noise sensors <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the noise sensors that you want to list.

        :param device_types: Device types of the noise sensors that you want to list.

        :param manufacturer: Manufacturers of the noise sensors that you want to list.

        :returns: OK"""
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

    @route_metadata(
        path="/noise_sensors/list", has_required_parameters=False, has_pagination=False
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
        """Returns a list of all `noise sensors <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type of the noise sensors that you want to list.

        :param device_types: Device types of the noise sensors that you want to list.

        :param manufacturer: Manufacturers of the noise sensors that you want to list.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer

        res = self.client.post("/noise_sensors/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]
