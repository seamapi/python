from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Pagination:
    """Information about the current page of results.

    :ivar has_next_page: Indicates whether there is another page of results after this one.
    :vartype has_next_page: bool

    :ivar next_page_cursor: Opaque value that can be used to select the next page of results via the ``page_cursor`` parameter.
    :vartype next_page_cursor: str

    :ivar next_page_url: URL to get the next page of results.
    :vartype next_page_url: str"""

    has_next_page: bool
    next_page_cursor: str
    next_page_url: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Pagination(
            has_next_page=d.get("has_next_page", None),
            next_page_cursor=d.get("next_page_cursor", None),
            next_page_url=d.get("next_page_url", None),
        )
