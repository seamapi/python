from typing import Callable, Dict, Any, Tuple, Generator, List


class Pagination:
    def __init__(
        self,
        has_next_page: bool,
        next_page_cursor: str | None,
        next_page_url: str | None,
    ):
        self.has_next_page = has_next_page
        self.next_page_cursor = next_page_cursor
        self.next_page_url = next_page_url


class Paginator:
    """
    Handles pagination for API list endpoints.

    Iterates through pages of results returned by a callable function.
    """

    _FIRST_PAGE = "FIRST_PAGE"

    def __init__(self, request: Callable, params: Dict[str, Any] = None):
        """
        Initializes the Paginator.

        Args:
            request: The function to call to fetch a page of data.
            params: Initial parameters to pass to the callable function.
        """
        self._request = request
        self._params = params or {}
        self._pagination_cache: Dict[str, Pagination] = {}

    def _cache_pagination(self, response: Dict[str, Any], page_key: str) -> None:
        """Extracts pagination dict from response, creates Pagination object, and caches it."""
        pagination = response.get("pagination", {})

        if isinstance(pagination, dict):
            self._pagination_cache[page_key] = Pagination(
                has_next_page=pagination.get("has_next_page", False),
                next_page_cursor=pagination.get("next_page_cursor"),
                next_page_url=pagination.get("next_page_url"),
            )

    def first_page(self) -> Tuple[List[Any], Pagination | None]:
        """Fetches the first page of results."""
        params = {
            **self._params,
            "on_response": lambda response: self._cache_pagination(
                response, self._FIRST_PAGE
            ),
        }

        data = self._request(**params)
        pagination = self._pagination_cache.get(self._FIRST_PAGE)

        return data, pagination

    def next_page(self, next_page_cursor: str) -> Tuple[List[Any], Pagination | None]:
        """Fetches the next page of results using a cursor."""
        if not next_page_cursor:
            raise ValueError("Cannot get the next page with a null next_page_cursor.")

        params = {
            **self._params,
            "page_cursor": next_page_cursor,
            "on_response": lambda response: self._cache_pagination(
                response, next_page_cursor
            ),
        }

        data = self._request(**params)
        pagination = self._pagination_cache.get(next_page_cursor)

        return data, pagination

    def flatten_to_list(self) -> List[Any]:
        """Fetches all pages and returns all items as a single list."""
        all_items = []
        current_items, pagination = self.first_page()

        if current_items:
            all_items.extend(current_items)

        while pagination.has_next_page:
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
