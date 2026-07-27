from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessCode:
    access_code_id: str
    code: str
    common_code_key: str
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Dict[str, Any]
    ends_at: str
    errors: List[Dict[str, Any]]
    is_backup: bool
    is_backup_access_code_available: bool
    is_external_modification_allowed: bool
    is_managed: bool
    is_offline_access_code: bool
    is_one_time_use: bool
    is_scheduled_on_device: bool
    is_waiting_for_code_assignment: bool
    name: str
    pending_mutations: List[Dict[str, Any]]
    pulled_backup_access_code_id: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessCode(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            common_code_key=d.get("common_code_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=DeepAttrDict(
                d.get("dormakaba_oracode_metadata", None)
            ),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_backup=d.get("is_backup", None),
            is_backup_access_code_available=d.get(
                "is_backup_access_code_available", None
            ),
            is_external_modification_allowed=d.get(
                "is_external_modification_allowed", None
            ),
            is_managed=d.get("is_managed", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            is_waiting_for_code_assignment=d.get(
                "is_waiting_for_code_assignment", None
            ),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
