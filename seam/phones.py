from seam.types import AbstractPhones, AbstractSeam as Seam, Phone
from typing import Optional, Any, List, Dict, Union
from seam.phones_simulate import PhonesSimulate


class Phones(AbstractPhones):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam
        self._simulate = PhonesSimulate(seam=seam)

    @property
    def simulate(self) -> PhonesSimulate:
        return self._simulate

    def deactivate(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.seam.make_request("POST", "/phones/deactivate", json=json_payload)

        return None

    def list(self, *, owner_user_identity_id: Optional[str] = None) -> List[Phone]:
        json_payload = {}

        if owner_user_identity_id is not None:
            json_payload["owner_user_identity_id"] = owner_user_identity_id

        res = self.seam.make_request("POST", "/phones/list", json=json_payload)

        return [Phone.from_dict(item) for item in res["phones"]]
