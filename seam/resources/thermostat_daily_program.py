from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class ThermostatDailyProgram:
    """Represents a thermostat daily program, consisting of a set of periods, each of which has a starting time and the key that identifies the climate preset to apply at the starting time.

    :ivar created_at: Date and time at which the thermostat daily program was created.

    :ivar device_id: ID of the thermostat device on which the thermostat daily program is configured.

    :ivar name: User-friendly name to identify the thermostat daily program.

    :ivar periods: Array of thermostat daily program periods.

    :ivar thermostat_daily_program_id: ID of the thermostat daily program.

    :ivar workspace_id: ID of the workspace that contains the thermostat daily program.
    """

    @dataclass
    class Periods(ResourceMapping):
        """Array of thermostat daily program periods.

        :ivar climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to activate at the ``starts_at_time``.

        :ivar starts_at_time: Time at which the thermostat daily program period starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
        """

        climate_preset_key: str
        starts_at_time: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                climate_preset_key=d.get("climate_preset_key", None),
                starts_at_time=d.get("starts_at_time", None),
            )

    created_at: str
    device_id: str
    name: Optional[str]
    periods: List[Periods]
    thermostat_daily_program_id: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            name=d.get("name", None),
            periods=[cls.Periods.from_dict(i) for i in d.get("periods") or []],
            thermostat_daily_program_id=d.get("thermostat_daily_program_id", None),
            workspace_id=d.get("workspace_id", None),
        )
