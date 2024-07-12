from typing import Dict
from svix.webhooks import Webhook
from .routes.models import SeamEvent


class SeamWebhook:
    """Verifies and parses incoming Seam webhook events using the Svix library."""

    def __init__(self, secret: str):
        """
        :param secret: The secret key used for webhook verification.
        :type secret: str
        """
        self._webhook = Webhook(secret)

    def verify(self, payload: str, headers: Dict[str, str]) -> SeamEvent:
        """Verify and parse an incoming HTTP webhook request.

        Normalizes the headers, verifies the payload using the Svix
        Webhook instance, and returns a SeamEvent object.

        :param payload: The raw HTTP request body.
        :type payload: str
        :param headers: The HTTP request headers.
        :type headers: Dict[str, str]
        :return: The SeamEvent object created from the verified payload.
        :rtype: SeamEvent
        :raises WebhookVerificationError: If the webhook signature verification fails.
        """
        normalized_headers = {k.lower(): v for k, v in headers.items()}
        res = self._webhook.verify(payload, normalized_headers)

        return SeamEvent.from_dict(res)
