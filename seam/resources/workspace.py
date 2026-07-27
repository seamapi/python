from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Workspace:
    company_name: str
    connect_partner_name: str
    connect_webview_customization: Dict[str, Any]
    is_publishable_key_auth_enabled: bool
    is_sandbox: bool
    is_suspended: bool
    name: str
    organization_id: str
    publishable_key: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Workspace(
            company_name=d.get("company_name", None),
            connect_partner_name=d.get("connect_partner_name", None),
            connect_webview_customization=DeepAttrDict(
                d.get("connect_webview_customization", None)
            ),
            is_publishable_key_auth_enabled=d.get(
                "is_publishable_key_auth_enabled", None
            ),
            is_sandbox=d.get("is_sandbox", None),
            is_suspended=d.get("is_suspended", None),
            name=d.get("name", None),
            organization_id=d.get("organization_id", None),
            publishable_key=d.get("publishable_key", None),
            workspace_id=d.get("workspace_id", None),
        )
