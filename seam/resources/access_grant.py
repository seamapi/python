from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessGrant:
    access_grant_id: str
    access_grant_key: str
    access_method_ids: List[str]
    client_session_token: str
    created_at: str
    customization_profile_id: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    instant_key_url: str
    location_ids: List[str]
    name: str
    pending_mutations: List[Dict[str, Any]]
    requested_access_methods: List[Dict[str, Any]]
    reservation_key: str
    space_ids: List[str]
    starts_at: str
    user_identity_id: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessGrant(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            access_method_ids=d.get("access_method_ids", None),
            client_session_token=d.get("client_session_token", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            instant_key_url=d.get("instant_key_url", None),
            location_ids=d.get("location_ids", None),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            requested_access_methods=d.get("requested_access_methods", None),
            reservation_key=d.get("reservation_key", None),
            space_ids=d.get("space_ids", None),
            starts_at=d.get("starts_at", None),
            user_identity_id=d.get("user_identity_id", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
