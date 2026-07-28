from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ClientSession:
    """Represents a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens). If you want to restrict your users' access to their own devices, use client sessions.

    You create each client session with a custom `user_identifier_key`. Normally, the `user_identifier_key` is a user ID that your application provides.

    When calling the Seam API from your backend using an API key, you can pass the `user_identifier_key` as a parameter to limit results to the associated client session. For example, `/devices/list?user_identifier_key=123` only returns devices associated with the client session created with the `user_identifier_key` `123`.

    A client session has a token that you can use with the Seam JavaScript SDK to make requests from the client (browser) directly to the Seam API. The token restricts the user's access to only the devices that they own.

    See also [Get Started with React](https://docs.seam.co/ui-components/overview/getting-started-with-seam-components/get-started-with-react-components-and-client-session-tokens).

    :ivar client_session_id: ID of the client session.
    :vartype client_session_id: str

    :ivar connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype connect_webview_ids: List[str]

    :ivar connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/core-concepts/connected-accounts) associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype connected_account_ids: List[str]

    :ivar created_at: Date and time at which the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) was created.
    :vartype created_at: str

    :ivar customer_key: Customer key associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype customer_key: str

    :ivar device_count: Number of devices associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype device_count: float

    :ivar expires_at: Date and time at which the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) expires.
    :vartype expires_at: str

    :ivar token: Client session token associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype token: str

    :ivar user_identifier_key: Your user ID for the user associated with the [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).
    :vartype user_identifier_key: str

    :ivar user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) associated with the client session.
    :vartype user_identity_id: str

    :ivar user_identity_ids: Deprecated: Use `user_identity_id` instead. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) associated with the client session.
    :vartype user_identity_ids: List[str]

    :ivar workspace_id: ID of the workspace associated with the client session.
    :vartype workspace_id: str"""

    client_session_id: str
    connect_webview_ids: List[str]
    connected_account_ids: List[str]
    created_at: str
    customer_key: str
    device_count: float
    expires_at: str
    token: str
    user_identifier_key: str
    user_identity_id: str
    user_identity_ids: List[str]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ClientSession(
            client_session_id=d.get("client_session_id", None),
            connect_webview_ids=d.get("connect_webview_ids", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_count=d.get("device_count", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
            user_identifier_key=d.get("user_identifier_key", None),
            user_identity_id=d.get("user_identity_id", None),
            user_identity_ids=d.get("user_identity_ids", None),
            workspace_id=d.get("workspace_id", None),
        )
