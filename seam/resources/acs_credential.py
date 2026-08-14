from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


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

    :ivar akiles_metadata: Akiles-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

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

    @dataclass
    class AkilesMetadata(ResourceMapping):
        """Akiles-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar member_pin_id: ID of the Akiles member PIN."""

        member_pin_id: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                member_pin_id=d.get("member_pin_id", None),
            )

    @dataclass
    class AssaAbloyVostioMetadata(ResourceMapping):
        """Vostio-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar auto_join: Indicates whether the credential should auto-join. For an auto-join credential, Seam automatically issues an override card if there are no other cards and a joiner card if there are existing cards on the doors.

        :ivar door_names: Names of the doors to which to grant access in the Vostio access system.

        :ivar endpoint_id: Endpoint ID in the Vostio access system.

        :ivar key_id: Key ID in the Vostio access system.

        :ivar key_issuing_request_id: Key issuing request ID in the Vostio access system.

        :ivar override_guest_acs_entrance_ids: IDs of the guest entrances to override in the Vostio access system.
        """

        auto_join: Optional[bool]
        door_names: Optional[List[str]]
        endpoint_id: Optional[str]
        key_id: Optional[str]
        key_issuing_request_id: Optional[str]
        override_guest_acs_entrance_ids: Optional[List[str]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                auto_join=d.get("auto_join", None),
                door_names=d.get("door_names", None),
                endpoint_id=d.get("endpoint_id", None),
                key_id=d.get("key_id", None),
                key_issuing_request_id=d.get("key_issuing_request_id", None),
                override_guest_acs_entrance_ids=d.get(
                    "override_guest_acs_entrance_ids", None
                ),
            )

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message:"""

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class VisionlineMetadata(ResourceMapping):
        """Visionline-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar auto_join: Indicates whether the credential should auto-join. For an auto-join credential, Seam automatically issues an override card if there are no other cards and a joiner card if there are existing cards on the doors.

        :ivar card_function_type: Card function type in the Visionline access system.

        :ivar card_id: ID of the card in the Visionline access system.

        :ivar common_acs_entrance_ids: Common entrance IDs in the Visionline access system.

        :ivar credential_id: ID of the credential in the Visionline access system.

        :ivar guest_acs_entrance_ids: Guest entrance IDs in the Visionline access system.

        :ivar is_valid: Indicates whether the credential is valid.

        :ivar joiner_acs_credential_ids: IDs of the credentials to which you want to join.
        """

        auto_join: Optional[bool]
        card_function_type: Optional[str]
        card_id: Optional[str]
        common_acs_entrance_ids: Optional[List[str]]
        credential_id: Optional[str]
        guest_acs_entrance_ids: Optional[List[str]]
        is_valid: Optional[bool]
        joiner_acs_credential_ids: Optional[List[str]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                auto_join=d.get("auto_join", None),
                card_function_type=d.get("card_function_type", None),
                card_id=d.get("card_id", None),
                common_acs_entrance_ids=d.get("common_acs_entrance_ids", None),
                credential_id=d.get("credential_id", None),
                guest_acs_entrance_ids=d.get("guest_acs_entrance_ids", None),
                is_valid=d.get("is_valid", None),
                joiner_acs_credential_ids=d.get("joiner_acs_credential_ids", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar new_code: The PIN code that was assigned instead.

        :ivar original_code: The originally requested PIN code that could not be used.
        """

        created_at: str
        message: str
        warning_code: str
        new_code: Optional[str]
        original_code: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
                new_code=d.get("new_code", None),
                original_code=d.get("original_code", None),
            )

    access_method: str
    acs_credential_id: str
    acs_credential_pool_id: Optional[str]
    acs_system_id: str
    acs_user_id: Optional[str]
    akiles_metadata: Optional[AkilesMetadata]
    assa_abloy_vostio_metadata: Optional[AssaAbloyVostioMetadata]
    card_number: Optional[str]
    code: Optional[str]
    connected_account_id: str
    created_at: str
    display_name: str
    ends_at: Optional[str]
    errors: List[Errors]
    external_type: Optional[str]
    external_type_display_name: Optional[str]
    is_issued: Optional[bool]
    is_latest_desired_state_synced_with_provider: Optional[bool]
    is_managed: bool
    is_multi_phone_sync_credential: Optional[bool]
    is_one_time_use: Optional[bool]
    issued_at: Optional[str]
    latest_desired_state_synced_with_provider_at: Optional[str]
    parent_acs_credential_id: Optional[str]
    starts_at: Optional[str]
    user_identity_id: Optional[str]
    visionline_metadata: Optional[VisionlineMetadata]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_method=d.get("access_method", None),
            acs_credential_id=d.get("acs_credential_id", None),
            acs_credential_pool_id=d.get("acs_credential_pool_id", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            akiles_metadata=(
                cls.AkilesMetadata.from_dict(d.get("akiles_metadata"))
                if d.get("akiles_metadata") is not None
                else None
            ),
            assa_abloy_vostio_metadata=(
                cls.AssaAbloyVostioMetadata.from_dict(
                    d.get("assa_abloy_vostio_metadata")
                )
                if d.get("assa_abloy_vostio_metadata") is not None
                else None
            ),
            card_number=d.get("card_number", None),
            code=d.get("code", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
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
            visionline_metadata=(
                cls.VisionlineMetadata.from_dict(d.get("visionline_metadata"))
                if d.get("visionline_metadata") is not None
                else None
            ),
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
