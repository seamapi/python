from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class UnmanagedAccessMethodErrors(ResourceMapping):
    """Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

    :ivar created_at: Date and time at which Seam created the error.

    :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

    :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
    """

    created_at: str
    error_code: str
    message: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            error_code=d.get("error_code", None),
            message=d.get("message", None),
        )


@dataclass
class UnmanagedAccessMethodFrom(ResourceMapping):
    """Previous device configuration.

    :ivar device_ids: Previous device IDs where access was provisioned."""

    device_ids: List[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            device_ids=d.get("device_ids", None),
        )


@dataclass
class UnmanagedAccessMethodTo(ResourceMapping):
    """New device configuration.

    :ivar device_ids: New device IDs where access is being provisioned."""

    device_ids: List[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            device_ids=d.get("device_ids", None),
        )


@dataclass
class UnmanagedAccessMethodPendingMutations(ResourceMapping):
    """Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

    :ivar created_at: Date and time at which the mutation was created.

    :ivar from_: Previous device configuration.

    :ivar message: Detailed description of the mutation.

    :ivar mutation_code: Mutation code to indicate that Seam is in the process of provisioning access for this access method on new devices.

    :ivar to: New device configuration."""

    created_at: str
    from_: UnmanagedAccessMethodFrom
    message: str
    mutation_code: str
    to: UnmanagedAccessMethodTo

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            from_=(
                UnmanagedAccessMethodFrom.from_dict(d.get("from"))
                if d.get("from") is not None
                else None
            ),
            message=d.get("message", None),
            mutation_code=d.get("mutation_code", None),
            to=(
                UnmanagedAccessMethodTo.from_dict(d.get("to"))
                if d.get("to") is not None
                else None
            ),
        )


@dataclass
class UnmanagedAccessMethodWarnings(ResourceMapping):
    """Warnings associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

    :ivar created_at: Date and time at which Seam created the warning.

    :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

    :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

    :ivar original_access_method_id: ID of the original access method from which this backup access method was split, if applicable.
    """

    created_at: str
    message: str
    warning_code: str
    original_access_method_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            message=d.get("message", None),
            warning_code=d.get("warning_code", None),
            original_access_method_id=d.get("original_access_method_id", None),
        )


@dataclass
class UnmanagedAccessMethod:
    """Represents an unmanaged access method. Unmanaged access methods do not have client sessions, instant keys, customization profiles, or keys.

    :ivar access_method_id: ID of the access method.

    :ivar code: The actual PIN code for code access methods.

    :ivar created_at: Date and time at which the access method was created.

    :ivar display_name: Display name of the access method.

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

    access_method_id: str
    code: str
    created_at: str
    display_name: str
    errors: List[UnmanagedAccessMethodErrors]
    is_assignment_required: bool
    is_encoding_required: bool
    is_issued: bool
    is_ready_for_assignment: bool
    is_ready_for_encoding: bool
    issued_at: str
    mode: str
    pending_mutations: List[UnmanagedAccessMethodPendingMutations]
    warnings: List[UnmanagedAccessMethodWarnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            access_method_id=d.get("access_method_id", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=[
                UnmanagedAccessMethodErrors.from_dict(i) for i in d.get("errors") or []
            ],
            is_assignment_required=d.get("is_assignment_required", None),
            is_encoding_required=d.get("is_encoding_required", None),
            is_issued=d.get("is_issued", None),
            is_ready_for_assignment=d.get("is_ready_for_assignment", None),
            is_ready_for_encoding=d.get("is_ready_for_encoding", None),
            issued_at=d.get("issued_at", None),
            mode=d.get("mode", None),
            pending_mutations=[
                UnmanagedAccessMethodPendingMutations.from_dict(i)
                for i in d.get("pending_mutations") or []
            ],
            warnings=[
                UnmanagedAccessMethodWarnings.from_dict(i)
                for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
