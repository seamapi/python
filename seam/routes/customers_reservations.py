from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractCustomersReservations


class CustomersReservations(AbstractCustomersReservations):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_deep_link(self, *, customer_key: str, reservation_key: str) -> None:
        json_payload = {}

        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if reservation_key is not None:
            json_payload["reservation_key"] = reservation_key

        self.client.post("/customers/reservations/create_deep_link", json=json_payload)

        return None
