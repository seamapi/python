from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractConnectWebviews, ConnectWebview


class ConnectWebviews(AbstractConnectWebviews):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        accepted_providers: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        custom_redirect_failure_url: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        customer_id: Optional[str] = None,
        device_selection_mode: Optional[str] = None,
        provider_category: Optional[str] = None,
        wait_for_device_creation: Optional[bool] = None
    ) -> ConnectWebview:
        json_payload = {}

        if accepted_providers is not None:
            json_payload["accepted_providers"] = accepted_providers
        if automatically_manage_new_devices is not None:
            json_payload["automatically_manage_new_devices"] = (
                automatically_manage_new_devices
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if custom_redirect_failure_url is not None:
            json_payload["custom_redirect_failure_url"] = custom_redirect_failure_url
        if custom_redirect_url is not None:
            json_payload["custom_redirect_url"] = custom_redirect_url
        if customer_id is not None:
            json_payload["customer_id"] = customer_id
        if device_selection_mode is not None:
            json_payload["device_selection_mode"] = device_selection_mode
        if provider_category is not None:
            json_payload["provider_category"] = provider_category
        if wait_for_device_creation is not None:
            json_payload["wait_for_device_creation"] = wait_for_device_creation

        res = self.client.post("/connect_webviews/create", json=json_payload)

        return ConnectWebview.from_dict(res["connect_webview"])

    def delete(self, *, connect_webview_id: str) -> None:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        self.client.post("/connect_webviews/delete", json=json_payload)

        return None

    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        res = self.client.post("/connect_webviews/get", json=json_payload)

        return ConnectWebview.from_dict(res["connect_webview"])

    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_id: Optional[str] = None,
        limit: Optional[float] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[ConnectWebview]:
        json_payload = {}

        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if customer_id is not None:
            json_payload["customer_id"] = customer_id
        if limit is not None:
            json_payload["limit"] = limit
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/connect_webviews/list", json=json_payload)

        return [ConnectWebview.from_dict(item) for item in res["connect_webviews"]]
