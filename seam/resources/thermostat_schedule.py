from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


@dataclass
class ThermostatSchedule:
    """Represents a `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ that activates a configured `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ on a `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ at a specified starting time and deactivates the climate preset at a specified ending time.

    :ivar climate_preset_key: Key of the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ to use for the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

    :ivar created_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ was created.

    :ivar device_id: ID of the desired `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ device.

    :ivar ends_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

    :ivar errors: Errors associated with the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

    :ivar is_override_allowed: Indicates whether a person at the thermostat can change the thermostat's settings after the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ starts.

    :ivar max_override_period_minutes: Number of minutes for which a person at the thermostat can change the thermostat's settings after the activation of the scheduled `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_. See also `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

    :ivar name: User-friendly name to identify the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

    :ivar starts_at: Date and time at which the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_ starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

    :ivar thermostat_schedule_id: ID of the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

    :ivar workspace_id: ID of the workspace that contains the thermostat schedule."""

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the `thermostat schedule <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    climate_preset_key: str
    created_at: str
    device_id: str
    ends_at: str
    errors: List[Errors]
    is_override_allowed: Optional[bool]
    max_override_period_minutes: Optional[int]
    name: Optional[str]
    starts_at: str
    thermostat_schedule_id: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            climate_preset_key=d.get("climate_preset_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            ends_at=d.get("ends_at", None),
            errors=_object_list_from_dict(cls.Errors, d.get("errors")),
            is_override_allowed=d.get("is_override_allowed", None),
            max_override_period_minutes=d.get("max_override_period_minutes", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            workspace_id=d.get("workspace_id", None),
        )
