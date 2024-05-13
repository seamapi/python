from seam.types import AbstractSeam as Seam
from seam.routes.types import AbstractWorkspaces, Workspace, ActionAttempt
from typing import Optional, Any, List, Dict, Union


class Workspaces(AbstractWorkspaces):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def create(
        self,
        *,
        connect_partner_name: str,
        name: str,
        is_sandbox: Optional[bool] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None
    ) -> Workspace:
        json_payload = {}

        if connect_partner_name is not None:
            json_payload["connect_partner_name"] = connect_partner_name
        if name is not None:
            json_payload["name"] = name
        if is_sandbox is not None:
            json_payload["is_sandbox"] = is_sandbox
        if webview_logo_shape is not None:
            json_payload["webview_logo_shape"] = webview_logo_shape
        if webview_primary_button_color is not None:
            json_payload["webview_primary_button_color"] = webview_primary_button_color

        res = self.seam.make_request("POST", "/workspaces/create", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def get(
        self,
    ) -> Workspace:
        json_payload = {}

        res = self.seam.make_request("POST", "/workspaces/get", json=json_payload)

        return Workspace.from_dict(res["workspace"])

    def list(
        self,
    ) -> List[Workspace]:
        json_payload = {}

        res = self.seam.make_request("POST", "/workspaces/list", json=json_payload)

        return [Workspace.from_dict(item) for item in res["workspaces"]]

    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        res = self.seam.make_request(
            "POST", "/workspaces/reset_sandbox", json=json_payload
        )

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
