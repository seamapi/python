from typing import Any, Dict
from .routes.models import ActionAttempt


# HTTP
class SeamHttpApiError(Exception):
    """
    Base exception for Seam HTTP API errors.

    This exception encapsulates details about HTTP errors returned by the Seam API,
    including the error message, error code, HTTP status code, request ID, and any
    additional error data.

    :param error: Dictionary containing error details from the API response
    :type error: Dict[str, Any]
    :param status_code: HTTP status code of the error response
    :type status_code: int
    :param request_id: Unique identifier for the API request
    :type request_id: str

    :ivar code: The error type returned by the API
    :ivar status_code: The HTTP status code of the error response
    :ivar request_id: The unique identifier for the API request
    :ivar data: Additional error data, if provided by the API
    """

    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        super().__init__(error.get("message"))
        self.code = error.get("type")
        self.status_code = status_code
        self.request_id = request_id
        self.data = error.get("data")


class SeamHttpUnauthorizedError(SeamHttpApiError):
    """
    Exception raised when the API request is unauthorized.

    This exception is a specific type of SeamHttpApiError for 401 Unauthorized errors.

    :param request_id: Unique identifier for the API request
    :type request_id: str
    """

    def __init__(self, request_id: str):
        super().__init__(
            {"type": "unauthorized", "message": "Unauthorized"}, 401, request_id
        )


class SeamHttpInvalidInputError(SeamHttpApiError):
    """
    Exception raised when the API request contains invalid input params.

    This exception is a specific type of SeamHttpApiError for invalid input param errors.

    :param error: Dictionary containing error details from the API response
    :type error: Dict[str, Any]
    :param status_code: HTTP status code of the error response
    :type status_code: int
    :param request_id: Unique identifier for the API request
    :type request_id: str
    """

    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        super().__init__(error, status_code, request_id)
        self.code = "invalid_input"


# Action Attempt
class SeamActionAttemptError(Exception):
    """
    Base exception for Seam Action Attempt errors.

    :param message: Error message
    :type message: str
    :param action_attempt: The ActionAttempt object associated with this error
    :type action_attempt: ActionAttempt

    :ivar name: Name of the exception class
    :ivar action_attempt: The ActionAttempt object associated with this error
    """

    def __init__(self, message: str, action_attempt: ActionAttempt):
        super().__init__(message)
        self.name = self.__class__.__name__
        self.action_attempt = action_attempt


class SeamActionAttemptFailedError(SeamActionAttemptError):
    """
    Exception raised when a Seam Action Attempt fails.

    :param action_attempt: The ActionAttempt object associated with this error
    :type action_attempt: ActionAttempt

    :ivar name: Name of the exception class
    :ivar code: The error type from the action attempt
    """

    def __init__(self, action_attempt: ActionAttempt):
        super().__init__(action_attempt.error.message, action_attempt)
        self.name = self.__class__.__name__
        self.code = action_attempt.error.type


class SeamActionAttemptTimeoutError(SeamActionAttemptError):
    def __init__(self, action_attempt: ActionAttempt, timeout: str):
        message = f"Timed out waiting for action attempt after {timeout}s"
        super().__init__(message, action_attempt)
        self.name = self.__class__.__name__
