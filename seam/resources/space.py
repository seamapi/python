from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Space:
    """Represents a space that is a logical grouping of devices and entrances. You can assign access to an entire space, thereby making granting access more efficient.

    :ivar acs_entrance_count: Number of entrances in the space.
    :vartype acs_entrance_count: float

    :ivar created_at: Date and time at which the space was created.
    :vartype created_at: str

    :ivar customer_data: Reservation/stay-related defaults for the space. Also carries the provider/PMS-supplied name under a ``<connector_type>_name`` key (e.g. ``guesty_name``), which Seam preserves when you rename the space (read-only — managed by Seam).
    :vartype customer_data: Dict[str, Any]

    :ivar customer_key: Customer key associated with the space.
    :vartype customer_key: str

    :ivar device_count: Number of devices in the space.
    :vartype device_count: float

    :ivar display_name: Display name for the space.
    :vartype display_name: str

    :ivar geolocation: Geographic coordinates (latitude and longitude) of the space.
    :vartype geolocation: Dict[str, Any]

    :ivar name: Name of the space.
    :vartype name: str

    :ivar space_id: ID of the space.
    :vartype space_id: str

    :ivar space_key: Unique key for the space within the workspace.
    :vartype space_key: str

    :ivar workspace_id: ID of the workspace associated with the space.
    :vartype workspace_id: str"""

    acs_entrance_count: float
    created_at: str
    customer_data: Dict[str, Any]
    customer_key: str
    device_count: float
    display_name: str
    geolocation: Dict[str, Any]
    name: str
    space_id: str
    space_key: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Space(
            acs_entrance_count=d.get("acs_entrance_count", None),
            created_at=d.get("created_at", None),
            customer_data=DeepAttrDict(d.get("customer_data", None)),
            customer_key=d.get("customer_key", None),
            device_count=d.get("device_count", None),
            display_name=d.get("display_name", None),
            geolocation=DeepAttrDict(d.get("geolocation", None)),
            name=d.get("name", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
        )
