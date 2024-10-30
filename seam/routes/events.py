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
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        unstable_offset: Optional[float] = None
    ) -> List[SeamEvent]:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if between is not None:
            json_payload["between"] = between
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if event_type is not None:
            json_payload["event_type"] = event_type
        if event_types is not None:
            json_payload["event_types"] = event_types
        if limit is not None:
            json_payload["limit"] = limit
        if since is not None:
            json_payload["since"] = since
        if unstable_offset is not None:
            json_payload["unstable_offset"] = unstable_offset

        res = self.client.post("/events/list", json=json_payload)

        return [SeamEvent.from_dict(item) for item in res["events"]]
