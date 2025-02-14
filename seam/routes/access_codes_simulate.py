from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAccessCodesSimulate, UnmanagedAccessCode


class AccessCodesSimulate(AbstractAccessCodesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        json_payload = {}

        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post(
            "/access_codes/simulate/create_unmanaged_access_code", json=json_payload
        )

        return UnmanagedAccessCode.from_dict(res["access_code"])
