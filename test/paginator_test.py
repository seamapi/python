from seam import Seam


def test_paginator_first_page(seam: Seam):
    paginator = seam.create_paginator(seam.connected_accounts.list, {"limit": 2})
    connected_accounts, pagination = paginator.first_page()

    assert isinstance(connected_accounts, list)
    assert len(connected_accounts) == 2
    assert pagination is not None
    assert pagination.has_next_page is True
    assert pagination.next_page_cursor is not None
    assert pagination.next_page_url is not None


def test_paginator_next_page(seam: Seam):
    paginator = seam.create_paginator(seam.connected_accounts.list, {"limit": 2})
    first_page_accounts, first_pagination = paginator.first_page()

    assert len(first_page_accounts) == 2
    assert first_pagination.has_next_page is True

    next_page_accounts, _ = paginator.next_page(first_pagination.next_page_cursor)

    assert isinstance(next_page_accounts, list)
    assert len(next_page_accounts) == 1


def test_paginator_flatten_to_list(seam: Seam):
    all_connected_accounts = seam.connected_accounts.list()

    paginator = seam.create_paginator(seam.connected_accounts.list, {"limit": 1})
    paginated_accounts = paginator.flatten_to_list()

    assert len(paginated_accounts) > 1
    assert len(paginated_accounts) == len(all_connected_accounts)


def test_paginator_flatten(seam: Seam):
    all_connected_accounts = seam.connected_accounts.list()

    paginator = seam.create_paginator(seam.connected_accounts.list, {"limit": 1})

    collected_accounts = []
    for account in paginator.flatten():
        collected_accounts.append(account)

    assert len(collected_accounts) > 1
    assert len(collected_accounts) == len(all_connected_accounts)
