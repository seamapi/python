from typing import Any, Dict, List, Literal, Optional, Tuple, Union, cast
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


@dataclass
class LockDoorSuccessActionAttempt:
    """Locking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of locking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar was_confirmed_by_device: Indicates whether the device confirmed that the lock action occurred.
        """

        was_confirmed_by_device: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                was_confirmed_by_device=d.get("was_confirmed_by_device", None),
            )

    action_attempt_id: str
    action_type: Literal["LOCK_DOOR"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class LockDoorPendingActionAttempt:
    """Locking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of locking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["LOCK_DOOR"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class LockDoorErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["LOCK_DOOR"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UnlockDoorSuccessActionAttempt:
    """Unlocking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of unlocking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar was_confirmed_by_device: Indicates whether the device confirmed that the unlock action occurred.
        """

        was_confirmed_by_device: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                was_confirmed_by_device=d.get("was_confirmed_by_device", None),
            )

    action_attempt_id: str
    action_type: Literal["UNLOCK_DOOR"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class UnlockDoorPendingActionAttempt:
    """Unlocking a door is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of unlocking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["UNLOCK_DOOR"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UnlockDoorErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["UNLOCK_DOOR"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ScanCredentialSuccessActionAttempt:
    """Reading credential data from the physical encoder is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a credential.

    :ivar error:

    :ivar result: Result of scanning a card. If the attempt was successful, includes a snapshot of credential data read from the physical encoder, the corresponding data stored on Seam and the access system, and any associated warnings.

    :ivar status:"""

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
                    if not isinstance(d, dict):
                        d = {}
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    card_number=d.get("card_number", None),
                    created_at=d.get("created_at", None),
                    ends_at=d.get("ends_at", None),
                    is_issued=d.get("is_issued", None),
                    starts_at=d.get("starts_at", None),
                    visionline_metadata=_object_from_dict(
                        cls.VisionlineMetadata, d.get("visionline_metadata")
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
                    if not isinstance(d, dict):
                        d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    access_method=d.get("access_method", None),
                    acs_credential_id=d.get("acs_credential_id", None),
                    acs_credential_pool_id=d.get("acs_credential_pool_id", None),
                    acs_system_id=d.get("acs_system_id", None),
                    acs_user_id=d.get("acs_user_id", None),
                    akiles_metadata=_object_from_dict(
                        cls.AkilesMetadata, d.get("akiles_metadata")
                    ),
                    assa_abloy_vostio_metadata=_object_from_dict(
                        cls.AssaAbloyVostioMetadata, d.get("assa_abloy_vostio_metadata")
                    ),
                    card_number=d.get("card_number", None),
                    code=d.get("code", None),
                    connected_account_id=d.get("connected_account_id", None),
                    created_at=d.get("created_at", None),
                    display_name=d.get("display_name", None),
                    ends_at=d.get("ends_at", None),
                    errors=_object_list_from_dict(cls.Errors, d.get("errors")),
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
                    visionline_metadata=_object_from_dict(
                        cls.VisionlineMetadata, d.get("visionline_metadata")
                    ),
                    warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    warning_code=d.get("warning_code", None),
                    warning_message=d.get("warning_message", None),
                )

        acs_credential_on_encoder: Optional[AcsCredentialOnEncoder]
        acs_credential_on_seam: Optional[AcsCredentialOnSeam]
        warnings: List[Warnings]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                acs_credential_on_encoder=_object_from_dict(
                    cls.AcsCredentialOnEncoder, d.get("acs_credential_on_encoder")
                ),
                acs_credential_on_seam=_object_from_dict(
                    cls.AcsCredentialOnSeam, d.get("acs_credential_on_seam")
                ),
                warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
            )

    action_attempt_id: str
    action_type: Literal["SCAN_CREDENTIAL"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class ScanCredentialPendingActionAttempt:
    """Reading credential data from the physical encoder is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a credential.

    :ivar error:

    :ivar result: Result of scanning a card. If the attempt was successful, includes a snapshot of credential data read from the physical encoder, the corresponding data stored on Seam and the access system, and any associated warnings.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SCAN_CREDENTIAL"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ScanCredentialErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SCAN_CREDENTIAL"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class EncodeCredentialSuccessActionAttempt:
    """Encoding credential data from the physical encoder onto a card is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of encoding credential data from the physical encoder onto a card.

    :ivar error:

    :ivar result: Result of an encoding attempt. If the attempt was successful, includes the credential data that was encoded onto the card.

    :ivar status:"""

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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                access_method=d.get("access_method", None),
                acs_credential_id=d.get("acs_credential_id", None),
                acs_credential_pool_id=d.get("acs_credential_pool_id", None),
                acs_system_id=d.get("acs_system_id", None),
                acs_user_id=d.get("acs_user_id", None),
                akiles_metadata=_object_from_dict(
                    cls.AkilesMetadata, d.get("akiles_metadata")
                ),
                assa_abloy_vostio_metadata=_object_from_dict(
                    cls.AssaAbloyVostioMetadata, d.get("assa_abloy_vostio_metadata")
                ),
                card_number=d.get("card_number", None),
                code=d.get("code", None),
                connected_account_id=d.get("connected_account_id", None),
                created_at=d.get("created_at", None),
                display_name=d.get("display_name", None),
                ends_at=d.get("ends_at", None),
                errors=_object_list_from_dict(cls.Errors, d.get("errors")),
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
                visionline_metadata=_object_from_dict(
                    cls.VisionlineMetadata, d.get("visionline_metadata")
                ),
                warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
                workspace_id=d.get("workspace_id", None),
            )

    action_attempt_id: str
    action_type: Literal["ENCODE_CREDENTIAL"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class EncodeCredentialPendingActionAttempt:
    """Encoding credential data from the physical encoder onto a card is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of encoding credential data from the physical encoder onto a card.

    :ivar error:

    :ivar result: Result of an encoding attempt. If the attempt was successful, includes the credential data that was encoded onto the card.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["ENCODE_CREDENTIAL"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class EncodeCredentialErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["ENCODE_CREDENTIAL"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ScanToAssignCredentialSuccessActionAttempt:
    """Scanning a physical card and assigning the credential is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a physical card and assigning the credential to an ACS user.

    :ivar error:

    :ivar result: Result of a scan to assign attempt. If the attempt was successful, includes the credential data that was scanned and assigned.

    :ivar status:"""

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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
                if not isinstance(d, dict):
                    d = {}
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                access_method=d.get("access_method", None),
                acs_credential_id=d.get("acs_credential_id", None),
                acs_credential_pool_id=d.get("acs_credential_pool_id", None),
                acs_system_id=d.get("acs_system_id", None),
                acs_user_id=d.get("acs_user_id", None),
                akiles_metadata=_object_from_dict(
                    cls.AkilesMetadata, d.get("akiles_metadata")
                ),
                assa_abloy_vostio_metadata=_object_from_dict(
                    cls.AssaAbloyVostioMetadata, d.get("assa_abloy_vostio_metadata")
                ),
                card_number=d.get("card_number", None),
                code=d.get("code", None),
                connected_account_id=d.get("connected_account_id", None),
                created_at=d.get("created_at", None),
                display_name=d.get("display_name", None),
                ends_at=d.get("ends_at", None),
                errors=_object_list_from_dict(cls.Errors, d.get("errors")),
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
                visionline_metadata=_object_from_dict(
                    cls.VisionlineMetadata, d.get("visionline_metadata")
                ),
                warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
                workspace_id=d.get("workspace_id", None),
            )

    action_attempt_id: str
    action_type: Literal["SCAN_TO_ASSIGN_CREDENTIAL"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class ScanToAssignCredentialPendingActionAttempt:
    """Scanning a physical card and assigning the credential is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of scanning a physical card and assigning the credential to an ACS user.

    :ivar error:

    :ivar result: Result of a scan to assign attempt. If the attempt was successful, includes the credential data that was scanned and assigned.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SCAN_TO_ASSIGN_CREDENTIAL"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ScanToAssignCredentialErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SCAN_TO_ASSIGN_CREDENTIAL"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class AssignCredentialSuccessActionAttempt:
    """Assigning a credential to an access method is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of assigning a pre-registered card credential to an access method.

    :ivar error:

    :ivar result: Result of assigning a credential. If successful, includes the updated access method with the assigned credential.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of assigning a credential. If successful, includes the updated access method with the assigned credential.

        :ivar access_method_id: ID of the access method.

        :ivar client_session_token: Token of the client session associated with the access method.

        :ivar code: The actual PIN code for code access methods.

        :ivar created_at: Date and time at which the access method was created.

        :ivar customization_profile_id: ID of the customization profile associated with the access method.

        :ivar display_name: Display name of the access method.

        :ivar display_status: Human-readable sentence describing where the access method sits in its relationship with the device or access system, for example ``Awaiting encoding``. For display only. The wording is not stable and is not an enumeration — it may change at any time, so never compare against or branch on it. To make decisions, read ``is_issued``, ``errors``, and ``pending_mutations``.

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
                if not isinstance(d, dict):
                    d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                    if not isinstance(d, dict):
                        d = {}
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    created_at=d.get("created_at", None),
                    from_=_object_from_dict(cls.From, d.get("from")),
                    message=d.get("message", None),
                    mutation_code=d.get("mutation_code", None),
                    to=_object_from_dict(cls.To, d.get("to")),
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
                if not isinstance(d, dict):
                    d = {}
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
        display_status: str
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                access_method_id=d.get("access_method_id", None),
                client_session_token=d.get("client_session_token", None),
                code=d.get("code", None),
                created_at=d.get("created_at", None),
                customization_profile_id=d.get("customization_profile_id", None),
                display_name=d.get("display_name", None),
                display_status=d.get("display_status", None),
                errors=_object_list_from_dict(cls.Errors, d.get("errors")),
                instant_key_url=d.get("instant_key_url", None),
                is_assignment_required=d.get("is_assignment_required", None),
                is_encoding_required=d.get("is_encoding_required", None),
                is_issued=d.get("is_issued", None),
                is_ready_for_assignment=d.get("is_ready_for_assignment", None),
                is_ready_for_encoding=d.get("is_ready_for_encoding", None),
                issued_at=d.get("issued_at", None),
                mode=d.get("mode", None),
                pending_mutations=_object_list_from_dict(
                    cls.PendingMutations, d.get("pending_mutations")
                ),
                warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
                workspace_id=d.get("workspace_id", None),
            )

    action_attempt_id: str
    action_type: Literal["ASSIGN_CREDENTIAL"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class AssignCredentialPendingActionAttempt:
    """Assigning a credential to an access method is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of assigning a pre-registered card credential to an access method.

    :ivar error:

    :ivar result: Result of assigning a credential. If successful, includes the updated access method with the assigned credential.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["ASSIGN_CREDENTIAL"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class AssignCredentialErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["ASSIGN_CREDENTIAL"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ResetSandboxWorkspaceSuccessActionAttempt:
    """Resetting a sandbox workspace is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of resetting a sandbox workspace.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["RESET_SANDBOX_WORKSPACE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class ResetSandboxWorkspacePendingActionAttempt:
    """Resetting a sandbox workspace is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of resetting a sandbox workspace.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["RESET_SANDBOX_WORKSPACE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ResetSandboxWorkspaceErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["RESET_SANDBOX_WORKSPACE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SetFanModeSuccessActionAttempt:
    """Setting the fan mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the fan mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["SET_FAN_MODE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class SetFanModePendingActionAttempt:
    """Setting the fan mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the fan mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SET_FAN_MODE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SetFanModeErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SET_FAN_MODE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SetHvacModeSuccessActionAttempt:
    """Setting the HVAC mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the HVAC mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["SET_HVAC_MODE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class SetHvacModePendingActionAttempt:
    """Setting the HVAC mode is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of setting the HVAC mode on a thermostat.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SET_HVAC_MODE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SetHvacModeErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SET_HVAC_MODE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ActivateClimatePresetSuccessActionAttempt:
    """Activating a climate preset is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of a climate preset activation.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["ACTIVATE_CLIMATE_PRESET"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class ActivateClimatePresetPendingActionAttempt:
    """Activating a climate preset is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of a climate preset activation.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["ACTIVATE_CLIMATE_PRESET"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ActivateClimatePresetErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["ACTIVATE_CLIMATE_PRESET"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SimulateKeypadCodeEntrySuccessActionAttempt:
    """Simulating a keypad code entry is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a keypad code entry.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["SIMULATE_KEYPAD_CODE_ENTRY"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class SimulateKeypadCodeEntryPendingActionAttempt:
    """Simulating a keypad code entry is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a keypad code entry.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SIMULATE_KEYPAD_CODE_ENTRY"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SimulateKeypadCodeEntryErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SIMULATE_KEYPAD_CODE_ENTRY"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SimulateManualLockViaKeypadSuccessActionAttempt:
    """Simulating a manual lock action using a keypad is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a manual lock action using a keypad.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["SIMULATE_MANUAL_LOCK_VIA_KEYPAD"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class SimulateManualLockViaKeypadPendingActionAttempt:
    """Simulating a manual lock action using a keypad is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of simulating a manual lock action using a keypad.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SIMULATE_MANUAL_LOCK_VIA_KEYPAD"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SimulateManualLockViaKeypadErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SIMULATE_MANUAL_LOCK_VIA_KEYPAD"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class PushThermostatProgramsSuccessActionAttempt:
    """Pushing thermostat weekly programs is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of pushing thermostat programs.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["PUSH_THERMOSTAT_PROGRAMS"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class PushThermostatProgramsPendingActionAttempt:
    """Pushing thermostat weekly programs is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of pushing thermostat programs.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["PUSH_THERMOSTAT_PROGRAMS"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class PushThermostatProgramsErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["PUSH_THERMOSTAT_PROGRAMS"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ConfigureAutoLockSuccessActionAttempt:
    """Configuring the auto-lock is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of configuring the auto-lock on a lock.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["CONFIGURE_AUTO_LOCK"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class ConfigureAutoLockPendingActionAttempt:
    """Configuring the auto-lock is pending.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of configuring the auto-lock on a lock.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["CONFIGURE_AUTO_LOCK"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class ConfigureAutoLockErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["CONFIGURE_AUTO_LOCK"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SyncAccessCodesSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Syncing access codes is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["SYNC_ACCESS_CODES"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class SyncAccessCodesPendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Syncing access codes is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["SYNC_ACCESS_CODES"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class SyncAccessCodesErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["SYNC_ACCESS_CODES"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class CreateAccessCodeSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar access_code: Created access code."""

        access_code: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                access_code=_record_from_dict(d.get("access_code", None)),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_ACCESS_CODE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class CreateAccessCodePendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["CREATE_ACCESS_CODE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class CreateAccessCodeErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_ACCESS_CODE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class DeleteAccessCodeSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["DELETE_ACCESS_CODE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class DeleteAccessCodePendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["DELETE_ACCESS_CODE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class DeleteAccessCodeErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["DELETE_ACCESS_CODE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UpdateAccessCodeSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar access_code: Updated access code."""

        access_code: Optional[Dict[str, Any]]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                access_code=_record_from_dict(d.get("access_code", None)),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_ACCESS_CODE"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class UpdateAccessCodePendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating an access code is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["UPDATE_ACCESS_CODE"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UpdateAccessCodeErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_ACCESS_CODE"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class CreateNoiseThresholdSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar noise_threshold: Created noise threshold."""

        noise_threshold: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                noise_threshold=_record_from_dict(d.get("noise_threshold", None)),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_NOISE_THRESHOLD"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class CreateNoiseThresholdPendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Creating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["CREATE_NOISE_THRESHOLD"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class CreateNoiseThresholdErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["CREATE_NOISE_THRESHOLD"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class DeleteNoiseThresholdSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action."""

        @classmethod
        def from_dict(cls, d: Any):
            # pylint: disable=unused-argument
            if not isinstance(d, dict):
                d = {}
            return cls()

    action_attempt_id: str
    action_type: Literal["DELETE_NOISE_THRESHOLD"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class DeleteNoiseThresholdPendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Deleting a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["DELETE_NOISE_THRESHOLD"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class DeleteNoiseThresholdErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["DELETE_NOISE_THRESHOLD"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UpdateNoiseThresholdSuccessActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    @dataclass
    class Result(ResourceMapping):
        """Result of the action.

        :ivar noise_threshold: Updated noise threshold."""

        noise_threshold: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                noise_threshold=_record_from_dict(d.get("noise_threshold", None)),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_NOISE_THRESHOLD"]
    error: None
    result: Result
    status: Literal["success"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=_required_object_from_dict(cls.Result, d.get("result")),
            status=d.get("status", None),
        )


@dataclass
class UpdateNoiseThresholdPendingActionAttempt:
    """

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Updating a noise threshold is pending.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: Literal["UPDATE_NOISE_THRESHOLD"]
    error: None
    result: None
    status: Literal["pending"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=d.get("error", None),
            result=d.get("result", None),
            status=d.get("status", None),
        )


@dataclass
class UpdateNoiseThresholdErrorActionAttempt:
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                message=d.get("message", None),
                type=d.get("type", None),
            )

    action_attempt_id: str
    action_type: Literal["UPDATE_NOISE_THRESHOLD"]
    error: Error
    result: None
    status: Literal["error"]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=_required_object_from_dict(cls.Error, d.get("error")),
            result=d.get("result", None),
            status=d.get("status", None),
        )


ActionAttempt = Union[
    LockDoorSuccessActionAttempt,
    LockDoorPendingActionAttempt,
    LockDoorErrorActionAttempt,
    UnlockDoorSuccessActionAttempt,
    UnlockDoorPendingActionAttempt,
    UnlockDoorErrorActionAttempt,
    ScanCredentialSuccessActionAttempt,
    ScanCredentialPendingActionAttempt,
    ScanCredentialErrorActionAttempt,
    EncodeCredentialSuccessActionAttempt,
    EncodeCredentialPendingActionAttempt,
    EncodeCredentialErrorActionAttempt,
    ScanToAssignCredentialSuccessActionAttempt,
    ScanToAssignCredentialPendingActionAttempt,
    ScanToAssignCredentialErrorActionAttempt,
    AssignCredentialSuccessActionAttempt,
    AssignCredentialPendingActionAttempt,
    AssignCredentialErrorActionAttempt,
    ResetSandboxWorkspaceSuccessActionAttempt,
    ResetSandboxWorkspacePendingActionAttempt,
    ResetSandboxWorkspaceErrorActionAttempt,
    SetFanModeSuccessActionAttempt,
    SetFanModePendingActionAttempt,
    SetFanModeErrorActionAttempt,
    SetHvacModeSuccessActionAttempt,
    SetHvacModePendingActionAttempt,
    SetHvacModeErrorActionAttempt,
    ActivateClimatePresetSuccessActionAttempt,
    ActivateClimatePresetPendingActionAttempt,
    ActivateClimatePresetErrorActionAttempt,
    SimulateKeypadCodeEntrySuccessActionAttempt,
    SimulateKeypadCodeEntryPendingActionAttempt,
    SimulateKeypadCodeEntryErrorActionAttempt,
    SimulateManualLockViaKeypadSuccessActionAttempt,
    SimulateManualLockViaKeypadPendingActionAttempt,
    SimulateManualLockViaKeypadErrorActionAttempt,
    PushThermostatProgramsSuccessActionAttempt,
    PushThermostatProgramsPendingActionAttempt,
    PushThermostatProgramsErrorActionAttempt,
    ConfigureAutoLockSuccessActionAttempt,
    ConfigureAutoLockPendingActionAttempt,
    ConfigureAutoLockErrorActionAttempt,
    SyncAccessCodesSuccessActionAttempt,
    SyncAccessCodesPendingActionAttempt,
    SyncAccessCodesErrorActionAttempt,
    CreateAccessCodeSuccessActionAttempt,
    CreateAccessCodePendingActionAttempt,
    CreateAccessCodeErrorActionAttempt,
    DeleteAccessCodeSuccessActionAttempt,
    DeleteAccessCodePendingActionAttempt,
    DeleteAccessCodeErrorActionAttempt,
    UpdateAccessCodeSuccessActionAttempt,
    UpdateAccessCodePendingActionAttempt,
    UpdateAccessCodeErrorActionAttempt,
    CreateNoiseThresholdSuccessActionAttempt,
    CreateNoiseThresholdPendingActionAttempt,
    CreateNoiseThresholdErrorActionAttempt,
    DeleteNoiseThresholdSuccessActionAttempt,
    DeleteNoiseThresholdPendingActionAttempt,
    DeleteNoiseThresholdErrorActionAttempt,
    UpdateNoiseThresholdSuccessActionAttempt,
    UpdateNoiseThresholdPendingActionAttempt,
    UpdateNoiseThresholdErrorActionAttempt,
]

LockDoorActionAttempt = Union[
    LockDoorSuccessActionAttempt,
    LockDoorPendingActionAttempt,
    LockDoorErrorActionAttempt,
]

UnlockDoorActionAttempt = Union[
    UnlockDoorSuccessActionAttempt,
    UnlockDoorPendingActionAttempt,
    UnlockDoorErrorActionAttempt,
]

ScanCredentialActionAttempt = Union[
    ScanCredentialSuccessActionAttempt,
    ScanCredentialPendingActionAttempt,
    ScanCredentialErrorActionAttempt,
]

EncodeCredentialActionAttempt = Union[
    EncodeCredentialSuccessActionAttempt,
    EncodeCredentialPendingActionAttempt,
    EncodeCredentialErrorActionAttempt,
]

ScanToAssignCredentialActionAttempt = Union[
    ScanToAssignCredentialSuccessActionAttempt,
    ScanToAssignCredentialPendingActionAttempt,
    ScanToAssignCredentialErrorActionAttempt,
]

AssignCredentialActionAttempt = Union[
    AssignCredentialSuccessActionAttempt,
    AssignCredentialPendingActionAttempt,
    AssignCredentialErrorActionAttempt,
]

ResetSandboxWorkspaceActionAttempt = Union[
    ResetSandboxWorkspaceSuccessActionAttempt,
    ResetSandboxWorkspacePendingActionAttempt,
    ResetSandboxWorkspaceErrorActionAttempt,
]

SetFanModeActionAttempt = Union[
    SetFanModeSuccessActionAttempt,
    SetFanModePendingActionAttempt,
    SetFanModeErrorActionAttempt,
]

SetHvacModeActionAttempt = Union[
    SetHvacModeSuccessActionAttempt,
    SetHvacModePendingActionAttempt,
    SetHvacModeErrorActionAttempt,
]

ActivateClimatePresetActionAttempt = Union[
    ActivateClimatePresetSuccessActionAttempt,
    ActivateClimatePresetPendingActionAttempt,
    ActivateClimatePresetErrorActionAttempt,
]

SimulateKeypadCodeEntryActionAttempt = Union[
    SimulateKeypadCodeEntrySuccessActionAttempt,
    SimulateKeypadCodeEntryPendingActionAttempt,
    SimulateKeypadCodeEntryErrorActionAttempt,
]

SimulateManualLockViaKeypadActionAttempt = Union[
    SimulateManualLockViaKeypadSuccessActionAttempt,
    SimulateManualLockViaKeypadPendingActionAttempt,
    SimulateManualLockViaKeypadErrorActionAttempt,
]

PushThermostatProgramsActionAttempt = Union[
    PushThermostatProgramsSuccessActionAttempt,
    PushThermostatProgramsPendingActionAttempt,
    PushThermostatProgramsErrorActionAttempt,
]

ConfigureAutoLockActionAttempt = Union[
    ConfigureAutoLockSuccessActionAttempt,
    ConfigureAutoLockPendingActionAttempt,
    ConfigureAutoLockErrorActionAttempt,
]

SyncAccessCodesActionAttempt = Union[
    SyncAccessCodesSuccessActionAttempt,
    SyncAccessCodesPendingActionAttempt,
    SyncAccessCodesErrorActionAttempt,
]

CreateAccessCodeActionAttempt = Union[
    CreateAccessCodeSuccessActionAttempt,
    CreateAccessCodePendingActionAttempt,
    CreateAccessCodeErrorActionAttempt,
]

DeleteAccessCodeActionAttempt = Union[
    DeleteAccessCodeSuccessActionAttempt,
    DeleteAccessCodePendingActionAttempt,
    DeleteAccessCodeErrorActionAttempt,
]

UpdateAccessCodeActionAttempt = Union[
    UpdateAccessCodeSuccessActionAttempt,
    UpdateAccessCodePendingActionAttempt,
    UpdateAccessCodeErrorActionAttempt,
]

CreateNoiseThresholdActionAttempt = Union[
    CreateNoiseThresholdSuccessActionAttempt,
    CreateNoiseThresholdPendingActionAttempt,
    CreateNoiseThresholdErrorActionAttempt,
]

DeleteNoiseThresholdActionAttempt = Union[
    DeleteNoiseThresholdSuccessActionAttempt,
    DeleteNoiseThresholdPendingActionAttempt,
    DeleteNoiseThresholdErrorActionAttempt,
]

UpdateNoiseThresholdActionAttempt = Union[
    UpdateNoiseThresholdSuccessActionAttempt,
    UpdateNoiseThresholdPendingActionAttempt,
    UpdateNoiseThresholdErrorActionAttempt,
]

SuccessActionAttempt = Union[
    LockDoorSuccessActionAttempt,
    UnlockDoorSuccessActionAttempt,
    ScanCredentialSuccessActionAttempt,
    EncodeCredentialSuccessActionAttempt,
    ScanToAssignCredentialSuccessActionAttempt,
    AssignCredentialSuccessActionAttempt,
    ResetSandboxWorkspaceSuccessActionAttempt,
    SetFanModeSuccessActionAttempt,
    SetHvacModeSuccessActionAttempt,
    ActivateClimatePresetSuccessActionAttempt,
    SimulateKeypadCodeEntrySuccessActionAttempt,
    SimulateManualLockViaKeypadSuccessActionAttempt,
    PushThermostatProgramsSuccessActionAttempt,
    ConfigureAutoLockSuccessActionAttempt,
    SyncAccessCodesSuccessActionAttempt,
    CreateAccessCodeSuccessActionAttempt,
    DeleteAccessCodeSuccessActionAttempt,
    UpdateAccessCodeSuccessActionAttempt,
    CreateNoiseThresholdSuccessActionAttempt,
    DeleteNoiseThresholdSuccessActionAttempt,
    UpdateNoiseThresholdSuccessActionAttempt,
]

PendingActionAttempt = Union[
    LockDoorPendingActionAttempt,
    UnlockDoorPendingActionAttempt,
    ScanCredentialPendingActionAttempt,
    EncodeCredentialPendingActionAttempt,
    ScanToAssignCredentialPendingActionAttempt,
    AssignCredentialPendingActionAttempt,
    ResetSandboxWorkspacePendingActionAttempt,
    SetFanModePendingActionAttempt,
    SetHvacModePendingActionAttempt,
    ActivateClimatePresetPendingActionAttempt,
    SimulateKeypadCodeEntryPendingActionAttempt,
    SimulateManualLockViaKeypadPendingActionAttempt,
    PushThermostatProgramsPendingActionAttempt,
    ConfigureAutoLockPendingActionAttempt,
    SyncAccessCodesPendingActionAttempt,
    CreateAccessCodePendingActionAttempt,
    DeleteAccessCodePendingActionAttempt,
    UpdateAccessCodePendingActionAttempt,
    CreateNoiseThresholdPendingActionAttempt,
    DeleteNoiseThresholdPendingActionAttempt,
    UpdateNoiseThresholdPendingActionAttempt,
]

ErrorActionAttempt = Union[
    LockDoorErrorActionAttempt,
    UnlockDoorErrorActionAttempt,
    ScanCredentialErrorActionAttempt,
    EncodeCredentialErrorActionAttempt,
    ScanToAssignCredentialErrorActionAttempt,
    AssignCredentialErrorActionAttempt,
    ResetSandboxWorkspaceErrorActionAttempt,
    SetFanModeErrorActionAttempt,
    SetHvacModeErrorActionAttempt,
    ActivateClimatePresetErrorActionAttempt,
    SimulateKeypadCodeEntryErrorActionAttempt,
    SimulateManualLockViaKeypadErrorActionAttempt,
    PushThermostatProgramsErrorActionAttempt,
    ConfigureAutoLockErrorActionAttempt,
    SyncAccessCodesErrorActionAttempt,
    CreateAccessCodeErrorActionAttempt,
    DeleteAccessCodeErrorActionAttempt,
    UpdateAccessCodeErrorActionAttempt,
    CreateNoiseThresholdErrorActionAttempt,
    DeleteNoiseThresholdErrorActionAttempt,
    UpdateNoiseThresholdErrorActionAttempt,
]

_ACTION_ATTEMPT_VARIANTS: Dict[Tuple[str, str], Any] = {
    ("LOCK_DOOR", "success"): LockDoorSuccessActionAttempt,
    ("LOCK_DOOR", "pending"): LockDoorPendingActionAttempt,
    ("LOCK_DOOR", "error"): LockDoorErrorActionAttempt,
    ("UNLOCK_DOOR", "success"): UnlockDoorSuccessActionAttempt,
    ("UNLOCK_DOOR", "pending"): UnlockDoorPendingActionAttempt,
    ("UNLOCK_DOOR", "error"): UnlockDoorErrorActionAttempt,
    ("SCAN_CREDENTIAL", "success"): ScanCredentialSuccessActionAttempt,
    ("SCAN_CREDENTIAL", "pending"): ScanCredentialPendingActionAttempt,
    ("SCAN_CREDENTIAL", "error"): ScanCredentialErrorActionAttempt,
    ("ENCODE_CREDENTIAL", "success"): EncodeCredentialSuccessActionAttempt,
    ("ENCODE_CREDENTIAL", "pending"): EncodeCredentialPendingActionAttempt,
    ("ENCODE_CREDENTIAL", "error"): EncodeCredentialErrorActionAttempt,
    (
        "SCAN_TO_ASSIGN_CREDENTIAL",
        "success",
    ): ScanToAssignCredentialSuccessActionAttempt,
    (
        "SCAN_TO_ASSIGN_CREDENTIAL",
        "pending",
    ): ScanToAssignCredentialPendingActionAttempt,
    ("SCAN_TO_ASSIGN_CREDENTIAL", "error"): ScanToAssignCredentialErrorActionAttempt,
    ("ASSIGN_CREDENTIAL", "success"): AssignCredentialSuccessActionAttempt,
    ("ASSIGN_CREDENTIAL", "pending"): AssignCredentialPendingActionAttempt,
    ("ASSIGN_CREDENTIAL", "error"): AssignCredentialErrorActionAttempt,
    ("RESET_SANDBOX_WORKSPACE", "success"): ResetSandboxWorkspaceSuccessActionAttempt,
    ("RESET_SANDBOX_WORKSPACE", "pending"): ResetSandboxWorkspacePendingActionAttempt,
    ("RESET_SANDBOX_WORKSPACE", "error"): ResetSandboxWorkspaceErrorActionAttempt,
    ("SET_FAN_MODE", "success"): SetFanModeSuccessActionAttempt,
    ("SET_FAN_MODE", "pending"): SetFanModePendingActionAttempt,
    ("SET_FAN_MODE", "error"): SetFanModeErrorActionAttempt,
    ("SET_HVAC_MODE", "success"): SetHvacModeSuccessActionAttempt,
    ("SET_HVAC_MODE", "pending"): SetHvacModePendingActionAttempt,
    ("SET_HVAC_MODE", "error"): SetHvacModeErrorActionAttempt,
    ("ACTIVATE_CLIMATE_PRESET", "success"): ActivateClimatePresetSuccessActionAttempt,
    ("ACTIVATE_CLIMATE_PRESET", "pending"): ActivateClimatePresetPendingActionAttempt,
    ("ACTIVATE_CLIMATE_PRESET", "error"): ActivateClimatePresetErrorActionAttempt,
    (
        "SIMULATE_KEYPAD_CODE_ENTRY",
        "success",
    ): SimulateKeypadCodeEntrySuccessActionAttempt,
    (
        "SIMULATE_KEYPAD_CODE_ENTRY",
        "pending",
    ): SimulateKeypadCodeEntryPendingActionAttempt,
    ("SIMULATE_KEYPAD_CODE_ENTRY", "error"): SimulateKeypadCodeEntryErrorActionAttempt,
    (
        "SIMULATE_MANUAL_LOCK_VIA_KEYPAD",
        "success",
    ): SimulateManualLockViaKeypadSuccessActionAttempt,
    (
        "SIMULATE_MANUAL_LOCK_VIA_KEYPAD",
        "pending",
    ): SimulateManualLockViaKeypadPendingActionAttempt,
    (
        "SIMULATE_MANUAL_LOCK_VIA_KEYPAD",
        "error",
    ): SimulateManualLockViaKeypadErrorActionAttempt,
    ("PUSH_THERMOSTAT_PROGRAMS", "success"): PushThermostatProgramsSuccessActionAttempt,
    ("PUSH_THERMOSTAT_PROGRAMS", "pending"): PushThermostatProgramsPendingActionAttempt,
    ("PUSH_THERMOSTAT_PROGRAMS", "error"): PushThermostatProgramsErrorActionAttempt,
    ("CONFIGURE_AUTO_LOCK", "success"): ConfigureAutoLockSuccessActionAttempt,
    ("CONFIGURE_AUTO_LOCK", "pending"): ConfigureAutoLockPendingActionAttempt,
    ("CONFIGURE_AUTO_LOCK", "error"): ConfigureAutoLockErrorActionAttempt,
    ("SYNC_ACCESS_CODES", "success"): SyncAccessCodesSuccessActionAttempt,
    ("SYNC_ACCESS_CODES", "pending"): SyncAccessCodesPendingActionAttempt,
    ("SYNC_ACCESS_CODES", "error"): SyncAccessCodesErrorActionAttempt,
    ("CREATE_ACCESS_CODE", "success"): CreateAccessCodeSuccessActionAttempt,
    ("CREATE_ACCESS_CODE", "pending"): CreateAccessCodePendingActionAttempt,
    ("CREATE_ACCESS_CODE", "error"): CreateAccessCodeErrorActionAttempt,
    ("DELETE_ACCESS_CODE", "success"): DeleteAccessCodeSuccessActionAttempt,
    ("DELETE_ACCESS_CODE", "pending"): DeleteAccessCodePendingActionAttempt,
    ("DELETE_ACCESS_CODE", "error"): DeleteAccessCodeErrorActionAttempt,
    ("UPDATE_ACCESS_CODE", "success"): UpdateAccessCodeSuccessActionAttempt,
    ("UPDATE_ACCESS_CODE", "pending"): UpdateAccessCodePendingActionAttempt,
    ("UPDATE_ACCESS_CODE", "error"): UpdateAccessCodeErrorActionAttempt,
    ("CREATE_NOISE_THRESHOLD", "success"): CreateNoiseThresholdSuccessActionAttempt,
    ("CREATE_NOISE_THRESHOLD", "pending"): CreateNoiseThresholdPendingActionAttempt,
    ("CREATE_NOISE_THRESHOLD", "error"): CreateNoiseThresholdErrorActionAttempt,
    ("DELETE_NOISE_THRESHOLD", "success"): DeleteNoiseThresholdSuccessActionAttempt,
    ("DELETE_NOISE_THRESHOLD", "pending"): DeleteNoiseThresholdPendingActionAttempt,
    ("DELETE_NOISE_THRESHOLD", "error"): DeleteNoiseThresholdErrorActionAttempt,
    ("UPDATE_NOISE_THRESHOLD", "success"): UpdateNoiseThresholdSuccessActionAttempt,
    ("UPDATE_NOISE_THRESHOLD", "pending"): UpdateNoiseThresholdPendingActionAttempt,
    ("UPDATE_NOISE_THRESHOLD", "error"): UpdateNoiseThresholdErrorActionAttempt,
}


def action_attempt_from_dict(d: Any) -> ActionAttempt:
    """Deserialize a known action_type and status variant.

    An unrecognized discriminator, or a known one whose payload does not
    convert, returns ``DeepAttrDict`` so payloads from a newer API remain
    readable. The static return type covers known variants.
    """
    if not isinstance(d, dict):
        return cast(ActionAttempt, DeepAttrDict(d) if isinstance(d, dict) else d)
    key = (d.get("action_type"), d.get("status"))
    variant = (
        _ACTION_ATTEMPT_VARIANTS.get(cast(Tuple[str, str], key))
        if isinstance(key[0], str) and isinstance(key[1], str)
        else None
    )
    if variant is None:
        return cast(ActionAttempt, DeepAttrDict(d))
    try:
        return variant.from_dict(d)
    except Exception:  # pylint: disable=broad-exception-caught
        return cast(ActionAttempt, DeepAttrDict(d))
