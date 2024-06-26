from typing import Any, Dict
from niquests import Response
from .routes.models import ActionAttempt


# HTTP
class SeamHttpApiError(Exception):
    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        super().__init__(error["message"])
        self.code = error["type"]
        self.status_code = status_code
        self.request_id = request_id
        self.data = error.get("data")


class SeamHttpUnauthorizedError(SeamHttpApiError):
    def __init__(self, request_id: str):
        super().__init__(
            {"type": "unauthorized", "message": "Unauthorized"}, 401, request_id
        )


class SeamHttpInvalidInputError(SeamHttpApiError):
    def __init__(self, error: Dict[str, Any], status_code: int, request_id: str):
        super().__init__(error, status_code, request_id)
        self.code = "invalid_input"


# Action Attempt
class SeamActionAttemptError(Exception):
    def __init__(self, message: str, action_attempt: ActionAttempt):
        super().__init__(message)
        self.name = self.__class__.__name__
        self.action_attempt = action_attempt


class SeamActionAttemptFailedError(SeamActionAttemptError):
    def __init__(self, action_attempt: ActionAttempt):
        super().__init__(action_attempt.error.message, action_attempt)
        self.name = self.__class__.__name__
        self.code = action_attempt.error.type


class SeamActionAttemptTimeoutError(SeamActionAttemptError):
    def __init__(self, action_attempt: ActionAttempt, timeout: str):
        message = f"Timed out waiting for action attempt after {timeout}s"
        super().__init__(message, action_attempt)
        self.name = self.__class__.__name__
