from seam import Seam, SeamHttpApiError

EMAIL = "john@example.com"


def test_connected_accounts(seam: Seam):

    connected_accounts = seam.connected_accounts.list()
    assert len(connected_accounts) > 0

    connected_account_id = connected_accounts[0].connected_account_id
    connected_account = seam.connected_accounts.get(
        connected_account_id=connected_account_id
    )
    email_account = seam.connected_accounts.get(email=EMAIL)

    assert connected_account.connected_account_id == connected_account_id
    assert email_account.connected_account_id == connected_account_id

    deleted_account = seam.connected_accounts.delete(
        connected_account_id=connected_account_id
    )
    assert deleted_account == None

    # Assert that an Exception is raised for the .get() method when
    # connected_account and email parameters are not provided.
    try:
        seam.connected_accounts.get()
    except SeamHttpApiError as e:
        assert e.metadata["message"] == "Invalid input"
