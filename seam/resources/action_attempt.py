from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class ActionAttempt:
    """An attempt to perform an action in the Seam API.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type:

    :ivar error: Error associated with the action.

    :ivar result:

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type:"""

        message: str
        type: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    @dataclass
    class Result(ResourceMapping):
        """

        :ivar was_confirmed_by_device:

        :ivar acs_credential_on_encoder: Snapshot of credential data read from the physical encoder.

        :ivar acs_credential_on_seam: Corresponding credential data as stored on Seam and the access system.

        :ivar warnings:

        :ivar access_method: Access method for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

        :ivar acs_credential_id: ID of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar acs_credential_pool_id: ID of the credential pool to which the credential belongs.

        :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar acs_user_id: ID of the `ACS user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to whom the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

        :ivar akiles_metadata: Akiles-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar assa_abloy_vostio_metadata: Vostio-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar card_number: Number of the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar code:

        :ivar connected_account_id: ID of the `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ to which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

        :ivar created_at:

        :ivar display_name:

        :ivar ends_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ validity ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :ivar errors:

        :ivar external_type: Brand-specific terminology for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ type. Supported values: ``pti_card``, ``brivo_credential``, ``hid_credential``, ``visionline_card``.

        :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ type.

        :ivar is_issued:

        :ivar is_latest_desired_state_synced_with_provider: Indicates whether the latest state of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ has been synced from Seam to the provider.

        :ivar is_managed: Indicates whether Seam manages the credential.

        :ivar is_multi_phone_sync_credential: Indicates whether the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is a `multi-phone sync credential <https://docs.seam.co/capability-guides/mobile-access/issuing-mobile-credentials-from-an-access-control-system#what-are-multi-phone-sync-credentials>`_.

        :ivar is_one_time_use: Indicates whether the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ can only be used once. If ``true``, the code becomes invalid after the first use.

        :ivar issued_at:

        :ivar latest_desired_state_synced_with_provider_at: Date and time at which the state of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was most recently synced from Seam to the provider.

        :ivar parent_acs_credential_id: ID of the parent `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar starts_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ validity starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :ivar user_identity_id: ID of the `user identity <https://docs.seam.co/api/user_identities>`_ to whom the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ belongs.

        :ivar visionline_metadata: Visionline-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :ivar workspace_id:

        :ivar access_method_id: ID of the access method.

        :ivar client_session_token: Token of the client session associated with the access method.

        :ivar customization_profile_id: ID of the customization profile associated with the access method.

        :ivar instant_key_url: URL of the Instant Key for mobile key access methods.

        :ivar is_assignment_required: Indicates whether an existing card credential must be assigned to this access method before it can be issued. Only applies to card-mode access methods on systems that support credential assignment.

        :ivar is_encoding_required: Indicates whether encoding with an card encoder is required to issue or reissue the plastic card associated with the access method.

        :ivar is_ready_for_assignment: Indicates whether the access method is ready for card assignment. This is true when the access method is in card mode, has not yet been issued, and the system supports credential assignment.

        :ivar is_ready_for_encoding: Indicates whether the access method is ready to be encoded. This is true when the credential has been created and the card has not yet been issued.

        :ivar mode: Access method mode. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

        :ivar pending_mutations: Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

        :ivar access_code:

        :ivar noise_threshold:"""

        @dataclass
        class AcsCredentialOnEncoder(ResourceMapping):
            """Snapshot of credential data read from the physical encoder.

            :ivar card_number: A number or string that physically identifies the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

            :ivar created_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was created.

            :ivar ends_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ will stop being usable.

            :ivar is_issued: Indicates whether the credential has been issued (encoded onto a card).

            :ivar starts_at: Date and time at which the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ becomes usable.

            :ivar visionline_metadata: Visionline-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.
            """

            @dataclass
            class VisionlineMetadata(ResourceMapping):
                """Visionline-specific metadata for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar cancelled: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is cancelled.

                :ivar card_format: Format of the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar card_holder: Holder of the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar card_id: Card ID for the Visionline card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar common_acs_entrance_ids: IDs of the common `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar discarded: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is discarded.

                :ivar expired: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is expired.

                :ivar guest_acs_entrance_ids: IDs of the guest `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ for the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar number_of_issued_cards: Number of issued cards associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

                :ivar overridden: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is overridden.

                :ivar overwritten: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is overwritten.

                :ivar pending_auto_update: Indicates whether the card associated with the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ is pending auto-update.
                """

                cancelled: Optional[bool]
                card_format: Optional[str]
                card_holder: Optional[str]
                card_id: Optional[str]
                common_acs_entrance_ids: Optional[List[str]]
                discarded: Optional[bool]
                expired: Optional[bool]
                guest_acs_entrance_ids: Optional[List[str]]
                number_of_issued_cards: Optional[float]
                overridden: Optional[bool]
                overwritten: Optional[bool]
                pending_auto_update: Optional[bool]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        cancelled=d.get("cancelled", None),
                        card_format=d.get("card_format", None),
                        card_holder=d.get("card_holder", None),
                        card_id=d.get("card_id", None),
                        common_acs_entrance_ids=d.get("common_acs_entrance_ids", None),
                        discarded=d.get("discarded", None),
                        expired=d.get("expired", None),
                        guest_acs_entrance_ids=d.get("guest_acs_entrance_ids", None),
                        number_of_issued_cards=d.get("number_of_issued_cards", None),
                        overridden=d.get("overridden", None),
                        overwritten=d.get("overwritten", None),
                        pending_auto_update=d.get("pending_auto_update", None),
                    )

            card_number: Optional[str]
            created_at: Optional[str]
            ends_at: Optional[str]
            is_issued: Optional[bool]
            starts_at: Optional[str]
            visionline_metadata: Optional[VisionlineMetadata]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    card_number=d.get("card_number", None),
                    created_at=d.get("created_at", None),
                    ends_at=d.get("ends_at", None),
                    is_issued=d.get("is_issued", None),
                    starts_at=d.get("starts_at", None),
                    visionline_metadata=(
                        cls.VisionlineMetadata.from_dict(d.get("visionline_metadata"))
                        if d.get("visionline_metadata") is not None
                        else None
                    ),
                )

        @dataclass
        class AcsCredentialOnSeam(ResourceMapping):
            """Corresponding credential data as stored on Seam and the access system.

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

            :ivar is_managed:

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
                        joiner_acs_credential_ids=d.get(
                            "joiner_acs_credential_ids", None
                        ),
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
                    external_type_display_name=d.get(
                        "external_type_display_name", None
                    ),
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
                    warnings=[
                        cls.Warnings.from_dict(i) for i in d.get("warnings") or []
                    ],
                    workspace_id=d.get("workspace_id", None),
                )

        @dataclass
        class Warnings(ResourceMapping):
            """

            :ivar warning_code:

            :ivar warning_message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

            :ivar created_at: Date and time at which Seam created the warning.

            :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

            :ivar new_code: The PIN code that was assigned instead.

            :ivar original_code: The originally requested PIN code that could not be used.

            :ivar original_access_method_id: ID of the original access method from which this backup access method was split, if applicable.
            """

            warning_code: str
            warning_message: Optional[str]
            created_at: Optional[str]
            message: Optional[str]
            new_code: Optional[str]
            original_code: Optional[str]
            original_access_method_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    warning_code=d.get("warning_code", None),
                    warning_message=d.get("warning_message", None),
                    created_at=d.get("created_at", None),
                    message=d.get("message", None),
                    new_code=d.get("new_code", None),
                    original_code=d.get("original_code", None),
                    original_access_method_id=d.get("original_access_method_id", None),
                )

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
            """

            :ivar created_at: Date and time at which Seam created the error.

            :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

            :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
            """

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
        class PendingMutations(ResourceMapping):
            """Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

            :ivar created_at: Date and time at which the mutation was created.

            :ivar from_: Previous access time configuration.

            :ivar message: Detailed description of the mutation.

            :ivar mutation_code: Mutation code to indicate that Seam is in the process of updating the access times for this access method.

            :ivar to: New access time configuration."""

            @dataclass
            class From(ResourceMapping):
                """Previous access time configuration.

                :ivar ends_at: Previous end time for access.

                :ivar starts_at: Previous start time for access."""

                ends_at: Optional[str]
                starts_at: Optional[str]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        ends_at=d.get("ends_at", None),
                        starts_at=d.get("starts_at", None),
                    )

            @dataclass
            class To(ResourceMapping):
                """New access time configuration.

                :ivar ends_at: New end time for access.

                :ivar starts_at: New start time for access."""

                ends_at: Optional[str]
                starts_at: Optional[str]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        ends_at=d.get("ends_at", None),
                        starts_at=d.get("starts_at", None),
                    )

            created_at: str
            from_: Optional[From]
            message: str
            mutation_code: str
            to: Optional[To]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    created_at=d.get("created_at", None),
                    from_=(
                        cls.From.from_dict(d.get("from"))
                        if d.get("from") is not None
                        else None
                    ),
                    message=d.get("message", None),
                    mutation_code=d.get("mutation_code", None),
                    to=(
                        cls.To.from_dict(d.get("to"))
                        if d.get("to") is not None
                        else None
                    ),
                )

        was_confirmed_by_device: Optional[bool]
        acs_credential_on_encoder: Optional[AcsCredentialOnEncoder]
        acs_credential_on_seam: Optional[AcsCredentialOnSeam]
        warnings: Optional[List[Warnings]]
        access_method: Optional[str]
        acs_credential_id: Optional[str]
        acs_credential_pool_id: Optional[str]
        acs_system_id: Optional[str]
        acs_user_id: Optional[str]
        akiles_metadata: Optional[AkilesMetadata]
        assa_abloy_vostio_metadata: Optional[AssaAbloyVostioMetadata]
        card_number: Optional[str]
        code: Optional[str]
        connected_account_id: Optional[str]
        created_at: Optional[str]
        display_name: Optional[str]
        ends_at: Optional[str]
        errors: Optional[List[Errors]]
        external_type: Optional[str]
        external_type_display_name: Optional[str]
        is_issued: Optional[bool]
        is_latest_desired_state_synced_with_provider: Optional[bool]
        is_managed: Optional[bool]
        is_multi_phone_sync_credential: Optional[bool]
        is_one_time_use: Optional[bool]
        issued_at: Optional[str]
        latest_desired_state_synced_with_provider_at: Optional[str]
        parent_acs_credential_id: Optional[str]
        starts_at: Optional[str]
        user_identity_id: Optional[str]
        visionline_metadata: Optional[VisionlineMetadata]
        workspace_id: Optional[str]
        access_method_id: Optional[str]
        client_session_token: Optional[str]
        customization_profile_id: Optional[str]
        instant_key_url: Optional[str]
        is_assignment_required: Optional[bool]
        is_encoding_required: Optional[bool]
        is_ready_for_assignment: Optional[bool]
        is_ready_for_encoding: Optional[bool]
        mode: Optional[str]
        pending_mutations: Optional[List[PendingMutations]]
        access_code: Optional[Dict[str, Any]]
        noise_threshold: Optional[Dict[str, Any]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                was_confirmed_by_device=d.get("was_confirmed_by_device", None),
                acs_credential_on_encoder=(
                    cls.AcsCredentialOnEncoder.from_dict(
                        d.get("acs_credential_on_encoder")
                    )
                    if d.get("acs_credential_on_encoder") is not None
                    else None
                ),
                acs_credential_on_seam=(
                    cls.AcsCredentialOnSeam.from_dict(d.get("acs_credential_on_seam"))
                    if d.get("acs_credential_on_seam") is not None
                    else None
                ),
                warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
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
                workspace_id=d.get("workspace_id", None),
                access_method_id=d.get("access_method_id", None),
                client_session_token=d.get("client_session_token", None),
                customization_profile_id=d.get("customization_profile_id", None),
                instant_key_url=d.get("instant_key_url", None),
                is_assignment_required=d.get("is_assignment_required", None),
                is_encoding_required=d.get("is_encoding_required", None),
                is_ready_for_assignment=d.get("is_ready_for_assignment", None),
                is_ready_for_encoding=d.get("is_ready_for_encoding", None),
                mode=d.get("mode", None),
                pending_mutations=[
                    cls.PendingMutations.from_dict(i)
                    for i in d.get("pending_mutations") or []
                ],
                access_code=DeepAttrDict(d.get("access_code", None)),
                noise_threshold=DeepAttrDict(d.get("noise_threshold", None)),
            )

    action_attempt_id: str
    action_type: str
    error: Optional[Error]
    result: Optional[Result]
    status: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=(
                cls.Error.from_dict(d.get("error"))
                if d.get("error") is not None
                else None
            ),
            result=(
                cls.Result.from_dict(d.get("result"))
                if d.get("result") is not None
                else None
            ),
            status=d.get("status", None),
        )
