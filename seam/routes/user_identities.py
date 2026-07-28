from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import (
    UserIdentity,
    InstantKey,
    Device,
    AcsEntrance,
    AcsSystem,
    AcsUser,
)
from .user_identities_unmanaged import (
    AbstractUserIdentitiesUnmanaged,
    UserIdentitiesUnmanaged,
)


class AbstractUserIdentities(abc.ABC):

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractUserIdentitiesUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_acs_user(
        self,
        *,
        acs_user_id: str,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        You must specify either ``user_identity_id`` or ``user_identity_key`` to identify the user identity.

        If ``user_identity_key`` is provided, but the user identity doesn't exist, a new user identity will be created automatically using information from the ACS user.

        :param acs_user_id: ID of the access system user that you want to add to the user identity.
        :type acs_user_id: str

        :param user_identity_id: ID of the user identity to which you want to add an access system user.
        :type user_identity_id: str

        :param user_identity_key: Key of the user identity to which you want to add an access system user.
        :type user_identity_key: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        acs_system_ids: Optional[List[str]] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        """Creates a new `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param acs_system_ids: List of access system IDs to associate with the new user identity through access system users. If there's no user with the same email address or phone number in the specified access systems, a new access system user is created. If there is an existing user with the same email or phone number in the specified access systems, the user is linked to the user identity.
        :type acs_system_ids: List[str]

        :param email_address: Unique email address for the new user identity.
        :type email_address: str

        :param full_name: Full name of the user associated with the new user identity.
        :type full_name: str

        :param phone_number: Unique phone number for the new user identity in E.164 format (for example, +15555550100).
        :type phone_number: str

        :param user_identity_key: Unique key for the new user identity.
        :type user_identity_key: str

        :returns: OK
        :rtype: UserIdentity"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, user_identity_id: str) -> None:
        """Deletes a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This deletes the user identity and all associated resources, including any `credentials <https://docs.seam.co/api/acs/credentials>`_, `acs users <https://docs.seam.co/api/acs/users>`_ and `client sessions <https://docs.seam.co/api/client_sessions>`_.

        :param user_identity_id: ID of the user identity that you want to delete.
        :type user_identity_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_instant_key(
        self,
        *,
        user_identity_id: str,
        customization_profile_id: Optional[str] = None,
        max_use_count: Optional[float] = None
    ) -> InstantKey:
        """Generates a new `instant key <https://docs.seam.co/capability-guides/instant-keys>`_ for a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to generate an instant key.
        :type user_identity_id: str

        :param customization_profile_id:
        :type customization_profile_id: str

        :param max_use_count: Maximum number of times the instant key can be used. Default: 1.
        :type max_use_count: float

        :returns: OK
        :rtype: InstantKey"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        """Returns a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to get.
        :type user_identity_id: str

        :param user_identity_key:
        :type user_identity_key: str

        :returns: OK
        :rtype: UserIdentity"""
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        """Grants a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ access to a specified `device <https://docs.seam.co/core-concepts/devices/>`_.

        :param device_id: ID of the managed device to which you want to grant access to the user identity.
        :type device_id: str

        :param user_identity_id: ID of the user identity that you want to grant access to a device.
        :type user_identity_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        created_before: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> List[UserIdentity]:
        """Returns a list of all `user identities <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param created_before: Timestamp by which to limit returned user identities. Returns user identities created before this timestamp.
        :type created_before: str

        :param credential_manager_acs_system_id: ``acs_system_id`` of the credential manager by which you want to filter the list of user identities.
        :type credential_manager_acs_system_id: str

        :param limit: Maximum number of records to return per page.
        :type limit: int

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.
        :type page_cursor: str

        :param search: String for which to search. Filters returned user identities to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address`` or ``user_identity_id``.
        :type search: str

        :param user_identity_ids: Array of user identity IDs by which to filter the list of user identities.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: List[UserIdentity]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_devices(self, *, user_identity_id: str) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_ associated with a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This includes devices derived from the access grants assigned to the user identity and devices directly linked to the user identity.

        :param user_identity_id: ID of the user identity for which you want to retrieve all accessible devices.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[Device]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(self, *, user_identity_id: str) -> List[AcsEntrance]:
        """Returns a list of all `ACS entrances <https://docs.seam.co/api/acs/entrances>`_ accessible to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This includes entrances derived from the access grants assigned to the user identity and entrances accessible through ACS users linked to the user identity.

        :param user_identity_id: ID of the user identity for which you want to retrieve all accessible entrances.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsEntrance]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_acs_systems(self, *, user_identity_id: str) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_ associated with a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access systems.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsSystem]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_acs_users(self, *, user_identity_id: str) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ assigned to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access system users.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsUser]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_acs_user(self, *, acs_user_id: str, user_identity_id: str) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param acs_user_id: ID of the access system user that you want to remove from the user identity..
        :type acs_user_id: str

        :param user_identity_id: ID of the user identity from which you want to remove an access system user.
        :type user_identity_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        """Revokes access to a specified `device <https://docs.seam.co/core-concepts/devices/>`_ from a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param device_id: ID of the managed device to which you want to revoke access from the user identity.
        :type device_id: str

        :param user_identity_id: ID of the user identity from which you want to revoke access to a device.
        :type user_identity_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        user_identity_id: str,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
        """Updates a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to update.
        :type user_identity_id: str

        :param email_address: Unique email address for the user identity.
        :type email_address: str

        :param full_name: Full name of the user associated with the user identity.
        :type full_name: str

        :param phone_number: Unique phone number for the user identity.
        :type phone_number: str

        :param user_identity_key: Unique key for the user identity.
        :type user_identity_key: str"""
        raise NotImplementedError()


class UserIdentities(AbstractUserIdentities):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._unmanaged = UserIdentitiesUnmanaged(client=client, defaults=defaults)

    @property
    def unmanaged(self) -> UserIdentitiesUnmanaged:
        return self._unmanaged

    def add_acs_user(
        self,
        *,
        acs_user_id: str,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        You must specify either ``user_identity_id`` or ``user_identity_key`` to identify the user identity.

        If ``user_identity_key`` is provided, but the user identity doesn't exist, a new user identity will be created automatically using information from the ACS user.

        :param acs_user_id: ID of the access system user that you want to add to the user identity.
        :type acs_user_id: str

        :param user_identity_id: ID of the user identity to which you want to add an access system user.
        :type user_identity_id: str

        :param user_identity_key: Key of the user identity to which you want to add an access system user.
        :type user_identity_key: str"""
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        self.client.post("/user_identities/add_acs_user", json=json_payload)

        return None

    def create(
        self,
        *,
        acs_system_ids: Optional[List[str]] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        """Creates a new `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param acs_system_ids: List of access system IDs to associate with the new user identity through access system users. If there's no user with the same email address or phone number in the specified access systems, a new access system user is created. If there is an existing user with the same email or phone number in the specified access systems, the user is linked to the user identity.
        :type acs_system_ids: List[str]

        :param email_address: Unique email address for the new user identity.
        :type email_address: str

        :param full_name: Full name of the user associated with the new user identity.
        :type full_name: str

        :param phone_number: Unique phone number for the new user identity in E.164 format (for example, +15555550100).
        :type phone_number: str

        :param user_identity_key: Unique key for the new user identity.
        :type user_identity_key: str

        :returns: OK
        :rtype: UserIdentity"""
        json_payload = {}

        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if email_address is not None:
            json_payload["email_address"] = email_address
        if full_name is not None:
            json_payload["full_name"] = full_name
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        res = self.client.post("/user_identities/create", json=json_payload)

        return UserIdentity.from_dict(res["user_identity"])

    def delete(self, *, user_identity_id: str) -> None:
        """Deletes a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This deletes the user identity and all associated resources, including any `credentials <https://docs.seam.co/api/acs/credentials>`_, `acs users <https://docs.seam.co/api/acs/users>`_ and `client sessions <https://docs.seam.co/api/client_sessions>`_.

        :param user_identity_id: ID of the user identity that you want to delete.
        :type user_identity_id: str"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/user_identities/delete", json=json_payload)

        return None

    def generate_instant_key(
        self,
        *,
        user_identity_id: str,
        customization_profile_id: Optional[str] = None,
        max_use_count: Optional[float] = None
    ) -> InstantKey:
        """Generates a new `instant key <https://docs.seam.co/capability-guides/instant-keys>`_ for a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to generate an instant key.
        :type user_identity_id: str

        :param customization_profile_id:
        :type customization_profile_id: str

        :param max_use_count: Maximum number of times the instant key can be used. Default: 1.
        :type max_use_count: float

        :returns: OK
        :rtype: InstantKey"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if customization_profile_id is not None:
            json_payload["customization_profile_id"] = customization_profile_id
        if max_use_count is not None:
            json_payload["max_use_count"] = max_use_count

        res = self.client.post(
            "/user_identities/generate_instant_key", json=json_payload
        )

        return InstantKey.from_dict(res["instant_key"])

    def get(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        """Returns a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to get.
        :type user_identity_id: str

        :param user_identity_key:
        :type user_identity_key: str

        :returns: OK
        :rtype: UserIdentity"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        res = self.client.post("/user_identities/get", json=json_payload)

        return UserIdentity.from_dict(res["user_identity"])

    def grant_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        """Grants a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ access to a specified `device <https://docs.seam.co/core-concepts/devices/>`_.

        :param device_id: ID of the managed device to which you want to grant access to the user identity.
        :type device_id: str

        :param user_identity_id: ID of the user identity that you want to grant access to a device.
        :type user_identity_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/user_identities/grant_access_to_device", json=json_payload)

        return None

    def list(
        self,
        *,
        created_before: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> List[UserIdentity]:
        """Returns a list of all `user identities <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param created_before: Timestamp by which to limit returned user identities. Returns user identities created before this timestamp.
        :type created_before: str

        :param credential_manager_acs_system_id: ``acs_system_id`` of the credential manager by which you want to filter the list of user identities.
        :type credential_manager_acs_system_id: str

        :param limit: Maximum number of records to return per page.
        :type limit: int

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.
        :type page_cursor: str

        :param search: String for which to search. Filters returned user identities to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address`` or ``user_identity_id``.
        :type search: str

        :param user_identity_ids: Array of user identity IDs by which to filter the list of user identities.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: List[UserIdentity]"""
        json_payload = {}

        if created_before is not None:
            json_payload["created_before"] = created_before
        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if user_identity_ids is not None:
            json_payload["user_identity_ids"] = user_identity_ids

        res = self.client.post("/user_identities/list", json=json_payload)

        return [UserIdentity.from_dict(item) for item in res["user_identities"]]

    def list_accessible_devices(self, *, user_identity_id: str) -> List[Device]:
        """Returns a list of all `devices <https://docs.seam.co/core-concepts/devices>`_ associated with a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This includes devices derived from the access grants assigned to the user identity and devices directly linked to the user identity.

        :param user_identity_id: ID of the user identity for which you want to retrieve all accessible devices.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[Device]"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post(
            "/user_identities/list_accessible_devices", json=json_payload
        )

        return [Device.from_dict(item) for item in res["devices"]]

    def list_accessible_entrances(self, *, user_identity_id: str) -> List[AcsEntrance]:
        """Returns a list of all `ACS entrances <https://docs.seam.co/api/acs/entrances>`_ accessible to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_. This includes entrances derived from the access grants assigned to the user identity and entrances accessible through ACS users linked to the user identity.

        :param user_identity_id: ID of the user identity for which you want to retrieve all accessible entrances.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsEntrance]"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post(
            "/user_identities/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def list_acs_systems(self, *, user_identity_id: str) -> List[AcsSystem]:
        """Returns a list of all `access systems <https://docs.seam.co/low-level-apis/access-systems>`_ associated with a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access systems.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsSystem]"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/user_identities/list_acs_systems", json=json_payload)

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    def list_acs_users(self, *, user_identity_id: str) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ assigned to a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access system users.
        :type user_identity_id: str

        :returns: OK
        :rtype: List[AcsUser]"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/user_identities/list_acs_users", json=json_payload)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    def remove_acs_user(self, *, acs_user_id: str, user_identity_id: str) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param acs_user_id: ID of the access system user that you want to remove from the user identity..
        :type acs_user_id: str

        :param user_identity_id: ID of the user identity from which you want to remove an access system user.
        :type user_identity_id: str"""
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/user_identities/remove_acs_user", json=json_payload)

        return None

    def revoke_access_to_device(self, *, device_id: str, user_identity_id: str) -> None:
        """Revokes access to a specified `device <https://docs.seam.co/core-concepts/devices/>`_ from a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param device_id: ID of the managed device to which you want to revoke access from the user identity.
        :type device_id: str

        :param user_identity_id: ID of the user identity from which you want to revoke access to a device.
        :type user_identity_id: str"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/user_identities/revoke_access_to_device", json=json_payload)

        return None

    def update(
        self,
        *,
        user_identity_id: str,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
        """Updates a specified `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to update.
        :type user_identity_id: str

        :param email_address: Unique email address for the user identity.
        :type email_address: str

        :param full_name: Full name of the user associated with the user identity.
        :type full_name: str

        :param phone_number: Unique phone number for the user identity.
        :type phone_number: str

        :param user_identity_key: Unique key for the user identity.
        :type user_identity_key: str"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if email_address is not None:
            json_payload["email_address"] = email_address
        if full_name is not None:
            json_payload["full_name"] = full_name
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        self.client.post("/user_identities/update", json=json_payload)

        return None
