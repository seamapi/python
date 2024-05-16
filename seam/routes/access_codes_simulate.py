from seam.types import AbstractSeam as Seam
from seam.routes.types import AbstractAccessCodesSimulate, UnmanagedAccessCode
from typing import Optional, Any, List, Dict, Union


class AccessCodesSimulate(AbstractAccessCodesSimulate):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        res = self.seam.make_request(
            "POST",
            "/access_codes/simulate/create_unmanaged_access_code",
            json=json_payload,
        )

        return UnmanagedAccessCode.from_dict(res["access_code"])
