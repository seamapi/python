from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class SpaceCustomerData(ResourceMapping):
    """Reservation/stay-related defaults for the space. Also carries the provider/PMS-supplied name under a ``<connector_type>_name`` key (e.g. ``guesty_name``), which Seam preserves when you rename the space (read-only — managed by Seam).

    :ivar address: Postal address for the space.

    :ivar default_checkin_time: Default check-in time for reservations at the space, as HH:mm or HH:mm:ss.

    :ivar default_checkout_time: Default check-out time for reservations at the space, as HH:mm or HH:mm:ss.

    :ivar time_zone: IANA time zone for the space, e.g. America/Los_Angeles."""

    address: str
    default_checkin_time: str
    default_checkout_time: str
    time_zone: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            address=d.get("address", None),
            default_checkin_time=d.get("default_checkin_time", None),
            default_checkout_time=d.get("default_checkout_time", None),
            time_zone=d.get("time_zone", None),
        )


@dataclass
class SpaceGeolocation(ResourceMapping):
    """Geographic coordinates (latitude and longitude) of the space.

    :ivar latitude: Latitude of the space, in decimal degrees.

    :ivar longitude: Longitude of the space, in decimal degrees."""

    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            latitude=d.get("latitude", None),
            longitude=d.get("longitude", None),
        )


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

    acs_entrance_count: float
    created_at: str
    customer_data: SpaceCustomerData
    customer_key: str
    device_count: float
    display_name: str
    geolocation: SpaceGeolocation
    name: str
    space_id: str
    space_key: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            acs_entrance_count=d.get("acs_entrance_count", None),
            created_at=d.get("created_at", None),
            customer_data=(
                SpaceCustomerData.from_dict(d.get("customer_data"))
                if d.get("customer_data") is not None
                else None
            ),
            customer_key=d.get("customer_key", None),
            device_count=d.get("device_count", None),
            display_name=d.get("display_name", None),
            geolocation=(
                SpaceGeolocation.from_dict(d.get("geolocation"))
                if d.get("geolocation") is not None
                else None
            ),
            name=d.get("name", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
        )
