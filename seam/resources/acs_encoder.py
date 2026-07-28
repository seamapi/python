from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AcsEncoder:
    """Represents a hardware device that encodes `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ data onto physical cards within an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    Some access control systems require credentials to be encoded onto plastic key cards using a card encoder. This process involves the following two key steps:

    1. Credential creation
       Configure the access parameters for the credential.
    2. Card encoding
       Write the credential data onto the card using a compatible card encoder.

    Separately, the Seam API also supports card scanning, which enables you to scan and read the encoded data on a card. You can use this action to confirm consistency with access control system records or diagnose discrepancies if needed.

    See `Working with Card Encoders and Scanners <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    To verify if your access control system requires a card encoder, see the corresponding `system integration guide <https://docs.seam.co/device-and-system-integration-guides#access-control-systems>`_.

    :ivar acs_encoder_id: ID of the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    :ivar connected_account_id: ID of the connected account that contains the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    :ivar created_at: Date and time at which the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ was created.

    :ivar display_name: Display name for the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    :ivar errors: Errors associated with the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

    :ivar workspace_id: ID of the workspace that contains the `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.
    """

    acs_encoder_id: str
    acs_system_id: str
    connected_account_id: str
    created_at: str
    display_name: str
    errors: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AcsEncoder(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            workspace_id=d.get("workspace_id", None),
        )
