from seam.types import AbstractConnectWebviews, AbstractSeam as Seam, ConnectWebview
from typing import Optional, Any, List, Dict, Union


class ConnectWebviews(AbstractConnectWebviews):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        res = self.seam.make_request(
            "POST", "/connect_webviews/create", json=json_payload
        )

        return ConnectWebview.from_dict(res["connect_webview"])

    def delete(self, *, connect_webview_id: str) -> None:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        self.seam.make_request("POST", "/connect_webviews/delete", json=json_payload)

        return None

    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        res = self.seam.make_request("POST", "/connect_webviews/get", json=json_payload)

        return ConnectWebview.from_dict(res["connect_webview"])

    def list(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None
    ) -> List[ConnectWebview]:
        json_payload = {}

        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has

        res = self.seam.make_request(
            "POST", "/connect_webviews/list", json=json_payload
        )

        return [ConnectWebview.from_dict(item) for item in res["connect_webviews"]]
