from typing import Any, Dict, List, Literal, Optional, Union
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
class UnmanagedAccessMethod:
    """Represents an unmanaged access method. Unmanaged access methods do not have client sessions, instant keys, customization profiles, or keys.

    :ivar access_method_id: ID of the access method.

    :ivar code: The actual PIN code for code access methods.

    :ivar created_at: Date and time at which the access method was created.

    :ivar display_name: Display name of the access method.

    :ivar display_status: Human-readable sentence describing where the access method sits in its relationship with the device or access system, for example ``Awaiting encoding``. For display only. The wording is not stable and is not an enumeration — it may change at any time, so never compare against or branch on it. To make decisions, read ``is_issued``, ``errors``, and ``pending_mutations``.

    :ivar errors: Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

    :ivar is_assignment_required: Indicates whether an existing card credential must be assigned to this access method before it can be issued. Only applies to card-mode access methods on systems that support credential assignment.

    :ivar is_encoding_required: Indicates whether encoding with an card encoder is required to issue or reissue the plastic card associated with the access method.

    :ivar is_issued: Indicates whether the access method has been issued.

    :ivar is_ready_for_assignment: Indicates whether the access method is ready for card assignment. This is true when the access method is in card mode, has not yet been issued, and the system supports credential assignment.

    :ivar is_ready_for_encoding: Indicates whether the access method is ready to be encoded. This is true when the credential has been created and the card has not yet been issued.

    :ivar issued_at: Date and time at which the access method was issued.

    :ivar mode: Access method mode. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

    :ivar pending_mutations: Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

    :ivar warnings: Warnings associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

    :ivar workspace_id: ID of the Seam workspace associated with the access method."""

    @dataclass
    class FailedToIssueError(ResourceMapping):
        """Indicates that Seam was unable to issue this `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_ before its access grant started, so the recipient may be unable to access the space. This usually points to a problem that needs attention, such as an offline or disconnected device. Seam keeps retrying, and this error clears automatically if the access method is eventually issued.

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
    class ProvisioningAccessPendingMutation(ResourceMapping):
        """Seam is in the process of provisioning access for this access method on new devices.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous device configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of provisioning access for this access method on new devices.

        :ivar to: New device configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous device configuration.

            :ivar device_ids: Previous device IDs where access was provisioned."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New device configuration.

            :ivar device_ids: New device IDs where access is being provisioned."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["provisioning_access"]
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
    class RevokingAccessPendingMutation(ResourceMapping):
        """Seam is in the process of revoking access for this access method from devices.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous device configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of revoking access for this access method from devices.

        :ivar to: New device configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous device configuration.

            :ivar device_ids: Previous device IDs where access existed."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New device configuration.

            :ivar device_ids: New device IDs where access should remain."""

            device_ids: List[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    device_ids=d.get("device_ids", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["revoking_access"]
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
    class UpdatingAccessTimesPendingMutation(ResourceMapping):
        """Seam is in the process of updating the access times for this access method.

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
        mutation_code: Literal["updating_access_times"]
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
    class BeingDeletedWarning(ResourceMapping):
        """Indicates that the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_ is being deleted.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["being_deleted"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UpdatingAccessTimesWarning(ResourceMapping):
        """Indicates that the access times for this `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_ are being updated.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["updating_access_times"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class PulledBackupAccessCodeWarning(ResourceMapping):
        """Indicates that all attempts to create an access code on this device before the start time failed and a backup access code was used to ensure access was provided in time.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar original_access_method_id: ID of the original access method from which this backup access method was split, if applicable.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        original_access_method_id: Optional[str]
        warning_code: Literal["pulled_backup_access_code"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                original_access_method_id=d.get("original_access_method_id", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DelayInIssuingWarning(ResourceMapping):
        """Indicates that Seam has not yet issued this `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_, even though its access grant is about to begin, so access may not be ready when the recipient arrives. Seam is still attempting to issue it, and this warning clears automatically once issuance succeeds.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["delay_in_issuing"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[FailedToIssueError]
    _ErrorsVariants = {
        "failed_to_issue": FailedToIssueError,
    }

    PendingMutations = Union[
        ProvisioningAccessPendingMutation,
        RevokingAccessPendingMutation,
        UpdatingAccessTimesPendingMutation,
    ]
    _PendingMutationsVariants = {
        "provisioning_access": ProvisioningAccessPendingMutation,
        "revoking_access": RevokingAccessPendingMutation,
        "updating_access_times": UpdatingAccessTimesPendingMutation,
    }

    Warnings = Union[
        BeingDeletedWarning,
        UpdatingAccessTimesWarning,
        PulledBackupAccessCodeWarning,
        DelayInIssuingWarning,
    ]
    _WarningsVariants = {
        "being_deleted": BeingDeletedWarning,
        "updating_access_times": UpdatingAccessTimesWarning,
        "pulled_backup_access_code": PulledBackupAccessCodeWarning,
        "delay_in_issuing": DelayInIssuingWarning,
    }

    access_method_id: str
    code: Optional[str]
    created_at: str
    display_name: str
    display_status: str
    errors: List[Errors]
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
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            display_status=d.get("display_status", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            is_assignment_required=d.get("is_assignment_required", None),
            is_encoding_required=d.get("is_encoding_required", None),
            is_issued=d.get("is_issued", None),
            is_ready_for_assignment=d.get("is_ready_for_assignment", None),
            is_ready_for_encoding=d.get("is_ready_for_encoding", None),
            issued_at=d.get("issued_at", None),
            mode=d.get("mode", None),
            pending_mutations=_discriminated_list_from_dict(
                d.get("pending_mutations"),
                cls._PendingMutationsVariants,
                "mutation_code",
            ),
            warnings=_discriminated_list_from_dict(
                d.get("warnings"), cls._WarningsVariants, "warning_code"
            ),
            workspace_id=d.get("workspace_id", None),
        )
