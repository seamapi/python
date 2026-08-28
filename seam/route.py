from typing import Any, Callable, Tuple, TypeVar, cast

F = TypeVar("F", bound=Callable)


def route_metadata(
    *,
    path: str,
    has_pagination: bool,
    at_least_one_parameter_names: Tuple[str, ...] = (),
):
    """Attach generated route metadata to a request callable."""

    def decorate(request: F) -> F:
        # Functions do not declare these attributes, so set them through Any.
        route = cast(Any, request)
        route.__seam_path__ = path
        route.__seam_has_pagination__ = has_pagination
        route.__seam_at_least_one_parameter_names__ = at_least_one_parameter_names
        return request

    return decorate
