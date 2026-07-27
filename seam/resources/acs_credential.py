from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsCredential:
    access_method: str
    acs_credential_id: str
    acs_credential_pool_id: str
    acs_system_id: str
    acs_user_id: str
    assa_abloy_vostio_metadata: Dict[str, Any]
    card_number: str
    code: str
    connected_account_id: str
    created_at: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    is_issued: bool
    is_latest_desired_state_synced_with_provider: bool
    is_managed: bool
    is_multi_phone_sync_credential: bool
    is_one_time_use: bool
    issued_at: str
    latest_desired_state_synced_with_provider_at: str
    parent_acs_credential_id: str
    starts_at: str
    user_identity_id: str
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsCredential(
            access_method=d.get("access_method", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            card_number=d.get("card_number", None),
            code=d.get("code", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_issued=d.get("is_issued", None),
            is_latest_desired_state_synced_with_provider=d.get(
                "is_latest_desired_state_synced_with_provider", None
            ),
            is_managed=d.get("is_managed", None),
            is_multi_phone_sync_credential=d.get(
                "is_multi_phone_sync_credential", None
            ),
            is_one_time_use=d.get("is_one_time_use", None),
            issued_at=d.get("issued_at", None),
            latest_desired_state_synced_with_provider_at=d.get(
                "latest_desired_state_synced_with_provider_at", None
            ),
            parent_acs_credential_id=d.get("parent_acs_credential_id", None),
            starts_at=d.get("starts_at", None),
            user_identity_id=d.get("user_identity_id", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
