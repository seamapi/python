from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAccessCodesSimulate, UnmanagedAccessCode


class AccessCodesSimulate(AbstractAccessCodesSimulate, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_unmanaged_access_code(
        self, *, device_id: str, name: str, code: str
    ) -> UnmanagedAccessCode:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name
        if code is not None:
            json_payload["code"] = code

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/simulate/create_unmanaged_access_code",
                method="POST",
                body=json_payload,
                response_key="access_code",
                model_type=UnmanagedAccessCode,
            ),
        )
