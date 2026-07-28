from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Phone
from .phones_simulate import AbstractPhonesSimulate, PhonesSimulate


class AbstractPhones(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractPhonesSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def deactivate(self, *, device_id: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, device_id: str) -> Phone:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_credential_id: Optional[str] = None,
        owner_user_identity_id: Optional[str] = None
    ) -> List[Phone]:
        raise NotImplementedError()


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

    def get(self, *, device_id: str) -> Phone:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/phones/get", json=json_payload)

        return Phone.from_dict(res["phone"])

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
