from seam.types import (
    AbstractAccessCodesSimulate,
    AbstractSeam as Seam,
    UnmanagedAccessCode,
)
from typing import Optional, Any, List, Dict, Union


class AccessCodesSimulate(AbstractAccessCodesSimulate):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        res = self.seam.make_request(
            "POST",
            "/access_codes/simulate/create_unmanaged_access_code",
            json=json_payload,
        )

        return UnmanagedAccessCode.from_dict(res["access_code"])
