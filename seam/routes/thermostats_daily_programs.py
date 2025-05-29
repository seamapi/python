from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractThermostatsDailyPrograms, ActionAttempt

from ..modules.action_attempts import resolve_action_attempt


class ThermostatsDailyPrograms(AbstractThermostatsDailyPrograms):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self, *, device_id: str, name: str, periods: List[Dict[str, Any]]
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name
        if periods is not None:
            json_payload["periods"] = periods

        self.client.post("/thermostats/daily_programs/create", json=json_payload)

        return None

    def delete(self, *, thermostat_daily_program_id: str) -> None:
        json_payload = {}

        if thermostat_daily_program_id is not None:
            json_payload["thermostat_daily_program_id"] = thermostat_daily_program_id

        self.client.post("/thermostats/daily_programs/delete", json=json_payload)

        return None

    def update(
        self,
        *,
        name: str,
        periods: List[Dict[str, Any]],
        thermostat_daily_program_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if name is not None:
            json_payload["name"] = name
        if periods is not None:
            json_payload["periods"] = periods
        if thermostat_daily_program_id is not None:
            json_payload["thermostat_daily_program_id"] = thermostat_daily_program_id

        res = self.client.post("/thermostats/daily_programs/update", json=json_payload)

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
