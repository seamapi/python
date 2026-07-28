from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


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

    access_group_type: str
    access_group_type_display_name: str
    access_schedule: Dict[str, Any]
    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    external_type: str
    external_type_display_name: str
    is_managed: bool
    name: str
    pending_mutations: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsAccessGroup(
            access_group_type=d.get("access_group_type", None),
            access_group_type_display_name=d.get(
                "access_group_type_display_name", None
            ),
            access_schedule=DeepAttrDict(d.get("access_schedule", None)),
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
