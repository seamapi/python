from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsCredentials, AcsCredential


class AcsCredentials(AbstractAcsCredentials):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_offline_code(
        self,
        *,
        acs_user_id: str,
        allowed_acs_entrance_id: str,
        ends_at: Optional[str] = None,
        is_one_time_use: Optional[bool] = None,
        starts_at: Optional[str] = None
    ) -> AcsCredential:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if allowed_acs_entrance_id is not None:
            json_payload["allowed_acs_entrance_id"] = allowed_acs_entrance_id
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_one_time_use is not None:
            json_payload["is_one_time_use"] = is_one_time_use
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        res = self.client.post(
            "/acs/credentials/create_offline_code", json=json_payload
        )

        return AcsCredential.from_dict(res["acs_credential"])
