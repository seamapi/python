from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Space:
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
