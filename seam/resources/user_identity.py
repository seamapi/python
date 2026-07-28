from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UserIdentity:
    """Represents a `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ associated with an application user account.

    :ivar acs_user_ids: Array of access system user IDs associated with the user identity.

    :ivar created_at: Date and time at which the user identity was created.

    :ivar display_name: Display name for the user identity.

    :ivar email_address: Unique email address for the user identity.

    :ivar errors: Array of errors associated with the user identity. Each error object within the array contains fields like "error_code" and "message." "error_code" is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. "message" provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar full_name: Full name of the user associated with the user identity.

    :ivar phone_number: Unique phone number for the user identity in `E.164 format <https://www.itu.int/rec/T-REC-E.164/en>`_ (for example, +15555550100).

    :ivar user_identity_id: ID of the user identity.

    :ivar user_identity_key: Unique key for the user identity.

    :ivar warnings: Array of warnings associated with the user identity. Each warning object within the array contains two fields: "warning_code" and "message." "warning_code" is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. "message" provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar workspace_id: ID of the workspace that contains the user identity."""

    acs_user_ids: List[str]
    created_at: str
    display_name: str
    email_address: str
    errors: List[Dict[str, Any]]
    full_name: str
    phone_number: str
    user_identity_id: str
    user_identity_key: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UserIdentity(
            acs_user_ids=d.get("acs_user_ids", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            email_address=d.get("email_address", None),
            errors=d.get("errors", None),
            full_name=d.get("full_name", None),
            phone_number=d.get("phone_number", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_key=d.get("user_identity_key", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
