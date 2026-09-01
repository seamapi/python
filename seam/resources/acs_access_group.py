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

        ends_at: Optional[str]
        starts_at: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class FailedToCreateOnAcsSystemError(ResourceMapping):
        """Indicates that the `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_ was not created on the `access system <https://docs.seam.co/low-level-apis/access-systems>`_. This is likely due to an internal unexpected error. Contact Seam `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["failed_to_create_on_acs_system"]
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
    class CreatingPendingMutation(ResourceMapping):
        """Seam is in the process of pushing an access group creation to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing an access group creation to the integrated access system.
        """

        created_at: str
        message: str
        mutation_code: Literal["creating"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class DeletingPendingMutation(ResourceMapping):
        """Seam is in the process of pushing an access group deletion to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing an access group deletion to the integrated access system.
        """

        created_at: str
        message: str
        mutation_code: Literal["deleting"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class DeferringDeletionPendingMutation(ResourceMapping):
        """This access group is scheduled for automatic deletion when its access window expires.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that this access group is scheduled for automatic deletion when its access window expires.
        """

        created_at: str
        message: str
        mutation_code: Literal["deferring_deletion"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class UpdatingGroupInformationPendingMutation(ResourceMapping):
        """Seam is in the process of pushing an access group information update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old access group information.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated access group information to the integrated access system.

        :ivar to: New access group information."""

        @dataclass
        class From(ResourceMapping):
            """Old access group information.

            :ivar name: Name of the access group."""

            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    name=d.get("name", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New access group information.

            :ivar name: Name of the access group."""

            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    name=d.get("name", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_group_information"]
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
    class UpdatingAccessSchedulePendingMutation(ResourceMapping):
        """Seam is in the process of pushing an access schedule update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old access schedule information.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated access schedule information to the integrated access system.

        :ivar to: New access schedule information."""

        @dataclass
        class From(ResourceMapping):
            """Old access schedule information.

            :ivar ends_at: Ending time for the access schedule.

            :ivar starts_at: Starting time for the access schedule."""

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
            """New access schedule information.

            :ivar ends_at: Ending time for the access schedule.

            :ivar starts_at: Starting time for the access schedule."""

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
        mutation_code: Literal["updating_access_schedule"]
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
    class UpdatingUserMembershipPendingMutation(ResourceMapping):
        """Seam is in the process of pushing a user membership update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old user membership.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated user membership information to the integrated access system.

        :ivar to: New user membership."""

        @dataclass
        class From(ResourceMapping):
            """Old user membership.

            :ivar acs_user_id: Old user ID."""

            acs_user_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    acs_user_id=d.get("acs_user_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New user membership.

            :ivar acs_user_id: New user ID."""

            acs_user_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    acs_user_id=d.get("acs_user_id", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_user_membership"]
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
    class UpdatingEntranceMembershipPendingMutation(ResourceMapping):
        """Seam is in the process of pushing an entrance membership update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old entrance membership.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated entrance membership information to the integrated access system.

        :ivar to: New entrance membership."""

        @dataclass
        class From(ResourceMapping):
            """Old entrance membership.

            :ivar acs_entrance_id: Old entrance ID."""

            acs_entrance_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    acs_entrance_id=d.get("acs_entrance_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New entrance membership.

            :ivar acs_entrance_id: New entrance ID."""

            acs_entrance_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    acs_entrance_id=d.get("acs_entrance_id", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_entrance_membership"]
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
    class DeferringUserMembershipUpdatePendingMutation(ResourceMapping):
        """A scheduled user membership change is pending for this access group.

        :ivar acs_user_id: ID of the user involved in the scheduled change.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that a scheduled user membership change is pending for this access group.

        :ivar variant: Whether the user is scheduled to be added to or removed from this access group.
        """

        acs_user_id: str
        created_at: str
        message: str
        mutation_code: Literal["deferring_user_membership_update"]
        variant: Literal["adding", "removing"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                acs_user_id=d.get("acs_user_id", None),
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
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
        warning_code: Literal["unknown_issue_with_acs_access_group", "being_deleted"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[FailedToCreateOnAcsSystemError]
    _ErrorsVariants = {
        "failed_to_create_on_acs_system": FailedToCreateOnAcsSystemError,
    }

    PendingMutations = Union[
        CreatingPendingMutation,
        DeletingPendingMutation,
        DeferringDeletionPendingMutation,
        UpdatingGroupInformationPendingMutation,
        UpdatingAccessSchedulePendingMutation,
        UpdatingUserMembershipPendingMutation,
        UpdatingEntranceMembershipPendingMutation,
        DeferringUserMembershipUpdatePendingMutation,
    ]
    _PendingMutationsVariants = {
        "creating": CreatingPendingMutation,
        "deleting": DeletingPendingMutation,
        "deferring_deletion": DeferringDeletionPendingMutation,
        "updating_group_information": UpdatingGroupInformationPendingMutation,
        "updating_access_schedule": UpdatingAccessSchedulePendingMutation,
        "updating_user_membership": UpdatingUserMembershipPendingMutation,
        "updating_entrance_membership": UpdatingEntranceMembershipPendingMutation,
        "deferring_user_membership_update": DeferringUserMembershipUpdatePendingMutation,
    }

    access_group_type: Literal[
        "pti_unit",
        "pti_access_level",
        "salto_ks_access_group",
        "brivo_group",
        "salto_space_group",
        "dormakaba_community_access_group",
        "dormakaba_ambiance_access_group",
        "avigilon_alta_group",
        "kisi_access_group",
        "akiles_member_group",
    ]
    access_group_type_display_name: str
    access_schedule: Optional[AccessSchedule]
    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Errors]
    external_type: Literal[
        "pti_unit",
        "pti_access_level",
        "salto_ks_access_group",
        "brivo_group",
        "salto_space_group",
        "dormakaba_community_access_group",
        "dormakaba_ambiance_access_group",
        "avigilon_alta_group",
        "kisi_access_group",
        "akiles_member_group",
    ]
    external_type_display_name: str
    is_managed: Literal[True]
    name: str
    pending_mutations: List[PendingMutations]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            access_schedule=_object_from_dict(
                cls.AccessSchedule, d.get("access_schedule")
            ),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            pending_mutations=_discriminated_list_from_dict(
                d.get("pending_mutations"),
                cls._PendingMutationsVariants,
                "mutation_code",
            ),
            warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
            workspace_id=d.get("workspace_id", None),
        )
