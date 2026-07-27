from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UnmanagedAccessCode:
    access_code_id: str
    cannot_be_managed: bool
    cannot_delete_unmanaged_access_code: bool
    code: str
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Dict[str, Any]
    ends_at: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    name: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAccessCode(
            access_code_id=d.get("access_code_id", None),
            cannot_be_managed=d.get("cannot_be_managed", None),
            cannot_delete_unmanaged_access_code=d.get(
                "cannot_delete_unmanaged_access_code", None
            ),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=DeepAttrDict(
                d.get("dormakaba_oracode_metadata", None)
            ),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
