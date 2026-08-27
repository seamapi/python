from json import JSONDecodeError
from typing import Dict

from svix.webhooks import Webhook

from .exceptions import SeamInvalidWebhookPayloadError
from .resources import SeamEvent, seam_event_from_dict


class SeamWebhook:
    """Verifies and parses incoming Seam webhook events using the Svix library.

    Verification failures raise svix's ``WebhookVerificationError``, which is
    re-exported as ``SeamWebhookVerificationError``. A verified payload that
    is not a readable event raises ``SeamInvalidWebhookPayloadError``.
    """

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
        :raises SeamWebhookVerificationError: If the webhook signature
            verification fails. Respond with an error status so the sender
            retries.
        :raises SeamInvalidWebhookPayloadError: If the payload is correctly
            signed but cannot be read as a Seam event. The payload will never
            become readable, so report it as a bug instead of letting the
            sender retry it.
        """
        normalized_headers = {str(key).lower(): value for key, value in headers.items()}

        try:
            res = self._webhook.verify(payload, normalized_headers)
        except JSONDecodeError as error:
            # The signature already checked out, so the payload is genuinely
            # from Seam but permanently unreadable.
            raise SeamInvalidWebhookPayloadError(
                f"The verified webhook payload is not valid JSON: {error}"
            ) from error

        if (
            not isinstance(res, dict)
            or not isinstance(res.get("event_id"), str)
            or not isinstance(res.get("event_type"), str)
        ):
            raise SeamInvalidWebhookPayloadError(
                "The verified webhook payload did not contain a Seam event"
            )

        return seam_event_from_dict(res)
