from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSpaces, Space


class Spaces(AbstractSpaces):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_acs_entrances(self, *, acs_entrance_ids: List[str], space_id: str) -> None:
        json_payload = {}

        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/add_acs_entrances", json=json_payload)

        return None

    def add_devices(self, *, device_ids: List[str], space_id: str) -> None:
        json_payload = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/add_devices", json=json_payload)

        return None

    def create(
        self,
        *,
        name: str,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None
    ) -> Space:
        json_payload = {}

        if name is not None:
            json_payload["name"] = name
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if device_ids is not None:
            json_payload["device_ids"] = device_ids

        res = self.client.post("/spaces/create", json=json_payload)

        return Space.from_dict(res["space"])

    def delete(self, *, space_id: str) -> None:
        json_payload = {}

        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/delete", json=json_payload)

        return None

    def get(self, *, space_id: str) -> Space:
        json_payload = {}

        if space_id is not None:
            json_payload["space_id"] = space_id

        res = self.client.post("/spaces/get", json=json_payload)

        return Space.from_dict(res["space"])

    def list(
        self,
    ) -> List[Space]:
        json_payload = {}

        res = self.client.post("/spaces/list", json=json_payload)

        return [Space.from_dict(item) for item in res["spaces"]]

    def remove_acs_entrances(
        self, *, acs_entrance_ids: List[str], space_id: str
    ) -> None:
        json_payload = {}

        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/remove_acs_entrances", json=json_payload)

        return None

    def remove_devices(self, *, device_ids: List[str], space_id: str) -> None:
        json_payload = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/remove_devices", json=json_payload)

        return None

    def update(self, *, space_id: str, name: Optional[str] = None) -> Space:
        json_payload = {}

        if space_id is not None:
            json_payload["space_id"] = space_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post("/spaces/update", json=json_payload)

        return Space.from_dict(res["space"])
