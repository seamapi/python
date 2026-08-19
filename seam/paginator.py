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
from json import JSONDecodeError
from httpx import Response
from .client import AsyncSeamHttpClient, SeamHttpClient
from .pagination import Pagination


def parse_pagination(pagination: Dict[str, Any]) -> Pagination:
    return Pagination(
        has_next_page=pagination.get("has_next_page", False),
        next_page_cursor=pagination.get("next_page_cursor"),
        next_page_url=pagination.get("next_page_url"),
    )


class SeamPaginator:
    """
    Handles pagination for API list endpoints.

    Iterates through pages of results returned by a callable function.
    """

    _FIRST_PAGE = "FIRST_PAGE"

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
        self._pagination_cache: Dict[str, Pagination] = {}

    def first_page(self) -> Tuple[List[Any], Pagination | None]:
        """Fetches the first page of results."""
        self.client.event_hooks["response"].append(
            lambda response: self._cache_pagination(response, self._FIRST_PAGE)
        )
        data = self._request(**self._params)
        self.client.event_hooks["response"].pop()

        pagination = self._pagination_cache.get(self._FIRST_PAGE)

        return data, pagination

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

        self.client.event_hooks["response"].append(
            lambda response: self._cache_pagination(response, next_page_cursor)
        )
        data = self._request(**params)
        self.client.event_hooks["response"].pop()

        pagination = self._pagination_cache.get(next_page_cursor)

        return data, pagination

    def flatten_to_list(self) -> List[Any]:
        """Fetches all pages and returns all items as a single list."""
        all_items = []
        current_items, pagination = self.first_page()

        if current_items:
            all_items.extend(current_items)

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            current_items, pagination = self.next_page(pagination.next_page_cursor)
            if current_items:
                all_items.extend(current_items)

        return all_items

    def flatten(self) -> Generator[Any, None, None]:
        """Fetches all pages and yields items one by one using a generator."""
        current_items, pagination = self.first_page()
        if current_items:
            yield from current_items

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            current_items, pagination = self.next_page(pagination.next_page_cursor)
            if current_items:
                yield from current_items

    def _cache_pagination(self, response: Response, page_key: str) -> None:
        """Extracts pagination dict from response, creates Pagination object, and caches it."""
        try:
            # httpx response hooks fire before the response body is read.
            response.read()
            pagination = response.json().get("pagination", {})
        except JSONDecodeError:
            pagination = {}

        if isinstance(pagination, dict):
            self._pagination_cache[page_key] = parse_pagination(pagination)


class AsyncSeamPaginator:
    """
    Handles pagination for API list endpoints using an async client.

    Iterates through pages of results returned by an awaitable function.
    """

    _FIRST_PAGE = "FIRST_PAGE"

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
        self._pagination_cache: Dict[str, Pagination] = {}

    async def first_page(self) -> Tuple[List[Any], Pagination | None]:
        """Fetches the first page of results."""

        async def cache_pagination(response: Response) -> None:
            await self._cache_pagination(response, self._FIRST_PAGE)

        self.client.event_hooks["response"].append(cache_pagination)
        data = await self._request(**self._params)
        self.client.event_hooks["response"].pop()

        pagination = self._pagination_cache.get(self._FIRST_PAGE)

        return data, pagination

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

        async def cache_pagination(response: Response) -> None:
            await self._cache_pagination(response, next_page_cursor)

        self.client.event_hooks["response"].append(cache_pagination)
        data = await self._request(**params)
        self.client.event_hooks["response"].pop()

        pagination = self._pagination_cache.get(next_page_cursor)

        return data, pagination

    async def flatten_to_list(self) -> List[Any]:
        """Fetches all pages and returns all items as a single list."""
        all_items = []
        current_items, pagination = await self.first_page()

        if current_items:
            all_items.extend(current_items)

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            current_items, pagination = await self.next_page(
                pagination.next_page_cursor
            )
            if current_items:
                all_items.extend(current_items)

        return all_items

    async def flatten(self) -> AsyncGenerator[Any, None]:
        """Fetches all pages and yields items one by one using an async generator."""
        current_items, pagination = await self.first_page()
        for item in current_items or []:
            yield item

        while pagination and pagination.has_next_page and pagination.next_page_cursor:
            current_items, pagination = await self.next_page(
                pagination.next_page_cursor
            )
            for item in current_items or []:
                yield item

    async def _cache_pagination(self, response: Response, page_key: str) -> None:
        """Extracts pagination dict from response, creates Pagination object, and caches it."""
        try:
            # httpx response hooks fire before the response body is read.
            await response.aread()
            pagination = response.json().get("pagination", {})
        except JSONDecodeError:
            pagination = {}

        if isinstance(pagination, dict):
            self._pagination_cache[page_key] = parse_pagination(pagination)
