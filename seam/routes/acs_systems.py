from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import (AcsSystem)


class AbstractAcsSystems(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_system_id: str) -> AcsSystem:
        """Returns a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :param acs_system_id: ID of the access system that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, connected_account_id: Optional[str] = None, customer_key: Optional[str] = None, search: Optional[str] = None) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_.
        
        To filter the list of returned access systems by a specific connected account ID, include the ``connected_account_id`` in the request body. If you omit the ``connected_account_id`` parameter, the response includes all access systems connected to your workspace.

        :param connected_account_id: ID of the connected account by which you want to filter the list of access systems.

        :param customer_key: Customer key for which you want to list access systems.

        :param search: String for which to search. Filters returned access systems to include all records that satisfy a partial match using ``name`` or ``acs_system_id``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_compatible_credential_manager_acs_systems(self, *, acs_system_id: str) -> List[AcsSystem]:
        """Returns a list of all credential manager systems that are compatible with a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.
        
        Specify the access system for which you want to retrieve all compatible credential manager systems by including the corresponding ``acs_system_id`` in the request body.

        :param acs_system_id: ID of the access system for which you want to retrieve all compatible credential manager systems.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def report_devices(self, *, acs_system_id: str, acs_encoders: Optional[List[Dict[str, Any]]] = None, acs_entrances: Optional[List[Dict[str, Any]]] = None) -> None:
        """Reports ACS system device status including encoders and entrances.

        :param acs_system_id: ID of the ACS system to report resources for

        :param acs_encoders: Array of ACS encoders to report

        :param acs_entrances: Array of ACS entrances to report

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AcsSystems(AbstractAcsSystems):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(path="/acs/systems/get", has_required_parameters=True, has_pagination=False)
    def get(self, *, acs_system_id: str) -> AcsSystem:
        """Returns a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :param acs_system_id: ID of the access system that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/systems/get")

        res = self.client.get("/acs/systems/get", params=params)

        return AcsSystem.from_dict(res["acs_system"])

    @route_metadata(path="/acs/systems/list", has_required_parameters=False, has_pagination=False)
    def list(self, *, connected_account_id: Optional[str] = None, customer_key: Optional[str] = None, search: Optional[str] = None) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_.
        
        To filter the list of returned access systems by a specific connected account ID, include the ``connected_account_id`` in the request body. If you omit the ``connected_account_id`` parameter, the response includes all access systems connected to your workspace.

        :param connected_account_id: ID of the connected account by which you want to filter the list of access systems.

        :param customer_key: Customer key for which you want to list access systems.

        :param search: String for which to search. Filters returned access systems to include all records that satisfy a partial match using ``name`` or ``acs_system_id``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if search is not None:
            params["search"] = search

        res = self.client.get("/acs/systems/list", params=params)

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    @route_metadata(path="/acs/systems/list_compatible_credential_manager_acs_systems", has_required_parameters=True, has_pagination=False)
    def list_compatible_credential_manager_acs_systems(self, *, acs_system_id: str) -> List[AcsSystem]:
        """Returns a list of all credential manager systems that are compatible with a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.
        
        Specify the access system for which you want to retrieve all compatible credential manager systems by including the corresponding ``acs_system_id`` in the request body.

        :param acs_system_id: ID of the access system for which you want to retrieve all compatible credential manager systems.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/systems/list_compatible_credential_manager_acs_systems")

        res = self.client.get("/acs/systems/list_compatible_credential_manager_acs_systems", params=params)

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    @route_metadata(path="/acs/systems/report_devices", has_required_parameters=True, has_pagination=False)
    def report_devices(self, *, acs_system_id: str, acs_encoders: Optional[List[Dict[str, Any]]] = None, acs_entrances: Optional[List[Dict[str, Any]]] = None) -> None:
        """Reports ACS system device status including encoders and entrances.

        :param acs_system_id: ID of the ACS system to report resources for

        :param acs_encoders: Array of ACS encoders to report

        :param acs_entrances: Array of ACS entrances to report

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_encoders is not None:
            json_payload["acs_encoders"] = acs_encoders
        if acs_entrances is not None:
            json_payload["acs_entrances"] = acs_entrances

        if not json_payload:
            raise ValueError("At least one parameter is required for /acs/systems/report_devices")

        self.client.post("/acs/systems/report_devices", json=json_payload)

        return None
