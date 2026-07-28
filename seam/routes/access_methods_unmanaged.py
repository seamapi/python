from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractAccessMethodsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> None:
        """Gets an unmanaged access method (where is_managed = false).

        :param access_method_id: ID of unmanaged access method to get.
        :type access_method_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> None:
        """Lists all unmanaged access methods (where is_managed = false), usually filtered by Access Grant.

        :param access_grant_id: ID of Access Grant to list unmanaged access methods for.
        :type access_grant_id: str

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all unmanaged access methods.
        :type acs_entrance_id: str

        :param device_id: ID of the device for which you want to retrieve all unmanaged access methods.
        :type device_id: str

        :param space_id: ID of the space for which you want to retrieve all unmanaged access methods.
        :type space_id: str"""
        raise NotImplementedError()


class AccessMethodsUnmanaged(AbstractAccessMethodsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, access_method_id: str) -> None:
        """Gets an unmanaged access method (where is_managed = false).

        :param access_method_id: ID of unmanaged access method to get.
        :type access_method_id: str"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        self.client.post("/access_methods/unmanaged/get", json=json_payload)

        return None

    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> None:
        """Lists all unmanaged access methods (where is_managed = false), usually filtered by Access Grant.

        :param access_grant_id: ID of Access Grant to list unmanaged access methods for.
        :type access_grant_id: str

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all unmanaged access methods.
        :type acs_entrance_id: str

        :param device_id: ID of the device for which you want to retrieve all unmanaged access methods.
        :type device_id: str

        :param space_id: ID of the space for which you want to retrieve all unmanaged access methods.
        :type space_id: str"""
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/access_methods/unmanaged/list", json=json_payload)

        return None
