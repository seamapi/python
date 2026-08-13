from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Space, Batch


class AbstractSpaces(abc.ABC):

    @abc.abstractmethod
    def add_acs_entrances(self, *, acs_entrance_ids: List[str], space_id: str) -> None:
        """Adds `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ to a specific space.

        :param acs_entrance_ids: IDs of the entrances that you want to add to the space.

        :param space_id: ID of the space to which you want to add entrances."""
        raise NotImplementedError()

    @abc.abstractmethod
    def add_connected_account(
        self, *, connected_account_id: str, space_id: str
    ) -> None:
        """Adds a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ to a specific space.

        :param connected_account_id: ID of the connected account that you want to add to the space.

        :param space_id: ID of the space to which you want to add the connected account.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def add_devices(self, *, device_ids: List[str], space_id: str) -> None:
        """Adds devices to a specific space.

        :param device_ids: IDs of the devices that you want to add to the space.

        :param space_id: ID of the space to which you want to add devices."""
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        name: str,
        acs_entrance_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        customer_data: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        space_key: Optional[str] = None,
    ) -> Space:
        """Creates a new space.

        :param name: Name of the space that you want to create.

        :param acs_entrance_ids: IDs of the entrances that you want to add to the new space.

        :param connected_account_ids: IDs of connected accounts to associate with the new space. Persisted on seam.location_third_party_account so the UI can show which provider account(s) a space came from.

        :param customer_data: Reservation/stay-related defaults for the space.

        :param customer_key: Customer key for which you want to create the space.

        :param device_ids: IDs of the devices that you want to add to the new space.

        :param space_key: Unique key for the space within the workspace.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, space_id: str) -> None:
        """Deletes a space.

        :param space_id: ID of the space that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, space_id: Optional[str] = None, space_key: Optional[str] = None
    ) -> Space:
        """Gets a space.

        :param space_id: ID of the space that you want to get.

        :param space_key: Unique key of the space that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        space_ids: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
    ) -> Batch:
        """Gets all related resources for one or more Spaces.

        :param exclude:

        :param include:

        :param space_ids: IDs of the spaces that you want to get along with their related resources.

        :param space_keys: Keys of the spaces that you want to get along with their related resources.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        customer_key: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_key: Optional[str] = None,
    ) -> List[Space]:
        """Returns a list of all spaces.

        :param customer_key: Customer key for which you want to list spaces.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned spaces to include all records that satisfy a partial match using ``name``, ``space_key``, or ``customer_key``.

        :param space_key: Filter spaces by space_key.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_acs_entrances(
        self, *, acs_entrance_ids: List[str], space_id: str
    ) -> None:
        """Removes `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ from a specific space.

        :param acs_entrance_ids: IDs of the entrances that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove entrances."""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_connected_account(
        self, *, connected_account_id: str, space_id: str
    ) -> None:
        """Removes a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ from a specific space.

        :param connected_account_id: ID of the connected account that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove the connected account.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_devices(self, *, device_ids: List[str], space_id: str) -> None:
        """Removes devices from a specific space.

        :param device_ids: IDs of the devices that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove devices."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        acs_entrance_ids: Optional[List[str]] = None,
        customer_data: Optional[Dict[str, Any]] = None,
        device_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        space_id: Optional[str] = None,
        space_key: Optional[str] = None,
    ) -> Space:
        """Updates an existing space.

        :param acs_entrance_ids: IDs of the entrances that you want to set for the space. If specified, this will replace all existing entrances.

        :param customer_data: Reservation/stay-related defaults for the space. Only the keys you provide are updated; omit a key to leave it unchanged. Pass null on a key to clear it.

        :param device_ids: IDs of the devices that you want to set for the space. If specified, this will replace all existing devices.

        :param name: Name of the space.

        :param space_id: ID of the space that you want to update.

        :param space_key: Unique key of the space that you want to update.

        :returns: OK"""
        raise NotImplementedError()


class Spaces(AbstractSpaces):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_acs_entrances(self, *, acs_entrance_ids: List[str], space_id: str) -> None:
        """Adds `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ to a specific space.

        :param acs_entrance_ids: IDs of the entrances that you want to add to the space.

        :param space_id: ID of the space to which you want to add entrances."""
        json_payload: Dict[str, Any] = {}

        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.put("/spaces/add_acs_entrances", json=json_payload)

        return None

    def add_connected_account(
        self, *, connected_account_id: str, space_id: str
    ) -> None:
        """Adds a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ to a specific space.

        :param connected_account_id: ID of the connected account that you want to add to the space.

        :param space_id: ID of the space to which you want to add the connected account.
        """
        json_payload: Dict[str, Any] = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.put("/spaces/add_connected_account", json=json_payload)

        return None

    def add_devices(self, *, device_ids: List[str], space_id: str) -> None:
        """Adds devices to a specific space.

        :param device_ids: IDs of the devices that you want to add to the space.

        :param space_id: ID of the space to which you want to add devices."""
        json_payload: Dict[str, Any] = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.put("/spaces/add_devices", json=json_payload)

        return None

    def create(
        self,
        *,
        name: str,
        acs_entrance_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        customer_data: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        space_key: Optional[str] = None,
    ) -> Space:
        """Creates a new space.

        :param name: Name of the space that you want to create.

        :param acs_entrance_ids: IDs of the entrances that you want to add to the new space.

        :param connected_account_ids: IDs of connected accounts to associate with the new space. Persisted on seam.location_third_party_account so the UI can show which provider account(s) a space came from.

        :param customer_data: Reservation/stay-related defaults for the space.

        :param customer_key: Customer key for which you want to create the space.

        :param device_ids: IDs of the devices that you want to add to the new space.

        :param space_key: Unique key for the space within the workspace.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if name is not None:
            json_payload["name"] = name
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if customer_data is not None:
            json_payload["customer_data"] = customer_data
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if space_key is not None:
            json_payload["space_key"] = space_key

        res = self.client.post("/spaces/create", json=json_payload)

        return Space.from_dict(res["space"])

    def delete(self, *, space_id: str) -> None:
        """Deletes a space.

        :param space_id: ID of the space that you want to delete."""
        params: Dict[str, Any] = {}

        if space_id is not None:
            params["space_id"] = space_id

        self.client.delete("/spaces/delete", params=params)

        return None

    def get(
        self, *, space_id: Optional[str] = None, space_key: Optional[str] = None
    ) -> Space:
        """Gets a space.

        :param space_id: ID of the space that you want to get.

        :param space_key: Unique key of the space that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if space_id is not None:
            params["space_id"] = space_id
        if space_key is not None:
            params["space_key"] = space_key

        res = self.client.get("/spaces/get", params=params)

        return Space.from_dict(res["space"])

    def get_related(
        self,
        *,
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
        space_ids: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
    ) -> Batch:
        """Gets all related resources for one or more Spaces.

        :param exclude:

        :param include:

        :param space_ids: IDs of the spaces that you want to get along with their related resources.

        :param space_keys: Keys of the spaces that you want to get along with their related resources.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if exclude is not None:
            json_payload["exclude"] = exclude
        if include is not None:
            json_payload["include"] = include
        if space_ids is not None:
            json_payload["space_ids"] = space_ids
        if space_keys is not None:
            json_payload["space_keys"] = space_keys

        res = self.client.post("/spaces/get_related", json=json_payload)

        return Batch.from_dict(res["batch"])

    def list(
        self,
        *,
        customer_key: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_key: Optional[str] = None,
    ) -> List[Space]:
        """Returns a list of all spaces.

        :param customer_key: Customer key for which you want to list spaces.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned spaces to include all records that satisfy a partial match using ``name``, ``space_key``, or ``customer_key``.

        :param space_key: Filter spaces by space_key.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if customer_key is not None:
            params["customer_key"] = customer_key
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if space_key is not None:
            params["space_key"] = space_key

        res = self.client.get("/spaces/list", params=params)

        return [Space.from_dict(item) for item in res["spaces"]]

    def remove_acs_entrances(
        self, *, acs_entrance_ids: List[str], space_id: str
    ) -> None:
        """Removes `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ from a specific space.

        :param acs_entrance_ids: IDs of the entrances that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove entrances."""
        json_payload: Dict[str, Any] = {}

        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/remove_acs_entrances", json=json_payload)

        return None

    def remove_connected_account(
        self, *, connected_account_id: str, space_id: str
    ) -> None:
        """Removes a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_ from a specific space.

        :param connected_account_id: ID of the connected account that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove the connected account.
        """
        params: Dict[str, Any] = {}

        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if space_id is not None:
            params["space_id"] = space_id

        self.client.delete("/spaces/remove_connected_account", params=params)

        return None

    def remove_devices(self, *, device_ids: List[str], space_id: str) -> None:
        """Removes devices from a specific space.

        :param device_ids: IDs of the devices that you want to remove from the space.

        :param space_id: ID of the space from which you want to remove devices."""
        json_payload: Dict[str, Any] = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if space_id is not None:
            json_payload["space_id"] = space_id

        self.client.post("/spaces/remove_devices", json=json_payload)

        return None

    def update(
        self,
        *,
        acs_entrance_ids: Optional[List[str]] = None,
        customer_data: Optional[Dict[str, Any]] = None,
        device_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        space_id: Optional[str] = None,
        space_key: Optional[str] = None,
    ) -> Space:
        """Updates an existing space.

        :param acs_entrance_ids: IDs of the entrances that you want to set for the space. If specified, this will replace all existing entrances.

        :param customer_data: Reservation/stay-related defaults for the space. Only the keys you provide are updated; omit a key to leave it unchanged. Pass null on a key to clear it.

        :param device_ids: IDs of the devices that you want to set for the space. If specified, this will replace all existing devices.

        :param name: Name of the space.

        :param space_id: ID of the space that you want to update.

        :param space_key: Unique key of the space that you want to update.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if customer_data is not None:
            json_payload["customer_data"] = customer_data
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if name is not None:
            json_payload["name"] = name
        if space_id is not None:
            json_payload["space_id"] = space_id
        if space_key is not None:
            json_payload["space_key"] = space_key

        res = self.client.patch("/spaces/update", json=json_payload)

        return Space.from_dict(res["space"])
