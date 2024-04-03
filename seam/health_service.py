from seam.types import AbstractHealthService, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union


class HealthService(AbstractHealthService):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def by_service_name(self, *, service_name: str) -> None:
        json_payload = {}

        if service_name is not None:
            json_payload["service_name"] = service_name

        self.seam.make_request(
            "POST", "/health/service/[service_name]", json=json_payload
        )

        return None
