from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractEvents, SeamEvent


class Events(AbstractEvents):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(
        self,
        *,
        device_id: Optional[str] = None,
        event_id: Optional[str] = None,
        event_type: Optional[str] = None
    ) -> SeamEvent:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if event_id is not None:
            json_payload["event_id"] = event_id
        if event_type is not None:
            json_payload["event_type"] = event_type

        res = self.client.post("/events/get", json=json_payload)

        return SeamEvent.from_dict(res["event"])

    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_method_id: Optional[str] = None,
        access_method_ids: Optional[List[str]] = None,
        acs_access_group_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_encoder_id: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_user_id: Optional[str] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        space_id: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        unstable_offset: Optional[float] = None,
        user_identity_id: Optional[str] = None
    ) -> List[SeamEvent]:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_ids is not None:
            json_payload["access_grant_ids"] = access_grant_ids
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if access_method_ids is not None:
            json_payload["access_method_ids"] = access_method_ids
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if between is not None:
            json_payload["between"] = between
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if event_ids is not None:
            json_payload["event_ids"] = event_ids
        if event_type is not None:
            json_payload["event_type"] = event_type
        if event_types is not None:
            json_payload["event_types"] = event_types
        if limit is not None:
            json_payload["limit"] = limit
        if since is not None:
            json_payload["since"] = since
        if space_id is not None:
            json_payload["space_id"] = space_id
        if space_ids is not None:
            json_payload["space_ids"] = space_ids
        if unstable_offset is not None:
            json_payload["unstable_offset"] = unstable_offset
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/events/list", json=json_payload)

        return [SeamEvent.from_dict(item) for item in res["events"]]
