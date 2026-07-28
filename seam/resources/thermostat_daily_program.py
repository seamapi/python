from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ThermostatDailyProgram:
    """Represents a thermostat daily program, consisting of a set of periods, each of which has a starting time and the key that identifies the climate preset to apply at the starting time.

    :ivar created_at: Date and time at which the thermostat daily program was created.
    :vartype created_at: str

    :ivar device_id: ID of the thermostat device on which the thermostat daily program is configured.
    :vartype device_id: str

    :ivar name: User-friendly name to identify the thermostat daily program.
    :vartype name: str

    :ivar periods: Array of thermostat daily program periods.
    :vartype periods: List[Dict[str, Any]]

    :ivar thermostat_daily_program_id: ID of the thermostat daily program.
    :vartype thermostat_daily_program_id: str

    :ivar workspace_id: ID of the workspace that contains the thermostat daily program.
    :vartype workspace_id: str"""

    created_at: str
    device_id: str
    name: str
    periods: List[Dict[str, Any]]
    thermostat_daily_program_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatDailyProgram(
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            periods=d.get("periods", None),
            thermostat_daily_program_id=d.get("thermostat_daily_program_id", None),
            workspace_id=d.get("workspace_id", None),
        )
