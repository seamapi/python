from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import (
    AcsEntrance,
    AcsCredential,
    ActionAttempt,
    action_attempt_from_dict,
)
from ..modules.action_attempts import (
    resolve_action_attempt,
    resolve_action_attempt_async,
)
from ..response import unwrap
from ..response import unwrap_list
from ..pagination import PaginatedList


class AbstractAcsEntrances(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[Union[str, Null]] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_credentials_with_access(
        self,
        *,
        acs_entrance_id: str,
        include_if: Optional[List[Literal["visionline_metadata.is_valid"]]] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncAcsEntrances(abc.ABC):

    @abc.abstractmethod
    async def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[Union[str, Null]] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list_credentials_with_access(
        self,
        *,
        acs_entrance_id: str,
        include_if: Optional[List[Literal["visionline_metadata.is_valid"]]] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AcsEntrances(AbstractAcsEntrances):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/acs/entrances/get", at_least_one_parameter_names=(), has_pagination=False
    )
    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id

        res = self.client.get("/acs/entrances/get", params=params)

        return AcsEntrance.from_dict(unwrap(res, "acs_entrance", "/acs/entrances/get"))

    @route_metadata(
        path="/acs/entrances/grant_access",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        json_payload: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/entrances/grant_access", json=json_payload)

        return None

    @route_metadata(
        path="/acs/entrances/list", at_least_one_parameter_names=(), has_pagination=True
    )
    def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[Union[str, Null]] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            params["acs_credential_id"] = acs_credential_id
        if acs_entrance_ids is not None:
            params["acs_entrance_ids"] = acs_entrance_ids
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if limit is not None:
            params["limit"] = limit
        if location_id is not None:
            params["location_id"] = location_id
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if space_id is not None:
            params["space_id"] = space_id

        res = self.client.get("/acs/entrances/list", params=params)

        return PaginatedList(
            [
                AcsEntrance.from_dict(item)
                for item in unwrap_list(res, "acs_entrances", "/acs/entrances/list")
            ],
            pagination=res.get("pagination"),
        )

    @route_metadata(
        path="/acs/entrances/list_credentials_with_access",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def list_credentials_with_access(
        self,
        *,
        acs_entrance_id: str,
        include_if: Optional[List[Literal["visionline_metadata.is_valid"]]] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if include_if is not None:
            params["include_if"] = include_if

        res = self.client.get(
            "/acs/entrances/list_credentials_with_access", params=params
        )

        return [
            AcsCredential.from_dict(item)
            for item in unwrap_list(
                res, "acs_credentials", "/acs/entrances/list_credentials_with_access"
            )
        ]

    @route_metadata(
        path="/acs/entrances/unlock",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/acs/entrances/unlock", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/entrances/unlock")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )


class AsyncAcsEntrances(AbstractAsyncAcsEntrances):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/acs/entrances/get", at_least_one_parameter_names=(), has_pagination=False
    )
    async def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id

        res = await self.client.get("/acs/entrances/get", params=params)

        return AcsEntrance.from_dict(unwrap(res, "acs_entrance", "/acs/entrances/get"))

    @route_metadata(
        path="/acs/entrances/grant_access",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        json_payload: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        await self.client.post("/acs/entrances/grant_access", json=json_payload)

        return None

    @route_metadata(
        path="/acs/entrances/list", at_least_one_parameter_names=(), has_pagination=True
    )
    async def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[Union[str, Null]] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            params["acs_credential_id"] = acs_credential_id
        if acs_entrance_ids is not None:
            params["acs_entrance_ids"] = acs_entrance_ids
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if limit is not None:
            params["limit"] = limit
        if location_id is not None:
            params["location_id"] = location_id
        if page_cursor is not None:
            params["page_cursor"] = page_cursor
        if search is not None:
            params["search"] = search
        if space_id is not None:
            params["space_id"] = space_id

        res = await self.client.get("/acs/entrances/list", params=params)

        return PaginatedList(
            [
                AcsEntrance.from_dict(item)
                for item in unwrap_list(res, "acs_entrances", "/acs/entrances/list")
            ],
            pagination=res.get("pagination"),
        )

    @route_metadata(
        path="/acs/entrances/list_credentials_with_access",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def list_credentials_with_access(
        self,
        *,
        acs_entrance_id: str,
        include_if: Optional[List[Literal["visionline_metadata.is_valid"]]] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if include_if is not None:
            params["include_if"] = include_if

        res = await self.client.get(
            "/acs/entrances/list_credentials_with_access", params=params
        )

        return [
            AcsCredential.from_dict(item)
            for item in unwrap_list(
                res, "acs_credentials", "/acs/entrances/list_credentials_with_access"
            )
        ]

    @route_metadata(
        path="/acs/entrances/unlock",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = await self.client.post("/acs/entrances/unlock", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/entrances/unlock")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )
