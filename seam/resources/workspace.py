from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class WorkspaceConnectWebviewCustomization(ResourceMapping):
    """

    :ivar inviter_logo_url: URL of the inviter logo for `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_ in the workspace. See also `Customize the Look and Feel of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews>`_.

    :ivar logo_shape: Logo shape for `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_ in the workspace. See also `Customize the Look and Feel of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews>`_.

    :ivar primary_button_color: Primary button color for `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_ in the workspace. See also `Customize the Look and Feel of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews>`_.

    :ivar primary_button_text_color: Primary button text color for `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_ in the workspace. See also `Customize the Look and Feel of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews>`_.

    :ivar success_message: Success message for `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_ in the workspace. See also `Customize the Look and Feel of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews>`_.
    """

    inviter_logo_url: str
    logo_shape: str
    primary_button_color: str
    primary_button_text_color: str
    success_message: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            inviter_logo_url=d.get("inviter_logo_url", None),
            logo_shape=d.get("logo_shape", None),
            primary_button_color=d.get("primary_button_color", None),
            primary_button_text_color=d.get("primary_button_text_color", None),
            success_message=d.get("success_message", None),
        )


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
    connect_webview_customization: WorkspaceConnectWebviewCustomization
    is_publishable_key_auth_enabled: bool
    is_sandbox: bool
    is_suspended: bool
    name: str
    organization_id: str
    publishable_key: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            company_name=d.get("company_name", None),
            connect_partner_name=d.get("connect_partner_name", None),
            connect_webview_customization=(
                WorkspaceConnectWebviewCustomization.from_dict(
                    d.get("connect_webview_customization")
                )
                if d.get("connect_webview_customization") is not None
                else None
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
