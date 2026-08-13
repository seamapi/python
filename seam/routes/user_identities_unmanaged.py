from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedUserIdentity


class AbstractUserIdentitiesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, user_identity_id: str) -> UnmanagedUserIdentity:
        """Returns a specified unmanaged `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ (where is_managed = false).

        :param user_identity_id: ID of the unmanaged user identity that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[UnmanagedUserIdentity]:
        """Returns a list of all unmanaged `user identities <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ (where is_managed = false).

        :param created_before: Timestamp by which to limit returned unmanaged user identities. Returns user identities created before this timestamp.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned unmanaged user identities to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address``,  ``user_identity_id`` or ``acs_system_id``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        is_managed: bool,
        user_identity_id: str,
        user_identity_key: Optional[str] = None,
    ) -> None:
        """Updates an unmanaged `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ to make it managed.

        This endpoint can only be used to convert unmanaged user identities to managed ones by setting ``is_managed`` to ``true``. It cannot be used to convert managed user identities back to unmanaged.

        :param is_managed: Must be set to true to convert the unmanaged user identity to managed.

        :param user_identity_id: ID of the unmanaged user identity that you want to update.

        :param user_identity_key: Unique key for the user identity. If not provided, the existing key will be preserved.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class UserIdentitiesUnmanaged(AbstractUserIdentitiesUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, user_identity_id: str) -> UnmanagedUserIdentity:
        """Returns a specified unmanaged `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ (where is_managed = false).

        :param user_identity_id: ID of the unmanaged user identity that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(user_identity_id is not None):
            raise ValueError("At least one parameter must be provided")
        params: Dict[str, Any] = {}

        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        res = self.client.get("/user_identities/unmanaged/get", params=params)

        return UnmanagedUserIdentity.from_dict(res["user_identity"])

    def list(
        self,
        *,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[UnmanagedUserIdentity]:
        """Returns a list of all unmanaged `user identities <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ (where is_managed = false).

        :param created_before: Timestamp by which to limit returned unmanaged user identities. Returns user identities created before this timestamp.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned unmanaged user identities to include all records that satisfy a partial match using ``full_name``, ``phone_number``, ``email_address``,  ``user_identity_id`` or ``acs_system_id``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if created_before is not None:
            params["created_before"] = created_before
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search

        res = self.client.get("/user_identities/unmanaged/list", params=params)

        return [
            UnmanagedUserIdentity.from_dict(item) for item in res["user_identities"]
        ]

    def update(
        self,
        *,
        is_managed: bool,
        user_identity_id: str,
        user_identity_key: Optional[str] = None,
    ) -> None:
        """Updates an unmanaged `user identity <https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity>`_ to make it managed.

        This endpoint can only be used to convert unmanaged user identities to managed ones by setting ``is_managed`` to ``true``. It cannot be used to convert managed user identities back to unmanaged.

        :param is_managed: Must be set to true to convert the unmanaged user identity to managed.

        :param user_identity_id: ID of the unmanaged user identity that you want to update.

        :param user_identity_key: Unique key for the user identity. If not provided, the existing key will be preserved.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            is_managed is not None,
            user_identity_id is not None,
            user_identity_key is not None,
        ):
            raise ValueError("At least one parameter must be provided")
        json_payload: Dict[str, Any] = {}

        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        self.client.patch("/user_identities/unmanaged/update", json=json_payload)

        return None
