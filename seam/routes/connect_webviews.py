from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractConnectWebviews, ConnectWebview


class ConnectWebviews(AbstractConnectWebviews, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        device_selection_mode: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        custom_redirect_failure_url: Optional[str] = None,
        accepted_providers: Optional[List[str]] = None,
        provider_category: Optional[str] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        wait_for_device_creation: Optional[bool] = None
    ) -> ConnectWebview:
        json_payload = {}

        if device_selection_mode is not None:
            json_payload["device_selection_mode"] = device_selection_mode
        if custom_redirect_url is not None:
            json_payload["custom_redirect_url"] = custom_redirect_url
        if custom_redirect_failure_url is not None:
            json_payload["custom_redirect_failure_url"] = custom_redirect_failure_url
        if accepted_providers is not None:
            json_payload["accepted_providers"] = accepted_providers
        if provider_category is not None:
            json_payload["provider_category"] = provider_category
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if automatically_manage_new_devices is not None:
            json_payload["automatically_manage_new_devices"] = (
                automatically_manage_new_devices
            )
        if wait_for_device_creation is not None:
            json_payload["wait_for_device_creation"] = wait_for_device_creation

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/connect_webviews/create",
                method="POST",
                body=json_payload,
                response_key="connect_webview",
                model_type=ConnectWebview,
            ),
        )

    def delete(self, *, connect_webview_id: str) -> None:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        return None

    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/connect_webviews/get",
                method="POST",
                body=json_payload,
                response_key="connect_webview",
                model_type=ConnectWebview,
            ),
        )

    def list(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        limit: Optional[float] = None
    ) -> List[ConnectWebview]:
        json_payload = {}

        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if limit is not None:
            json_payload["limit"] = limit

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/connect_webviews/list",
                method="POST",
                body=json_payload,
                response_key="connect_webviews",
                model_type=List[ConnectWebview],
            ),
        )
