from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UnmanagedUserIdentity:
    acs_user_ids: List[str]
    created_at: str
    display_name: str
    email_address: str
    errors: List[Dict[str, Any]]
    full_name: str
    phone_number: str
    user_identity_id: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedUserIdentity(
            acs_user_ids=d.get("acs_user_ids", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            full_name=d.get("full_name", None),
            phone_number=d.get("phone_number", None),
            user_identity_id=d.get("user_identity_id", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
