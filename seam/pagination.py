class Pagination:
    def __init__(
        self,
        has_next_page: bool,
        next_page_cursor: str | None,
        next_page_url: str | None,
    ):
        self.has_next_page = has_next_page
        self.next_page_cursor = next_page_cursor
        self.next_page_url = next_page_url
