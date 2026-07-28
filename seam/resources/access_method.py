from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessMethod:
    """Represents an access method for an Access Grant. Access methods describe the modes of access, such as PIN codes, plastic cards, and mobile keys. For a mobile key, the access method also stores the URL for the associated Instant Key.

    :ivar access_method_id: ID of the access method.

    :ivar client_session_token: Token of the client session associated with the access method.

    :ivar code: The actual PIN code for code access methods.

    :ivar created_at: Date and time at which the access method was created.

    :ivar customization_profile_id: ID of the customization profile associated with the access method.

    :ivar display_name: Display name of the access method.

    :ivar errors: Errors associated with the `access method <https://docs.seam.co/use-cases/granting-access/creating-an-access-grant>`_.

    :ivar instant_key_url: URL of the Instant Key for mobile key access methods.

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
    client_session_token: str
    code: str
    created_at: str
    customization_profile_id: str
    display_name: str
    errors: List[Dict[str, Any]]
    instant_key_url: str
    is_assignment_required: bool
    is_encoding_required: bool
    is_issued: bool
    is_ready_for_assignment: bool
    is_ready_for_encoding: bool
    issued_at: str
    mode: str
    pending_mutations: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessMethod(
            access_method_id=d.get("access_method_id", None),
            client_session_token=d.get("client_session_token", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            customization_profile_id=d.get("customization_profile_id", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            instant_key_url=d.get("instant_key_url", None),
            is_assignment_required=d.get("is_assignment_required", None),
            is_encoding_required=d.get("is_encoding_required", None),
            is_issued=d.get("is_issued", None),
            is_ready_for_assignment=d.get("is_ready_for_assignment", None),
            is_ready_for_encoding=d.get("is_ready_for_encoding", None),
            issued_at=d.get("issued_at", None),
            mode=d.get("mode", None),
            pending_mutations=d.get("pending_mutations", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
