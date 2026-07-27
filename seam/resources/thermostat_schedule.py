from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ThermostatSchedule:
    climate_preset_key: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Dict[str, Any]]
    is_override_allowed: bool
    max_override_period_minutes: int
    name: str
    starts_at: str
    thermostat_schedule_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ThermostatSchedule(
            climate_preset_key=d.get("climate_preset_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_override_allowed=d.get("is_override_allowed", None),
            max_override_period_minutes=d.get("max_override_period_minutes", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            workspace_id=d.get("workspace_id", None),
        )
