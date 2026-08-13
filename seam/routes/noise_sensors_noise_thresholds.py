from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import NoiseThreshold


class AbstractNoiseSensorsNoiseThresholds(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        ends_daily_at: str,
        starts_daily_at: str,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
    ) -> NoiseThreshold:
        """Creates a new `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_. Thresholds represent the limits of noise tolerated at a property, which can be customized for each hour of the day. Each device has its own default thresholds, but you can use the Seam API to modify them.

        :param device_id: ID of the device for which you want to create a noise threshold.

        :param ends_daily_at: Time at which the new noise threshold should become inactive daily.

        :param starts_daily_at: Time at which the new noise threshold should become active daily.

        :param name: Name of the new noise threshold.

        :param noise_threshold_decibels: Noise level in decibels for the new noise threshold.

        :param noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the new noise threshold. This parameter is only relevant for `Noiseaware sensors <https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors>`_.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, device_id: str, noise_threshold_id: str) -> None:
        """Deletes a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ from a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device that contains the noise threshold that you want to delete.

        :param noise_threshold_id: ID of the noise threshold that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, noise_threshold_id: str) -> NoiseThreshold:
        """Returns a specified `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param noise_threshold_id: ID of the noise threshold that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, device_id: str) -> List[NoiseThreshold]:
        """Returns a list of all `noise thresholds <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device for which you want to list noise thresholds.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        device_id: str,
        noise_threshold_id: str,
        ends_daily_at: Optional[str] = None,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
        starts_daily_at: Optional[str] = None,
    ) -> None:
        """Updates a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device that contains the noise threshold that you want to update.

        :param noise_threshold_id: ID of the noise threshold that you want to update.

        :param ends_daily_at: Time at which the noise threshold should become inactive daily.

        :param name: Name of the noise threshold that you want to update.

        :param noise_threshold_decibels: Noise level in decibels for the noise threshold.

        :param noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the noise threshold. This parameter is only relevant for `Noiseaware sensors <https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors>`_.

        :param starts_daily_at: Time at which the noise threshold should become active daily.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class NoiseSensorsNoiseThresholds(AbstractNoiseSensorsNoiseThresholds):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/noise_sensors/noise_thresholds/create",
        has_required_parameters=True,
        has_pagination=False,
    )
    def create(
        self,
        *,
        device_id: str,
        ends_daily_at: str,
        starts_daily_at: str,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
    ) -> NoiseThreshold:
        """Creates a new `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_. Thresholds represent the limits of noise tolerated at a property, which can be customized for each hour of the day. Each device has its own default thresholds, but you can use the Seam API to modify them.

        :param device_id: ID of the device for which you want to create a noise threshold.

        :param ends_daily_at: Time at which the new noise threshold should become inactive daily.

        :param starts_daily_at: Time at which the new noise threshold should become active daily.

        :param name: Name of the new noise threshold.

        :param noise_threshold_decibels: Noise level in decibels for the new noise threshold.

        :param noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the new noise threshold. This parameter is only relevant for `Noiseaware sensors <https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors>`_.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                ends_daily_at is not None,
                starts_daily_at is not None,
                name is not None,
                noise_threshold_decibels is not None,
                noise_threshold_nrs is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /noise_sensors/noise_thresholds/create"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if ends_daily_at is not None:
            json_payload["ends_daily_at"] = ends_daily_at
        if starts_daily_at is not None:
            json_payload["starts_daily_at"] = starts_daily_at
        if name is not None:
            json_payload["name"] = name
        if noise_threshold_decibels is not None:
            json_payload["noise_threshold_decibels"] = noise_threshold_decibels
        if noise_threshold_nrs is not None:
            json_payload["noise_threshold_nrs"] = noise_threshold_nrs

        res = self.client.post(
            "/noise_sensors/noise_thresholds/create", json=json_payload
        )

        return NoiseThreshold.from_dict(res["noise_threshold"])

    @route_metadata(
        path="/noise_sensors/noise_thresholds/delete",
        has_required_parameters=True,
        has_pagination=False,
    )
    def delete(self, *, device_id: str, noise_threshold_id: str) -> None:
        """Deletes a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ from a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device that contains the noise threshold that you want to delete.

        :param noise_threshold_id: ID of the noise threshold that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        if not any([device_id is not None, noise_threshold_id is not None]):
            raise ValueError(
                "At least one parameter is required for /noise_sensors/noise_thresholds/delete"
            )
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if noise_threshold_id is not None:
            params["noise_threshold_id"] = noise_threshold_id

        self.client.delete("/noise_sensors/noise_thresholds/delete", params=params)

        return None

    @route_metadata(
        path="/noise_sensors/noise_thresholds/get",
        has_required_parameters=True,
        has_pagination=False,
    )
    def get(self, *, noise_threshold_id: str) -> NoiseThreshold:
        """Returns a specified `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param noise_threshold_id: ID of the noise threshold that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any([noise_threshold_id is not None]):
            raise ValueError(
                "At least one parameter is required for /noise_sensors/noise_thresholds/get"
            )
        params: Dict[str, Any] = {}

        if noise_threshold_id is not None:
            params["noise_threshold_id"] = noise_threshold_id

        res = self.client.get("/noise_sensors/noise_thresholds/get", params=params)

        return NoiseThreshold.from_dict(res["noise_threshold"])

    @route_metadata(
        path="/noise_sensors/noise_thresholds/list",
        has_required_parameters=True,
        has_pagination=False,
    )
    def list(self, *, device_id: str) -> List[NoiseThreshold]:
        """Returns a list of all `noise thresholds <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device for which you want to list noise thresholds.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any([device_id is not None]):
            raise ValueError(
                "At least one parameter is required for /noise_sensors/noise_thresholds/list"
            )
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id

        res = self.client.get("/noise_sensors/noise_thresholds/list", params=params)

        return [NoiseThreshold.from_dict(item) for item in res["noise_thresholds"]]

    @route_metadata(
        path="/noise_sensors/noise_thresholds/update",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update(
        self,
        *,
        device_id: str,
        noise_threshold_id: str,
        ends_daily_at: Optional[str] = None,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None,
        starts_daily_at: Optional[str] = None,
    ) -> None:
        """Updates a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_.

        :param device_id: ID of the device that contains the noise threshold that you want to update.

        :param noise_threshold_id: ID of the noise threshold that you want to update.

        :param ends_daily_at: Time at which the noise threshold should become inactive daily.

        :param name: Name of the noise threshold that you want to update.

        :param noise_threshold_decibels: Noise level in decibels for the noise threshold.

        :param noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the noise threshold. This parameter is only relevant for `Noiseaware sensors <https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors>`_.

        :param starts_daily_at: Time at which the noise threshold should become active daily.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                noise_threshold_id is not None,
                ends_daily_at is not None,
                name is not None,
                noise_threshold_decibels is not None,
                noise_threshold_nrs is not None,
                starts_daily_at is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /noise_sensors/noise_thresholds/update"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if noise_threshold_id is not None:
            json_payload["noise_threshold_id"] = noise_threshold_id
        if ends_daily_at is not None:
            json_payload["ends_daily_at"] = ends_daily_at
        if name is not None:
            json_payload["name"] = name
        if noise_threshold_decibels is not None:
            json_payload["noise_threshold_decibels"] = noise_threshold_decibels
        if noise_threshold_nrs is not None:
            json_payload["noise_threshold_nrs"] = noise_threshold_nrs
        if starts_daily_at is not None:
            json_payload["starts_daily_at"] = starts_daily_at

        self.client.put("/noise_sensors/noise_thresholds/update", json=json_payload)

        return None
