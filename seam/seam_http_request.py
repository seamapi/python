from typing import (
    Any,
    Dict,
    Generic,
    Optional,
    TypeVar,
    cast,
    TypeVar,
    Type,
)
from urllib.parse import urljoin, urlencode
import asyncio
from concurrent.futures import Future

from .client import SeamHttpClient
from .exceptions import SeamHttpApiError
from .routes.models import ActionAttempt
from .modules.action_attempts import resolve_action_attempt

T = TypeVar("T")
TResponseKey = TypeVar("TResponseKey", bound=Optional[str])


class SeamHttpRequestParent:
    """Container for the client and default options used by SeamHttpRequest."""

    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        """
        Initialize a SeamHttpRequestParent.

        Args:
            client: The HTTP client used to make requests.
            defaults: Default options for requests.
        """
        self.client = client
        self.defaults = defaults


class SeamHttpRequestConfig(Generic[TResponseKey]):
    """Configuration for a SeamHttpRequest."""

    def __init__(
        self,
        pathname: str,
        method: str,
        body: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        response_key: TResponseKey = None,
        options: Optional[Dict[str, Any]] = None,
        model_type: Optional[Type[Any]] = None,
    ):
        """
        Initialize a SeamHttpRequestConfig.

        Args:
            pathname: The path for the request.
            method: The HTTP method for the request.
            body: The request body, if any.
            params: The query parameters, if any.
            response_key: The key in the response to extract.
            options: Additional options for the request.
            model_type: The model class to use for converting response data.
                        Must have a from_dict method.
        """
        self.pathname = pathname
        self.method = method
        self.body = body
        self.params = params
        self.response_key = response_key
        self.options = options or {}
        self.model_type = model_type


class SeamHttpRequest(Generic[T, TResponseKey]):
    """
    A class representing an HTTP request to the Seam API.

    This class provides multiple ways to interact with it:

    1. Direct execution: `result = request.execute()`
    2. Context manager: `with request as result: ...`
    3. Async/await: `result = await request`
    4. Callback-based: `request.then(callback).catch(error_handler)`

    Examples:
        ```python
        # Direct execution
        request = client.action_attempts.get(action_attempt_id="act_123")
        result = request.execute()

        # Context manager
        with client.action_attempts.get(action_attempt_id="act_123") as result:
            print(result.status)

        # Async/await
        result = await client.action_attempts.get(action_attempt_id="act_123")

        # Callback pattern
        client.action_attempts.get(action_attempt_id="act_123").then(
            lambda result: print(f"Success: {result.status}"),
            lambda error: print(f"Error: {error}")
        )
        ```
    """

    def __init__(
        self,
        parent: SeamHttpRequestParent,
        config: SeamHttpRequestConfig[TResponseKey],
    ):
        """
        Initialize a SeamHttpRequest.

        Args:
            parent: The parent container with client and defaults.
            config: The configuration for this request.
        """
        self._parent = parent
        self._config = config
        self._future: Optional[Future] = None

    @property
    def response_key(self) -> TResponseKey:
        """Get the response key for this request."""
        return self._config.response_key

    @property
    def url(self) -> str:
        """
        Construct the full URL for this request, including query parameters.

        Returns:
            The complete URL for the request.
        """
        client = self._parent.client
        base_url = client.base_url

        pathname = self.pathname

        if self.params:
            query_string = urlencode(self.params)
            pathname = f"{pathname}?{query_string}"

        return urljoin(base_url, pathname)

    @property
    def pathname(self) -> str:
        """Get the path for this request, ensuring it starts with a slash."""
        if self._config.pathname.startswith("/"):
            return self._config.pathname
        return f"/{self._config.pathname}"

    @property
    def method(self) -> str:
        """Get the HTTP method for this request."""
        return self._config.method

    @property
    def params(self) -> Optional[Dict[str, Any]]:
        """Get the query parameters for this request."""
        return self._config.params

    @property
    def body(self) -> Any:
        """Get the body for this request."""
        return self._config.body

    def execute(self) -> T:
        """
        Execute the request and process the response.

        Returns:
            The response data, extracted using the response_key if provided.

        Raises:
            SeamHttpApiError: If the request fails.
        """
        response = self.fetch_response()

        if self.response_key is None:
            return cast(T, None)

        data = response[self.response_key]
        model_type = self._config.model_type

        if self.response_key == "action_attempt":
            wait_for_action_attempt = self._config.options.get(
                "wait_for_action_attempt",
                self._parent.defaults.get("wait_for_action_attempt"),
            )

            if wait_for_action_attempt is not False:
                if model_type and hasattr(model_type, "from_dict"):
                    action_attempt = model_type.from_dict(data)
                else:
                    action_attempt = cast(ActionAttempt, data)

                wait_options = (
                    {}
                    if isinstance(wait_for_action_attempt, bool)
                    else wait_for_action_attempt
                )

                return cast(
                    T,
                    resolve_action_attempt(
                        client=self._parent.client,
                        action_attempt=action_attempt,
                        wait_for_action_attempt=wait_options,
                    ),
                )

        if model_type and hasattr(model_type, "from_dict"):
            if isinstance(data, list):
                return cast(T, [model_type.from_dict(item) for item in data])
            else:
                return cast(T, model_type.from_dict(data))

        return cast(T, data)

    def fetch_response(self) -> Dict[str, Any]:
        """
        Fetch the raw response from the API.

        Returns:
            The raw API response.

        Raises:
            SeamHttpApiError: If the request fails.
        """
        client = self._parent.client
        response = client.request(
            method=self.method, url=self.pathname, json=self.body, params=self.params
        )
        return response

    # Context manager support
    def __enter__(self) -> T:
        """Allow usage as a context manager that returns the executed result."""
        return self.execute()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        pass

    # Async/await support
    def __await__(self):
        """Allow the request to be awaited like a coroutine."""
        # Create a future to wrap the synchronous execution
        if self._future is None:
            loop = asyncio.get_event_loop()
            self._future = loop.run_in_executor(None, self.execute)
        return self._future.__await__()

    def then(self, on_fulfilled=None, on_rejected=None):
        """
        Chain operations to be performed after the request is complete.

        This provides a promise-like interface similar to JavaScript, but
        adapted to be more Pythonic. The method returns self to allow chaining.

        Args:
            on_fulfilled: Function to call if the request succeeds.
            on_rejected: Function to call if the request fails.

        Returns:
            Self, allowing method chaining.

        Example:
            ```python
            request.then(
                lambda result: print(f"Success: {result}"),
                lambda error: print(f"Error: {error}")
            )
            ```
        """
        try:
            result = self.execute()
            if on_fulfilled:
                on_fulfilled(result)
        except Exception as e:
            if on_rejected:
                on_rejected(e)
            else:
                raise
        return self

    def catch(self, on_rejected):
        """
        Handle errors from the request.

        A Pythonic adaptation of the Promise.catch pattern.

        Args:
            on_rejected: Function to call if the request fails.

        Returns:
            Self, allowing method chaining.

        Example:
            ```python
            request.catch(lambda error: print(f"Error: {error}"))
            ```
        """
        try:
            self.execute()
        except Exception as e:
            on_rejected(e)
        return self

    def finally_do(self, on_finally=None):
        """
        Perform operations after the request completes, regardless of success or failure.

        A Pythonic adaptation of the Promise.finally pattern. Named 'finally_do'
        to avoid conflicts with the Python keyword 'finally'.

        Args:
            on_finally: Function to call after the request completes.

        Returns:
            Self, allowing method chaining.

        Example:
            ```python
            request.finally_do(lambda: print("Request completed"))
            ```
        """
        try:
            self.execute()
        except Exception:
            pass
        finally:
            if on_finally:
                on_finally()
        return self
