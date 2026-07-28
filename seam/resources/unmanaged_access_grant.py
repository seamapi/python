from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UnmanagedAccessGrant:
    """Represents an unmanaged Access Grant. Unmanaged Access Grants do not have client sessions, instant keys, customization profiles, or keys.

    :ivar access_grant_id: ID of the Access Grant.

    :ivar access_method_ids: IDs of the access methods created for the Access Grant.

    :ivar created_at: Date and time at which the Access Grant was created.

    :ivar display_name: Display name of the Access Grant.

    :ivar ends_at: Date and time at which the Access Grant ends.

    :ivar errors: Errors associated with the `access grant <https://docs.seam.co/use-cases/granting-access>`_.

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

    access_grant_id: str
    access_method_ids: List[str]
    created_at: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    location_ids: List[str]
    name: str
    pending_mutations: List[Dict[str, Any]]
    requested_access_methods: List[Dict[str, Any]]
    reservation_key: str
    space_ids: List[str]
    starts_at: str
    user_identity_id: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAccessGrant(
            access_grant_id=d.get("access_grant_id", None),
            access_method_ids=d.get("access_method_ids", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            location_ids=d.get("location_ids", None),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            requested_access_methods=d.get("requested_access_methods", None),
            reservation_key=d.get("reservation_key", None),
            space_ids=d.get("space_ids", None),
            starts_at=d.get("starts_at", None),
            user_identity_id=d.get("user_identity_id", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
