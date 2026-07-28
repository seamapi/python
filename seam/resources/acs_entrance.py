from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsEntrance:
    """Represents an `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ within an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    In an access control system, an entrance is a secured door, gate, zone, or other method of entry. You can list details for all the ``acs_entrance`` resources in your workspace or get these details for a specific ``acs_entrance``. You can also list all entrances associated with a specific credential, and you can list all credentials associated with a specific entrance.

    :ivar acs_entrance_id: ID of the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype acs_entrance_id: str

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype acs_system_id: str

    :ivar akiles_metadata: Akiles-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype akiles_metadata: Dict[str, Any]

    :ivar assa_abloy_vostio_metadata: ASSA ABLOY Vostio-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype assa_abloy_vostio_metadata: Dict[str, Any]

    :ivar avigilon_alta_metadata: Avigilon Alta-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype avigilon_alta_metadata: Dict[str, Any]

    :ivar brivo_metadata: Brivo-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype brivo_metadata: Dict[str, Any]

    :ivar can_belong_to_reservation: Indicates whether the ACS entrance can belong to a reservation via an access_grant.reservation_key.
    :vartype can_belong_to_reservation: bool

    :ivar can_unlock_with_card: Indicates whether the ACS entrance can be unlocked with card credentials.
    :vartype can_unlock_with_card: bool

    :ivar can_unlock_with_cloud_key: Indicates whether the ACS entrance can be unlocked with cloud key credentials.
    :vartype can_unlock_with_cloud_key: bool

    :ivar can_unlock_with_code: Indicates whether the ACS entrance can be unlocked with pin codes.
    :vartype can_unlock_with_code: bool

    :ivar can_unlock_with_mobile_key: Indicates whether the ACS entrance can be unlocked with mobile key credentials.
    :vartype can_unlock_with_mobile_key: bool

    :ivar connected_account_id: ID of the `connected account <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype connected_account_id: str

    :ivar created_at: Date and time at which the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ was created.
    :vartype created_at: str

    :ivar display_name: Display name for the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype display_name: str

    :ivar dormakaba_ambiance_metadata: dormakaba Ambiance-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype dormakaba_ambiance_metadata: Dict[str, Any]

    :ivar dormakaba_community_metadata: dormakaba Community-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype dormakaba_community_metadata: Dict[str, Any]

    :ivar errors: Errors associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype errors: List[Dict[str, Any]]

    :ivar hotek_metadata: Hotek-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype hotek_metadata: Dict[str, Any]

    :ivar is_locked: Indicates whether the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ is currently locked.
    :vartype is_locked: bool

    :ivar latch_metadata: Latch-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype latch_metadata: Dict[str, Any]

    :ivar salto_ks_metadata: Salto KS-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype salto_ks_metadata: Dict[str, Any]

    :ivar salto_space_metadata: Salto Space-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype salto_space_metadata: Dict[str, Any]

    :ivar space_ids: IDs of the spaces that the entrance is in.
    :vartype space_ids: List[str]

    :ivar visionline_metadata: Visionline-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype visionline_metadata: Dict[str, Any]

    :ivar warnings: Warnings associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    :vartype warnings: List[Dict[str, Any]]"""

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
