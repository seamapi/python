from seam import (
    SeamActionAttemptError,
    SeamActionAttemptFailedError,
    SeamActionAttemptTimeoutError,
    SeamError,
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
    SeamInvalidOptionsError,
    SeamInvalidTokenError,
    UnserializableParamError,
)


def test_seam_error_is_the_base_of_every_sdk_error():
    for error_class in [
        SeamHttpApiError,
        SeamHttpUnauthorizedError,
        SeamHttpInvalidInputError,
        SeamActionAttemptError,
        SeamActionAttemptFailedError,
        SeamActionAttemptTimeoutError,
        SeamInvalidOptionsError,
        SeamInvalidTokenError,
        UnserializableParamError,
    ]:
        assert issubclass(error_class, SeamError)


def test_seam_error_catches_an_api_error():
    error = SeamHttpApiError(
        {"type": "device_not_found", "message": "Device not found"},
        404,
        "request-id",
    )

    assert isinstance(error, SeamError)
