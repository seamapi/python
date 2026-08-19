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
class AcsUser:
    """Represents a `user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in an `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

    An access system user typically refers to an individual who requires access, like an employee or resident. Each user can possess multiple credentials that serve as their keys or identifiers for access. The type of credential can vary widely. For example, in the Salto system, a user can have a PIN code, a mobile app account, and a fob. In other platforms, it is not uncommon for a user to have more than one of the same credential type, such as multiple key cards. Additionally, these credentials can have a schedule or validity period.

    For details about how to configure users in your access system, see the corresponding `system integration guide <https://docs.seam.co/device-and-system-integration-guides#access-control-systems>`_.

    :ivar access_schedule: ``starts_at`` and ``ends_at`` timestamps for the `access system user's <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access.

    :ivar acs_system_id: ID of the `access system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar acs_user_id: ID of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar connected_account_id: The ID of the connected account that is associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar created_at: Date and time at which the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was created.

    :ivar display_name: Display name for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar email: Deprecated: use email_address.

    :ivar email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar errors: Errors associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar external_type: Brand-specific terminology for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ type.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ type.

    :ivar full_name: Full name of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar hid_acs_system_id: ID of the HID access control system associated with the user.

    :ivar is_managed: Indicates whether Seam manages the access system user.

    :ivar is_suspended: Indicates whether the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ is currently `suspended <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users>`_.

    :ivar pending_mutations: Pending mutations associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. Seam is in the process of pushing these mutations to the integrated access system.

    :ivar phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

    :ivar salto_ks_metadata: Salto KS-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar salto_space_metadata: Salto Space-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_email_address: Email address of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_full_name: Full name of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_id: ID of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar user_identity_phone_number: Phone number of the user identity associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

    :ivar warnings: Warnings associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

    :ivar workspace_id: ID of the workspace that contains the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.
    """

    @dataclass
    class AccessSchedule(ResourceMapping):
        """``starts_at`` and ``ends_at`` timestamps for the `access system user's <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access.

        :ivar ends_at: Date and time at which the user's access ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :ivar starts_at: Date and time at which the user's access starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.
        """

        ends_at: Optional[str]
        starts_at: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class DeletedExternallyError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was deleted from the `access system <https://docs.seam.co/low-level-apis/access-systems>`_ outside of Seam.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["deleted_externally"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitExceededError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ could not be subscribed on Salto KS because the subscription limit has been exceeded.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["salto_ks_subscription_limit_exceeded"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToCreateOnAcsSystemError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was not created on the `access system <https://docs.seam.co/low-level-apis/access-systems>`_. This is likely due to an internal unexpected error. Contact Seam `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["failed_to_create_on_acs_system"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToUpdateOnAcsSystemError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was not updated on the `access system <https://docs.seam.co/low-level-apis/access-systems>`_. This is likely due to an internal unexpected error. Contact Seam `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["failed_to_update_on_acs_system"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToDeleteOnAcsSystemError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was not deleted on the `access system <https://docs.seam.co/low-level-apis/access-systems>`_. This is likely due to an internal unexpected error. Contact Seam `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["failed_to_delete_on_acs_system"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class LatchConflictWithResidentUserError(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was created from the Seam API but also exists on Mission Control. This is unsupported. Contact Seam `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["latch_conflict_with_resident_user"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class CreatingPendingMutation(ResourceMapping):
        """Seam is in the process of pushing a user creation to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing a user creation to the integrated access system.
        """

        created_at: str
        message: str
        mutation_code: Literal["creating"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class DeletingPendingMutation(ResourceMapping):
        """Seam is in the process of pushing a user deletion to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing a user deletion to the integrated access system.
        """

        created_at: str
        message: str
        mutation_code: Literal["deleting"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class DeferringCreationPendingMutation(ResourceMapping):
        """User exists in Seam but has not been pushed to the provider yet. Will be created when a credential is issued.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is intentionally deferring the creation of the user on the access control system until the appropriate time.

        :ivar scheduled_at: Optional: When the user creation is scheduled to occur."""

        created_at: str
        message: str
        mutation_code: Literal["deferring_creation"]
        scheduled_at: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                scheduled_at=d.get("scheduled_at", None),
            )

    @dataclass
    class UpdatingUserInformationPendingMutation(ResourceMapping):
        """

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old access system user information.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated user information to the integrated access system.

        :ivar to: New access system user information."""

        @dataclass
        class From(ResourceMapping):
            """Old access system user information.

            :ivar email_address: Email address of the access system user.

            :ivar full_name: Full name of the access system user.

            :ivar phone_number: Phone number of the access system user."""

            email_address: Optional[str]
            full_name: Optional[str]
            phone_number: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    email_address=d.get("email_address", None),
                    full_name=d.get("full_name", None),
                    phone_number=d.get("phone_number", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New access system user information.

            :ivar email_address: Email address of the access system user.

            :ivar full_name: Full name of the access system user.

            :ivar phone_number: Phone number of the access system user."""

            email_address: Optional[str]
            full_name: Optional[str]
            phone_number: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    email_address=d.get("email_address", None),
                    full_name=d.get("full_name", None),
                    phone_number=d.get("phone_number", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_user_information"]
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

            :ivar ends_at: Starting time for the access schedule.

            :ivar starts_at: Starting time for the access schedule."""

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
            """New access schedule information.

            :ivar ends_at: Starting time for the access schedule.

            :ivar starts_at: Starting time for the access schedule."""

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
        mutation_code: Literal["updating_access_schedule"]
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
    class UpdatingSuspensionStatePendingMutation(ResourceMapping):
        """Seam is in the process of pushing a suspension state update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old user suspension state information.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated user suspension state information to the integrated access system.

        :ivar to: New user suspension state information."""

        @dataclass
        class From(ResourceMapping):
            """Old user suspension state information.

            :ivar is_suspended:"""

            is_suspended: bool

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    is_suspended=d.get("is_suspended", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New user suspension state information.

            :ivar is_suspended:"""

            is_suspended: bool

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    is_suspended=d.get("is_suspended", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_suspension_state"]
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
    class UpdatingGroupMembershipPendingMutation(ResourceMapping):
        """Seam is in the process of pushing an access group membership update to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Old access group membership.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated access group membership information to the integrated access system.

        :ivar to: New access group membership."""

        @dataclass
        class From(ResourceMapping):
            """Old access group membership.

            :ivar acs_access_group_id: Old access group ID."""

            acs_access_group_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    acs_access_group_id=d.get("acs_access_group_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New access group membership.

            :ivar acs_access_group_id: New access group ID."""

            acs_access_group_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    acs_access_group_id=d.get("acs_access_group_id", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_group_membership"]
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
    class DeferringGroupMembershipUpdatePendingMutation(ResourceMapping):
        """A scheduled access group membership change is pending for this user.

        :ivar acs_access_group_id: ID of the access group involved in the scheduled change.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that a scheduled access group membership change is pending for this user.

        :ivar variant: Whether the user is scheduled to be added to or removed from the access group.
        """

        acs_access_group_id: str
        created_at: str
        message: str
        mutation_code: Literal["deferring_group_membership_update"]
        variant: Literal["adding", "removing"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                acs_access_group_id=d.get("acs_access_group_id", None),
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                variant=d.get("variant", None),
            )

    @dataclass
    class UpdatingCredentialAssignmentPendingMutation(ResourceMapping):
        """Seam is in the process of assigning or unassigning a credential to the user on the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous credential assignment.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of assigning or unassigning a credential to the user on the integrated access system.

        :ivar to: New credential assignment."""

        @dataclass
        class From(ResourceMapping):
            """Previous credential assignment.

            :ivar acs_credential_id: Previous credential ID."""

            acs_credential_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    acs_credential_id=d.get("acs_credential_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New credential assignment.

            :ivar acs_credential_id: New credential ID."""

            acs_credential_id: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    acs_credential_id=d.get("acs_credential_id", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_credential_assignment"]
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
    class SaltoKsMetadata(ResourceMapping):
        """Salto KS-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar is_subscribed: Indicates whether the user holds an active subscription slot on the Salto KS site. Only subscribed users can unlock doors and count against the site's user-subscription limit. A user may not be subscribed because their access schedule has not started or has ended, the site has reached its subscription limit, or they were manually unsubscribed. This is distinct from ``is_suspended``, which reflects whether the user has been explicitly blocked.
        """

        is_subscribed: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                is_subscribed=d.get("is_subscribed", None),
            )

    @dataclass
    class SaltoSpaceMetadata(ResourceMapping):
        """Salto Space-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar audit_openings: Indicates whether AuditOpenings is enabled for the user in the Salto Space access system.

        :ivar user_id: User ID in the Salto Space access system."""

        audit_openings: Optional[bool]
        user_id: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                audit_openings=d.get("audit_openings", None),
                user_id=d.get("user_id", None),
            )

    @dataclass
    class BeingDeletedWarning(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ is being deleted from the `access system <https://docs.seam.co/low-level-apis/access-systems>`_. This is a temporary state, and the access system user will be deleted shortly.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

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
    class SaltoKsUserNotSubscribedWarning(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ is not subscribed on Salto KS, so they cannot unlock doors or perform any actions. This occurs when the their access schedule hasn’t started yet, if their access schedule has ended, if the site has reached its limit for active users (subscription slots), or if they have been manually unsubscribed.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

        created_at: str
        message: str
        warning_code: Literal["salto_ks_user_not_subscribed"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AcsUserInactiveWarning(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ exists but is not currently able to gain access—for example, because their access schedule has not started yet or has ended, the access system has reached its limit for active users, or they have been unsubscribed or deactivated. Refer to the warning message for the provider-specific reason. This is distinct from ``is_suspended``, which indicates the user has been explicitly blocked.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

        created_at: str
        message: str
        warning_code: Literal["acs_user_inactive"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnknownIssueWithAcsUserWarning(ResourceMapping):
        """An unknown issue occurred while syncing the state of this `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ with the provider. This issue may affect the proper functioning of this user.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

        created_at: str
        message: str
        warning_code: Literal["unknown_issue_with_acs_user"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class LatchResidentUserWarning(ResourceMapping):
        """Indicates that the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was created on Latch Mission Control. Please use the Latch Mission Control to manage this user.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

        created_at: str
        message: str
        warning_code: Literal["latch_resident_user"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[
        DeletedExternallyError,
        SaltoKsSubscriptionLimitExceededError,
        FailedToCreateOnAcsSystemError,
        FailedToUpdateOnAcsSystemError,
        FailedToDeleteOnAcsSystemError,
        LatchConflictWithResidentUserError,
    ]
    _ErrorsVariants = {
        "deleted_externally": DeletedExternallyError,
        "salto_ks_subscription_limit_exceeded": SaltoKsSubscriptionLimitExceededError,
        "failed_to_create_on_acs_system": FailedToCreateOnAcsSystemError,
        "failed_to_update_on_acs_system": FailedToUpdateOnAcsSystemError,
        "failed_to_delete_on_acs_system": FailedToDeleteOnAcsSystemError,
        "latch_conflict_with_resident_user": LatchConflictWithResidentUserError,
    }

    PendingMutations = Union[
        CreatingPendingMutation,
        DeletingPendingMutation,
        DeferringCreationPendingMutation,
        UpdatingUserInformationPendingMutation,
        UpdatingAccessSchedulePendingMutation,
        UpdatingSuspensionStatePendingMutation,
        UpdatingGroupMembershipPendingMutation,
        DeferringGroupMembershipUpdatePendingMutation,
        UpdatingCredentialAssignmentPendingMutation,
    ]
    _PendingMutationsVariants = {
        "creating": CreatingPendingMutation,
        "deleting": DeletingPendingMutation,
        "deferring_creation": DeferringCreationPendingMutation,
        "updating_user_information": UpdatingUserInformationPendingMutation,
        "updating_access_schedule": UpdatingAccessSchedulePendingMutation,
        "updating_suspension_state": UpdatingSuspensionStatePendingMutation,
        "updating_group_membership": UpdatingGroupMembershipPendingMutation,
        "deferring_group_membership_update": DeferringGroupMembershipUpdatePendingMutation,
        "updating_credential_assignment": UpdatingCredentialAssignmentPendingMutation,
    }

    Warnings = Union[
        BeingDeletedWarning,
        SaltoKsUserNotSubscribedWarning,
        AcsUserInactiveWarning,
        UnknownIssueWithAcsUserWarning,
        LatchResidentUserWarning,
    ]
    _WarningsVariants = {
        "being_deleted": BeingDeletedWarning,
        "salto_ks_user_not_subscribed": SaltoKsUserNotSubscribedWarning,
        "acs_user_inactive": AcsUserInactiveWarning,
        "unknown_issue_with_acs_user": UnknownIssueWithAcsUserWarning,
        "latch_resident_user": LatchResidentUserWarning,
    }

    access_schedule: Optional[AccessSchedule]
    acs_system_id: str
    acs_user_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    email: Optional[str]
    email_address: Optional[str]
    errors: List[Errors]
    external_type: Optional[
        Literal[
            "pti_user",
            "brivo_user",
            "hid_credential_manager_user",
            "salto_site_user",
            "latch_user",
            "dormakaba_community_user",
            "salto_space_user",
            "avigilon_alta_user",
            "kisi_user",
        ]
    ]
    external_type_display_name: Optional[str]
    full_name: Optional[str]
    hid_acs_system_id: Optional[str]
    is_managed: Literal[True]
    is_suspended: Optional[bool]
    pending_mutations: Optional[List[PendingMutations]]
    phone_number: Optional[str]
    salto_ks_metadata: Optional[SaltoKsMetadata]
    salto_space_metadata: Optional[SaltoSpaceMetadata]
    user_identity_email_address: Optional[str]
    user_identity_full_name: Optional[str]
    user_identity_id: Optional[str]
    user_identity_phone_number: Optional[str]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_schedule=(
                cls.AccessSchedule.from_dict(d.get("access_schedule"))
                if d.get("access_schedule") is not None
                else None
            ),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email=d.get("email", None),
            email_address=d.get("email_address", None),
            errors=[
                _from_discriminated_dict(i, cls._ErrorsVariants, "error_code")
                for i in d.get("errors") or []
            ],
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            pending_mutations=[
                _from_discriminated_dict(
                    i, cls._PendingMutationsVariants, "mutation_code"
                )
                for i in d.get("pending_mutations") or []
            ],
            phone_number=d.get("phone_number", None),
            salto_ks_metadata=(
                cls.SaltoKsMetadata.from_dict(d.get("salto_ks_metadata"))
                if d.get("salto_ks_metadata") is not None
                else None
            ),
            salto_space_metadata=(
                cls.SaltoSpaceMetadata.from_dict(d.get("salto_space_metadata"))
                if d.get("salto_space_metadata") is not None
                else None
            ),
            user_identity_email_address=d.get("user_identity_email_address", None),
            user_identity_full_name=d.get("user_identity_full_name", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_phone_number=d.get("user_identity_phone_number", None),
            warnings=[
                _from_discriminated_dict(i, cls._WarningsVariants, "warning_code")
                for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
