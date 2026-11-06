from functools import wraps
from inspect import iscoroutinefunction
from typing import Any, Callable, Mapping, Tuple, TypeVar, cast

F = TypeVar("F", bound=Callable)


def validate_at_least_one_parameter(
    path: str, parameter_names: Tuple[str, ...], parameters: Mapping[str, Any]
) -> None:
    if parameter_names and all(
        parameters.get(name) is None for name in parameter_names
    ):
        raise ValueError(f"At least one parameter is required for {path}")


def route_metadata(
    *,
    path: str,
    has_pagination: bool,
    at_least_one_parameter_names: Tuple[str, ...] = (),
):
    """Attach generated route metadata to a request callable."""

    def decorate(request: F) -> F:
        if iscoroutinefunction(request):

            @wraps(request)
            async def validated_request(*args, **kwargs):
                validate_at_least_one_parameter(
                    path, at_least_one_parameter_names, kwargs
                )
                return await request(*args, **kwargs)

        else:

            @wraps(request)
            def validated_request(*args, **kwargs):
                validate_at_least_one_parameter(
                    path, at_least_one_parameter_names, kwargs
                )
                return request(*args, **kwargs)

        # Functions do not declare these attributes, so set them through Any.
        route = cast(Any, validated_request)
        route.__seam_path__ = path
        route.__seam_has_pagination__ = has_pagination
        route.__seam_at_least_one_parameter_names__ = at_least_one_parameter_names
        return cast(F, validated_request)

    return decorate
