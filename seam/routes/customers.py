from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractCustomers, MagicLink


class Customers(AbstractCustomers):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_portal(
        self,
        *,
        features: Optional[Dict[str, Any]] = None,
        is_embedded: Optional[bool] = None,
        customer_data: Optional[Dict[str, Any]] = None
    ) -> MagicLink:
        json_payload = {}

        if features is not None:
            json_payload["features"] = features
        if is_embedded is not None:
            json_payload["is_embedded"] = is_embedded
        if customer_data is not None:
            json_payload["customer_data"] = customer_data

        res = self.client.post("/customers/create_portal", json=json_payload)

        return MagicLink.from_dict(res["magic_link"])

    def push_data(
        self,
        *,
        customer_key: str,
        access_grants: Optional[List[Dict[str, Any]]] = None,
        bookings: Optional[List[Dict[str, Any]]] = None,
        buildings: Optional[List[Dict[str, Any]]] = None,
        common_areas: Optional[List[Dict[str, Any]]] = None,
        facilities: Optional[List[Dict[str, Any]]] = None,
        guests: Optional[List[Dict[str, Any]]] = None,
        listings: Optional[List[Dict[str, Any]]] = None,
        properties: Optional[List[Dict[str, Any]]] = None,
        property_listings: Optional[List[Dict[str, Any]]] = None,
        reservations: Optional[List[Dict[str, Any]]] = None,
        residents: Optional[List[Dict[str, Any]]] = None,
        rooms: Optional[List[Dict[str, Any]]] = None,
        spaces: Optional[List[Dict[str, Any]]] = None,
        tenants: Optional[List[Dict[str, Any]]] = None,
        units: Optional[List[Dict[str, Any]]] = None,
        user_identities: Optional[List[Dict[str, Any]]] = None,
        users: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        json_payload = {}

        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if access_grants is not None:
            json_payload["access_grants"] = access_grants
        if bookings is not None:
            json_payload["bookings"] = bookings
        if buildings is not None:
            json_payload["buildings"] = buildings
        if common_areas is not None:
            json_payload["common_areas"] = common_areas
        if facilities is not None:
            json_payload["facilities"] = facilities
        if guests is not None:
            json_payload["guests"] = guests
        if listings is not None:
            json_payload["listings"] = listings
        if properties is not None:
            json_payload["properties"] = properties
        if property_listings is not None:
            json_payload["property_listings"] = property_listings
        if reservations is not None:
            json_payload["reservations"] = reservations
        if residents is not None:
            json_payload["residents"] = residents
        if rooms is not None:
            json_payload["rooms"] = rooms
        if spaces is not None:
            json_payload["spaces"] = spaces
        if tenants is not None:
            json_payload["tenants"] = tenants
        if units is not None:
            json_payload["units"] = units
        if user_identities is not None:
            json_payload["user_identities"] = user_identities
        if users is not None:
            json_payload["users"] = users

        self.client.post("/customers/push_data", json=json_payload)

        return None
