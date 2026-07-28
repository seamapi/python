from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


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

    access_grant_id: str
    access_grant_key: str
    access_method_ids: List[str]
    client_session_token: str
    created_at: str
    customization_profile_id: str
    display_name: str
    ends_at: str
    errors: List[Dict[str, Any]]
    instant_key_url: str
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
        return AccessGrant(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            access_method_ids=d.get("access_method_ids", None),
            client_session_token=d.get("client_session_token", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            instant_key_url=d.get("instant_key_url", None),
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
