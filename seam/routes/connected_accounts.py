from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractConnectedAccounts, ConnectedAccount


class ConnectedAccounts(AbstractConnectedAccounts):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, connected_account_id: str, sync: Optional[bool] = None) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if sync is not None:
            json_payload["sync"] = sync

        self.client.post("/connected_accounts/delete", json=json_payload)

        return None

    def get(
        self, *, connected_account_id: Optional[str] = None, email: Optional[str] = None
    ) -> ConnectedAccount:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if email is not None:
            json_payload["email"] = email

        res = self.client.post("/connected_accounts/get", json=json_payload)

        return ConnectedAccount.from_dict(res["connected_account"])

    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_ids: Optional[List[str]] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[ConnectedAccount]:
        json_payload = {}

        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if customer_ids is not None:
            json_payload["customer_ids"] = customer_ids
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/connected_accounts/list", json=json_payload)

        return [ConnectedAccount.from_dict(item) for item in res["connected_accounts"]]

    def sync(self, *, connected_account_id: str) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/sync", json=json_payload)

        return None

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

        self.client.post("/connected_accounts/update", json=json_payload)

        return None
