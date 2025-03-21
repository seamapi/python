from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsAccessGroups, AcsAccessGroup, AcsEntrance, AcsUser


class AcsAccessGroups(AbstractAcsAccessGroups, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/access_groups/get",
                method="POST",
                body=json_payload,
                response_key="acs_access_group",
                model_type=AcsAccessGroup,
            ),
        )

    def list(
        self, *, acs_system_id: Optional[str] = None, acs_user_id: Optional[str] = None
    ) -> List[AcsAccessGroup]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/access_groups/list",
                method="POST",
                body=json_payload,
                response_key="acs_access_groups",
                model_type=List[AcsAccessGroup],
            ),
        )

    def list_accessible_entrances(
        self, *, acs_access_group_id: str
    ) -> List[AcsEntrance]:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/access_groups/list_accessible_entrances",
                method="POST",
                body=json_payload,
                response_key="acs_entrances",
                model_type=List[AcsEntrance],
            ),
        )

    def list_users(self, *, acs_access_group_id: str) -> List[AcsUser]:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/access_groups/list_users",
                method="POST",
                body=json_payload,
                response_key="acs_users",
                model_type=List[AcsUser],
            ),
        )

    def remove_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None
