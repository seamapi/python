from typing import Dict
from svix import Webhook
from .routes.models import SeamEvent


class SeamWebhook:
    """
    A class to handle Seam webhook verification.

    This class provides functionality to verify incoming webhook payloads
    using the Svix library.
    """

    def __init__(self, secret: str):
        """
        Initialize the SeamWebhook instance.

        Args:
            secret (str): The secret key used for webhook verification.
        """
        self._webhook = Webhook(secret)

    def verify(self, payload: str, headers: Dict[str, str]) -> SeamEvent:
        """
        Verify the incoming webhook payload and headers.

        This method normalizes the headers, verifies the payload using the Svix
        Webhook instance, and returns a SeamEvent object.

        Args:
            payload (str): The webhook payload as a string.
            headers (Dict[str, str]): A dictionary of HTTP headers.

        Returns:
            SeamEvent: An instance of SeamEvent created from the verified payload.

        Raises:
            Any exceptions raised by the Svix Webhook.verify() method.
        """
        normalized_headers = {k.lower(): v for k, v in headers.items()}
        res = self._webhook.verify(payload, normalized_headers)

        return SeamEvent.from_dict(res)
