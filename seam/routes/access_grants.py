from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import AccessGrant, Batch
from .access_grants_unmanaged import (
    AbstractAccessGrantsUnmanaged,
    AccessGrantsUnmanaged,
)


class AbstractAccessGrants(abc.ABC):

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAccessGrantsUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        requested_access_methods: List[Dict[str, Any]],
        user_identity_id: Optional[str] = None,
        user_identity: Optional[Dict[str, Any]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        customization_profile_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        ends_at: Optional[str] = None,
        location: Optional[Dict[str, Any]] = None,
        location_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        reservation_key: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
        starts_at: Optional[str] = None,
    ) -> AccessGrant:
        """Creates a new `Access Grant <https://docs.seam.co/use-cases/granting-access/access-grants>`_. Access Grants are the default and recommended way to grant a user access to any physical space, irrespective of the locking hardware. They work with both standalone smart locks (using ``device_ids``) and access control systems (using ``acs_entrance_ids`` or ``space_ids``), and can issue PIN codes, key cards, and mobile keys through a single request.

        :param requested_access_methods:

        :param user_identity_id: ID of user identity for whom access is being granted.

        :param user_identity: When used, creates a new user identity with the given details, and grants them access.

        :param access_grant_key: Unique key for the access grant within the workspace.

        :param acs_entrance_ids: Set of IDs of the `entrances <https://docs.seam.co/api/acs/systems/list>`_ to which access is being granted.

        :param customization_profile_id: ID of the customization profile to apply to the Access Grant and its access methods.

        :param device_ids: Set of IDs of the `devices <https://docs.seam.co/api/devices/list>`_ to which access is being granted.

        :param ends_at: Date and time at which the validity of the new grant ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param location: Deprecated: Create a space first, then reference it using ``space_ids``.

        :param location_ids: Deprecated: Use ``space_ids``.

        :param name: Name for the access grant.

        :param reservation_key: Reservation key for the access grant.

        :param space_ids: Set of IDs of existing spaces to which access is being granted.

        :param space_keys: Set of keys of existing spaces to which access is being granted.

        :param starts_at: Date and time at which the validity of the new grant starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, access_grant_id: str) -> None:
        """Delete an Access Grant.

        :param access_grant_id: ID of Access Grant to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
    ) -> AccessGrant:
        """Get an Access Grant.

        :param access_grant_id: ID of Access Grant to get.

        :param access_grant_key: Unique key of Access Grant to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        access_grant_ids: Optional[List[str]] = None,
        access_grant_keys: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Grants.

        :param access_grant_ids: IDs of the access grants that you want to get along with their related resources.

        :param access_grant_keys: Keys of the access grants that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[float] = None,
        location_id: Optional[str] = None,
        page_cursor: Optional[str] = None,
        reservation_key: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AccessGrant]:
        """Gets an Access Grant.

        :param access_code_id: ID of the access code by which you want to filter the list of Access Grants.

        :param access_grant_ids: IDs of the access grants to retrieve.

        :param access_grant_key: Filter Access Grants by access_grant_key. Use null to filter for Access Grants without an access_grant_key.

        :param acs_entrance_id: ID of the entrance by which you want to filter the list of Access Grants.

        :param acs_system_id: ID of the access system by which you want to filter the list of Access Grants.

        :param customer_key: Customer key for which you want to list access grants.

        :param device_id: ID of the device by which you want to filter the list of Access Grants.

        :param limit: Numerical limit on the number of access grants to return.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param reservation_key: Filter Access Grants by reservation_key.

        :param space_id: ID of the space by which you want to filter the list of Access Grants.

        :param user_identity_id: ID of user identity by which you want to filter the list of Access Grants.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def request_access_methods(
        self, *, access_grant_id: str, requested_access_methods: List[Dict[str, Any]]
    ) -> AccessGrant:
        """Adds additional requested access methods to an existing Access Grant.

        :param access_grant_id: ID of the Access Grant to add access methods to.

        :param requested_access_methods: Array of requested access methods to add to the access grant.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
    ) -> None:
        """Updates an existing Access Grant's time window.

        :param access_grant_id: ID of the Access Grant to update. Provide either ``access_grant_id`` or ``access_grant_key``.

        :param access_grant_key: Key of the Access Grant to update. Provide either ``access_grant_id`` or ``access_grant_key``.

        :param ends_at: Date and time at which the validity of the grant ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param name: Display name for the access grant.

        :param starts_at: Date and time at which the validity of the grant starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AccessGrants(AbstractAccessGrants):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._unmanaged = AccessGrantsUnmanaged(client=client, defaults=defaults)

    @property
    def unmanaged(self) -> AccessGrantsUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/access_grants/create", has_required_parameters=True, has_pagination=False
    )
    def create(
        self,
        *,
        requested_access_methods: List[Dict[str, Any]],
        user_identity_id: Optional[str] = None,
        user_identity: Optional[Dict[str, Any]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        customization_profile_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        ends_at: Optional[str] = None,
        location: Optional[Dict[str, Any]] = None,
        location_ids: Optional[List[str]] = None,
        name: Optional[str] = None,
        reservation_key: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
        starts_at: Optional[str] = None,
    ) -> AccessGrant:
        """Creates a new `Access Grant <https://docs.seam.co/use-cases/granting-access/access-grants>`_. Access Grants are the default and recommended way to grant a user access to any physical space, irrespective of the locking hardware. They work with both standalone smart locks (using ``device_ids``) and access control systems (using ``acs_entrance_ids`` or ``space_ids``), and can issue PIN codes, key cards, and mobile keys through a single request.

        :param requested_access_methods:

        :param user_identity_id: ID of user identity for whom access is being granted.

        :param user_identity: When used, creates a new user identity with the given details, and grants them access.

        :param access_grant_key: Unique key for the access grant within the workspace.

        :param acs_entrance_ids: Set of IDs of the `entrances <https://docs.seam.co/api/acs/systems/list>`_ to which access is being granted.

        :param customization_profile_id: ID of the customization profile to apply to the Access Grant and its access methods.

        :param device_ids: Set of IDs of the `devices <https://docs.seam.co/api/devices/list>`_ to which access is being granted.

        :param ends_at: Date and time at which the validity of the new grant ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param location: Deprecated: Create a space first, then reference it using ``space_ids``.

        :param location_ids: Deprecated: Use ``space_ids``.

        :param name: Name for the access grant.

        :param reservation_key: Reservation key for the access grant.

        :param space_ids: Set of IDs of existing spaces to which access is being granted.

        :param space_keys: Set of keys of existing spaces to which access is being granted.

        :param starts_at: Date and time at which the validity of the new grant starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            requested_access_methods is not None,
            user_identity_id is not None,
            user_identity is not None,
            access_grant_key is not None,
            acs_entrance_ids is not None,
            customization_profile_id is not None,
            device_ids is not None,
            ends_at is not None,
            location is not None,
            location_ids is not None,
            name is not None,
            reservation_key is not None,
            space_ids is not None,
            space_keys is not None,
            starts_at is not None,
        ):
            raise ValueError(
                "At least one parameter is required for /access_grants/create"
            )
        json_payload: Dict[str, Any] = {}

        if requested_access_methods is not None:
            json_payload["requested_access_methods"] = requested_access_methods
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity is not None:
            json_payload["user_identity"] = user_identity
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if customization_profile_id is not None:
            json_payload["customization_profile_id"] = customization_profile_id
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if location is not None:
            json_payload["location"] = location
        if location_ids is not None:
            json_payload["location_ids"] = location_ids
        if name is not None:
            json_payload["name"] = name
        if reservation_key is not None:
            json_payload["reservation_key"] = reservation_key
        if space_ids is not None:
            json_payload["space_ids"] = space_ids
        if space_keys is not None:
            json_payload["space_keys"] = space_keys
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        res = self.client.post("/access_grants/create", json=json_payload)

        return AccessGrant.from_dict(res["access_grant"])

    @route_metadata(
        path="/access_grants/delete", has_required_parameters=True, has_pagination=False
    )
    def delete(self, *, access_grant_id: str) -> None:
        """Delete an Access Grant.

        :param access_grant_id: ID of Access Grant to delete.

        :raises ValueError: At least one parameter must be provided."""
        if not any(access_grant_id is not None):
            raise ValueError(
                "At least one parameter is required for /access_grants/delete"
            )
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id

        self.client.delete("/access_grants/delete", params=params)

        return None

    @route_metadata(
        path="/access_grants/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
    ) -> AccessGrant:
        """Get an Access Grant.

        :param access_grant_id: ID of Access Grant to get.

        :param access_grant_key: Unique key of Access Grant to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(access_grant_id is not None, access_grant_key is not None):
            raise ValueError(
                "At least one parameter is required for /access_grants/get"
            )
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            params["access_grant_key"] = access_grant_key

        res = self.client.get("/access_grants/get", params=params)

        return AccessGrant.from_dict(res["access_grant"])

    @route_metadata(
        path="/access_grants/get_related",
        has_required_parameters=True,
        has_pagination=False,
    )
    def get_related(
        self,
        *,
        access_grant_ids: Optional[List[str]] = None,
        access_grant_keys: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Grants.

        :param access_grant_ids: IDs of the access grants that you want to get along with their related resources.

        :param access_grant_keys: Keys of the access grants that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            access_grant_ids is not None,
            access_grant_keys is not None,
            exclude is not None,
            include is not None,
        ):
            raise ValueError(
                "At least one parameter is required for /access_grants/get_related"
            )
        json_payload: Dict[str, Any] = {}

        if access_grant_ids is not None:
            json_payload["access_grant_ids"] = access_grant_ids
        if access_grant_keys is not None:
            json_payload["access_grant_keys"] = access_grant_keys
        if exclude is not None:
            json_payload["exclude"] = exclude
        if include is not None:
            json_payload["include"] = include

        res = self.client.post("/access_grants/get_related", json=json_payload)

        return Batch.from_dict(res["batch"])

    @route_metadata(
        path="/access_grants/list", has_required_parameters=False, has_pagination=True
    )
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[float] = None,
        location_id: Optional[str] = None,
        page_cursor: Optional[str] = None,
        reservation_key: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[AccessGrant]:
        """Gets an Access Grant.

        :param access_code_id: ID of the access code by which you want to filter the list of Access Grants.

        :param access_grant_ids: IDs of the access grants to retrieve.

        :param access_grant_key: Filter Access Grants by access_grant_key. Use null to filter for Access Grants without an access_grant_key.

        :param acs_entrance_id: ID of the entrance by which you want to filter the list of Access Grants.

        :param acs_system_id: ID of the access system by which you want to filter the list of Access Grants.

        :param customer_key: Customer key for which you want to list access grants.

        :param device_id: ID of the device by which you want to filter the list of Access Grants.

        :param limit: Numerical limit on the number of access grants to return.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param reservation_key: Filter Access Grants by reservation_key.

        :param space_id: ID of the space by which you want to filter the list of Access Grants.

        :param user_identity_id: ID of user identity by which you want to filter the list of Access Grants.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_grant_ids is not None:
            json_payload["access_grant_ids"] = access_grant_ids
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if limit is not None:
            json_payload["limit"] = limit
        if location_id is not None:
            json_payload["location_id"] = location_id
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if reservation_key is not None:
            json_payload["reservation_key"] = reservation_key
        if space_id is not None:
            json_payload["space_id"] = space_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/access_grants/list", json=json_payload)

        return [AccessGrant.from_dict(item) for item in res["access_grants"]]

    @route_metadata(
        path="/access_grants/request_access_methods",
        has_required_parameters=True,
        has_pagination=False,
    )
    def request_access_methods(
        self, *, access_grant_id: str, requested_access_methods: List[Dict[str, Any]]
    ) -> AccessGrant:
        """Adds additional requested access methods to an existing Access Grant.

        :param access_grant_id: ID of the Access Grant to add access methods to.

        :param requested_access_methods: Array of requested access methods to add to the access grant.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(access_grant_id is not None, requested_access_methods is not None):
            raise ValueError(
                "At least one parameter is required for /access_grants/request_access_methods"
            )
        json_payload: Dict[str, Any] = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if requested_access_methods is not None:
            json_payload["requested_access_methods"] = requested_access_methods

        res = self.client.post(
            "/access_grants/request_access_methods", json=json_payload
        )

        return AccessGrant.from_dict(res["access_grant"])

    @route_metadata(
        path="/access_grants/update", has_required_parameters=True, has_pagination=False
    )
    def update(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
    ) -> None:
        """Updates an existing Access Grant's time window.

        :param access_grant_id: ID of the Access Grant to update. Provide either ``access_grant_id`` or ``access_grant_key``.

        :param access_grant_key: Key of the Access Grant to update. Provide either ``access_grant_id`` or ``access_grant_key``.

        :param ends_at: Date and time at which the validity of the grant ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param name: Display name for the access grant.

        :param starts_at: Date and time at which the validity of the grant starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            access_grant_id is not None,
            access_grant_key is not None,
            ends_at is not None,
            name is not None,
            starts_at is not None,
        ):
            raise ValueError(
                "At least one parameter is required for /access_grants/update"
            )
        json_payload: Dict[str, Any] = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        self.client.patch("/access_grants/update", json=json_payload)

        return None
