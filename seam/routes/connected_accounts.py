from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractConnectedAccounts, ConnectedAccount


class ConnectedAccounts(AbstractConnectedAccounts, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, connected_account_id: str, sync: Optional[bool] = None) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if sync is not None:
            json_payload["sync"] = sync

        return None

    def get(
        self, *, connected_account_id: Optional[str] = None, email: Optional[str] = None
    ) -> ConnectedAccount:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if email is not None:
            json_payload["email"] = email

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/connected_accounts/get",
                method="POST",
                body=json_payload,
                response_key="connected_account",
                model_type=ConnectedAccount,
            ),
        )

    def list(
        self,
        *,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None
    ) -> List[ConnectedAccount]:
        json_payload = {}

        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/connected_accounts/list",
                method="POST",
                body=json_payload,
                response_key="connected_accounts",
                model_type=List[ConnectedAccount],
            ),
        )

    def update(
        self,
        *,
        connected_account_id: str,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if automatically_manage_new_devices is not None:
            json_payload["automatically_manage_new_devices"] = (
                automatically_manage_new_devices
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata

        return None
