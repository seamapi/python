import time
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from typing import FrozenSet, Optional

import httpx

# Methods safe to retry by default. The Seam API is POST-only, so pass
# allowed_methods=["POST"] to opt in to retrying API requests on status.
DEFAULT_ALLOWED_METHODS = frozenset(
    ["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
)

# Statuses retried when the response includes a Retry-After header,
# even if they are not in the status_forcelist.
RETRY_AFTER_STATUS_CODES = frozenset([413, 429, 503])

# Never sleep longer than this between attempts, in seconds.
BACKOFF_MAX = 120


@dataclass(frozen=True)
class Retry:
    """Retry behavior for failed requests.

    The fields mirror urllib3.util.Retry, which previous SDK versions
    accepted for the retries option.

    :ivar total: Number of retries allowed after the initial request.
        Set to 0 to disable retries.
    :ivar backoff_factor: Sleep backoff_factor * (2 ** retry_number)
        seconds between attempts, where retry_number starts at 0.
    :ivar status_forcelist: Response status codes to retry.
    :ivar allowed_methods: HTTP methods eligible for retry on status.
        Connection errors are always eligible, as the request never
        reached the server. Pass None to allow all methods.
    :ivar respect_retry_after_header: Honor the Retry-After header on
        413, 429, and 503 responses.
    """

    total: int = 10
    backoff_factor: float = 0
    status_forcelist: Optional[FrozenSet[int]] = None
    allowed_methods: Optional[FrozenSet[str]] = DEFAULT_ALLOWED_METHODS
    respect_retry_after_header: bool = True

    def __post_init__(self):
        if self.status_forcelist is not None:
            object.__setattr__(
                self, "status_forcelist", frozenset(self.status_forcelist)
            )
        if self.allowed_methods is not None:
            object.__setattr__(
                self,
                "allowed_methods",
                frozenset(method.upper() for method in self.allowed_methods),
            )

    def is_retryable_response(self, method: str, response: httpx.Response) -> bool:
        if (
            self.allowed_methods is not None
            and method.upper() not in self.allowed_methods
        ):
            return False

        if (
            self.status_forcelist is not None
            and response.status_code in self.status_forcelist
        ):
            return True

        return (
            self.respect_retry_after_header
            and "retry-after" in response.headers
            and response.status_code in RETRY_AFTER_STATUS_CODES
        )

    def get_backoff_time(self, retry_number: int) -> float:
        return min(BACKOFF_MAX, self.backoff_factor * (2**retry_number))


class RetryTransport(httpx.BaseTransport):
    """Transport that retries requests according to a Retry configuration."""

    def __init__(self, retries: Retry, transport: Optional[httpx.BaseTransport] = None):
        self.retries = retries
        self.transport = transport if transport is not None else httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        retries_left = self.retries.total
        retry_number = 0

        while True:
            try:
                response = self.transport.handle_request(request)
            except (httpx.ConnectError, httpx.ConnectTimeout):
                if retries_left <= 0:
                    raise
                retry_after = None
            else:
                if retries_left <= 0 or not self.retries.is_retryable_response(
                    request.method, response
                ):
                    return response
                retry_after = parse_retry_after(response)
                response.close()

            self._sleep(retry_number, retry_after)
            retries_left -= 1
            retry_number += 1

    def close(self) -> None:
        self.transport.close()

    def _sleep(self, retry_number: int, retry_after: Optional[float]) -> None:
        backoff = self.retries.get_backoff_time(retry_number)

        if retry_after is not None and self.retries.respect_retry_after_header:
            backoff = max(backoff, min(BACKOFF_MAX, retry_after))

        if backoff > 0:
            time.sleep(backoff)


def parse_retry_after(response: httpx.Response) -> Optional[float]:
    retry_after = response.headers.get("retry-after")

    if retry_after is None:
        return None

    if retry_after.isdigit():
        return float(retry_after)

    try:
        retry_date = parsedate_to_datetime(retry_after)
    except (TypeError, ValueError):
        return None

    return max(0.0, retry_date.timestamp() - time.time())
