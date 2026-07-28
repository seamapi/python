from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsCredential:
    """Means by which an `access control system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ gains access at an `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_. The ``acs_credential`` object represents a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ that provides an ACS user access within an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    An access control system generally uses digital means of access to authorize a user trying to get through a specific entrance. Examples of credentials include plastic key cards, mobile keys, biometric identifiers, and PIN codes. The electronic nature of these credentials, as well as the fact that access is centralized, enables both the rapid provisioning and rescinding of access and the ability to compile access audit logs.

    For each ``acs_credential``, you define the access method. You can also specify additional properties, such as a PIN code, depending on the credential type.

    For granting a person access to a space, `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ are the default and recommended approach. Use the lower-level ACS credential API directly only when you specifically need to manage individual credentials.

    :ivar access_method: Access method for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

    :ivar acs_credential_id: ID of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar acs_credential_pool_id: ID of the credential pool to which the credential belongs.

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar acs_user_id: ID of the `ACS user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to whom the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

    :ivar assa_abloy_vostio_metadata: Vostio-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar card_number: Number of the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar code: Access (PIN) code for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar connected_account_id: ID of the `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ to which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

    :ivar created_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was created.

    :ivar display_name: Display name that corresponds to the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ type.

    :ivar ends_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ validity ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

    :ivar errors: Errors associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar external_type: Brand-specific terminology for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ type. Supported values: ``pti_card``, ``brivo_credential``, ``hid_credential``, ``visionline_card``.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ type.

    :ivar is_issued: Indicates whether the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ has been encoded onto a card.

    :ivar is_latest_desired_state_synced_with_provider: Indicates whether the latest state of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ has been synced from Seam to the provider.

    :ivar is_managed: Indicates whether Seam manages the credential.

    :ivar is_multi_phone_sync_credential: Indicates whether the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is a `multi-phone sync credential <https://docs.seam.co/capability-guides/mobile-access/issuing-mobile-credentials-from-an-access-control-system#what-are-multi-phone-sync-credentials>`_.

    :ivar is_one_time_use: Indicates whether the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ can only be used once. If ``true``, the code becomes invalid after the first use.

    :ivar issued_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was encoded onto a card.

    :ivar latest_desired_state_synced_with_provider_at: Date and time at which the state of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was most recently synced from Seam to the provider.

    :ivar parent_acs_credential_id: ID of the parent `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar starts_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ validity starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

    :ivar user_identity_id: ID of the `user identity <https://docs.seam.co/api/user_identities>`_ to whom the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

    :ivar visionline_metadata: Visionline-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar warnings: Warnings associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

    :ivar workspace_id: ID of the workspace that contains the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.
    """

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
