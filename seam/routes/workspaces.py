from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractWorkspaces, Workspace, ActionAttempt

from ..modules.action_attempts import resolve_action_attempt


class Workspaces(AbstractWorkspaces, SeamHttpRequestParent):
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
        webview_primary_button_color: Optional[str] = None,
        webview_primary_button_text_color: Optional[str] = None,
        webview_logo_shape: Optional[str] = None
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
        if webview_primary_button_color is not None:
            json_payload["webview_primary_button_color"] = webview_primary_button_color
        if webview_primary_button_text_color is not None:
            json_payload["webview_primary_button_text_color"] = (
                webview_primary_button_text_color
            )
        if webview_logo_shape is not None:
            json_payload["webview_logo_shape"] = webview_logo_shape

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/workspaces/create",
                method="POST",
                body=json_payload,
                response_key="workspace",
                model_type=Workspace,
            ),
        )

    def get(
        self,
    ) -> Workspace:
        json_payload = {}

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/workspaces/get",
                method="POST",
                body=json_payload,
                response_key="workspace",
                model_type=Workspace,
            ),
        )

    def list(
        self,
    ) -> List[Workspace]:
        json_payload = {}

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/workspaces/list",
                method="POST",
                body=json_payload,
                response_key="workspaces",
                model_type=List[Workspace],
            ),
        )

    def reset_sandbox(
        self, wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/workspaces/reset_sandbox",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )
