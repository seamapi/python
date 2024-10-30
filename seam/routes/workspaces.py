from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractWorkspaces, Workspace, ActionAttempt

from ..modules.action_attempts import resolve_action_attempt


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
        is_sandbox: Optional[bool] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None
    ) -> Workspace:
        json_payload = {}

        if name is not None:
            json_payload["name"] = name
        if company_name is not None:
            json_payload["company_name"] = company_name
        if connect_partner_name is not None:
            json_payload["connect_partner_name"] = connect_partner_name
        if is_sandbox is not None:
            json_payload["is_sandbox"] = is_sandbox
        if webview_logo_shape is not None:
            json_payload["webview_logo_shape"] = webview_logo_shape
        if webview_primary_button_color is not None:
            json_payload["webview_primary_button_color"] = webview_primary_button_color
        if webview_primary_button_text_color is not None:
            json_payload["webview_primary_button_text_color"] = (
                webview_primary_button_text_color
            )

        res = self.client.post("/workspaces/create", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def get(
        self,
    ) -> Workspace:
        json_payload = {}

        res = self.client.post("/workspaces/get", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def list(
        self,
    ) -> List[Workspace]:
        json_payload = {}

        res = self.client.post("/workspaces/list", json=json_payload)

        return [Workspace.from_dict(item) for item in res["workspaces"]]

    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
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
