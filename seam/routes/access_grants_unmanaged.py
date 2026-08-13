from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import UnmanagedAccessGrant


class AbstractAccessGrantsUnmanaged(abc.ABC):

    @abc.abstractmethod
    def get(self, *, access_grant_id: str) -> UnmanagedAccessGrant:
        """Get an unmanaged Access Grant (where is_managed = false).

        :param access_grant_id: ID of unmanaged Access Grant to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        reservation_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[UnmanagedAccessGrant]:
        """Gets unmanaged Access Grants (where is_managed = false).

        :param acs_entrance_id: ID of the entrance by which you want to filter the list of unmanaged Access Grants.

        :param acs_system_id: ID of the access system by which you want to filter the list of unmanaged Access Grants.

        :param limit: Numerical limit on the number of unmanaged access grants to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param reservation_key: Filter unmanaged Access Grants by reservation_key.

        :param user_identity_id: ID of user identity by which you want to filter the list of unmanaged Access Grants.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_grant_id: str,
        is_managed: bool,
        access_grant_key: Optional[str] = None,
    ) -> None:
        """Updates an unmanaged Access Grant to make it managed.

        This endpoint can only be used to convert unmanaged access grants to managed ones by setting ``is_managed`` to ``true``. It cannot be used to convert managed access grants back to unmanaged.

        When converting an unmanaged access grant to managed, all associated access methods will also be converted to managed.

        :param access_grant_id: ID of the unmanaged Access Grant to update.

        :param is_managed: Must be set to true to convert the unmanaged access grant to managed.

        :param access_grant_key: Unique key for the access grant. If not provided, the existing key will be preserved.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AccessGrantsUnmanaged(AbstractAccessGrantsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/access_grants/unmanaged/get",
        has_required_parameters=True,
        has_pagination=False,
    )
    def get(self, *, access_grant_id: str) -> UnmanagedAccessGrant:
        """Get an unmanaged Access Grant (where is_managed = false).

        :param access_grant_id: ID of unmanaged Access Grant to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any([access_grant_id is not None]):
            raise ValueError(
                "At least one parameter is required for /access_grants/unmanaged/get"
            )
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id

        res = self.client.get("/access_grants/unmanaged/get", params=params)

        return UnmanagedAccessGrant.from_dict(res["access_grant"])

    @route_metadata(
        path="/access_grants/unmanaged/list",
        has_required_parameters=False,
        has_pagination=True,
    )
    def list(
        self,
        *,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        reservation_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[UnmanagedAccessGrant]:
        """Gets unmanaged Access Grants (where is_managed = false).

        :param acs_entrance_id: ID of the entrance by which you want to filter the list of unmanaged Access Grants.

        :param acs_system_id: ID of the access system by which you want to filter the list of unmanaged Access Grants.

        :param limit: Numerical limit on the number of unmanaged access grants to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param reservation_key: Filter unmanaged Access Grants by reservation_key.

        :param user_identity_id: ID of user identity by which you want to filter the list of unmanaged Access Grants.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if reservation_key is not None:
            params["reservation_key"] = reservation_key
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        res = self.client.get("/access_grants/unmanaged/list", params=params)

        return [UnmanagedAccessGrant.from_dict(item) for item in res["access_grants"]]

    @route_metadata(
        path="/access_grants/unmanaged/update",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update(
        self,
        *,
        access_grant_id: str,
        is_managed: bool,
        access_grant_key: Optional[str] = None,
    ) -> None:
        """Updates an unmanaged Access Grant to make it managed.

        This endpoint can only be used to convert unmanaged access grants to managed ones by setting ``is_managed`` to ``true``. It cannot be used to convert managed access grants back to unmanaged.

        When converting an unmanaged access grant to managed, all associated access methods will also be converted to managed.

        :param access_grant_id: ID of the unmanaged Access Grant to update.

        :param is_managed: Must be set to true to convert the unmanaged access grant to managed.

        :param access_grant_key: Unique key for the access grant. If not provided, the existing key will be preserved.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                access_grant_id is not None,
                is_managed is not None,
                access_grant_key is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /access_grants/unmanaged/update"
            )
        json_payload: Dict[str, Any] = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key

        self.client.patch("/access_grants/unmanaged/update", json=json_payload)

        return None
