from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class Pagination:
    """Information about the current page of results.

    :ivar has_next_page: Indicates whether there is another page of results after this one.

    :ivar next_page_cursor: Opaque value that can be used to select the next page of results via the ``page_cursor`` parameter.

    :ivar next_page_url: URL to get the next page of results."""

    has_next_page: bool
    next_page_cursor: Optional[str]
    next_page_url: Optional[str]

    # The payload is decoded JSON, so every value read out of it is untyped.
    # Typing d as Any keeps that at this boundary instead of casting each
    # read, and the dataclass fields carry the real types.
    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            has_next_page=d.get("has_next_page", None),
            next_page_cursor=d.get("next_page_cursor", None),
            next_page_url=d.get("next_page_url", None),
        )
