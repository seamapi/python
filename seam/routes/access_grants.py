from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAccessGrants, AccessGrant


class AccessGrants(AbstractAccessGrants):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        requested_access_methods: List[Dict[str, Any]],
        user_identity_id: Optional[str] = None,
        user_identity: Optional[Dict[str, Any]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        ends_at: Optional[str] = None,
        location: Optional[Dict[str, Any]] = None,
        location_ids: Optional[List[str]] = None,
        space_ids: Optional[List[str]] = None,
        starts_at: Optional[str] = None
    ) -> AccessGrant:
        json_payload = {}

        if requested_access_methods is not None:
            json_payload["requested_access_methods"] = requested_access_methods
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity is not None:
            json_payload["user_identity"] = user_identity
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if location is not None:
            json_payload["location"] = location
        if location_ids is not None:
            json_payload["location_ids"] = location_ids
        if space_ids is not None:
            json_payload["space_ids"] = space_ids
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        res = self.client.post("/access_grants/create", json=json_payload)

        return AccessGrant.from_dict(res["access_grant"])

    def delete(self, *, access_grant_id: str) -> None:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id

        self.client.post("/access_grants/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None
    ) -> AccessGrant:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key

        res = self.client.post("/access_grants/get", json=json_payload)

        return AccessGrant.from_dict(res["access_grant"])

    def list(
        self,
        *,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        location_id: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> List[AccessGrant]:
        json_payload = {}

        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if location_id is not None:
            json_payload["location_id"] = location_id
        if space_id is not None:
            json_payload["space_id"] = space_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/access_grants/list", json=json_payload)

        return [AccessGrant.from_dict(item) for item in res["access_grants"]]

    def update(
        self,
        *,
        access_grant_id: str,
        ends_at: Optional[str] = None,
        starts_at: Optional[str] = None
    ) -> None:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        self.client.post("/access_grants/update", json=json_payload)

        return None
