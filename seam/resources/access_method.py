from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessMethod:
    access_method_id: str
    client_session_token: str
    code: str
    created_at: str
    customization_profile_id: str
    display_name: str
    errors: List[Dict[str, Any]]
    instant_key_url: str
    is_assignment_required: bool
    is_encoding_required: bool
    is_issued: bool
    is_ready_for_assignment: bool
    is_ready_for_encoding: bool
    issued_at: str
    mode: str
    pending_mutations: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessMethod(
            access_method_id=d.get("access_method_id", None),
            client_session_token=d.get("client_session_token", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            instant_key_url=d.get("instant_key_url", None),
            is_assignment_required=d.get("is_assignment_required", None),
            is_encoding_required=d.get("is_encoding_required", None),
            is_issued=d.get("is_issued", None),
            is_ready_for_assignment=d.get("is_ready_for_assignment", None),
            is_ready_for_encoding=d.get("is_ready_for_encoding", None),
            issued_at=d.get("issued_at", None),
            mode=d.get("mode", None),
            pending_mutations=d.get("pending_mutations", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
