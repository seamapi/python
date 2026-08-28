from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Tuple,
)
from .client import AsyncSeamHttpClient, SeamHttpClient
from .exceptions import SeamHttpInvalidResponseError
from .pagination import Pagination


def parse_pagination(pagination: Dict[str, Any]) -> Pagination:
    return Pagination(
        has_next_page=pagination.get("has_next_page", False),
        next_page_cursor=pagination.get("next_page_cursor"),
        next_page_url=pagination.get("next_page_url"),
    )


def read_pagination(data: Any, request: Callable) -> Pagination:
    """Read the pagination envelope a paginated route attaches to its result."""

    pagination = getattr(data, "pagination", None)

    if not isinstance(pagination, dict):
        path = getattr(request, "__seam_path__", "this endpoint")
        raise SeamHttpInvalidResponseError(
            path,
            "pagination",
            f"got {type(pagination).__name__} instead of a pagination object",
        )

    return parse_pagination(pagination)


class SeamPaginator:
    """
    Handles pagination for API list endpoints.

    Iterates through pages of results returned by a callable function.
    """

    def __init__(
        self,
        client: SeamHttpClient,
        request: Callable,
        params: Optional[Dict[str, Any]] = None,
    ):
        """
        Initializes the Paginator.

        Args:
            request: The function to call to fetch a page of data.
            http_client: The Seam HTTP client used in the request.
            params: Initial parameters to pass to the callable function.
        """
        self._request = request
        self.client = client
        self._params = params or {}

    def first_page(self) -> Tuple[List[Any], Pagination | None]:
        """Fetches the first page of results."""
        data = self._request(**self._params)

        return data, read_pagination(data, self._request)

    def next_page(
        self, next_page_cursor: str, /
    ) -> Tuple[List[Any], Pagination | None]:
        """Fetches the next page of results using a cursor."""
        if not next_page_cursor:
            raise ValueError("Cannot get the next page with a null next_page_cursor.")

        params = {
            **self._params,
            "page_cursor": next_page_cursor,
        }

        data = self._request(**params)

        return data, read_pagination(data, self._request)

    def flatten_to_list(self) -> List[Any]:
        """Fetches all pages and returns all items as a single list."""
        all_items = []
        for current_items in self._walk():
            all_items.extend(current_items)

        return all_items

    def flatten(self) -> Generator[Any, None, None]:
        """Fetches all pages and yields items one by one using a generator."""
        for current_items in self._walk():
            yield from current_items

    def _walk(self) -> Generator[List[Any], None, None]:
        """Yields each page once, stopping if the server repeats a cursor."""
        current_items, pagination = self.first_page()
        yield current_items or []

        seen_cursors = set()

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            cursor = pagination.next_page_cursor

            if cursor in seen_cursors:
                return
            seen_cursors.add(cursor)

            current_items, pagination = self.next_page(cursor)
            yield current_items or []


class AsyncSeamPaginator:
    """
    Handles pagination for API list endpoints using an async client.

    Iterates through pages of results returned by an awaitable function.
    """

    def __init__(
        self,
        client: AsyncSeamHttpClient,
        request: Callable,
        params: Optional[Dict[str, Any]] = None,
    ):
        """
        Initializes the Paginator.

        Args:
            request: The coroutine function to call to fetch a page of data.
            http_client: The async Seam HTTP client used in the request.
            params: Initial parameters to pass to the callable function.
        """
        self._request = request
        self.client = client
        self._params = params or {}

    async def first_page(self) -> Tuple[List[Any], Pagination | None]:
        """Fetches the first page of results."""
        data = await self._request(**self._params)

        return data, read_pagination(data, self._request)

    async def next_page(
        self, next_page_cursor: str, /
    ) -> Tuple[List[Any], Pagination | None]:
        """Fetches the next page of results using a cursor."""
        if not next_page_cursor:
            raise ValueError("Cannot get the next page with a null next_page_cursor.")

        params = {
            **self._params,
            "page_cursor": next_page_cursor,
        }

        data = await self._request(**params)

        return data, read_pagination(data, self._request)

    async def flatten_to_list(self) -> List[Any]:
        """Fetches all pages and returns all items as a single list."""
        all_items = []
        async for current_items in self._walk():
            all_items.extend(current_items)

        return all_items

    async def flatten(self) -> AsyncGenerator[Any, None]:
        """Fetches all pages and yields items one by one using an async generator."""
        async for current_items in self._walk():
            for item in current_items:
                yield item

    async def _walk(self) -> AsyncGenerator[List[Any], None]:
        """Yields each page once, stopping if the server repeats a cursor."""
        current_items, pagination = await self.first_page()
        yield current_items or []

        seen_cursors = set()

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            cursor = pagination.next_page_cursor

            if cursor in seen_cursors:
                return
            seen_cursors.add(cursor)

            current_items, pagination = await self.next_page(cursor)
            yield current_items or []
