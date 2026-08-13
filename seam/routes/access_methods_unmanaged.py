from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedAccessMethod


class AbstractAccessMethodsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> UnmanagedAccessMethod:
        """Gets an unmanaged access method (where is_managed = false).

        :param access_method_id: ID of unmanaged access method to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[UnmanagedAccessMethod]:
        """Lists all unmanaged access methods (where is_managed = false), usually filtered by Access Grant.

        :param access_grant_id: ID of Access Grant to list unmanaged access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all unmanaged access methods.

        :param device_id: ID of the device for which you want to retrieve all unmanaged access methods.

        :param space_id: ID of the space for which you want to retrieve all unmanaged access methods.

        :returns: OK"""
        raise NotImplementedError()


class AccessMethodsUnmanaged(AbstractAccessMethodsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, access_method_id: str) -> UnmanagedAccessMethod:
        """Gets an unmanaged access method (where is_managed = false).

        :param access_method_id: ID of unmanaged access method to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_id is not None:
            params["access_method_id"] = access_method_id

        res = self.client.get("/access_methods/unmanaged/get", params=params)

        return UnmanagedAccessMethod.from_dict(res["access_method"])

    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[UnmanagedAccessMethod]:
        """Lists all unmanaged access methods (where is_managed = false), usually filtered by Access Grant.

        :param access_grant_id: ID of Access Grant to list unmanaged access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all unmanaged access methods.

        :param device_id: ID of the device for which you want to retrieve all unmanaged access methods.

        :param space_id: ID of the space for which you want to retrieve all unmanaged access methods.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            params["device_id"] = device_id
        if space_id is not None:
            params["space_id"] = space_id

        res = self.client.get("/access_methods/unmanaged/list", params=params)

        return [UnmanagedAccessMethod.from_dict(item) for item in res["access_methods"]]
