from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ClientSession:
    client_session_id: str
    connect_webview_ids: List[str]
    connected_account_ids: List[str]
    created_at: str
    customer_key: str
    device_count: float
    expires_at: str
    token: str
    user_identifier_key: str
    user_identity_id: str
    user_identity_ids: List[str]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ClientSession(
            client_session_id=d.get("client_session_id", None),
            connect_webview_ids=d.get("connect_webview_ids", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_count=d.get("device_count", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
            user_identifier_key=d.get("user_identifier_key", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_ids=d.get("user_identity_ids", None),
            workspace_id=d.get("workspace_id", None),
        )
