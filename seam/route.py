from typing import Callable, TypeVar


F = TypeVar("F", bound=Callable)


def route_metadata(*, path: str, has_required_parameters: bool, has_pagination: bool):
    """Attach generated route metadata to a request callable."""

    def decorate(request: F) -> F:
        request.__seam_path__ = path
        request.__seam_has_required_parameters__ = has_required_parameters
        request.__seam_has_pagination__ = has_pagination
        return request

    return decorate
