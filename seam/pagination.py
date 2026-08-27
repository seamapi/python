from typing import Any, Dict, List, Optional


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


class PaginatedList(List[Any]):
    """A list of results that carries the response's pagination envelope.

    Behaves exactly like the plain list it replaces; the paginator reads
    the ``pagination`` attribute instead of intercepting the response
    through a client-wide event hook.
    """

    def __init__(self, items: List[Any], pagination: Optional[Dict[str, Any]] = None):
        super().__init__(items)
        self.pagination = pagination
