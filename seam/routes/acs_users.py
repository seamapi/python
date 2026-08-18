from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import AcsUser, AcsEntrance


class AbstractAcsUsers(abc.ABC):

    @abc.abstractmethod
    def add_to_access_group(
        self, *, acs_access_group_id: str, acs_user_id: str
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group to which you want to add an access system user.

        :param acs_user_id: ID of the access system user that you want to add to an access group.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        acs_system_id: str,
        full_name: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_access_group_ids: Optional[List[str]] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> AcsUser:
        """Creates a new `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the access system to which you want to add the new access system user.

        :param full_name: Full name of the new access system user.

        :param access_schedule: ``starts_at`` and ``ends_at`` timestamps for the new access system user's access. If you specify an ``access_schedule``, you may include both ``starts_at`` and ``ends_at``. If you omit ``starts_at``, it defaults to the current time. ``ends_at`` is optional and must be a time in the future and after ``starts_at``.

        :param acs_access_group_ids: Array of access group IDs to indicate the access groups to which you want to add the new access system user.

        :param email: Deprecated: use email_address.

        :param email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

        :param user_identity_id: ID of the user identity with which you want to associate the new access system user.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Deletes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ and invalidates the access system user's `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_system_id: ID of the access system that you want to delete. You must provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to delete. You must provide either acs_user_id or user_identity_id

        :param user_identity_id: ID of the user identity that you want to delete. You must provide either acs_user_id or user_identity_id. If you provide user_identity_id, you must also provide acs_system_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> AcsUser:
        """Returns a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_user_id: ID of the access system user that you want to get. You can only provide acs_user_id or user_identity_id.

        :param acs_system_id: ID of the access system that you want to get. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity that you want to get. You can only provide acs_user_id or user_identity_id.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None,
    ) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the ``acs_system`` for which you want to retrieve all access system users.

        :param created_before: Timestamp by which to limit returned access system users. Returns users created before this timestamp.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access system users to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address``, ``acs_user_id``, ``user_identity_id``, ``user_identity_full_name`` or ``user_identity_phone_number``.

        :param user_identity_email_address: Email address of the user identity for which you want to retrieve all access system users.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access system users.

        :param user_identity_phone_number: Phone number of the user identity for which you want to retrieve all access system users, in `E.164 format <https://www.itu.int/rec/T-REC-E.164/en>`_ (for example, ``+15555550100``).

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Lists the `entrances <https://docs.seam.co/api/acs/entrances>`_ to which a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ has access.

        :param acs_system_id: ID of the access system for which you want to list accessible entrances. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user for whom you want to list accessible entrances. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity for whom you want to list accessible entrances. You can only provide acs_user_id or user_identity_id.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_from_access_group(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group from which you want to remove an access system user.

        :param acs_user_id: ID of the access system user that you want to remove from an access group. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity that you want to remove from an access group. You can only provide acs_user_id or user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke_access_to_all_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Revokes access to all `entrances <https://docs.seam.co/api/acs/entrances>`_ for a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the access system for which you want to revoke access. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user for whom you want to revoke access. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity for whom you want to revoke access. You can only provide acs_user_id or user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def suspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """`Suspends <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users#suspend-an-acs-user>`_ a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. Suspending an access system user revokes their access temporarily. To restore an access system user's access, you can `unsuspend <https://docs.seam.co/api/acs/users/unsuspend>`_ them.

        :param acs_system_id: ID of the access system that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param acs_user_id: ID of the access system user that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param user_identity_id: ID of the user identity that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def unsuspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """`Unsuspends <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users#unsuspend-an-acs-user>`_ a specified suspended `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. While `suspending an access system user <https://docs.seam.co/api/acs/users/suspend>`_ revokes their access temporarily, unsuspending the access system user restores their access.

        :param acs_system_id: ID of the access system of the user that you want to unsuspend. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to unsuspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param user_identity_id: ID of the user identity that you want to unsuspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_schedule: Optional[Union[Dict[str, Any], Null]] = None,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Updates the properties of a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param access_schedule: ``starts_at`` and ``ends_at`` timestamps for the access system user's access. If you specify an ``access_schedule``, you may include both ``starts_at`` and ``ends_at``. If you omit ``starts_at``, it defaults to the current time. ``ends_at`` is optional and must be a time in the future and after ``starts_at``.

        :param acs_system_id: ID of the access system that you want to update. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to update. You can only provide acs_user_id or user_identity_id.

        :param email: Deprecated: use email_address.

        :param email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param full_name: Full name of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param hid_acs_system_id: ID of the HID access control system associated with the user.

        :param phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

        :param user_identity_id: ID of the user identity that you want to update. You can only provide acs_user_id or user_identity_id. If you provide user_identity_id, you must also provide acs_system_id.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AcsUsers(AbstractAcsUsers):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/acs/users/add_to_access_group",
        has_required_parameters=True,
        has_pagination=False,
    )
    def add_to_access_group(
        self, *, acs_access_group_id: str, acs_user_id: str
    ) -> None:
        """Adds a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ to a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group to which you want to add an access system user.

        :param acs_user_id: ID of the access system user that you want to add to an access group.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/users/add_to_access_group"
            )

        self.client.put("/acs/users/add_to_access_group", json=json_payload)

        return None

    @route_metadata(
        path="/acs/users/create", has_required_parameters=True, has_pagination=False
    )
    def create(
        self,
        *,
        acs_system_id: str,
        full_name: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_access_group_ids: Optional[List[str]] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> AcsUser:
        """Creates a new `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the access system to which you want to add the new access system user.

        :param full_name: Full name of the new access system user.

        :param access_schedule: ``starts_at`` and ``ends_at`` timestamps for the new access system user's access. If you specify an ``access_schedule``, you may include both ``starts_at`` and ``ends_at``. If you omit ``starts_at``, it defaults to the current time. ``ends_at`` is optional and must be a time in the future and after ``starts_at``.

        :param acs_access_group_ids: Array of access group IDs to indicate the access groups to which you want to add the new access system user.

        :param email: Deprecated: use email_address.

        :param email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

        :param user_identity_id: ID of the user identity with which you want to associate the new access system user.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if full_name is not None:
            json_payload["full_name"] = full_name
        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if acs_access_group_ids is not None:
            json_payload["acs_access_group_ids"] = acs_access_group_ids
        if email is not None:
            json_payload["email"] = email
        if email_address is not None:
            json_payload["email_address"] = email_address
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /acs/users/create")

        res = self.client.post("/acs/users/create", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    @route_metadata(
        path="/acs/users/delete", has_required_parameters=True, has_pagination=False
    )
    def delete(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Deletes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ and invalidates the access system user's `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_system_id: ID of the access system that you want to delete. You must provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to delete. You must provide either acs_user_id or user_identity_id

        :param user_identity_id: ID of the user identity that you want to delete. You must provide either acs_user_id or user_identity_id. If you provide user_identity_id, you must also provide acs_system_id.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/users/delete")

        self.client.delete("/acs/users/delete", params=params)

        return None

    @route_metadata(
        path="/acs/users/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> AcsUser:
        """Returns a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_user_id: ID of the access system user that you want to get. You can only provide acs_user_id or user_identity_id.

        :param acs_system_id: ID of the access system that you want to get. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity that you want to get. You can only provide acs_user_id or user_identity_id.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/users/get")

        res = self.client.get("/acs/users/get", params=params)

        return AcsUser.from_dict(res["acs_user"])

    @route_metadata(
        path="/acs/users/list", has_required_parameters=False, has_pagination=True
    )
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None,
    ) -> List[AcsUser]:
        """Returns a list of all `access system users <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the ``acs_system`` for which you want to retrieve all access system users.

        :param created_before: Timestamp by which to limit returned access system users. Returns users created before this timestamp.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access system users to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address``, ``acs_user_id``, ``user_identity_id``, ``user_identity_full_name`` or ``user_identity_phone_number``.

        :param user_identity_email_address: Email address of the user identity for which you want to retrieve all access system users.

        :param user_identity_id: ID of the user identity for which you want to retrieve all access system users.

        :param user_identity_phone_number: Phone number of the user identity for which you want to retrieve all access system users, in `E.164 format <https://www.itu.int/rec/T-REC-E.164/en>`_ (for example, ``+15555550100``).

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if created_before is not None:
            params["created_before"] = created_before
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if user_identity_email_address is not None:
            params["user_identity_email_address"] = user_identity_email_address
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id
        if user_identity_phone_number is not None:
            params["user_identity_phone_number"] = user_identity_phone_number

        res = self.client.get("/acs/users/list", params=params)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    @route_metadata(
        path="/acs/users/list_accessible_entrances",
        has_required_parameters=True,
        has_pagination=False,
    )
    def list_accessible_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Lists the `entrances <https://docs.seam.co/api/acs/entrances>`_ to which a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ has access.

        :param acs_system_id: ID of the access system for which you want to list accessible entrances. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user for whom you want to list accessible entrances. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity for whom you want to list accessible entrances. You can only provide acs_user_id or user_identity_id.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError(
                "At least one parameter is required for /acs/users/list_accessible_entrances"
            )

        res = self.client.get("/acs/users/list_accessible_entrances", params=params)

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    @route_metadata(
        path="/acs/users/remove_from_access_group",
        has_required_parameters=True,
        has_pagination=False,
    )
    def remove_from_access_group(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Removes a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ from a specified `access group <https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups>`_.

        :param acs_access_group_id: ID of the access group from which you want to remove an access system user.

        :param acs_user_id: ID of the access system user that you want to remove from an access group. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity that you want to remove from an access group. You can only provide acs_user_id or user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_access_group_id is not None:
            params["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError(
                "At least one parameter is required for /acs/users/remove_from_access_group"
            )

        self.client.delete("/acs/users/remove_from_access_group", params=params)

        return None

    @route_metadata(
        path="/acs/users/revoke_access_to_all_entrances",
        has_required_parameters=True,
        has_pagination=False,
    )
    def revoke_access_to_all_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Revokes access to all `entrances <https://docs.seam.co/api/acs/entrances>`_ for a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_system_id: ID of the access system for which you want to revoke access. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user for whom you want to revoke access. You can only provide acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity for whom you want to revoke access. You can only provide acs_user_id or user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/users/revoke_access_to_all_entrances"
            )

        self.client.post("/acs/users/revoke_access_to_all_entrances", json=json_payload)

        return None

    @route_metadata(
        path="/acs/users/suspend", has_required_parameters=True, has_pagination=False
    )
    def suspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """`Suspends <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users#suspend-an-acs-user>`_ a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. Suspending an access system user revokes their access temporarily. To restore an access system user's access, you can `unsuspend <https://docs.seam.co/api/acs/users/unsuspend>`_ them.

        :param acs_system_id: ID of the access system that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param acs_user_id: ID of the access system user that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param user_identity_id: ID of the user identity that you want to suspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/users/suspend"
            )

        self.client.post("/acs/users/suspend", json=json_payload)

        return None

    @route_metadata(
        path="/acs/users/unsuspend", has_required_parameters=True, has_pagination=False
    )
    def unsuspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """`Unsuspends <https://docs.seam.co/low-level-apis/access-systems/user-management/suspending-and-unsuspending-users#unsuspend-an-acs-user>`_ a specified suspended `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. While `suspending an access system user <https://docs.seam.co/api/acs/users/suspend>`_ revokes their access temporarily, unsuspending the access system user restores their access.

        :param acs_system_id: ID of the access system of the user that you want to unsuspend. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to unsuspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :param user_identity_id: ID of the user identity that you want to unsuspend. You can only provide acs_user_id or the combination of acs_system_id and user_identity_id.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/users/unsuspend"
            )

        self.client.post("/acs/users/unsuspend", json=json_payload)

        return None

    @route_metadata(
        path="/acs/users/update", has_required_parameters=True, has_pagination=False
    )
    def update(
        self,
        *,
        access_schedule: Optional[Union[Dict[str, Any], Null]] = None,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Updates the properties of a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param access_schedule: ``starts_at`` and ``ends_at`` timestamps for the access system user's access. If you specify an ``access_schedule``, you may include both ``starts_at`` and ``ends_at``. If you omit ``starts_at``, it defaults to the current time. ``ends_at`` is optional and must be a time in the future and after ``starts_at``.

        :param acs_system_id: ID of the access system that you want to update. You can only provide acs_system_id with user_identity_id.

        :param acs_user_id: ID of the access system user that you want to update. You can only provide acs_user_id or user_identity_id.

        :param email: Deprecated: use email_address.

        :param email_address: Email address of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param full_name: Full name of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param hid_acs_system_id: ID of the HID access control system associated with the user.

        :param phone_number: Phone number of the `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ in E.164 format (for example, ``+15555550100``).

        :param user_identity_id: ID of the user identity that you want to update. You can only provide acs_user_id or user_identity_id. If you provide user_identity_id, you must also provide acs_system_id.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if email is not None:
            json_payload["email"] = email
        if email_address is not None:
            json_payload["email_address"] = email_address
        if full_name is not None:
            json_payload["full_name"] = full_name
        if hid_acs_system_id is not None:
            json_payload["hid_acs_system_id"] = hid_acs_system_id
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /acs/users/update")

        self.client.patch("/acs/users/update", json=json_payload)

        return None
