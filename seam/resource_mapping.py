"""Mapping compatibility for generated nested resource dataclasses."""

from typing import Any, ClassVar, Iterator


class ResourceMapping:
    """Provide legacy dictionary-style reads for a nested resource object."""

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self, key, default)

    def __contains__(self, key: object) -> bool:
        return isinstance(key, str) and key in self.__dataclass_fields__

    def __iter__(self) -> Iterator[str]:
        return iter(self.keys())

    def keys(self) -> Iterator[str]:
        return iter(self.__dataclass_fields__)

    __dataclass_fields__: ClassVar[dict[str, Any]]
