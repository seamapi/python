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
class Space:
    """Represents a space that is a logical grouping of devices and entrances. You can assign access to an entire space, thereby making granting access more efficient.

    :ivar acs_entrance_count: Number of entrances in the space.

    :ivar created_at: Date and time at which the space was created.

    :ivar customer_data: Reservation/stay-related defaults for the space. Also carries the provider/PMS-supplied name under a ``<connector_type>_name`` key (e.g. ``guesty_name``), which Seam preserves when you rename the space (read-only — managed by Seam).

    :ivar customer_key: Customer key associated with the space.

    :ivar device_count: Number of devices in the space.

    :ivar display_name: Display name for the space.

    :ivar geolocation: Geographic coordinates (latitude and longitude) of the space.

    :ivar name: Name of the space.

    :ivar space_id: ID of the space.

    :ivar space_key: Unique key for the space within the workspace.

    :ivar workspace_id: ID of the workspace associated with the space."""

    @dataclass
    class CustomerData(ResourceMapping):
        """Reservation/stay-related defaults for the space. Also carries the provider/PMS-supplied name under a ``<connector_type>_name`` key (e.g. ``guesty_name``), which Seam preserves when you rename the space (read-only — managed by Seam).

        :ivar address: Postal address for the space.

        :ivar default_checkin_time: Default check-in time for reservations at the space, as HH:mm or HH:mm:ss.

        :ivar default_checkout_time: Default check-out time for reservations at the space, as HH:mm or HH:mm:ss.

        :ivar time_zone: IANA time zone for the space, e.g. America/Los_Angeles."""

        address: Optional[str]
        default_checkin_time: Optional[str]
        default_checkout_time: Optional[str]
        time_zone: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                address=d.get("address", None),
                default_checkin_time=d.get("default_checkin_time", None),
                default_checkout_time=d.get("default_checkout_time", None),
                time_zone=d.get("time_zone", None),
            )

    @dataclass
    class Geolocation(ResourceMapping):
        """Geographic coordinates (latitude and longitude) of the space.

        :ivar latitude: Latitude of the space, in decimal degrees.

        :ivar longitude: Longitude of the space, in decimal degrees."""

        latitude: float
        longitude: float

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                latitude=d.get("latitude", None),
                longitude=d.get("longitude", None),
            )

    acs_entrance_count: float
    created_at: str
    customer_data: Optional[CustomerData]
    customer_key: Optional[str]
    device_count: float
    display_name: str
    geolocation: Optional[Geolocation]
    name: str
    space_id: str
    space_key: Optional[str]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            acs_entrance_count=d.get("acs_entrance_count", None),
            created_at=d.get("created_at", None),
            customer_data=_object_from_dict(cls.CustomerData, d.get("customer_data")),
            customer_key=d.get("customer_key", None),
            device_count=d.get("device_count", None),
            display_name=d.get("display_name", None),
            geolocation=_object_from_dict(cls.Geolocation, d.get("geolocation")),
            name=d.get("name", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
        )
