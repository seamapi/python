from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ConnectWebview:
    accepted_capabilities: List[str]
    accepted_providers: List[str]
    any_provider_allowed: bool
    authorized_at: str
    automatically_manage_new_devices: bool
    connect_webview_id: str
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    custom_redirect_failure_url: str
    custom_redirect_url: str
    customer_key: str
    device_selection_mode: str
    login_successful: bool
    selected_provider: str
    status: str
    url: str
    wait_for_device_creation: bool
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectWebview(
            accepted_capabilities=d.get("accepted_capabilities", None),
            accepted_providers=d.get("accepted_providers", None),
            any_provider_allowed=d.get("any_provider_allowed", None),
            authorized_at=d.get("authorized_at", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            custom_redirect_failure_url=d.get("custom_redirect_failure_url", None),
            custom_redirect_url=d.get("custom_redirect_url", None),
            customer_key=d.get("customer_key", None),
            device_selection_mode=d.get("device_selection_mode", None),
            login_successful=d.get("login_successful", None),
            selected_provider=d.get("selected_provider", None),
            status=d.get("status", None),
            url=d.get("url", None),
            wait_for_device_creation=d.get("wait_for_device_creation", None),
            workspace_id=d.get("workspace_id", None),
        )
