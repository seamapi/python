from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import ActionAttempt, AccessMethod, Batch, action_attempt_from_dict
from .access_methods_unmanaged import (
    AbstractAccessMethodsUnmanaged,
    AccessMethodsUnmanaged,
    AbstractAsyncAccessMethodsUnmanaged,
    AsyncAccessMethodsUnmanaged,
)
from ..modules.action_attempts import (
    resolve_action_attempt,
    resolve_action_attempt_async,
)
from ..response import unwrap
from ..response import unwrap_list
from ..pagination import PaginatedList


class AbstractAccessMethods(abc.ABC):

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAccessMethodsUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_method_id: Optional[str] = None,
        reservation_key: Optional[str] = None,
    ) -> None:
        """Deletes an access method.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param access_method_id: ID of access method to delete.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
        include: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        space_id: Optional[str] = None,
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncAccessMethods(abc.ABC):

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAsyncAccessMethodsUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    async def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def delete(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_method_id: Optional[str] = None,
        reservation_key: Optional[str] = None,
    ) -> None:
        """Deletes an access method.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param access_method_id: ID of access method to delete.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
        include: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        space_id: Optional[str] = None,
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AccessMethods(AbstractAccessMethods):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._unmanaged = AccessMethodsUnmanaged(client=client, defaults=defaults)

    @property
    def unmanaged(self) -> AccessMethodsUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/access_methods/assign_card",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if card_number is not None:
            json_payload["card_number"] = card_number

        res = self.client.post("/access_methods/assign_card", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/assign_card")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/access_methods/delete",
        at_least_one_parameter_names=(
            "access_grant_id",
            "access_method_id",
            "reservation_key",
        ),
        has_pagination=False,
    )
    def delete(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_method_id: Optional[str] = None,
        reservation_key: Optional[str] = None,
    ) -> None:
        """Deletes an access method.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param access_method_id: ID of access method to delete.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if reservation_key is not None:
            params["reservation_key"] = reservation_key

        if all(
            param is None
            for param in (
                access_grant_id,
                access_method_id,
                reservation_key,
            )
        ):
            raise ValueError(
                "At least one parameter is required for /access_methods/delete"
            )

        self.client.delete("/access_methods/delete", params=params)

        return None

    @route_metadata(
        path="/access_methods/encode",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = self.client.post("/access_methods/encode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/encode")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/access_methods/get",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_id is not None:
            params["access_method_id"] = access_method_id

        res = self.client.get("/access_methods/get", params=params)

        return AccessMethod.from_dict(
            unwrap(res, "access_method", "/access_methods/get")
        )

    @route_metadata(
        path="/access_methods/get_related",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
        include: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_ids is not None:
            params["access_method_ids"] = access_method_ids
        if exclude is not None:
            params["exclude"] = exclude
        if include is not None:
            params["include"] = include

        res = self.client.get("/access_methods/get_related", params=params)

        return Batch.from_dict(unwrap(res, "batch", "/access_methods/get_related"))

    @route_metadata(
        path="/access_methods/list",
        at_least_one_parameter_names=(
            "access_code_id",
            "access_grant_id",
            "access_grant_key",
            "acs_entrance_id",
            "device_id",
            "space_id",
        ),
        has_pagination=True,
    )
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        space_id: Optional[str] = None,
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            params["access_grant_key"] = access_grant_key
        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            params["device_id"] = device_id
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if space_id is not None:
            params["space_id"] = space_id

        if all(
            param is None
            for param in (
                access_code_id,
                access_grant_id,
                access_grant_key,
                acs_entrance_id,
                device_id,
                space_id,
            )
        ):
            raise ValueError(
                "At least one parameter is required for /access_methods/list"
            )

        res = self.client.get("/access_methods/list", params=params)

        return PaginatedList(
            [
                AccessMethod.from_dict(item)
                for item in unwrap_list(res, "access_methods", "/access_methods/list")
            ],
            pagination=res.get("pagination"),
        )

    @route_metadata(
        path="/access_methods/unlock_door",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/access_methods/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/unlock_door")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )


class AsyncAccessMethods(AbstractAsyncAccessMethods):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._unmanaged = AsyncAccessMethodsUnmanaged(client=client, defaults=defaults)

    @property
    def unmanaged(self) -> AsyncAccessMethodsUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/access_methods/assign_card",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if card_number is not None:
            json_payload["card_number"] = card_number

        res = await self.client.post("/access_methods/assign_card", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/assign_card")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/access_methods/delete",
        at_least_one_parameter_names=(
            "access_grant_id",
            "access_method_id",
            "reservation_key",
        ),
        has_pagination=False,
    )
    async def delete(
        self,
        *,
        access_grant_id: Optional[str] = None,
        access_method_id: Optional[str] = None,
        reservation_key: Optional[str] = None,
    ) -> None:
        """Deletes an access method.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param access_method_id: ID of access method to delete.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if reservation_key is not None:
            params["reservation_key"] = reservation_key

        if all(
            param is None
            for param in (
                access_grant_id,
                access_method_id,
                reservation_key,
            )
        ):
            raise ValueError(
                "At least one parameter is required for /access_methods/delete"
            )

        await self.client.delete("/access_methods/delete", params=params)

        return None

    @route_metadata(
        path="/access_methods/encode",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = await self.client.post("/access_methods/encode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/encode")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/access_methods/get",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_id is not None:
            params["access_method_id"] = access_method_id

        res = await self.client.get("/access_methods/get", params=params)

        return AccessMethod.from_dict(
            unwrap(res, "access_method", "/access_methods/get")
        )

    @route_metadata(
        path="/access_methods/get_related",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
        include: Optional[
            List[
                Literal[
                    "spaces",
                    "devices",
                    "acs_entrances",
                    "access_grants",
                    "access_methods",
                    "instant_keys",
                    "client_sessions",
                    "acs_credentials",
                ]
            ]
        ] = None,
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_ids is not None:
            params["access_method_ids"] = access_method_ids
        if exclude is not None:
            params["exclude"] = exclude
        if include is not None:
            params["include"] = include

        res = await self.client.get("/access_methods/get_related", params=params)

        return Batch.from_dict(unwrap(res, "batch", "/access_methods/get_related"))

    @route_metadata(
        path="/access_methods/list",
        at_least_one_parameter_names=(
            "access_code_id",
            "access_grant_id",
            "access_grant_key",
            "acs_entrance_id",
            "device_id",
            "space_id",
        ),
        has_pagination=True,
    )
    async def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        space_id: Optional[str] = None,
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            params["access_grant_key"] = access_grant_key
        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            params["device_id"] = device_id
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if space_id is not None:
            params["space_id"] = space_id

        if all(
            param is None
            for param in (
                access_code_id,
                access_grant_id,
                access_grant_key,
                acs_entrance_id,
                device_id,
                space_id,
            )
        ):
            raise ValueError(
                "At least one parameter is required for /access_methods/list"
            )

        res = await self.client.get("/access_methods/list", params=params)

        return PaginatedList(
            [
                AccessMethod.from_dict(item)
                for item in unwrap_list(res, "access_methods", "/access_methods/list")
            ],
            pagination=res.get("pagination"),
        )

    @route_metadata(
        path="/access_methods/unlock_door",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = await self.client.post("/access_methods/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/access_methods/unlock_door")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )
