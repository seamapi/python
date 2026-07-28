from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedAccessMethod


class AbstractAccessMethodsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> UnmanagedAccessMethod:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[UnmanagedAccessMethod]:
        raise NotImplementedError()


class AccessMethodsUnmanaged(AbstractAccessMethodsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, access_method_id: str) -> UnmanagedAccessMethod:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        res = self.client.post("/access_methods/unmanaged/get", json=json_payload)

        return UnmanagedAccessMethod.from_dict(res["access_method"])

    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[UnmanagedAccessMethod]:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if space_id is not None:
            json_payload["space_id"] = space_id

        res = self.client.post("/access_methods/unmanaged/list", json=json_payload)

        return [UnmanagedAccessMethod.from_dict(item) for item in res["access_methods"]]
