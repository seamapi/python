from seam.types import ActionAttempt


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
