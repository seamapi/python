from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .resources import ActionAttempt, ErrorActionAttempt, PendingActionAttempt


@dataclass(frozen=True)
class SeamValidationError:
    """A request parameter that failed validation and its error messages."""

    parameter_name: str
    error_messages: List[str]


class SeamError(Exception):
    """Base exception for all errors raised by the Seam SDK."""


# Webhook
class SeamInvalidWebhookPayloadError(SeamError):
    """
    Exception raised when a webhook payload passes signature verification
    but cannot be read as a Seam event.

    The payload is genuinely from Seam and will never become readable, so
    report it as a bug instead of letting the sender retry it, and do not
    treat it as forgery.
    """


# HTTP
class SeamHttpInvalidResponseError(SeamError):
    """
    Exception raised when a success response from the Seam API has an
    unexpected shape, e.g., a proxy rewrote the body or the expected
    response key is missing.

    :ivar path: The request path that produced the response
    :vartype path: str
    :ivar response_key: The response key the SDK expected to read
    :vartype response_key: str
    """

    def __init__(self, path: str, response_key: str, reason: str):
        """
        :param path: The request path that produced the response
        :type path: str
        :param response_key: The response key the SDK expected to read
        :type response_key: str
        :param reason: Description of how the response diverged
        :type reason: str
        """

        super().__init__(
            f"Seam returned an invalid response for {path}: "
            f'expected "{response_key}", {reason}'
        )
        self.path = path
        self.response_key = response_key


class SeamHttpApiError(SeamError):
    """
    Base exception for Seam HTTP API errors.

    This exception encapsulates details about HTTP errors returned by the Seam API,
    including the error message, error code, HTTP status code, request ID, and any
    additional error data.

    :ivar code: The error type returned by the API
    :vartype code: str
    :ivar status_code: The HTTP status code of the error response
    :vartype status_code: int
    :ivar request_id: The unique identifier for the API request, when the
        response carried one
    :vartype request_id: Optional[str]
    :ivar data: Additional error data, if provided by the API
    :vartype data: Dict[str, Any]
    """

    def __init__(
        self, error: Dict[str, Any], status_code: int, request_id: Optional[str]
    ):
        """
        :param error: Dictionary containing error details from the API response
        :type error: Dict[str, Any]
        :param status_code: HTTP status code of the error response
        :type status_code: int
        :param request_id: Unique identifier for the API request, when the
            response carried one
        :type request_id: Optional[str]
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

    def __init__(self, request_id: Optional[str]):
        """
        :param request_id: Unique identifier for the API request, when the
            response carried one
        :type request_id: Optional[str]
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

    def __init__(
        self, error: Dict[str, Any], status_code: int, request_id: Optional[str]
    ):
        """
        :param error: Dictionary containing error details from the API response
        :type error: Dict[str, Any]
        :param status_code: HTTP status code of the error response
        :type status_code: int
        :param request_id: Unique identifier for the API request, when the
            response carried one
        :type request_id: Optional[str]
        """

        super().__init__(error, status_code, request_id)
        self.code = "invalid_input"
        validation_errors = error.get("validation_errors")
        self._validation_errors = (
            validation_errors if isinstance(validation_errors, dict) else {}
        )

    @property
    def validation_errors(self) -> List[SeamValidationError]:
        """Validation errors, one entry per failed request parameter."""

        return [
            SeamValidationError(
                param_name, self.get_validation_error_messages(param_name)
            )
            for param_name in self._validation_errors
            if param_name != "_errors"
        ]

    def get_validation_error_messages(self, param_name: str) -> List[str]:
        """
        The validation messages for a request parameter, or an empty list when
        that parameter has none.

        :param param_name: Name of the request parameter
        :type param_name: str
        :rtype: List[str]
        """

        messages = self._validation_errors.get(param_name)

        if not isinstance(messages, dict):
            return []

        errors = messages.get("_errors", [])

        return errors if isinstance(errors, list) else []


# Action Attempt
class SeamActionAttemptError(SeamError):
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

    def __init__(self, action_attempt: ErrorActionAttempt):
        """
        :param action_attempt: The failed ActionAttempt object associated with this error
        :type action_attempt: ErrorActionAttempt
        """

        # A failed action attempt carries an error, but reading through it
        # unguarded would raise AttributeError over the actual failure if one
        # ever arrives without it.
        error = action_attempt.error

        super().__init__(
            error.message if error is not None else "Action attempt failed",
            action_attempt,
        )
        self.name = self.__class__.__name__
        self.code = error.type if error is not None else "unknown_error"


class SeamActionAttemptTimeoutError(SeamActionAttemptError):
    """
    Exception raised when a Seam Action Attempt times out while waiting for the action attempt to reach a resolved state.

    This error occurs when the system has waited for the specified timeout period, but the action
    attempt has not reached either a success or failed state within that time.

    :ivar name: Name of the exception class
    :vartype name: str
    """

    def __init__(self, action_attempt: PendingActionAttempt, timeout: float):
        """
        :param action_attempt: The still-pending ActionAttempt object associated with this error
        :type action_attempt: PendingActionAttempt
        :param timeout: The timeout duration in seconds
        :type timeout: float
        """

        message = f"Timed out waiting for action attempt after {timeout}s"
        super().__init__(message, action_attempt)
        self.name = self.__class__.__name__
