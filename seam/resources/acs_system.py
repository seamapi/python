from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsSystem:
    acs_access_group_count: float
    acs_system_id: str
    acs_user_count: float
    connected_account_id: str
    connected_account_ids: List[str]
    created_at: str
    default_credential_manager_acs_system_id: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    image_alt_text: str
    image_url: str
    is_credential_manager: bool
    location: Dict[str, Any]
    name: str
    system_type: str
    system_type_display_name: str
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsSystem(
            acs_access_group_count=d.get("acs_access_group_count", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_count=d.get("acs_user_count", None),
            connected_account_id=d.get("connected_account_id", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            default_credential_manager_acs_system_id=d.get(
                "default_credential_manager_acs_system_id", None
            ),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            image_alt_text=d.get("image_alt_text", None),
            image_url=d.get("image_url", None),
            is_credential_manager=d.get("is_credential_manager", None),
            location=DeepAttrDict(d.get("location", None)),
            name=d.get("name", None),
            system_type=d.get("system_type", None),
            system_type_display_name=d.get("system_type_display_name", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
