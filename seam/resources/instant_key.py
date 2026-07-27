from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class InstantKey:
    client_session_id: str
    created_at: str
    customization: Dict[str, Any]
    customization_profile_id: str
    expires_at: str
    instant_key_id: str
    instant_key_url: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return InstantKey(
            client_session_id=d.get("client_session_id", None),
            created_at=d.get("created_at", None),
            customization=DeepAttrDict(d.get("customization", None)),
            customization_profile_id=d.get("customization_profile_id", None),
            expires_at=d.get("expires_at", None),
            instant_key_id=d.get("instant_key_id", None),
            instant_key_url=d.get("instant_key_url", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )
