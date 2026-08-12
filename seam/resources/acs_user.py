from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


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
        """Errors associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code:

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
        """Pending mutations associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. Seam is in the process of pushing these mutations to the integrated access system.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code:

        :ivar scheduled_at: Optional: When the user creation is scheduled to occur.

        :ivar from_:

        :ivar to:

        :ivar acs_access_group_id: ID of the access group involved in the scheduled change.

        :ivar variant: Whether the user is scheduled to be added to or removed from the access group.
        """

        @dataclass
        class From(ResourceMapping):
            """

            :ivar email_address: Email address of the access system user.

            :ivar full_name: Full name of the access system user.

            :ivar phone_number: Phone number of the access system user.

            :ivar ends_at: Starting time for the access schedule.

            :ivar starts_at: Starting time for the access schedule.

            :ivar is_suspended:

            :ivar acs_access_group_id: Old access group ID.

            :ivar acs_credential_id: Previous credential ID."""

            email_address: str
            full_name: str
            phone_number: str
            ends_at: str
            starts_at: str
            is_suspended: bool
            acs_access_group_id: str
            acs_credential_id: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    email_address=d.get("email_address", None),
                    full_name=d.get("full_name", None),
                    phone_number=d.get("phone_number", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                    is_suspended=d.get("is_suspended", None),
                    acs_access_group_id=d.get("acs_access_group_id", None),
                    acs_credential_id=d.get("acs_credential_id", None),
                )

        @dataclass
        class To(ResourceMapping):
            """

            :ivar email_address: Email address of the access system user.

            :ivar full_name: Full name of the access system user.

            :ivar phone_number: Phone number of the access system user.

            :ivar ends_at: Starting time for the access schedule.

            :ivar starts_at: Starting time for the access schedule.

            :ivar is_suspended:

            :ivar acs_access_group_id: New access group ID.

            :ivar acs_credential_id: New credential ID."""

            email_address: str
            full_name: str
            phone_number: str
            ends_at: str
            starts_at: str
            is_suspended: bool
            acs_access_group_id: str
            acs_credential_id: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    email_address=d.get("email_address", None),
                    full_name=d.get("full_name", None),
                    phone_number=d.get("phone_number", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                    is_suspended=d.get("is_suspended", None),
                    acs_access_group_id=d.get("acs_access_group_id", None),
                    acs_credential_id=d.get("acs_credential_id", None),
                )

        created_at: str
        message: str
        mutation_code: str
        scheduled_at: str
        from_: From
        to: To
        acs_access_group_id: str
        variant: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                scheduled_at=d.get("scheduled_at", None),
                from_=(
                    cls.From.from_dict(d.get("from"))
                    if d.get("from") is not None
                    else None
                ),
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
                acs_access_group_id=d.get("acs_access_group_id", None),
                variant=d.get("variant", None),
            )

    @dataclass
    class SaltoKsMetadata(ResourceMapping):
        """Salto KS-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar is_subscribed: Indicates whether the user holds an active subscription slot on the Salto KS site. Only subscribed users can unlock doors and count against the site's user-subscription limit. A user may not be subscribed because their access schedule has not started or has ended, the site has reached its subscription limit, or they were manually unsubscribed. This is distinct from ``is_suspended``, which reflects whether the user has been explicitly blocked.
        """

        is_subscribed: bool

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                is_subscribed=d.get("is_subscribed", None),
            )

    @dataclass
    class SaltoSpaceMetadata(ResourceMapping):
        """Salto Space-specific metadata associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar audit_openings: Indicates whether AuditOpenings is enabled for the user in the Salto Space access system.

        :ivar user_id: User ID in the Salto Space access system."""

        audit_openings: bool
        user_id: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                audit_openings=d.get("audit_openings", None),
                user_id=d.get("user_id", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code:"""

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

    access_schedule: AccessSchedule
    acs_system_id: str
    acs_user_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    email: str
    email_address: str
    errors: List[Errors]
    external_type: str
    external_type_display_name: str
    full_name: str
    hid_acs_system_id: str
    is_managed: bool
    is_suspended: bool
    pending_mutations: List[PendingMutations]
    phone_number: str
    salto_ks_metadata: SaltoKsMetadata
    salto_space_metadata: SaltoSpaceMetadata
    user_identity_email_address: str
    user_identity_full_name: str
    user_identity_id: str
    user_identity_phone_number: str
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
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
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            full_name=d.get("full_name", None),
            hid_acs_system_id=d.get("hid_acs_system_id", None),
            is_managed=d.get("is_managed", None),
            is_suspended=d.get("is_suspended", None),
            pending_mutations=[
                cls.PendingMutations.from_dict(i)
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
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
