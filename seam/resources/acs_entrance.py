from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsEntrance:
    acs_entrance_id: str
    acs_system_id: str
    akiles_metadata: Dict[str, Any]
    assa_abloy_vostio_metadata: Dict[str, Any]
    avigilon_alta_metadata: Dict[str, Any]
    brivo_metadata: Dict[str, Any]
    can_belong_to_reservation: bool
    can_unlock_with_card: bool
    can_unlock_with_cloud_key: bool
    can_unlock_with_code: bool
    can_unlock_with_mobile_key: bool
    connected_account_id: str
    created_at: str
    display_name: str
    dormakaba_ambiance_metadata: Dict[str, Any]
    dormakaba_community_metadata: Dict[str, Any]
    errors: List[Dict[str, Any]]
    hotek_metadata: Dict[str, Any]
    is_locked: bool
    latch_metadata: Dict[str, Any]
    salto_ks_metadata: Dict[str, Any]
    salto_space_metadata: Dict[str, Any]
    space_ids: List[str]
    visionline_metadata: Dict[str, Any]
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEntrance(
            acs_entrance_id=d.get("acs_entrance_id", None),
            acs_system_id=d.get("acs_system_id", None),
            akiles_metadata=DeepAttrDict(d.get("akiles_metadata", None)),
            assa_abloy_vostio_metadata=DeepAttrDict(
                d.get("assa_abloy_vostio_metadata", None)
            ),
            avigilon_alta_metadata=DeepAttrDict(d.get("avigilon_alta_metadata", None)),
            brivo_metadata=DeepAttrDict(d.get("brivo_metadata", None)),
            can_belong_to_reservation=d.get("can_belong_to_reservation", None),
            can_unlock_with_card=d.get("can_unlock_with_card", None),
            can_unlock_with_cloud_key=d.get("can_unlock_with_cloud_key", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
            can_unlock_with_mobile_key=d.get("can_unlock_with_mobile_key", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            dormakaba_ambiance_metadata=DeepAttrDict(
                d.get("dormakaba_ambiance_metadata", None)
            ),
            dormakaba_community_metadata=DeepAttrDict(
                d.get("dormakaba_community_metadata", None)
            ),
            errors=d.get("errors", None),
            hotek_metadata=DeepAttrDict(d.get("hotek_metadata", None)),
            is_locked=d.get("is_locked", None),
            latch_metadata=DeepAttrDict(d.get("latch_metadata", None)),
            salto_ks_metadata=DeepAttrDict(d.get("salto_ks_metadata", None)),
            salto_space_metadata=DeepAttrDict(d.get("salto_space_metadata", None)),
            space_ids=d.get("space_ids", None),
            visionline_metadata=DeepAttrDict(d.get("visionline_metadata", None)),
            warnings=d.get("warnings", None),
        )
