from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


@dataclass
class Pagination:
    """Information about the current page of results.

    :ivar has_next_page: Indicates whether there is another page of results after this one.

    :ivar next_page_cursor: Opaque value that can be used to select the next page of results via the ``page_cursor`` parameter.

    :ivar next_page_url: URL to get the next page of results."""

    has_next_page: bool
    next_page_cursor: Optional[str]
    next_page_url: Optional[str]

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            has_next_page=d.get("has_next_page", None),
            next_page_cursor=d.get("next_page_cursor", None),
            next_page_url=d.get("next_page_url", None),
        )
