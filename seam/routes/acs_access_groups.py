from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import AcsAccessGroup, AcsEntrance, AcsUser


class AbstractAcsAccessGroups(abc.ABC):

    @abc.abstractmethod
    def add_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group to which you want to add an access system user.

        :param acs_user_id: ID of the access system user that you want to add to an access group. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the desired user identity that you want to add to an access group. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, acs_access_group_id: str) -> None:
        """Deletes a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        """Returns a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AcsAccessGroup]:
        """Returns a list of all `access groups <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all access groups.

        :param acs_user_id: ID of the access system user for which you want to retrieve all access groups.

        :param search: String for which to search. Filters returned access groups to include all records that satisfy a partial match using ``name`` or ``acs_access_group_id``.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access groups.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(
        self, *, acs_access_group_id: str
    ) -> List[AcsEntrance]:
        """Returns a list of all accessible entrances for a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group for which you want to retrieve all accessible entrances.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_users(self, *, acs_access_group_id: str) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in an `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group for which you want to retrieve all access system users.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group from which you want to remove an access system user.

        :param acs_user_id: ID of the access system user that you want to remove from an access group.

        :param user_identity_id: ID of the user identity associated with the user that you want to remove from an access group.
        """
        raise NotImplementedError()


class AcsAccessGroups(AbstractAcsAccessGroups):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group to which you want to add an access system user.

        :param acs_user_id: ID of the access system user that you want to add to an access group. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the desired user identity that you want to add to an access group. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/access_groups/add_user", json=json_payload)

        return None

    def delete(self, *, acs_access_group_id: str) -> None:
        """Deletes a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group that you want to delete."""
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        self.client.post("/acs/access_groups/delete", json=json_payload)

        return None

    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        """Returns a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group that you want to get.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.client.post("/acs/access_groups/get", json=json_payload)

        return AcsAccessGroup.from_dict(res["acs_access_group"])

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AcsAccessGroup]:
        """Returns a list of all `access groups <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all access groups.

        :param acs_user_id: ID of the access system user for which you want to retrieve all access groups.

        :param search: String for which to search. Filters returned access groups to include all records that satisfy a partial match using ``name`` or ``acs_access_group_id``.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access groups.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if search is not None:
            json_payload["search"] = search
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/acs/access_groups/list", json=json_payload)

        return [AcsAccessGroup.from_dict(item) for item in res["acs_access_groups"]]

    def list_accessible_entrances(
        self, *, acs_access_group_id: str
    ) -> List[AcsEntrance]:
        """Returns a list of all accessible entrances for a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group for which you want to retrieve all accessible entrances.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.client.post(
            "/acs/access_groups/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def list_users(self, *, acs_access_group_id: str) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in an `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group for which you want to retrieve all access system users.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.client.post("/acs/access_groups/list_users", json=json_payload)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    def remove_user(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group from which you want to remove an access system user.

        :param acs_user_id: ID of the access system user that you want to remove from an access group.

        :param user_identity_id: ID of the user identity associated with the user that you want to remove from an access group.
        """
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/access_groups/remove_user", json=json_payload)

        return None
