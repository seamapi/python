from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable)


def route_metadata(*, path: str, has_required_parameters: bool, has_pagination: bool):
    """Attach generated route metadata to a request callable."""

    def decorate(request: F) -> F:
        # Functions do not declare these attributes, so set them through Any.
        route = cast(Any, request)
        route.__seam_path__ = path
        route.__seam_has_required_parameters__ = has_required_parameters
        route.__seam_has_pagination__ = has_pagination
        return request

    return decorate
