from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import AcsSystem


class AbstractAcsSystems(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_system_id: str) -> AcsSystem:
        """Returns a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :param acs_system_id: ID of the access system that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        search: Optional[str] = None
    ) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_.

        To filter the list of returned access systems by a specific connected account ID, include the ``connected_account_id`` in the request body. If you omit the ``connected_account_id`` parameter, the response includes all access systems connected to your workspace.

        :param connected_account_id: ID of the connected account by which you want to filter the list of access systems.

        :param customer_key: Customer key for which you want to list access systems.

        :param search: String for which to search. Filters returned access systems to include all records that satisfy a partial match using ``name`` or ``acs_system_id``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_compatible_credential_manager_acs_systems(
        self, *, acs_system_id: str
    ) -> List[AcsSystem]:
        """Returns a list of all credential manager systems that are compatible with a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        Specify the access system for which you want to retrieve all compatible credential manager systems by including the corresponding ``acs_system_id`` in the request body.

        :param acs_system_id: ID of the access system for which you want to retrieve all compatible credential manager systems.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def report_devices(
        self,
        *,
        acs_system_id: str,
        acs_encoders: Optional[List[Dict[str, Any]]] = None,
        acs_entrances: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        """Reports ACS system device status including encoders and entrances.

        :param acs_system_id: ID of the ACS system to report resources for

        :param acs_encoders: Array of ACS encoders to report

        :param acs_entrances: Array of ACS entrances to report"""
        raise NotImplementedError()


class AcsSystems(AbstractAcsSystems):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_system_id: str) -> AcsSystem:
        """Returns a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :param acs_system_id: ID of the access system that you want to get.

        :returns: OK"""
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post("/acs/systems/get", json=json_payload)

        return AcsSystem.from_dict(res["acs_system"])

    def list(
        self,
        *,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        search: Optional[str] = None
    ) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_.

        To filter the list of returned access systems by a specific connected account ID, include the ``connected_account_id`` in the request body. If you omit the ``connected_account_id`` parameter, the response includes all access systems connected to your workspace.

        :param connected_account_id: ID of the connected account by which you want to filter the list of access systems.

        :param customer_key: Customer key for which you want to list access systems.

        :param search: String for which to search. Filters returned access systems to include all records that satisfy a partial match using ``name`` or ``acs_system_id``.

        :returns: OK"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if search is not None:
            json_payload["search"] = search

        res = self.client.post("/acs/systems/list", json=json_payload)

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    def list_compatible_credential_manager_acs_systems(
        self, *, acs_system_id: str
    ) -> List[AcsSystem]:
        """Returns a list of all credential manager systems that are compatible with a specified `access system <https://docs.seam.co/low-level-apis/access-systems>`_.

        Specify the access system for which you want to retrieve all compatible credential manager systems by including the corresponding ``acs_system_id`` in the request body.

        :param acs_system_id: ID of the access system for which you want to retrieve all compatible credential manager systems.

        :returns: OK"""
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post(
            "/acs/systems/list_compatible_credential_manager_acs_systems",
            json=json_payload,
        )

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    def report_devices(
        self,
        *,
        acs_system_id: str,
        acs_encoders: Optional[List[Dict[str, Any]]] = None,
        acs_entrances: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        """Reports ACS system device status including encoders and entrances.

        :param acs_system_id: ID of the ACS system to report resources for

        :param acs_encoders: Array of ACS encoders to report

        :param acs_entrances: Array of ACS entrances to report"""
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_encoders is not None:
            json_payload["acs_encoders"] = acs_encoders
        if acs_entrances is not None:
            json_payload["acs_entrances"] = acs_entrances

        self.client.post("/acs/systems/report_devices", json=json_payload)

        return None
