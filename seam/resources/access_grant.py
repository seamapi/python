from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


def _from_discriminated_dict(
    d: Any, variants: Dict[str, Any], discriminator: str
) -> Any:
    variant = variants.get(d.get(discriminator))
    return DeepAttrDict(d) if variant is None else variant.from_dict(d)


@dataclass
class AccessGrant:
    """Represents an Access Grant. Access Grants enable you to grant a user identity access to spaces, entrances, and devices through one or more access methods, such as mobile keys, plastic cards, and PIN codes. You can create an Access Grant for an existing user identity, or you can create a new user identity *while* creating the new Access Grant.

    :ivar access_grant_id: ID of the Access Grant.

    :ivar access_grant_key: Unique key for the access grant within the workspace.

    :ivar access_method_ids: IDs of the access methods created for the Access Grant.

    :ivar client_session_token: Client Session Token. Only returned if the Access Grant has a mobile_key access method.

    :ivar created_at: Date and time at which the Access Grant was created.

    :ivar customization_profile_id: ID of the customization profile associated with the Access Grant.

    :ivar display_name: Display name of the Access Grant.

    :ivar display_status: Human-readable sentence answering whether the user can currently get in, for example ``Awaiting encoding`` on an access method or ``Upcoming`` here. For display only. The wording is not stable and is not an enumeration — it may change at any time, so never compare against or branch on it. To make decisions, read ``starts_at``, ``ends_at``, ``errors``, and the access methods' own fields.

    :ivar ends_at: Date and time at which the Access Grant ends.

    :ivar errors: Errors associated with the `access grant <https://docs.seam.co/use-cases/granting-access>`_.

    :ivar instant_key_url: Instant Key URL. Only returned if the Access Grant has a single mobile_key access_method.

    :ivar location_ids: Deprecated: Use ``space_ids``.

    :ivar name: Name of the Access Grant. If not provided, the display name will be computed.

    :ivar pending_mutations: List of pending mutations for the access grant. This shows updates that are in progress.

    :ivar requested_access_methods: Access methods that the user requested for the Access Grant.

    :ivar reservation_key: Reservation key for the access grant.

    :ivar space_ids: IDs of the spaces to which the Access Grant gives access.

    :ivar starts_at: Date and time at which the Access Grant starts.

    :ivar user_identity_id: ID of user identity to which the Access Grant gives access.

    :ivar warnings: Warnings associated with the `access grant <https://docs.seam.co/use-cases/granting-access>`_.

    :ivar workspace_id: ID of the Seam workspace associated with the Access Grant."""

    @dataclass
    class CannotCreateRequestedAccessMethodsError(ResourceMapping):
        """Indicates that Seam could not create one or more of the requested access methods for the access grant.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar missing_device_ids: IDs of the devices that did not receive an access code at grant creation. Use these to identify which specific devices failed when the message reports a partial failure.
        """

        created_at: str
        error_code: Literal["cannot_create_requested_access_methods"]
        message: str
        missing_device_ids: Optional[List[str]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
                missing_device_ids=d.get("missing_device_ids", None),
            )

    @dataclass
    class UpdatingSpacesPendingMutation(ResourceMapping):
        """Seam is in the process of updating the devices/spaces associated with this access grant.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous location configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of updating the spaces (devices) associated with this access grant.

        :ivar to: New location configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous location configuration.

            :ivar device_ids: Previous device IDs where access codes existed."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New location configuration.

            :ivar common_code_key: Common code key to ensure PIN code reuse across devices.

            :ivar device_ids: New device IDs where access codes should be created."""

            common_code_key: Optional[str]
            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    common_code_key=d.get("common_code_key", None),
                    device_ids=d.get("device_ids", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_spaces"]
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
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            )

    @dataclass
    class UpdatingAccessTimesPendingMutation(ResourceMapping):
        """Seam is in the process of updating the access times for this access grant.

        :ivar access_method_ids: IDs of the access methods being updated.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous access time configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of updating the access times for this access grant.

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

        access_method_ids: List[str]
        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_access_times"]
        to: Optional[To]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                access_method_ids=d.get("access_method_ids", None),
                created_at=d.get("created_at", None),
                from_=(
                    cls.From.from_dict(d.get("from"))
                    if d.get("from") is not None
                    else None
                ),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            )

    @dataclass
    class RequestedAccessMethods(ResourceMapping):
        """Access methods that the user requested for the Access Grant.

        :ivar code: Specific PIN code to use for this access method. Only applicable when mode is 'code'.

        :ivar created_access_method_ids: IDs of the access methods created for the requested access method.

        :ivar created_at: Date and time at which the requested access method was added to the Access Grant.

        :ivar display_name: Display name of the access method.

        :ivar instant_key_max_use_count: Maximum number of times the instant key can be used. Only applicable when mode is 'mobile_key'. Defaults to 1 if not specified.

        :ivar mode: Access method mode. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.
        """

        code: Optional[str]
        created_access_method_ids: List[str]
        created_at: str
        display_name: str
        instant_key_max_use_count: Optional[int]
        mode: Literal["code", "card", "mobile_key", "cloud_key"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                code=d.get("code", None),
                created_access_method_ids=d.get("created_access_method_ids", None),
                created_at=d.get("created_at", None),
                display_name=d.get("display_name", None),
                instant_key_max_use_count=d.get("instant_key_max_use_count", None),
                mode=d.get("mode", None),
            )

    @dataclass
    class BeingDeletedWarning(ResourceMapping):
        """Indicates that the `access grant <https://docs.seam.co/use-cases/granting-access>`_ is being deleted.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["being_deleted"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnderprovisionedAccessWarning(ResourceMapping):
        """Indicates that the access grant should have access to more locations than it currently does. Access methods are being created for the missing locations.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["underprovisioned_access"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class OverprovisionedAccessWarning(ResourceMapping):
        """Indicates that the access grant has access to locations it should not have. Access methods are being removed from the extra locations.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar failed_devices: Devices whose access codes could not be revoked during reconciliation. Present when the provider does not support revoking an offline access code (e.g. Dormakaba oracode with exhausted override budget).

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        @dataclass
        class FailedDevices(ResourceMapping):
            """Devices whose access codes could not be revoked during reconciliation. Present when the provider does not support revoking an offline access code (e.g. Dormakaba oracode with exhausted override budget).

            :ivar device_id: Device whose access code could not be revoked.

            :ivar error_code: Reason the access code could not be revoked (e.g. ``offline_access_code_not_revocable``).

            :ivar message: Human-readable description of why revocation failed."""

            device_id: str
            error_code: str
            message: str

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    device_id=d.get("device_id", None),
                    error_code=d.get("error_code", None),
                    message=d.get("message", None),
                )

        created_at: str
        failed_devices: Optional[List[FailedDevices]]
        message: str
        warning_code: Literal["overprovisioned_access"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                failed_devices=[
                    cls.FailedDevices.from_dict(i)
                    for i in d.get("failed_devices") or []
                ],
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UpdatingAccessTimesWarning(ResourceMapping):
        """Indicates that the access times for this `access grant <https://docs.seam.co/use-cases/granting-access>`_ are being updated.

        :ivar access_method_ids: IDs of the access methods being updated.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        access_method_ids: List[str]
        created_at: str
        message: str
        warning_code: Literal["updating_access_times"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                access_method_ids=d.get("access_method_ids", None),
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class RequestedCodeUnavailableWarning(ResourceMapping):
        """Indicates that the requested PIN code was already in use on a device, so a different code was assigned.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar device_id: ID of the device where the requested code was unavailable.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar new_code: The new PIN code that was assigned instead.

        :ivar original_code: The originally requested PIN code that was unavailable.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        device_id: str
        message: str
        new_code: str
        original_code: str
        warning_code: Literal["requested_code_unavailable"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                device_id=d.get("device_id", None),
                message=d.get("message", None),
                new_code=d.get("new_code", None),
                original_code=d.get("original_code", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceDoesNotSupportAccessCodesWarning(ResourceMapping):
        """Indicates that a device in the access grant does not support access codes and was excluded from code materialization.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar device_id: ID of the device that does not support access codes.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        device_id: str
        message: str
        warning_code: Literal["device_does_not_support_access_codes"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                device_id=d.get("device_id", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceTimeConstraintsViolatedWarning(ResourceMapping):
        """Indicates that a device in the access grant cannot program an access code for the grant's time range because of device-specific time constraints.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar device_id: ID of the device whose time constraints the access grant violates.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar reason: Specific reason why the grant's times are not programmable on the device.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        device_id: str
        message: str
        reason: Literal[
            "duration_exceeds_max", "times_do_not_match_slots", "ongoing_not_supported"
        ]
        warning_code: Literal["device_time_constraints_violated"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                device_id=d.get("device_id", None),
                message=d.get("message", None),
                reason=d.get("reason", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[CannotCreateRequestedAccessMethodsError]
    _ErrorsVariants = {
        "cannot_create_requested_access_methods": CannotCreateRequestedAccessMethodsError,
    }

    PendingMutations = Union[
        UpdatingSpacesPendingMutation, UpdatingAccessTimesPendingMutation
    ]
    _PendingMutationsVariants = {
        "updating_spaces": UpdatingSpacesPendingMutation,
        "updating_access_times": UpdatingAccessTimesPendingMutation,
    }

    Warnings = Union[
        BeingDeletedWarning,
        UnderprovisionedAccessWarning,
        OverprovisionedAccessWarning,
        UpdatingAccessTimesWarning,
        RequestedCodeUnavailableWarning,
        DeviceDoesNotSupportAccessCodesWarning,
        DeviceTimeConstraintsViolatedWarning,
    ]
    _WarningsVariants = {
        "being_deleted": BeingDeletedWarning,
        "underprovisioned_access": UnderprovisionedAccessWarning,
        "overprovisioned_access": OverprovisionedAccessWarning,
        "updating_access_times": UpdatingAccessTimesWarning,
        "requested_code_unavailable": RequestedCodeUnavailableWarning,
        "device_does_not_support_access_codes": DeviceDoesNotSupportAccessCodesWarning,
        "device_time_constraints_violated": DeviceTimeConstraintsViolatedWarning,
    }

    access_grant_id: str
    access_grant_key: Optional[str]
    access_method_ids: List[str]
    client_session_token: Optional[str]
    created_at: str
    customization_profile_id: Optional[str]
    display_name: str
    display_status: str
    ends_at: Optional[str]
    errors: List[Errors]
    instant_key_url: Optional[str]
    location_ids: List[str]
    name: Optional[str]
    pending_mutations: List[PendingMutations]
    requested_access_methods: List[RequestedAccessMethods]
    reservation_key: Optional[str]
    space_ids: List[str]
    starts_at: str
    user_identity_id: str
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            access_method_ids=d.get("access_method_ids", None),
            client_session_token=d.get("client_session_token", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            display_status=d.get("display_status", None),
            ends_at=d.get("ends_at", None),
            errors=[
                _from_discriminated_dict(i, cls._ErrorsVariants, "error_code")
                for i in d.get("errors") or []
            ],
            instant_key_url=d.get("instant_key_url", None),
            location_ids=d.get("location_ids", None),
            name=d.get("name", None),
            pending_mutations=[
                _from_discriminated_dict(
                    i, cls._PendingMutationsVariants, "mutation_code"
                )
                for i in d.get("pending_mutations") or []
            ],
            requested_access_methods=[
                cls.RequestedAccessMethods.from_dict(i)
                for i in d.get("requested_access_methods") or []
            ],
            reservation_key=d.get("reservation_key", None),
            space_ids=d.get("space_ids", None),
            starts_at=d.get("starts_at", None),
            user_identity_id=d.get("user_identity_id", None),
            warnings=[
                _from_discriminated_dict(i, cls._WarningsVariants, "warning_code")
                for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
