from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import ThermostatDailyProgram, ActionAttempt
from ..modules.action_attempts import resolve_action_attempt


class AbstractThermostatsDailyPrograms(abc.ABC):

    @abc.abstractmethod
    def create(
        self, *, device_id: str, name: str, periods: List[Dict[str, Any]]
    ) -> ThermostatDailyProgram:
        """Creates a new thermostat daily program. A daily program consists of a set of periods, where each period includes a start time and the key of a configured climate preset. Once you have defined a daily program, you can assign it to one or more days within a weekly program.

        :param device_id: ID of the thermostat device for which you want to create a daily program.

        :param name: Name of the thermostat daily program.

        :param periods: Array of thermostat daily program periods.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, thermostat_daily_program_id: str) -> None:
        """Deletes a thermostat daily program.

        :param thermostat_daily_program_id: ID of the thermostat daily program that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        name: str,
        periods: List[Dict[str, Any]],
        thermostat_daily_program_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Updates a specified thermostat daily program. The periods that you specify overwrite any existing periods for the daily program.

        :param name: Name of the thermostat daily program that you want to update.

        :param periods: Array of thermostat daily program periods. The periods that you specify overwrite any existing periods for the daily program.

        :param thermostat_daily_program_id: ID of the thermostat daily program that you want to update.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class ThermostatsDailyPrograms(AbstractThermostatsDailyPrograms):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/thermostats/daily_programs/create",
        has_required_parameters=True,
        has_pagination=False,
    )
    def create(
        self, *, device_id: str, name: str, periods: List[Dict[str, Any]]
    ) -> ThermostatDailyProgram:
        """Creates a new thermostat daily program. A daily program consists of a set of periods, where each period includes a start time and the key of a configured climate preset. Once you have defined a daily program, you can assign it to one or more days within a weekly program.

        :param device_id: ID of the thermostat device for which you want to create a daily program.

        :param name: Name of the thermostat daily program.

        :param periods: Array of thermostat daily program periods.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name
        if periods is not None:
            json_payload["periods"] = periods

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /thermostats/daily_programs/create"
            )

        res = self.client.post("/thermostats/daily_programs/create", json=json_payload)

        return ThermostatDailyProgram.from_dict(res["thermostat_daily_program"])

    @route_metadata(
        path="/thermostats/daily_programs/delete",
        has_required_parameters=True,
        has_pagination=False,
    )
    def delete(self, *, thermostat_daily_program_id: str) -> None:
        """Deletes a thermostat daily program.

        :param thermostat_daily_program_id: ID of the thermostat daily program that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if thermostat_daily_program_id is not None:
            params["thermostat_daily_program_id"] = thermostat_daily_program_id

        if not params:
            raise ValueError(
                "At least one parameter is required for /thermostats/daily_programs/delete"
            )

        self.client.delete("/thermostats/daily_programs/delete", params=params)

        return None

    @route_metadata(
        path="/thermostats/daily_programs/update",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update(
        self,
        *,
        name: str,
        periods: List[Dict[str, Any]],
        thermostat_daily_program_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Updates a specified thermostat daily program. The periods that you specify overwrite any existing periods for the daily program.

        :param name: Name of the thermostat daily program that you want to update.

        :param periods: Array of thermostat daily program periods. The periods that you specify overwrite any existing periods for the daily program.

        :param thermostat_daily_program_id: ID of the thermostat daily program that you want to update.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if name is not None:
            json_payload["name"] = name
        if periods is not None:
            json_payload["periods"] = periods
        if thermostat_daily_program_id is not None:
            json_payload["thermostat_daily_program_id"] = thermostat_daily_program_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /thermostats/daily_programs/update"
            )

        res = self.client.patch("/thermostats/daily_programs/update", json=json_payload)

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
