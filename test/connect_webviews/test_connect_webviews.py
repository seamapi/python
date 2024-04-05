from seam import Seam


def test_connect_webviews(seam: Seam):
    created_webview = seam.connect_webviews.create(accepted_providers=["schlage"])
    assert created_webview.url is not None

    webview = seam.connect_webviews.get(
        connect_webview_id=created_webview.connect_webview_id
    )
    assert webview.connect_webview_id == created_webview.connect_webview_id

    webviews = seam.connect_webviews.list()
    assert len(webviews) > 0

    # Test with provider_category
    new_webview = seam.connect_webviews.create(provider_category="stable")
    assert created_webview.url is not None

    webview = seam.connect_webviews.get(
        connect_webview_id=new_webview.connect_webview_id
    )
    assert len(webview.accepted_providers) > 0
