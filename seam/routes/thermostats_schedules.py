from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import (ThermostatSchedule)


class AbstractThermostatsSchedules(abc.ABC):

    @abc.abstractmethod
    def create(self, *, climate_preset_key: str, device_id: str, ends_at: str, starts_at: str, is_override_allowed: Optional[bool] = None, max_override_period_minutes: Optional[Union[int, Null]] = None, name: Optional[str] = None) -> ThermostatSchedule:
        """Creates a new `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the new thermostat schedule.

        :param device_id: ID of the thermostat device for which you want to create a schedule.

        :param ends_at: Date and time at which the new thermostat schedule ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param starts_at: Date and time at which the new thermostat schedule starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param is_override_allowed: Indicates whether a person at the thermostat or using the API can change the thermostat's settings while the new schedule is active. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param max_override_period_minutes: Number of minutes for which a person at the thermostat or using the API can change the thermostat's settings after the activation of the scheduled climate preset. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: Name of the thermostat schedule.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, thermostat_schedule_id: str) -> None:
        """Deletes a `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, thermostat_schedule_id: str) -> ThermostatSchedule:
        """Returns a specified `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, device_id: str, user_identifier_key: Optional[str] = None) -> List[ThermostatSchedule]:
        """Returns a list of all `thermostat schedules <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to list schedules.

        :param user_identifier_key: User identifier key by which to filter the list of returned thermostat schedules.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, thermostat_schedule_id: str, climate_preset_key: Optional[str] = None, ends_at: Optional[str] = None, is_override_allowed: Optional[bool] = None, max_override_period_minutes: Optional[Union[int, Null]] = None, name: Optional[str] = None, starts_at: Optional[str] = None) -> None:
        """Updates a specified `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to update.

        :param climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the thermostat schedule.

        :param ends_at: Date and time at which the thermostat schedule ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param is_override_allowed: Indicates whether a person at the thermostat or using the API can change the thermostat's settings while the schedule is active. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param max_override_period_minutes: Number of minutes for which a person at the thermostat or using the API can change the thermostat's settings after the activation of the scheduled climate preset. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: Name of the thermostat schedule.

        :param starts_at: Date and time at which the thermostat schedule starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class ThermostatsSchedules(AbstractThermostatsSchedules):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(path="/thermostats/schedules/create", has_required_parameters=True, has_pagination=False)
    def create(self, *, climate_preset_key: str, device_id: str, ends_at: str, starts_at: str, is_override_allowed: Optional[bool] = None, max_override_period_minutes: Optional[Union[int, Null]] = None, name: Optional[str] = None) -> ThermostatSchedule:
        """Creates a new `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the new thermostat schedule.

        :param device_id: ID of the thermostat device for which you want to create a schedule.

        :param ends_at: Date and time at which the new thermostat schedule ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param starts_at: Date and time at which the new thermostat schedule starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param is_override_allowed: Indicates whether a person at the thermostat or using the API can change the thermostat's settings while the new schedule is active. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param max_override_period_minutes: Number of minutes for which a person at the thermostat or using the API can change the thermostat's settings after the activation of the scheduled climate preset. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: Name of the thermostat schedule.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if name is not None:
            json_payload["name"] = name

        if not json_payload:
            raise ValueError("At least one parameter is required for /thermostats/schedules/create")

        res = self.client.post("/thermostats/schedules/create", json=json_payload)

        return ThermostatSchedule.from_dict(res["thermostat_schedule"])

    @route_metadata(path="/thermostats/schedules/delete", has_required_parameters=True, has_pagination=False)
    def delete(self, *, thermostat_schedule_id: str) -> None:
        """Deletes a `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if thermostat_schedule_id is not None:
            params["thermostat_schedule_id"] = thermostat_schedule_id

        if not params:
            raise ValueError("At least one parameter is required for /thermostats/schedules/delete")

        self.client.delete("/thermostats/schedules/delete", params=params)

        return None

    @route_metadata(path="/thermostats/schedules/get", has_required_parameters=True, has_pagination=False)
    def get(self, *, thermostat_schedule_id: str) -> ThermostatSchedule:
        """Returns a specified `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if thermostat_schedule_id is not None:
            params["thermostat_schedule_id"] = thermostat_schedule_id

        if not params:
            raise ValueError("At least one parameter is required for /thermostats/schedules/get")

        res = self.client.get("/thermostats/schedules/get", params=params)

        return ThermostatSchedule.from_dict(res["thermostat_schedule"])

    @route_metadata(path="/thermostats/schedules/list", has_required_parameters=True, has_pagination=False)
    def list(self, *, device_id: str, user_identifier_key: Optional[str] = None) -> List[ThermostatSchedule]:
        """Returns a list of all `thermostat schedules <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to list schedules.

        :param user_identifier_key: User identifier key by which to filter the list of returned thermostat schedules.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id
        if user_identifier_key is not None:
            params["user_identifier_key"] = user_identifier_key

        if not params:
            raise ValueError("At least one parameter is required for /thermostats/schedules/list")

        res = self.client.get("/thermostats/schedules/list", params=params)

        return [ThermostatSchedule.from_dict(item) for item in res["thermostat_schedules"]]

    @route_metadata(path="/thermostats/schedules/update", has_required_parameters=True, has_pagination=False)
    def update(self, *, thermostat_schedule_id: str, climate_preset_key: Optional[str] = None, ends_at: Optional[str] = None, is_override_allowed: Optional[bool] = None, max_override_period_minutes: Optional[Union[int, Null]] = None, name: Optional[str] = None, starts_at: Optional[str] = None) -> None:
        """Updates a specified `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :param thermostat_schedule_id: ID of the thermostat schedule that you want to update.

        :param climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the thermostat schedule.

        :param ends_at: Date and time at which the thermostat schedule ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param is_override_allowed: Indicates whether a person at the thermostat or using the API can change the thermostat's settings while the schedule is active. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param max_override_period_minutes: Number of minutes for which a person at the thermostat or using the API can change the thermostat's settings after the activation of the scheduled climate preset. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: Name of the thermostat schedule.

        :param starts_at: Date and time at which the thermostat schedule starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if thermostat_schedule_id is not None:
            json_payload["thermostat_schedule_id"] = thermostat_schedule_id
        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_override_allowed is not None:
            json_payload["is_override_allowed"] = is_override_allowed
        if max_override_period_minutes is not None:
            json_payload["max_override_period_minutes"] = max_override_period_minutes
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        if not json_payload:
            raise ValueError("At least one parameter is required for /thermostats/schedules/update")

        self.client.patch("/thermostats/schedules/update", json=json_payload)

        return None
