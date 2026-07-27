from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ThermostatDailyProgram:
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
