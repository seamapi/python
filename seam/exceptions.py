from typing import Any, Dict
from .routes.models import ActionAttempt


# HTTP
class SeamHttpApiError(Exception):
    """
    Base exception for Seam HTTP API errors.

    This exception encapsulates details about HTTP errors returned by the Seam API,
    including the error message, error code, HTTP status code, request ID, and any
    additional error data.

    :ivar code: The error type returned by the API
    :vartype code: str
    :ivar status_code: The HTTP status code of the error response
    :vartype status_code: int
    :ivar request_id: The unique identifier for the API request
    :vartype request_id: str
    :ivar data: Additional error data, if provided by the API
    :vartype data: Dict[str, Any]
    """

    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        """
        :param error: Dictionary containing error details from the API response
        :type error: Dict[str, Any]
        :param status_code: HTTP status code of the error response
        :type status_code: int
        :param request_id: Unique identifier for the API request
        :type request_id: str
        """

        super().__init__(error.get("message"))
        self.code = error.get("type")
        self.status_code = status_code
        self.request_id = request_id
        self.data = error.get("data")


class SeamHttpUnauthorizedError(SeamHttpApiError):
    """
    Exception raised when the API request is unauthorized.

    This exception is a specific type of SeamHttpApiError for 401 Unauthorized errors.
    """

    def __init__(self, request_id: str):
        """
        :param request_id: Unique identifier for the API request
        :type request_id: str
        """

        super().__init__(
            {"type": "unauthorized", "message": "Unauthorized"}, 401, request_id
        )


class SeamHttpInvalidInputError(SeamHttpApiError):
    """
    Exception raised when the API request contains invalid input params.

    This exception is a specific type of SeamHttpApiError for invalid input param errors.

    :ivar code: "invalid_input" error type
    :vartype code: str
    """

    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        """
        :param error: Dictionary containing error details from the API response
        :type error: Dict[str, Any]
        :param status_code: HTTP status code of the error response
        :type status_code: int
        :param request_id: Unique identifier for the API request
        :type request_id: str
        """

        super().__init__(error, status_code, request_id)
        self.code = "invalid_input"


# Action Attempt
class SeamActionAttemptError(Exception):
    """
    Base exception for Seam Action Attempt errors.

    :ivar name: Name of the exception class
    :vartype name: str
    :ivar action_attempt: The ActionAttempt object associated with this error
    :vartype action_attempt: ActionAttempt
    """

    def __init__(self, message: str, action_attempt: ActionAttempt):
        """
        :param message: Error message
        :type message: str
        :param action_attempt: The ActionAttempt object associated with this error
        :type action_attempt: ActionAttempt
        """

        super().__init__(message)
        self.name = self.__class__.__name__
        self.action_attempt = action_attempt


class SeamActionAttemptFailedError(SeamActionAttemptError):
    """
    Exception raised when a Seam Action Attempt fails.

    :ivar name: Name of the exception class
    :vartype name: str
    :ivar code: The error type from the action attempt
    :vartype code: str
    """

    def __init__(self, action_attempt: ActionAttempt):
        """
        :param action_attempt: The ActionAttempt object associated with this error
        :type action_attempt: ActionAttempt
        """

        super().__init__(action_attempt.error.message, action_attempt)
        self.name = self.__class__.__name__
        self.code = action_attempt.error.type


class SeamActionAttemptTimeoutError(SeamActionAttemptError):
    """
    Exception raised when a Seam Action Attempt times out while waiting for the action attempt to reach a resolved state.

    This error occurs when the system has waited for the specified timeout period, but the action
    attempt has not reached either a success or failed state within that time.

    :ivar name: Name of the exception class
    :vartype name: str
    """

    def __init__(self, action_attempt: ActionAttempt, timeout: str):
        """
        :param action_attempt: The ActionAttempt object associated with this error
        :type action_attempt: ActionAttempt
        :param timeout: The timeout duration in seconds
        :type timeout: str
        """

        message = f"Timed out waiting for action attempt after {timeout}s"
        super().__init__(message, action_attempt)
        self.name = self.__class__.__name__
