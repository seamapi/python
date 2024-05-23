from niquests import Response
from .routes.models import ActionAttempt


# HTTP
class SeamHttpApiError(Exception):
    def __init__(
        self,
        response: Response,
    ):
        self.status_code = response.status_code
        self.request_id = response.headers.get("seam-request-id", None)

        self.metadata = None
        if "application/json" in response.headers["content-type"]:
            parsed_response = response.json()
            self.metadata = parsed_response.get("error", None)

        super().__init__(
            f"SeamApiException: status={self.status_code}, request_id={self.request_id}, metadata={self.metadata}"
        )


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
