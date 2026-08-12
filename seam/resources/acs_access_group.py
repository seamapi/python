from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class AcsAccessGroup:
    """Group that defines the entrances to which a set of users has access and, in some cases, the access schedule for these entrances and users.

    Some access control systems use `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_, which are sets of users, combined with sets of permissions. These permissions include both the set of areas or assets that the users can access and the schedule during which the users can access these areas or assets. Instead of assigning access rights individually to each access control system user, which can be time-consuming and error-prone, administrators can assign users to an access group, thereby ensuring that the users inherit all the permissions associated with the access group. Using access groups streamlines the process of managing large numbers of access control system users, especially in bigger organizations or complexes.

    To learn whether your access control system supports access groups, see the corresponding `system integration guide <https://docs.seam.co/device-and-system-integration-guides#access-control-systems>`_.

    :ivar access_group_type: Deprecated: Use ``external_type``.

    :ivar access_group_type_display_name: Deprecated: Use ``external_type_display_name``.

    :ivar access_schedule: ``starts_at`` and ``ends_at`` timestamps for the access group's access.

    :ivar acs_access_group_id: ID of the access group.

    :ivar acs_system_id: ID of the access control system that contains the access group.

    :ivar connected_account_id: ID of the connected account that contains the access group.

    :ivar created_at: Date and time at which the access group was created.

    :ivar display_name: Display name for the access group.

    :ivar errors: Errors associated with the ``acs_access_group``.

    :ivar external_type: Brand-specific terminology for the access group type.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the access group type.

    :ivar is_managed: Indicates whether Seam manages the access group.

    :ivar name: Name of the access group.

    :ivar pending_mutations: Collection of pending mutations for the access group. Represents operations that have been requested but not yet completed on the integrated access system.

    :ivar warnings: Warnings associated with the ``acs_access_group``.

    :ivar workspace_id: ID of the workspace that contains the access group."""

    @dataclass
    class AccessSchedule(ResourceMapping):
        """``starts_at`` and ``ends_at`` timestamps for the access group's access.

        :ivar ends_at: Date and time at which the user's access ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :ivar starts_at: Date and time at which the user's access starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
        """

        ends_at: str
        starts_at: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the ``acs_access_group``.

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
    class PendingMutations(ResourceMapping):
        """Collection of pending mutations for the access group. Represents operations that have been requested but not yet completed on the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code:

        :ivar from_:

        :ivar to:

        :ivar acs_user_id: ID of the user involved in the scheduled change.

        :ivar variant: Whether the user is scheduled to be added to or removed from this access group.
        """

        @dataclass
        class From(ResourceMapping):
            """

            :ivar name: Name of the access group.

            :ivar ends_at: Ending time for the access schedule.

            :ivar starts_at: Starting time for the access schedule.

            :ivar acs_user_id: Old user ID.

            :ivar acs_entrance_id: Old entrance ID."""

            name: str
            ends_at: str
            starts_at: str
            acs_user_id: str
            acs_entrance_id: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    name=d.get("name", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                    acs_user_id=d.get("acs_user_id", None),
                    acs_entrance_id=d.get("acs_entrance_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """

            :ivar name: Name of the access group.

            :ivar ends_at: Ending time for the access schedule.

            :ivar starts_at: Starting time for the access schedule.

            :ivar acs_user_id: New user ID.

            :ivar acs_entrance_id: New entrance ID."""

            name: str
            ends_at: str
            starts_at: str
            acs_user_id: str
            acs_entrance_id: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    name=d.get("name", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                    acs_user_id=d.get("acs_user_id", None),
                    acs_entrance_id=d.get("acs_entrance_id", None),
                )

        created_at: str
        message: str
        mutation_code: str
        from_: From
        to: To
        acs_user_id: str
        variant: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                from_=(
                    cls.From.from_dict(d.get("from"))
                    if d.get("from") is not None
                    else None
                ),
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
                acs_user_id=d.get("acs_user_id", None),
                variant=d.get("variant", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the ``acs_access_group``.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_group_type: str
    access_group_type_display_name: str
    access_schedule: AccessSchedule
    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Errors]
    external_type: str
    external_type_display_name: str
    is_managed: bool
    name: str
    pending_mutations: List[PendingMutations]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            access_schedule=(
                cls.AccessSchedule.from_dict(d.get("access_schedule"))
                if d.get("access_schedule") is not None
                else None
            ),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            pending_mutations=[
                cls.PendingMutations.from_dict(i)
                for i in d.get("pending_mutations") or []
            ],
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
