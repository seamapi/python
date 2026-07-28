from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Workspace:
    """Represents a Seam `workspace <https://docs.seam.co/core-concepts/workspaces>`_. A workspace is a top-level entity that encompasses all other resources below it, such as devices, connected accounts, and Connect Webviews. Seam provides two types of workspaces. A `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_ is a special type of workspace designed for testing code. Sandbox workspaces offer test device accounts and virtual devices that you can connect and control. This ability to work with virtual devices is quite handy because it removes the need to own physical devices from multiple brands. To connect real devices and systems to Seam, use a `production workspace <https://docs.seam.co/core-concepts/workspaces#production-workspaces>`_.

    :ivar company_name: Company name associated with the `workspace <https://docs.seam.co/core-concepts/workspaces>`_.

    :ivar connect_partner_name: Deprecated: Use ``company_name`` instead.

    :ivar connect_webview_customization:

    :ivar is_publishable_key_auth_enabled: Indicates whether publishable key authentication is enabled for this workspace.

    :ivar is_sandbox: Indicates whether the workspace is a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

    :ivar is_suspended: Indicates whether the `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_ is suspended. Seam suspends sandbox workspaces that have not been accessed in 14 days.

    :ivar name: Name of the `workspace <https://docs.seam.co/core-concepts/workspaces>`_.

    :ivar organization_id: ID of the organization to which the workspace belongs, or ``null`` if the workspace is not assigned to an organization.

    :ivar publishable_key: Publishable key for the `workspace <https://docs.seam.co/core-concepts/workspaces>`_. This key is used to identify the workspace in client-side applications.

    :ivar workspace_id: ID of the workspace."""

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
