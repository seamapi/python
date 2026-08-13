from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class ConnectWebview:
    """Represents a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_.

    Connect Webviews are fully-embedded client-side components that you add to your app. Your users interact with your embedded Connect Webviews to link their IoT device or system accounts to Seam. That is, Connect Webviews walk your users through the process of logging in to their device or system accounts. Seam handles all the authentication steps, and—once your user has completed the authorization through your app—you can access and control their devices or systems using the Seam API.

    Connect Webviews perform credential validation, multifactor authentication (when applicable), and error handling for each brand that Seam supports. Further, Connect Webviews work across all modern browsers and platforms, including Chrome, Safari, and Firefox.

    To enable a user to connect their device or system account to Seam through your app, first create a ``connect_webview``. Once created, this ``connect_webview`` includes a URL that you can use to open an `iframe <https://www.w3schools.com/html/html_iframe.asp>`_ or new window containing the Connect Webview for your user.

    When you create a Connect Webview, specify the desired provider category key in the ``provider_category`` parameter. Alternately, to specify a list of providers explicitly, use the ``accepted_providers`` parameter with a list of device provider keys.

    To list all providers within a category, use ``/devices/list_device_providers`` with the desired ``provider_category`` filter. To list all provider keys, use ``/devices/list_device_providers`` with no filters.

    :ivar accepted_capabilities: High-level device capabilities that the Connect Webview can accept. When creating a Connect Webview, you can specify the types of devices that it can connect to Seam. If you do not set custom ``accepted_capabilities``, Seam uses a default set of ``accepted_capabilities`` for each provider. For example, if you create a Connect Webview that accepts SmartThing devices, without specifying ``accepted_capabilities``, Seam accepts only SmartThings locks. To connect SmartThings thermostats and locks to Seam, create a Connect Webview and include both ``thermostat`` and ``lock`` in the ``accepted_capabilities``.

    :ivar accepted_providers: List of accepted `provider keys <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

    :ivar any_provider_allowed: Indicates whether any provider is allowed.

    :ivar authorized_at: Date and time at which the user authorized (through the Connect Webview) the management of their devices.

    :ivar automatically_manage_new_devices: Indicates whether Seam should `import all new devices <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#automatically_manage_new_devices>`_ for the connected account to make these devices available for use and management by the Seam API.

    :ivar connect_webview_id: ID of the Connect Webview.

    :ivar connected_account_id: ID of the connected account associated with the Connect Webview.

    :ivar created_at: Date and time at which the Connect Webview was created.

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_, `connected account <https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account>`_, or `device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_, enables you to store custom information, like customer details or internal IDs from your application.

    :ivar custom_redirect_failure_url: URL to which the Connect Webview should redirect when an unexpected error occurs.

    :ivar custom_redirect_url: URL to which the Connect Webview should redirect when the user successfully pairs a device or system. If you do not set the ``custom_redirect_failure_url``, the Connect Webview redirects to the ``custom_redirect_url`` when an unexpected error occurs.

    :ivar customer_key: The customer key associated with this webview, if any.

    :ivar device_selection_mode: Device selection mode of the Connect Webview. Supported values: ``none``, ``single``, ``multiple``.

    :ivar login_successful: Indicates whether the user logged in successfully using the Connect Webview.

    :ivar selected_provider: Selected provider of the Connect Webview, one of the `provider keys <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#customize-the-brands-to-display-in-your-connect-webviews>`_.

    :ivar status: Status of the Connect Webview. ``authorized`` indicates that the user has successfully logged into their device or system account, thereby completing the Connect Webview.

    :ivar url: URL for the Connect Webview. You use the URL to display the Connect Webview flow to your user.

    :ivar wait_for_device_creation: Indicates whether Seam should `finish syncing all devices <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#wait_for_device_creation>`_ in a newly-connected account before completing the associated Connect Webview.

    :ivar workspace_id: ID of the workspace that contains the Connect Webview."""

    accepted_capabilities: List[str]
    accepted_providers: List[str]
    any_provider_allowed: bool
    authorized_at: Optional[str]
    automatically_manage_new_devices: bool
    connect_webview_id: str
    connected_account_id: Optional[str]
    created_at: str
    custom_metadata: Dict[str, Any]
    custom_redirect_failure_url: Optional[str]
    custom_redirect_url: Optional[str]
    customer_key: Optional[str]
    device_selection_mode: str
    login_successful: bool
    selected_provider: Optional[str]
    status: str
    url: str
    wait_for_device_creation: bool
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            accepted_capabilities=d.get("accepted_capabilities", None),
            accepted_providers=d.get("accepted_providers", None),
            any_provider_allowed=d.get("any_provider_allowed", None),
            authorized_at=d.get("authorized_at", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            custom_redirect_failure_url=d.get("custom_redirect_failure_url", None),
            custom_redirect_url=d.get("custom_redirect_url", None),
            customer_key=d.get("customer_key", None),
            device_selection_mode=d.get("device_selection_mode", None),
            login_successful=d.get("login_successful", None),
            selected_provider=d.get("selected_provider", None),
            status=d.get("status", None),
            url=d.get("url", None),
            wait_for_device_creation=d.get("wait_for_device_creation", None),
            workspace_id=d.get("workspace_id", None),
        )
