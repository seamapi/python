from seam import Seam


def test_webhooks(seam: Seam):
    webhook = seam.webhooks.create(
        url="https://example.com", event_types=["connected_account.connected"]
    )
    assert webhook.url == "https://example.com"

    webhook = seam.webhooks.get(webhook_id=webhook.webhook_id)
    assert webhook is not None

    webhook_list = seam.webhooks.list()
    assert len(webhook_list) > 0

    seam.webhooks.delete(webhook_id=webhook.webhook_id)
    webhook_list = seam.webhooks.list()
    assert len(webhook_list) == 0
