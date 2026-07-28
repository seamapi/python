from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Workspace, ActionAttempt
from ..modules.action_attempts import resolve_action_attempt


class AbstractWorkspaces(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        name: str,
        company_name: Optional[str] = None,
        connect_partner_name: Optional[str] = None,
        connect_webview_customization: Optional[Dict[str, Any]] = None,
        is_sandbox: Optional[bool] = None,
        organization_id: Optional[str] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None,
        webview_success_message: Optional[str] = None
    ) -> Workspace:
        """Creates a new [workspace](https://docs.seam.co/core-concepts/workspaces).

        :param name: Name of the new workspace.
        :type name: str

        :param company_name: Company name for the new workspace.
        :type company_name: str

        :param connect_partner_name: Deprecated: Use `company_name` instead. Connect partner name for the new workspace.
        :type connect_partner_name: str

        :param connect_webview_customization: [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) customizations for the new workspace. See also [Customize the Look and Feel of Your Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews).
        :type connect_webview_customization: Dict[str, Any]

        :param is_sandbox: Indicates whether the new workspace is a [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).
        :type is_sandbox: bool

        :param organization_id: ID of the organization to associate with the new workspace.
        :type organization_id: str

        :param webview_logo_shape: Deprecated: Use `connect_webview_customization.webview_logo_shape` instead.
        :type webview_logo_shape: str

        :param webview_primary_button_color: Deprecated: Use `connect_webview_customization.webview_primary_button_color` instead.
        :type webview_primary_button_color: str

        :param webview_primary_button_text_color: Deprecated: Use `connect_webview_customization.webview_primary_button_text_color` instead.
        :type webview_primary_button_text_color: str

        :param webview_success_message: Deprecated: Use `connect_webview_customization.webview_success_message` instead.
        :type webview_success_message: str

        :returns: OK
        :rtype: Workspace"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
    ) -> Workspace:
        """Returns the [workspace](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :returns: OK
        :rtype: Workspace"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Workspace]:
        """Returns a list of [workspaces](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :returns: OK
        :rtype: List[Workspace]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Resets the [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces) associated with the authentication value. Note that this endpoint is only available for sandbox workspaces.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        connect_partner_name: Optional[str] = None,
        connect_webview_customization: Optional[Dict[str, Any]] = None,
        is_publishable_key_auth_enabled: Optional[bool] = None,
        is_suspended: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None
    ) -> None:
        """Updates the [workspace](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :param connect_partner_name: Connect partner name for the workspace.
        :type connect_partner_name: str

        :param connect_webview_customization: [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) customizations for the workspace. See also [Customize the Look and Feel of Your Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews).
        :type connect_webview_customization: Dict[str, Any]

        :param is_publishable_key_auth_enabled: Indicates whether publishable key authentication is enabled for this workspace.
        :type is_publishable_key_auth_enabled: bool

        :param is_suspended: Indicates whether the workspace is suspended.
        :type is_suspended: bool

        :param name: Name of the workspace.
        :type name: str

        :param organization_id: ID of the organization to assign the workspace to. The authenticated user must be the owner of the workspace and an admin of the target organization.
        :type organization_id: str"""
        raise NotImplementedError()


class Workspaces(AbstractWorkspaces):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        name: str,
        company_name: Optional[str] = None,
        connect_partner_name: Optional[str] = None,
        connect_webview_customization: Optional[Dict[str, Any]] = None,
        is_sandbox: Optional[bool] = None,
        organization_id: Optional[str] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None,
        webview_success_message: Optional[str] = None
    ) -> Workspace:
        """Creates a new [workspace](https://docs.seam.co/core-concepts/workspaces).

        :param name: Name of the new workspace.
        :type name: str

        :param company_name: Company name for the new workspace.
        :type company_name: str

        :param connect_partner_name: Deprecated: Use `company_name` instead. Connect partner name for the new workspace.
        :type connect_partner_name: str

        :param connect_webview_customization: [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) customizations for the new workspace. See also [Customize the Look and Feel of Your Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews).
        :type connect_webview_customization: Dict[str, Any]

        :param is_sandbox: Indicates whether the new workspace is a [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).
        :type is_sandbox: bool

        :param organization_id: ID of the organization to associate with the new workspace.
        :type organization_id: str

        :param webview_logo_shape: Deprecated: Use `connect_webview_customization.webview_logo_shape` instead.
        :type webview_logo_shape: str

        :param webview_primary_button_color: Deprecated: Use `connect_webview_customization.webview_primary_button_color` instead.
        :type webview_primary_button_color: str

        :param webview_primary_button_text_color: Deprecated: Use `connect_webview_customization.webview_primary_button_text_color` instead.
        :type webview_primary_button_text_color: str

        :param webview_success_message: Deprecated: Use `connect_webview_customization.webview_success_message` instead.
        :type webview_success_message: str

        :returns: OK
        :rtype: Workspace"""
        json_payload = {}

        if name is not None:
            json_payload["name"] = name
        if company_name is not None:
            json_payload["company_name"] = company_name
        if connect_partner_name is not None:
            json_payload["connect_partner_name"] = connect_partner_name
        if connect_webview_customization is not None:
            json_payload["connect_webview_customization"] = (
                connect_webview_customization
            )
        if is_sandbox is not None:
            json_payload["is_sandbox"] = is_sandbox
        if organization_id is not None:
            json_payload["organization_id"] = organization_id
        if webview_logo_shape is not None:
            json_payload["webview_logo_shape"] = webview_logo_shape
        if webview_primary_button_color is not None:
            json_payload["webview_primary_button_color"] = webview_primary_button_color
        if webview_primary_button_text_color is not None:
            json_payload["webview_primary_button_text_color"] = (
                webview_primary_button_text_color
            )
        if webview_success_message is not None:
            json_payload["webview_success_message"] = webview_success_message

        res = self.client.post("/workspaces/create", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def get(
        self,
    ) -> Workspace:
        """Returns the [workspace](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :returns: OK
        :rtype: Workspace"""
        json_payload = {}

        res = self.client.post("/workspaces/get", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def list(
        self,
    ) -> List[Workspace]:
        """Returns a list of [workspaces](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :returns: OK
        :rtype: List[Workspace]"""
        json_payload = {}

        res = self.client.post("/workspaces/list", json=json_payload)

        return [Workspace.from_dict(item) for item in res["workspaces"]]

    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Resets the [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces) associated with the authentication value. Note that this endpoint is only available for sandbox workspaces.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        res = self.client.post("/workspaces/reset_sandbox", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def update(
        self,
        *,
        connect_partner_name: Optional[str] = None,
        connect_webview_customization: Optional[Dict[str, Any]] = None,
        is_publishable_key_auth_enabled: Optional[bool] = None,
        is_suspended: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None
    ) -> None:
        """Updates the [workspace](https://docs.seam.co/core-concepts/workspaces) associated with the authentication value.

        :param connect_partner_name: Connect partner name for the workspace.
        :type connect_partner_name: str

        :param connect_webview_customization: [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) customizations for the workspace. See also [Customize the Look and Feel of Your Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-look-and-feel-of-your-connect-webviews).
        :type connect_webview_customization: Dict[str, Any]

        :param is_publishable_key_auth_enabled: Indicates whether publishable key authentication is enabled for this workspace.
        :type is_publishable_key_auth_enabled: bool

        :param is_suspended: Indicates whether the workspace is suspended.
        :type is_suspended: bool

        :param name: Name of the workspace.
        :type name: str

        :param organization_id: ID of the organization to assign the workspace to. The authenticated user must be the owner of the workspace and an admin of the target organization.
        :type organization_id: str"""
        json_payload = {}

        if connect_partner_name is not None:
            json_payload["connect_partner_name"] = connect_partner_name
        if connect_webview_customization is not None:
            json_payload["connect_webview_customization"] = (
                connect_webview_customization
            )
        if is_publishable_key_auth_enabled is not None:
            json_payload["is_publishable_key_auth_enabled"] = (
                is_publishable_key_auth_enabled
            )
        if is_suspended is not None:
            json_payload["is_suspended"] = is_suspended
        if name is not None:
            json_payload["name"] = name
        if organization_id is not None:
            json_payload["organization_id"] = organization_id

        self.client.post("/workspaces/update", json=json_payload)

        return None
