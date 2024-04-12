from seam.types import AbstractEvents, AbstractSeam as Seam, Event
from typing import Optional, Any, List, Dict, Union


class Events(AbstractEvents):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(
        self,
        *,
        device_id: Optional[str] = None,
        event_id: Optional[str] = None,
        event_type: Optional[str] = None
    ) -> Event:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if event_id is not None:
            json_payload["event_id"] = event_id
        if event_type is not None:
            json_payload["event_type"] = event_type

        res = self.seam.make_request("POST", "/events/get", json=json_payload)

        return Event.from_dict(res["event"])

    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        between: Optional[List[str]] = None,
        connected_account_id: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None
    ) -> List[Event]:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if between is not None:
            json_payload["between"] = between
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

        res = self.seam.make_request("POST", "/events/list", json=json_payload)

        return [Event.from_dict(item) for item in res["events"]]
