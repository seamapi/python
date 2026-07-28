from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsSystem:
    """Represents an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    Within an ``acs_system``, create ```acs_user``s <https://docs.seam.co/api/acs/users/object>`_ and ```acs_credential``s <https://docs.seam.co/api/acs/credentials/object>`_ to grant access to the ``acs_user``s.

    For details about the resources associated with an access control system, see the `access control systems namespace <https://docs.seam.co/api/acs>`_.

    :ivar acs_access_group_count: Number of access groups in the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar acs_user_count: Number of users in the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar connected_account_id: ID of the connected account associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar connected_account_ids: Deprecated: Use ``connected_account_id``. IDs of the `connected accounts <https://docs.seam.co/core-concepts/connected-accounts>`_ associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar created_at: Date and time at which the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ was created.

    :ivar default_credential_manager_acs_system_id: ID of the default credential manager ``acs_system`` for this `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar errors: Errors associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar external_type: Brand-specific terminology for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ type.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ type.

    :ivar image_alt_text: Alternative text for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ image.

    :ivar image_url: URL for the image that represents the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar is_credential_manager: Indicates whether the ``acs_system`` is a credential manager.

    :ivar location: Location information for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar name: Name of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar system_type: Deprecated: Use ``external_type``.

    :ivar system_type_display_name: Deprecated: Use ``external_type_display_name``.

    :ivar visionline_metadata: Visionline-specific metadata for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar warnings: Warnings associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar workspace_id: ID of the workspace that contains the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.
    """

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
