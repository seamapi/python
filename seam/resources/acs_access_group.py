from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsAccessGroup:
    access_group_type: str
    access_group_type_display_name: str
    access_schedule: Dict[str, Any]
    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    is_managed: bool
    name: str
    pending_mutations: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsAccessGroup(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
