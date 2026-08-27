from typing import Any, Dict, List, Optional

from .resources.pagination import Pagination

__all__ = ["PaginatedList", "Pagination"]


class PaginatedList(List[Any]):
    """A list of results that carries the response's pagination envelope.

    Behaves exactly like the plain list it replaces; the paginator reads
    the ``pagination`` attribute instead of intercepting the response
    through a client-wide event hook.
    """

    def __init__(self, items: List[Any], pagination: Optional[Dict[str, Any]] = None):
        super().__init__(items)
        self.pagination = pagination
