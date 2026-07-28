from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ConnectedAccount
from .connected_accounts_simulate import (
    AbstractConnectedAccountsSimulate,
    ConnectedAccountsSimulate,
)


class AbstractConnectedAccounts(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractConnectedAccountsSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, connected_account_id: str) -> None:
        """Deletes a specified [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        Deleting a connected account triggers a `connected_account.deleted` event and removes the connected account and all data associated with the connected account from Seam, including devices, events, access codes, and so on. For every deleted resource, Seam sends a corresponding deleted event, but the resource is not deleted from the provider.

        For example, if you delete a connected account with a device that has an access code, Seam sends a `connected_account.deleted` event, a `device.deleted` event, and an `access_code.deleted` event, but Seam does not remove the access code from the device.

        :param connected_account_id: ID of the connected account that you want to delete.
        :type connected_account_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self, *, connected_account_id: Optional[str] = None, email: Optional[str] = None
    ) -> ConnectedAccount:
        """Returns a specified [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        :param connected_account_id: ID of the connected account that you want to get.
        :type connected_account_id: str

        :param email: Email address associated with the connected account that you want to get.
        :type email: str

        :returns: OK
        :rtype: ConnectedAccount"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[ConnectedAccount]:
        """Returns a list of all [connected accounts](https://docs.seam.co/core-concepts/connected-accounts).

        :param custom_metadata_has: Custom metadata pairs by which you want to filter connected accounts. Returns connected accounts with `custom_metadata` that contains all of the provided key:value pairs.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key by which you want to filter connected accounts.
        :type customer_key: str

        :param limit: Maximum number of records to return per page.
        :type limit: int

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :param search: String for which to search. Filters returned connected accounts to include all records that satisfy a partial match using `connected_account_id`, `account_type`, `customer_key`, `custom_metadata`, `user_identifier.username`, `user_identifier.email` or `user_identifier.phone`.
        :type search: str

        :param space_id: ID of the space by which you want to filter connected accounts.
        :type space_id: str

        :param user_identifier_key: Your user ID for the user by which you want to filter connected accounts.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[ConnectedAccount]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def sync(self, *, connected_account_id: str) -> None:
        """Request a [connected account](https://docs.seam.co/core-concepts/connected-accounts) sync attempt for the specified `connected_account_id`.

        :param connected_account_id: ID of the connected account that you want to sync.
        :type connected_account_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        connected_account_id: str,
        accepted_capabilities: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        display_name: Optional[str] = None
    ) -> None:
        """Updates a [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        :param connected_account_id: ID of the connected account that you want to update.
        :type connected_account_id: str

        :param accepted_capabilities: List of accepted device capabilities that restrict the types of devices that can be connected through this connected account. Valid values are `lock`, `thermostat`, `noise_sensor`, and `access_control`.
        :type accepted_capabilities: List[str]

        :param automatically_manage_new_devices: Indicates whether newly-added devices should appear as [managed devices](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).
        :type automatically_manage_new_devices: bool

        :param custom_metadata: Custom metadata that you want to associate with the connected account. Entirely replaces the existing custom metadata object. If a new Connect Webview contains custom metadata and is used to reconnect a connected account, the custom metadata from the Connect Webview will entirely replace the entire custom metadata object on the connected account. Supports up to 50 JSON key:value pairs. [Adding custom metadata to a connected account](https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account) enables you to store custom information, like customer details or internal IDs from your application. Then, you can [filter connected accounts by the desired metadata](https://docs.seam.co/core-concepts/connected-accounts/filtering-connected-accounts-by-custom-metadata).
        :type custom_metadata: Dict[str, Any]

        :param customer_key: The customer key to associate with this connected account. If provided, the connected account and all resources under the connected account will be moved to this customer. May only be provided if the connected account is not already associated with a customer.
        :type customer_key: str

        :param display_name: Human-readable name for the connected account, shown in the dashboard. For example, `Booking from Airbnb House 1`.
        :type display_name: str"""
        raise NotImplementedError()


class ConnectedAccounts(AbstractConnectedAccounts):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = ConnectedAccountsSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> ConnectedAccountsSimulate:
        return self._simulate

    def delete(self, *, connected_account_id: str) -> None:
        """Deletes a specified [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        Deleting a connected account triggers a `connected_account.deleted` event and removes the connected account and all data associated with the connected account from Seam, including devices, events, access codes, and so on. For every deleted resource, Seam sends a corresponding deleted event, but the resource is not deleted from the provider.

        For example, if you delete a connected account with a device that has an access code, Seam sends a `connected_account.deleted` event, a `device.deleted` event, and an `access_code.deleted` event, but Seam does not remove the access code from the device.

        :param connected_account_id: ID of the connected account that you want to delete.
        :type connected_account_id: str"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/delete", json=json_payload)

        return None

    def get(
        self, *, connected_account_id: Optional[str] = None, email: Optional[str] = None
    ) -> ConnectedAccount:
        """Returns a specified [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        :param connected_account_id: ID of the connected account that you want to get.
        :type connected_account_id: str

        :param email: Email address associated with the connected account that you want to get.
        :type email: str

        :returns: OK
        :rtype: ConnectedAccount"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if email is not None:
            json_payload["email"] = email

        res = self.client.post("/connected_accounts/get", json=json_payload)

        return ConnectedAccount.from_dict(res["connected_account"])

    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[ConnectedAccount]:
        """Returns a list of all [connected accounts](https://docs.seam.co/core-concepts/connected-accounts).

        :param custom_metadata_has: Custom metadata pairs by which you want to filter connected accounts. Returns connected accounts with `custom_metadata` that contains all of the provided key:value pairs.
        :type custom_metadata_has: Dict[str, Any]

        :param customer_key: Customer key by which you want to filter connected accounts.
        :type customer_key: str

        :param limit: Maximum number of records to return per page.
        :type limit: int

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :param search: String for which to search. Filters returned connected accounts to include all records that satisfy a partial match using `connected_account_id`, `account_type`, `customer_key`, `custom_metadata`, `user_identifier.username`, `user_identifier.email` or `user_identifier.phone`.
        :type search: str

        :param space_id: ID of the space by which you want to filter connected accounts.
        :type space_id: str

        :param user_identifier_key: Your user ID for the user by which you want to filter connected accounts.
        :type user_identifier_key: str

        :returns: OK
        :rtype: List[ConnectedAccount]"""
        json_payload = {}

        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if space_id is not None:
            json_payload["space_id"] = space_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/connected_accounts/list", json=json_payload)

        return [ConnectedAccount.from_dict(item) for item in res["connected_accounts"]]

    def sync(self, *, connected_account_id: str) -> None:
        """Request a [connected account](https://docs.seam.co/core-concepts/connected-accounts) sync attempt for the specified `connected_account_id`.

        :param connected_account_id: ID of the connected account that you want to sync.
        :type connected_account_id: str"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/sync", json=json_payload)

        return None

    def update(
        self,
        *,
        connected_account_id: str,
        accepted_capabilities: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        display_name: Optional[str] = None
    ) -> None:
        """Updates a [connected account](https://docs.seam.co/core-concepts/connected-accounts).

        :param connected_account_id: ID of the connected account that you want to update.
        :type connected_account_id: str

        :param accepted_capabilities: List of accepted device capabilities that restrict the types of devices that can be connected through this connected account. Valid values are `lock`, `thermostat`, `noise_sensor`, and `access_control`.
        :type accepted_capabilities: List[str]

        :param automatically_manage_new_devices: Indicates whether newly-added devices should appear as [managed devices](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices).
        :type automatically_manage_new_devices: bool

        :param custom_metadata: Custom metadata that you want to associate with the connected account. Entirely replaces the existing custom metadata object. If a new Connect Webview contains custom metadata and is used to reconnect a connected account, the custom metadata from the Connect Webview will entirely replace the entire custom metadata object on the connected account. Supports up to 50 JSON key:value pairs. [Adding custom metadata to a connected account](https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account) enables you to store custom information, like customer details or internal IDs from your application. Then, you can [filter connected accounts by the desired metadata](https://docs.seam.co/core-concepts/connected-accounts/filtering-connected-accounts-by-custom-metadata).
        :type custom_metadata: Dict[str, Any]

        :param customer_key: The customer key to associate with this connected account. If provided, the connected account and all resources under the connected account will be moved to this customer. May only be provided if the connected account is not already associated with a customer.
        :type customer_key: str

        :param display_name: Human-readable name for the connected account, shown in the dashboard. For example, `Booking from Airbnb House 1`.
        :type display_name: str"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if accepted_capabilities is not None:
            json_payload["accepted_capabilities"] = accepted_capabilities
        if automatically_manage_new_devices is not None:
            json_payload["automatically_manage_new_devices"] = (
                automatically_manage_new_devices
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if display_name is not None:
            json_payload["display_name"] = display_name

        self.client.post("/connected_accounts/update", json=json_payload)

        return None
