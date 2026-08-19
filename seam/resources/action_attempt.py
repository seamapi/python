from typing import Any, Dict, List, Literal, Optional, Union, cast
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class LockDoorActionAttempt:
    """Locking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of locking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar was_confirmed_by_device: Indicates whether the device confirmed that the lock action occurred.
        """

        was_confirmed_by_device: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                was_confirmed_by_device=d.get("was_confirmed_by_device", None),
            )

    action_attempt_id: str
    action_type: Literal["LOCK_DOOR"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class UnlockDoorActionAttempt:
    """Unlocking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of unlocking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar was_confirmed_by_device: Indicates whether the device confirmed that the unlock action occurred.
        """

        was_confirmed_by_device: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                was_confirmed_by_device=d.get("was_confirmed_by_device", None),
            )

    action_attempt_id: str
    action_type: Literal["UNLOCK_DOOR"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class ScanCredentialActionAttempt:
    """Reading credential data from the physical encoder is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a credential.

    :ivar error:

    :ivar result: Result of scanning a card. If the attempt was successful, includes a snapshot of credential data read from the physical encoder, the corresponding data stored on Seam and the access system, and any associated warnings.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Error type to indicate that the Seam Bridge is disconnected or cannot reach the access control system.
        """

        message: str
        type: Literal[
            "uncategorized_error",
            "action_attempt_expired",
            "no_credential_on_encoder",
            "encoder_not_online",
            "encoder_communication_timeout",
            "bridge_disconnected",
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    @dataclass
    class Result(ResourceMapping):
        """Result of scanning a card. If the attempt was successful, includes a snapshot of credential data read from the physical encoder, the corresponding data stored on Seam and the access system, and any associated warnings.

        :ivar acs_credential_on_encoder: Snapshot of credential data read from the physical encoder.

        :ivar acs_credential_on_seam: Corresponding credential data as stored on Seam and the access system.

        :ivar warnings: Warnings related to scanning the credential, such as mismatches between the credential data currently encoded on the card and the corresponding data stored on Seam and the access system.
        """

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
                card_format: Optional[Literal["TLCode", "rfid48"]]
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
                card_function_type: Optional[Literal["guest", "staff"]]
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
                warning_code: Literal[
                    "waiting_to_be_issued",
                    "schedule_externally_modified",
                    "schedule_modified",
                    "being_deleted",
                    "unknown_issue_with_acs_credential",
                    "needs_to_be_reissued",
                    "requested_code_unavailable",
                ]
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

            access_method: Literal["code", "card", "mobile_key", "cloud_key"]
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
            external_type: Optional[
                Literal[
                    "pti_card",
                    "brivo_credential",
                    "hid_credential",
                    "visionline_card",
                    "salto_ks_credential",
                    "assa_abloy_vostio_key",
                    "salto_space_key",
                    "latch_access",
                    "dormakaba_ambiance_credential",
                    "hotek_card",
                    "salto_ks_tag",
                    "avigilon_alta_credential",
                    "kisi_credential",
                    "akiles_credential",
                ]
            ]
            external_type_display_name: Optional[str]
            is_issued: Optional[bool]
            is_latest_desired_state_synced_with_provider: Optional[bool]
            is_managed: Literal[True, False]
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
            """Warnings related to scanning the credential, such as mismatches between the credential data currently encoded on the card and the corresponding data stored on Seam and the access system.

            :ivar warning_code: Indicates a warning related to scanning a credential.

            :ivar warning_message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.
            """

            warning_code: Literal[
                "acs_credential_on_encoder_out_of_sync",
                "acs_credential_on_seam_not_found",
            ]
            warning_message: str

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    warning_code=d.get("warning_code", None),
                    warning_message=d.get("warning_message", None),
                )

        acs_credential_on_encoder: Optional[AcsCredentialOnEncoder]
        acs_credential_on_seam: Optional[AcsCredentialOnSeam]
        warnings: List[Warnings]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
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
            )

    action_attempt_id: str
    action_type: Literal["SCAN_CREDENTIAL"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class EncodeCredentialActionAttempt:
    """Encoding credential data from the physical encoder onto a card is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of encoding credential data from the physical encoder onto a card.

    :ivar error:

    :ivar result: Result of an encoding attempt. If the attempt was successful, includes the credential data that was encoded onto the card.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Error type to indicate that the credential was deleted and can no longer be encoded.
        """

        message: str
        type: Literal[
            "uncategorized_error",
            "action_attempt_expired",
            "no_credential_on_encoder",
            "incompatible_card_format",
            "credential_cannot_be_reissued",
            "encoder_not_online",
            "encoder_communication_timeout",
            "bridge_disconnected",
            "encoding_interrupted",
            "credential_deleted",
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    @dataclass
    class Result(ResourceMapping):
        """Result of an encoding attempt. If the attempt was successful, includes the credential data that was encoded onto the card.

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
            card_function_type: Optional[Literal["guest", "staff"]]
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
            warning_code: Literal[
                "waiting_to_be_issued",
                "schedule_externally_modified",
                "schedule_modified",
                "being_deleted",
                "unknown_issue_with_acs_credential",
                "needs_to_be_reissued",
                "requested_code_unavailable",
            ]
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

        access_method: Literal["code", "card", "mobile_key", "cloud_key"]
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
        external_type: Optional[
            Literal[
                "pti_card",
                "brivo_credential",
                "hid_credential",
                "visionline_card",
                "salto_ks_credential",
                "assa_abloy_vostio_key",
                "salto_space_key",
                "latch_access",
                "dormakaba_ambiance_credential",
                "hotek_card",
                "salto_ks_tag",
                "avigilon_alta_credential",
                "kisi_credential",
                "akiles_credential",
            ]
        ]
        external_type_display_name: Optional[str]
        is_issued: Optional[bool]
        is_latest_desired_state_synced_with_provider: Optional[bool]
        is_managed: Literal[True, False]
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

    action_attempt_id: str
    action_type: Literal["ENCODE_CREDENTIAL"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class ScanToAssignCredentialActionAttempt:
    """Scanning a physical card and assigning the credential is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a physical card and assigning the credential to an ACS user.

    :ivar error:

    :ivar result: Result of a scan to assign attempt. If the attempt was successful, includes the credential data that was scanned and assigned.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Error type to indicate that there is no credential on the encoder.
        """

        message: str
        type: Literal[
            "uncategorized_error", "action_attempt_expired", "no_credential_on_encoder"
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    @dataclass
    class Result(ResourceMapping):
        """Result of a scan to assign attempt. If the attempt was successful, includes the credential data that was scanned and assigned.

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
            card_function_type: Optional[Literal["guest", "staff"]]
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
            warning_code: Literal[
                "waiting_to_be_issued",
                "schedule_externally_modified",
                "schedule_modified",
                "being_deleted",
                "unknown_issue_with_acs_credential",
                "needs_to_be_reissued",
                "requested_code_unavailable",
            ]
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

        access_method: Literal["code", "card", "mobile_key", "cloud_key"]
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
        external_type: Optional[
            Literal[
                "pti_card",
                "brivo_credential",
                "hid_credential",
                "visionline_card",
                "salto_ks_credential",
                "assa_abloy_vostio_key",
                "salto_space_key",
                "latch_access",
                "dormakaba_ambiance_credential",
                "hotek_card",
                "salto_ks_tag",
                "avigilon_alta_credential",
                "kisi_credential",
                "akiles_credential",
            ]
        ]
        external_type_display_name: Optional[str]
        is_issued: Optional[bool]
        is_latest_desired_state_synced_with_provider: Optional[bool]
        is_managed: Literal[True]
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

    action_attempt_id: str
    action_type: Literal["SCAN_TO_ASSIGN_CREDENTIAL"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class AssignCredentialActionAttempt:
    """Assigning a credential to an access method is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of assigning a pre-registered card credential to an access method.

    :ivar error:

    :ivar result: Result of assigning a credential. If successful, includes the updated access method with the assigned credential.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Error type to indicate that no matching credential was found."""

        message: str
        type: Literal[
            "uncategorized_error", "action_attempt_expired", "credential_not_found"
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    @dataclass
    class Result(ResourceMapping):
        """Result of assigning a credential. If successful, includes the updated access method with the assigned credential.

        :ivar access_method_id: ID of the access method.

        :ivar client_session_token: Token of the client session associated with the access method.

        :ivar code: The actual PIN code for code access methods.

        :ivar created_at: Date and time at which the access method was created.

        :ivar customization_profile_id: ID of the customization profile associated with the access method.

        :ivar display_name: Display name of the access method.

        :ivar errors: Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

        :ivar instant_key_url: URL of the Instant Key for mobile key access methods.

        :ivar is_assignment_required: Indicates whether an existing card credential must be assigned to this access method before it can be issued. Only applies to card-mode access methods on systems that support credential assignment.

        :ivar is_encoding_required: Indicates whether encoding with an card encoder is required to issue or reissue the plastic card associated with the access method.

        :ivar is_issued: Indicates whether the access method has been issued.

        :ivar is_ready_for_assignment: Indicates whether the access method is ready for card assignment. This is true when the access method is in card mode, has not yet been issued, and the system supports credential assignment.

        :ivar is_ready_for_encoding: Indicates whether the access method is ready to be encoded. This is true when the credential has been created and the card has not yet been issued.

        :ivar issued_at: Date and time at which the access method was issued.

        :ivar mode: Access method mode. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

        :ivar pending_mutations: Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

        :ivar warnings: Warnings associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

        :ivar workspace_id: ID of the Seam workspace associated with the access method.
        """

        @dataclass
        class Errors(ResourceMapping):
            """Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

            :ivar created_at: Date and time at which Seam created the error.

            :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

            :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
            """

            created_at: str
            error_code: Literal["failed_to_issue"]
            message: str

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    created_at=d.get("created_at", None),
                    error_code=d.get("error_code", None),
                    message=d.get("message", None),
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
            mutation_code: Literal[
                "provisioning_access", "revoking_access", "updating_access_times"
            ]
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

        @dataclass
        class Warnings(ResourceMapping):
            """Warnings associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

            :ivar created_at: Date and time at which Seam created the warning.

            :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

            :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

            :ivar original_access_method_id: ID of the original access method from which this backup access method was split, if applicable.
            """

            created_at: str
            message: str
            warning_code: Literal[
                "being_deleted",
                "updating_access_times",
                "pulled_backup_access_code",
                "delay_in_issuing",
            ]
            original_access_method_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    created_at=d.get("created_at", None),
                    message=d.get("message", None),
                    warning_code=d.get("warning_code", None),
                    original_access_method_id=d.get("original_access_method_id", None),
                )

        access_method_id: str
        client_session_token: Optional[str]
        code: Optional[str]
        created_at: str
        customization_profile_id: Optional[str]
        display_name: str
        errors: List[Errors]
        instant_key_url: Optional[str]
        is_assignment_required: Optional[bool]
        is_encoding_required: Optional[bool]
        is_issued: bool
        is_ready_for_assignment: Optional[bool]
        is_ready_for_encoding: Optional[bool]
        issued_at: Optional[str]
        mode: Literal["code", "card", "mobile_key", "cloud_key"]
        pending_mutations: List[PendingMutations]
        warnings: List[Warnings]
        workspace_id: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                access_method_id=d.get("access_method_id", None),
                client_session_token=d.get("client_session_token", None),
                code=d.get("code", None),
                created_at=d.get("created_at", None),
                customization_profile_id=d.get("customization_profile_id", None),
                display_name=d.get("display_name", None),
                errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
                instant_key_url=d.get("instant_key_url", None),
                is_assignment_required=d.get("is_assignment_required", None),
                is_encoding_required=d.get("is_encoding_required", None),
                is_issued=d.get("is_issued", None),
                is_ready_for_assignment=d.get("is_ready_for_assignment", None),
                is_ready_for_encoding=d.get("is_ready_for_encoding", None),
                issued_at=d.get("issued_at", None),
                mode=d.get("mode", None),
                pending_mutations=[
                    cls.PendingMutations.from_dict(i)
                    for i in d.get("pending_mutations") or []
                ],
                warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
                workspace_id=d.get("workspace_id", None),
            )

    action_attempt_id: str
    action_type: Literal["ASSIGN_CREDENTIAL"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class ResetSandboxWorkspaceActionAttempt:
    """Resetting a sandbox workspace is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of resetting a sandbox workspace.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["RESET_SANDBOX_WORKSPACE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class SetFanModeActionAttempt:
    """Setting the fan mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the fan mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["SET_FAN_MODE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class SetHvacModeActionAttempt:
    """Setting the HVAC mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the HVAC mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["SET_HVAC_MODE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class ActivateClimatePresetActionAttempt:
    """Activating a climate preset is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of a climate preset activation.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["ACTIVATE_CLIMATE_PRESET"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class SimulateKeypadCodeEntryActionAttempt:
    """Simulating a keypad code entry is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a keypad code entry.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["SIMULATE_KEYPAD_CODE_ENTRY"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class SimulateManualLockViaKeypadActionAttempt:
    """Simulating a manual lock action using a keypad is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a manual lock action using a keypad.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["SIMULATE_MANUAL_LOCK_VIA_KEYPAD"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class PushThermostatProgramsActionAttempt:
    """Pushing thermostat weekly programs is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of pushing thermostat programs.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["PUSH_THERMOSTAT_PROGRAMS"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class ConfigureAutoLockActionAttempt:
    """Configuring the auto-lock is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of configuring the auto-lock on a lock.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["CONFIGURE_AUTO_LOCK"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class SyncAccessCodesActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Syncing access codes is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["SYNC_ACCESS_CODES"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class CreateAccessCodeActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar access_code: Created access code."""

        access_code: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                access_code=DeepAttrDict(d.get("access_code", None)),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_ACCESS_CODE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class DeleteAccessCodeActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["DELETE_ACCESS_CODE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class UpdateAccessCodeActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar access_code: Updated access code."""

        access_code: Optional[Dict[str, Any]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                access_code=DeepAttrDict(d.get("access_code", None)),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_ACCESS_CODE"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class CreateNoiseThresholdActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar noise_threshold: Created noise threshold."""

        noise_threshold: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                noise_threshold=DeepAttrDict(d.get("noise_threshold", None)),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_NOISE_THRESHOLD"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class DeleteNoiseThresholdActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            return cls()

    action_attempt_id: str
    action_type: Literal["DELETE_NOISE_THRESHOLD"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


@dataclass
class UpdateNoiseThresholdActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Error(ResourceMapping):
        """Error associated with the action.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar type: Type of the error."""

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
        """Result of the action.

        :ivar noise_threshold: Updated noise threshold."""

        noise_threshold: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                noise_threshold=DeepAttrDict(d.get("noise_threshold", None)),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_NOISE_THRESHOLD"]
    error: Optional[Error]
    result: Optional[Result]
    status: Literal["success", "pending", "error"]

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


ActionAttempt = Union[
    LockDoorActionAttempt,
    UnlockDoorActionAttempt,
    ScanCredentialActionAttempt,
    EncodeCredentialActionAttempt,
    ScanToAssignCredentialActionAttempt,
    AssignCredentialActionAttempt,
    ResetSandboxWorkspaceActionAttempt,
    SetFanModeActionAttempt,
    SetHvacModeActionAttempt,
    ActivateClimatePresetActionAttempt,
    SimulateKeypadCodeEntryActionAttempt,
    SimulateManualLockViaKeypadActionAttempt,
    PushThermostatProgramsActionAttempt,
    ConfigureAutoLockActionAttempt,
    SyncAccessCodesActionAttempt,
    CreateAccessCodeActionAttempt,
    DeleteAccessCodeActionAttempt,
    UpdateAccessCodeActionAttempt,
    CreateNoiseThresholdActionAttempt,
    DeleteNoiseThresholdActionAttempt,
    UpdateNoiseThresholdActionAttempt,
]

_ACTION_ATTEMPT_VARIANTS: Dict[str, Any] = {
    "LOCK_DOOR": LockDoorActionAttempt,
    "UNLOCK_DOOR": UnlockDoorActionAttempt,
    "SCAN_CREDENTIAL": ScanCredentialActionAttempt,
    "ENCODE_CREDENTIAL": EncodeCredentialActionAttempt,
    "SCAN_TO_ASSIGN_CREDENTIAL": ScanToAssignCredentialActionAttempt,
    "ASSIGN_CREDENTIAL": AssignCredentialActionAttempt,
    "RESET_SANDBOX_WORKSPACE": ResetSandboxWorkspaceActionAttempt,
    "SET_FAN_MODE": SetFanModeActionAttempt,
    "SET_HVAC_MODE": SetHvacModeActionAttempt,
    "ACTIVATE_CLIMATE_PRESET": ActivateClimatePresetActionAttempt,
    "SIMULATE_KEYPAD_CODE_ENTRY": SimulateKeypadCodeEntryActionAttempt,
    "SIMULATE_MANUAL_LOCK_VIA_KEYPAD": SimulateManualLockViaKeypadActionAttempt,
    "PUSH_THERMOSTAT_PROGRAMS": PushThermostatProgramsActionAttempt,
    "CONFIGURE_AUTO_LOCK": ConfigureAutoLockActionAttempt,
    "SYNC_ACCESS_CODES": SyncAccessCodesActionAttempt,
    "CREATE_ACCESS_CODE": CreateAccessCodeActionAttempt,
    "DELETE_ACCESS_CODE": DeleteAccessCodeActionAttempt,
    "UPDATE_ACCESS_CODE": UpdateAccessCodeActionAttempt,
    "CREATE_NOISE_THRESHOLD": CreateNoiseThresholdActionAttempt,
    "DELETE_NOISE_THRESHOLD": DeleteNoiseThresholdActionAttempt,
    "UPDATE_NOISE_THRESHOLD": UpdateNoiseThresholdActionAttempt,
}


def action_attempt_from_dict(d: Any) -> ActionAttempt:
    """Deserialize a known action_type variant.

    Unknown discriminator values return ``DeepAttrDict`` so payloads from a
    newer API remain readable. The static return type covers known variants.
    """
    variant = _ACTION_ATTEMPT_VARIANTS.get(d.get("action_type"))
    if variant is None:
        return cast(ActionAttempt, DeepAttrDict(d))
    return variant.from_dict(d)
