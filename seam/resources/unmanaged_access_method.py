from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


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

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

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
    class PendingMutations(ResourceMapping):
        """Pending mutations for the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_. Indicates operations that are in progress.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_:

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code:

        :ivar to:"""

        @dataclass
        class From(ResourceMapping):
            """

            :ivar device_ids:

            :ivar ends_at: Previous end time for access.

            :ivar starts_at: Previous start time for access."""

            device_ids: Optional[List[str]]
            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    device_ids=d.get("device_ids", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                )

        @dataclass
        class To(ResourceMapping):
            """

            :ivar device_ids:

            :ivar ends_at: New end time for access.

            :ivar starts_at: New start time for access."""

            device_ids: Optional[List[str]]
            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    device_ids=d.get("device_ids", None),
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
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
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
        warning_code: str
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
    code: Optional[str]
    created_at: str
    display_name: str
    errors: List[Errors]
    is_assignment_required: Optional[bool]
    is_encoding_required: Optional[bool]
    is_issued: bool
    is_ready_for_assignment: Optional[bool]
    is_ready_for_encoding: Optional[bool]
    issued_at: Optional[str]
    mode: str
    pending_mutations: List[PendingMutations]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_method_id=d.get("access_method_id", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
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
