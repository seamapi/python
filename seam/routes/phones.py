from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractPhones, Phone
from .phones_simulate import PhonesSimulate


class Phones(AbstractPhones):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = PhonesSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> PhonesSimulate:
        return self._simulate

    def deactivate(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/phones/deactivate", json=json_payload)

        return None

    def list(
        self,
        *,
        acs_credential_id: Optional[str] = None,
        owner_user_identity_id: Optional[str] = None
    ) -> List[Phone]:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if owner_user_identity_id is not None:
            json_payload["owner_user_identity_id"] = owner_user_identity_id

        res = self.client.post("/phones/list", json=json_payload)

        return [Phone.from_dict(item) for item in res["phones"]]
