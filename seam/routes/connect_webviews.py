from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ConnectWebview


class AbstractConnectWebviews(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        accepted_capabilities: Optional[List[str]] = None,
        accepted_providers: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        custom_redirect_failure_url: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        customer_key: Optional[str] = None,
        excluded_providers: Optional[List[str]] = None,
        provider_category: Optional[str] = None,
        wait_for_device_creation: Optional[bool] = None,
    ) -> ConnectWebview:
        """Creates a new `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        To enable a user to connect their devices or systems to Seam, they must sign in to their device or system account. To enable a user to sign in, you create a ``connect_webview``. After creating the Connect Webview, you receive a URL that you can use to display the visual component of this Connect Webview for your user. You can open an iframe or new window to display the Connect Webview.

        You should make a new ``connect_webview`` for each unique login request. Each ``connect_webview`` tracks the user that signed in with it. You receive an error if you reuse a Connect Webview for the same user twice or if you use the same Connect Webview for multiple users.

        See also: `Connect Webview Process <https://docs.seam.co/core-concepts/connect-webviews/connect-webview-process>`_.

        :param accepted_capabilities: List of accepted device capabilities that restrict the types of devices that can be connected through the Connect Webview. If not provided, defaults will be determined based on the accepted providers.

        :param accepted_providers: Accepted device provider keys as an alternative to ``provider_category``. Use this parameter to specify accepted providers explicitly. See `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_. To list all provider keys, use ```/devices/list_device_providers`` <https://docs.seam.co/api/devices/list_device_providers>`_ with no filters.

        :param automatically_manage_new_devices: Indicates whether newly-added devices should appear as `managed devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. See also: `Customize the Behavior Settings of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-behavior-settings-of-your-connect-webviews>`_.

        :param custom_metadata: Custom metadata that you want to associate with the Connect Webview. Supports up to 50 JSON key:value pairs. `Adding custom metadata to a Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_ enables you to store custom information, like customer details or internal IDs from your application. The custom metadata is then transferred to any `connected accounts <https://docs.seam.co/core-concepts/connected-accounts>`_ that were connected using the Connect Webview, making it easy to find and filter these resources in your `workspace <https://docs.seam.co/core-concepts/workspaces>`_. You can also `filter Connect Webviews by custom metadata <https://docs.seam.co/core-concepts/connect-webviews/filtering-connect-webviews-by-custom-metadata>`_.

        :param custom_redirect_failure_url: Alternative URL that you want to redirect the user to on an error. If you do not set this parameter, the Connect Webview falls back to the ``custom_redirect_url``.

        :param custom_redirect_url: URL that you want to redirect the user to after the provider login is complete.

        :param customer_key: Associate the Connect Webview, the connected account, and all resources under the connected account with a customer. If the connected account already exists, it will be associated with the customer. If the connected account already exists, but is already associated with a customer, the Connect Webview will show an error.

        :param excluded_providers: List of provider keys to exclude from the Connect Webview. These providers will not be shown when the user tries to connect an account.

        :param provider_category: Specifies the category of providers that you want to include. To list all providers within a category, use ```/devices/list_device_providers`` <https://docs.seam.co/api/devices/list_device_providers>`_ with the desired ``provider_category`` filter.

        :param wait_for_device_creation: Indicates whether Seam should finish syncing all devices in a newly-connected account before completing the associated Connect Webview. See also: `Customize the Behavior Settings of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-behavior-settings-of-your-connect-webviews>`_.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, connect_webview_id: str) -> None:
        """Deletes a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        You do not need to delete a Connect Webview once a user completes it. Instead, you can simply ignore completed Connect Webviews.

        :param connect_webview_id: ID of the Connect Webview that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        """Returns a specified `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        Unless you're using a ``custom_redirect_url``, you should poll a newly-created ``connect_webview`` to find out if the user has signed in or to get details about what devices they've connected.

        :param connect_webview_id: ID of the Connect Webview that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[ConnectWebview]:
        """Returns a list of all `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_.

        :param custom_metadata_has: Custom metadata pairs by which you want to `filter Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/filtering-connect-webviews-by-custom-metadata>`_. Returns Connect Webviews with ``custom_metadata`` that contains all of the provided key:value pairs.

        :param customer_key: Customer key for which you want to list connect webviews.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned Connect Webviews to include all records that satisfy a partial match using ``connect_webview_id``, ``accepted_providers``, ``custom_metadata``, or ``customer_key``.

        :param user_identifier_key: Your user ID for the user by which you want to filter Connect Webviews.

        :returns: OK"""
        raise NotImplementedError()


class ConnectWebviews(AbstractConnectWebviews):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        accepted_capabilities: Optional[List[str]] = None,
        accepted_providers: Optional[List[str]] = None,
        automatically_manage_new_devices: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None,
        custom_redirect_failure_url: Optional[str] = None,
        custom_redirect_url: Optional[str] = None,
        customer_key: Optional[str] = None,
        excluded_providers: Optional[List[str]] = None,
        provider_category: Optional[str] = None,
        wait_for_device_creation: Optional[bool] = None,
    ) -> ConnectWebview:
        """Creates a new `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        To enable a user to connect their devices or systems to Seam, they must sign in to their device or system account. To enable a user to sign in, you create a ``connect_webview``. After creating the Connect Webview, you receive a URL that you can use to display the visual component of this Connect Webview for your user. You can open an iframe or new window to display the Connect Webview.

        You should make a new ``connect_webview`` for each unique login request. Each ``connect_webview`` tracks the user that signed in with it. You receive an error if you reuse a Connect Webview for the same user twice or if you use the same Connect Webview for multiple users.

        See also: `Connect Webview Process <https://docs.seam.co/core-concepts/connect-webviews/connect-webview-process>`_.

        :param accepted_capabilities: List of accepted device capabilities that restrict the types of devices that can be connected through the Connect Webview. If not provided, defaults will be determined based on the accepted providers.

        :param accepted_providers: Accepted device provider keys as an alternative to ``provider_category``. Use this parameter to specify accepted providers explicitly. See `Customize the Brands to Display in Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_. To list all provider keys, use ```/devices/list_device_providers`` <https://docs.seam.co/api/devices/list_device_providers>`_ with no filters.

        :param automatically_manage_new_devices: Indicates whether newly-added devices should appear as `managed devices <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_. See also: `Customize the Behavior Settings of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-behavior-settings-of-your-connect-webviews>`_.

        :param custom_metadata: Custom metadata that you want to associate with the Connect Webview. Supports up to 50 JSON key:value pairs. `Adding custom metadata to a Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_ enables you to store custom information, like customer details or internal IDs from your application. The custom metadata is then transferred to any `connected accounts <https://docs.seam.co/core-concepts/connected-accounts>`_ that were connected using the Connect Webview, making it easy to find and filter these resources in your `workspace <https://docs.seam.co/core-concepts/workspaces>`_. You can also `filter Connect Webviews by custom metadata <https://docs.seam.co/core-concepts/connect-webviews/filtering-connect-webviews-by-custom-metadata>`_.

        :param custom_redirect_failure_url: Alternative URL that you want to redirect the user to on an error. If you do not set this parameter, the Connect Webview falls back to the ``custom_redirect_url``.

        :param custom_redirect_url: URL that you want to redirect the user to after the provider login is complete.

        :param customer_key: Associate the Connect Webview, the connected account, and all resources under the connected account with a customer. If the connected account already exists, it will be associated with the customer. If the connected account already exists, but is already associated with a customer, the Connect Webview will show an error.

        :param excluded_providers: List of provider keys to exclude from the Connect Webview. These providers will not be shown when the user tries to connect an account.

        :param provider_category: Specifies the category of providers that you want to include. To list all providers within a category, use ```/devices/list_device_providers`` <https://docs.seam.co/api/devices/list_device_providers>`_ with the desired ``provider_category`` filter.

        :param wait_for_device_creation: Indicates whether Seam should finish syncing all devices in a newly-connected account before completing the associated Connect Webview. See also: `Customize the Behavior Settings of Your Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-behavior-settings-of-your-connect-webviews>`_.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if accepted_capabilities is not None:
            json_payload["accepted_capabilities"] = accepted_capabilities
        if accepted_providers is not None:
            json_payload["accepted_providers"] = accepted_providers
        if automatically_manage_new_devices is not None:
            json_payload["automatically_manage_new_devices"] = (
                automatically_manage_new_devices
            )
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if custom_redirect_failure_url is not None:
            json_payload["custom_redirect_failure_url"] = custom_redirect_failure_url
        if custom_redirect_url is not None:
            json_payload["custom_redirect_url"] = custom_redirect_url
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if excluded_providers is not None:
            json_payload["excluded_providers"] = excluded_providers
        if provider_category is not None:
            json_payload["provider_category"] = provider_category
        if wait_for_device_creation is not None:
            json_payload["wait_for_device_creation"] = wait_for_device_creation

        res = self.client.post("/connect_webviews/create", json=json_payload)

        return ConnectWebview.from_dict(res["connect_webview"])

    def delete(self, *, connect_webview_id: str) -> None:
        """Deletes a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        You do not need to delete a Connect Webview once a user completes it. Instead, you can simply ignore completed Connect Webviews.

        :param connect_webview_id: ID of the Connect Webview that you want to delete."""
        json_payload: Dict[str, Any] = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        self.client.post("/connect_webviews/delete", json=json_payload)

        return None

    def get(self, *, connect_webview_id: str) -> ConnectWebview:
        """Returns a specified `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

        Unless you're using a ``custom_redirect_url``, you should poll a newly-created ``connect_webview`` to find out if the user has signed in or to get details about what devices they've connected.

        :param connect_webview_id: ID of the Connect Webview that you want to get.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id

        res = self.client.post("/connect_webviews/get", json=json_payload)

        return ConnectWebview.from_dict(res["connect_webview"])

    def list(
        self,
        *,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        customer_key: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[ConnectWebview]:
        """Returns a list of all `Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews>`_.

        :param custom_metadata_has: Custom metadata pairs by which you want to `filter Connect Webviews <https://docs.seam.co/core-concepts/connect-webviews/filtering-connect-webviews-by-custom-metadata>`_. Returns Connect Webviews with ``custom_metadata`` that contains all of the provided key:value pairs.

        :param customer_key: Customer key for which you want to list connect webviews.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned Connect Webviews to include all records that satisfy a partial match using ``connect_webview_id``, ``accepted_providers``, ``custom_metadata``, or ``customer_key``.

        :param user_identifier_key: Your user ID for the user by which you want to filter Connect Webviews.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

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
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/connect_webviews/list", json=json_payload)

        return [ConnectWebview.from_dict(item) for item in res["connect_webviews"]]
