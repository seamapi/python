from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsUser:
    access_schedule: Dict[str, Any]
    acs_system_id: str
    acs_user_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_managed: bool
    is_suspended: bool
    pending_mutations: List[Dict[str, Any]]
    phone_number: str
    salto_ks_metadata: Dict[str, Any]
    salto_space_metadata: Dict[str, Any]
    user_identity_email_address: str
    user_identity_full_name: str
    user_identity_id: str
    user_identity_phone_number: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsUser(
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            pending_mutations=d.get("pending_mutations", None),
            phone_number=d.get("phone_number", None),
            salto_ks_metadata=DeepAttrDict(d.get("salto_ks_metadata", None)),
            salto_space_metadata=DeepAttrDict(d.get("salto_space_metadata", None)),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
