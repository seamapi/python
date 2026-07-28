from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ClientSession


class AbstractClientSessions(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        customer_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> ClientSession:
        """Creates a new [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) for which you want to create a client session.
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/core-concepts/connected-accounts) for which you want to create a client session.
        :type connected_account_ids: List[str]

        :param customer_id: Customer ID that you want to associate with the new client session.
        :type customer_id: str

        :param customer_key: Customer key that you want to associate with the new client session.
        :type customer_key: str

        :param expires_at: Date and time at which the client session should expire, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :type expires_at: str

        :param user_identifier_key: Your user ID for the user for whom you want to create a client session.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) for which you want to create a client session.
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id` instead. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: ClientSession"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, client_session_id: str) -> None:
        """Deletes a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to delete.
        :type client_session_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        client_session_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> ClientSession:
        """Returns a specified [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to get.
        :type client_session_id: str

        :param user_identifier_key: User identifier key associated with the client session that you want to get.
        :type user_identifier_key: str

        :returns: OK
        :rtype: ClientSession"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_or_create(
        self,
        *,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> ClientSession:
        """Returns a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) with specific characteristics or creates a new client session with these characteristics if it does not yet exist.

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) that you want to associate with the client session (or that are already associated with the existing client session).
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/api/connected_accounts) that you want to associate with the client session (or that are already associated with the existing client session).
        :type connected_account_ids: List[str]

        :param expires_at: Date and time at which the client session should expire in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. If the client session already exists, this will update the expiration before returning it.
        :type expires_at: str

        :param user_identifier_key: Your user ID for the user that you want to associate with the client session (or that is already associated with the existing client session).
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session (or that are already associated with the existing client session).
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id`. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: ClientSession"""
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> None:
        """Grants a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) access to one or more resources, such as [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews), [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity), and so on.

        :param client_session_id: ID of the client session to which you want to grant access to resources.
        :type client_session_id: str

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) that you want to associate with the client session.
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/core-concepts/connected-accounts) that you want to associate with the client session.
        :type connected_account_ids: List[str]

        :param user_identifier_key: Your user ID for the user that you want to associate with the client session.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id`. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        without_user_identifier_key: Optional[bool] = None
    ) -> List[ClientSession]:
        """Returns a list of all [client sessions](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to retrieve.
        :type client_session_id: str

        :param connect_webview_id: ID of the [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) for which you want to retrieve client sessions.
        :type connect_webview_id: str

        :param user_identifier_key: Your user ID for the user by which you want to filter client sessions.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) for which you want to retrieve client sessions.
        :type user_identity_id: str

        :param without_user_identifier_key: Indicates whether to retrieve only client sessions without associated user identifier keys.
        :type without_user_identifier_key: bool

        :returns: OK
        :rtype: List[ClientSession]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def revoke(self, *, client_session_id: str) -> None:
        """Revokes a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        Note that [deleting a client session](https://docs.seam.co/api/client_sessions/delete) is a separate action.

        :param client_session_id: ID of the client session that you want to revoke.
        :type client_session_id: str"""
        raise NotImplementedError()


class ClientSessions(AbstractClientSessions):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        customer_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> ClientSession:
        """Creates a new [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) for which you want to create a client session.
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/core-concepts/connected-accounts) for which you want to create a client session.
        :type connected_account_ids: List[str]

        :param customer_id: Customer ID that you want to associate with the new client session.
        :type customer_id: str

        :param customer_key: Customer key that you want to associate with the new client session.
        :type customer_key: str

        :param expires_at: Date and time at which the client session should expire, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :type expires_at: str

        :param user_identifier_key: Your user ID for the user for whom you want to create a client session.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) for which you want to create a client session.
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id` instead. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: ClientSession"""
        json_payload = {}

        if connect_webview_ids is not None:
            json_payload["connect_webview_ids"] = connect_webview_ids
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if customer_id is not None:
            json_payload["customer_id"] = customer_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if expires_at is not None:
            json_payload["expires_at"] = expires_at
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_ids is not None:
            json_payload["user_identity_ids"] = user_identity_ids

        res = self.client.post("/client_sessions/create", json=json_payload)

        return ClientSession.from_dict(res["client_session"])

    def delete(self, *, client_session_id: str) -> None:
        """Deletes a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to delete.
        :type client_session_id: str"""
        json_payload = {}

        if client_session_id is not None:
            json_payload["client_session_id"] = client_session_id

        self.client.post("/client_sessions/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        client_session_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> ClientSession:
        """Returns a specified [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to get.
        :type client_session_id: str

        :param user_identifier_key: User identifier key associated with the client session that you want to get.
        :type user_identifier_key: str

        :returns: OK
        :rtype: ClientSession"""
        json_payload = {}

        if client_session_id is not None:
            json_payload["client_session_id"] = client_session_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/client_sessions/get", json=json_payload)

        return ClientSession.from_dict(res["client_session"])

    def get_or_create(
        self,
        *,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        expires_at: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> ClientSession:
        """Returns a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) with specific characteristics or creates a new client session with these characteristics if it does not yet exist.

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) that you want to associate with the client session (or that are already associated with the existing client session).
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/api/connected_accounts) that you want to associate with the client session (or that are already associated with the existing client session).
        :type connected_account_ids: List[str]

        :param expires_at: Date and time at which the client session should expire in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. If the client session already exists, this will update the expiration before returning it.
        :type expires_at: str

        :param user_identifier_key: Your user ID for the user that you want to associate with the client session (or that is already associated with the existing client session).
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session (or that are already associated with the existing client session).
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id`. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]

        :returns: OK
        :rtype: ClientSession"""
        json_payload = {}

        if connect_webview_ids is not None:
            json_payload["connect_webview_ids"] = connect_webview_ids
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if expires_at is not None:
            json_payload["expires_at"] = expires_at
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_ids is not None:
            json_payload["user_identity_ids"] = user_identity_ids

        res = self.client.post("/client_sessions/get_or_create", json=json_payload)

        return ClientSession.from_dict(res["client_session"])

    def grant_access(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_ids: Optional[List[str]] = None,
        connected_account_ids: Optional[List[str]] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_ids: Optional[List[str]] = None
    ) -> None:
        """Grants a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens) access to one or more resources, such as [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews), [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity), and so on.

        :param client_session_id: ID of the client session to which you want to grant access to resources.
        :type client_session_id: str

        :param connect_webview_ids: IDs of the [Connect Webviews](https://docs.seam.co/core-concepts/connect-webviews) that you want to associate with the client session.
        :type connect_webview_ids: List[str]

        :param connected_account_ids: IDs of the [connected accounts](https://docs.seam.co/core-concepts/connected-accounts) that you want to associate with the client session.
        :type connected_account_ids: List[str]

        :param user_identifier_key: Your user ID for the user that you want to associate with the client session.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_id: str

        :param user_identity_ids: Deprecated: Use `user_identity_id`. IDs of the [user identities](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) that you want to associate with the client session.
        :type user_identity_ids: List[str]"""
        json_payload = {}

        if client_session_id is not None:
            json_payload["client_session_id"] = client_session_id
        if connect_webview_ids is not None:
            json_payload["connect_webview_ids"] = connect_webview_ids
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_ids is not None:
            json_payload["user_identity_ids"] = user_identity_ids

        self.client.post("/client_sessions/grant_access", json=json_payload)

        return None

    def list(
        self,
        *,
        client_session_id: Optional[str] = None,
        connect_webview_id: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        without_user_identifier_key: Optional[bool] = None
    ) -> List[ClientSession]:
        """Returns a list of all [client sessions](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        :param client_session_id: ID of the client session that you want to retrieve.
        :type client_session_id: str

        :param connect_webview_id: ID of the [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews) for which you want to retrieve client sessions.
        :type connect_webview_id: str

        :param user_identifier_key: Your user ID for the user by which you want to filter client sessions.
        :type user_identifier_key: str

        :param user_identity_id: ID of the [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) for which you want to retrieve client sessions.
        :type user_identity_id: str

        :param without_user_identifier_key: Indicates whether to retrieve only client sessions without associated user identifier keys.
        :type without_user_identifier_key: bool

        :returns: OK
        :rtype: List[ClientSession]"""
        json_payload = {}

        if client_session_id is not None:
            json_payload["client_session_id"] = client_session_id
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if without_user_identifier_key is not None:
            json_payload["without_user_identifier_key"] = without_user_identifier_key

        res = self.client.post("/client_sessions/list", json=json_payload)

        return [ClientSession.from_dict(item) for item in res["client_sessions"]]

    def revoke(self, *, client_session_id: str) -> None:
        """Revokes a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens).

        Note that [deleting a client session](https://docs.seam.co/api/client_sessions/delete) is a separate action.

        :param client_session_id: ID of the client session that you want to revoke.
        :type client_session_id: str"""
        json_payload = {}

        if client_session_id is not None:
            json_payload["client_session_id"] = client_session_id

        self.client.post("/client_sessions/revoke", json=json_payload)

        return None
