from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


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
    class Errors(ResourceMapping):
        """Errors associated with the `access grant <https://docs.seam.co/use-cases/granting-access>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar missing_device_ids: IDs of the devices that did not receive an access code at grant creation. Use these to identify which specific devices failed when the message reports a partial failure.
        """

        created_at: str
        error_code: str
        message: str
        missing_device_ids: List[str]

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
                missing_device_ids=d.get("missing_device_ids", None),
            )

    @dataclass
    class PendingMutations(ResourceMapping):
        """List of pending mutations for the access grant. This shows updates that are in progress.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous location configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of updating the spaces (devices) associated with this access grant.

        :ivar to: New location configuration.

        :ivar access_method_ids: IDs of the access methods being updated."""

        @dataclass
        class From(ResourceMapping):
            """Previous location configuration.

            :ivar device_ids: Previous device IDs where access codes existed."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New location configuration.

            :ivar common_code_key: Common code key to ensure PIN code reuse across devices.

            :ivar device_ids: New device IDs where access codes should be created."""

            common_code_key: str
            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    common_code_key=d.get("common_code_key", None),
                    device_ids=d.get("device_ids", None),
                )

        created_at: str
        from_: From
        message: str
        mutation_code: str
        to: To
        access_method_ids: List[str]

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
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
                access_method_ids=d.get("access_method_ids", None),
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

        code: str
        created_access_method_ids: List[str]
        created_at: str
        display_name: str
        instant_key_max_use_count: int
        mode: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                code=d.get("code", None),
                created_access_method_ids=d.get("created_access_method_ids", None),
                created_at=d.get("created_at", None),
                display_name=d.get("display_name", None),
                instant_key_max_use_count=d.get("instant_key_max_use_count", None),
                mode=d.get("mode", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `access grant <https://docs.seam.co/use-cases/granting-access>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar failed_devices: Devices whose access codes could not be revoked during reconciliation. Present when the provider does not support revoking an offline access code (e.g. Dormakaba oracode with exhausted override budget).

        :ivar access_method_ids: IDs of the access methods being updated.

        :ivar device_id: ID of the device where the requested code was unavailable.

        :ivar new_code: The new PIN code that was assigned instead.

        :ivar original_code: The originally requested PIN code that was unavailable.

        :ivar reason: Specific reason why the grant's times are not programmable on the device.
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
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    device_id=d.get("device_id", None),
                    error_code=d.get("error_code", None),
                    message=d.get("message", None),
                )

        created_at: str
        message: str
        warning_code: str
        failed_devices: List[FailedDevices]
        access_method_ids: List[str]
        device_id: str
        new_code: str
        original_code: str
        reason: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
                failed_devices=[
                    cls.FailedDevices.from_dict(i)
                    for i in d.get("failed_devices") or []
                ],
                access_method_ids=d.get("access_method_ids", None),
                device_id=d.get("device_id", None),
                new_code=d.get("new_code", None),
                original_code=d.get("original_code", None),
                reason=d.get("reason", None),
            )

    access_grant_id: str
    access_grant_key: str
    access_method_ids: List[str]
    client_session_token: str
    created_at: str
    customization_profile_id: str
    display_name: str
    ends_at: str
    errors: List[Errors]
    instant_key_url: str
    location_ids: List[str]
    name: str
    pending_mutations: List[PendingMutations]
    requested_access_methods: List[RequestedAccessMethods]
    reservation_key: str
    space_ids: List[str]
    starts_at: str
    user_identity_id: str
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            access_method_ids=d.get("access_method_ids", None),
            client_session_token=d.get("client_session_token", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            instant_key_url=d.get("instant_key_url", None),
            location_ids=d.get("location_ids", None),
            name=d.get("name", None),
            pending_mutations=[
                cls.PendingMutations.from_dict(i)
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
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
