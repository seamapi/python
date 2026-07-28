from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsUser:
    """Represents a `user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in an `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

    An access system user typically refers to an individual who requires access, like an employee or resident. Each user can possess multiple credentials that serve as their keys or identifiers for access. The type of credential can vary widely. For example, in the Salto system, a user can have a PIN code, a mobile app account, and a fob. In other platforms, it is not uncommon for a user to have more than one of the same credential type, such as multiple key cards. Additionally, these credentials can have a schedule or validity period.

    For details about how to configure users in your access system, see the corresponding `system integration guide <https://docs.seam.co/device-and-system-integration-guides#access-control-systems>`_.

    :ivar access_schedule: ``starts_at`` and ``ends_at`` timestamps for the `access system user's <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access.

    :ivar acs_system_id: ID of the `access system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar acs_user_id: ID of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar connected_account_id: The ID of the connected account that is associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar created_at: Date and time at which the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was created.

    :ivar display_name: Display name for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar email: Deprecated: use email_address.

    :ivar email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar errors: Errors associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar external_type: Brand-specific terminology for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ type.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ type.

    :ivar full_name: Full name of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar hid_acs_system_id: ID of the HID access control system associated with the user.

    :ivar is_managed: Indicates whether Seam manages the access system user.

    :ivar is_suspended: Indicates whether the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ is currently `suspended <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users>`_.

    :ivar pending_mutations: Pending mutations associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. Seam is in the process of pushing these mutations to the integrated access system.

    :ivar phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

    :ivar salto_ks_metadata: Salto KS-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar salto_space_metadata: Salto Space-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_email_address: Email address of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_full_name: Full name of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_id: ID of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_phone_number: Phone number of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

    :ivar warnings: Warnings associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar workspace_id: ID of the workspace that contains the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.
    """

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
