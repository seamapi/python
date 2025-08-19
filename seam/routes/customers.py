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
        landing_page: Optional[Dict[str, Any]] = None,
        customer_data: Optional[Dict[str, Any]] = None
    ) -> MagicLink:
        json_payload = {}

        if features is not None:
            json_payload["features"] = features
        if is_embedded is not None:
            json_payload["is_embedded"] = is_embedded
        if landing_page is not None:
            json_payload["landing_page"] = landing_page
        if customer_data is not None:
            json_payload["customer_data"] = customer_data

        res = self.client.post("/customers/create_portal", json=json_payload)

        return MagicLink.from_dict(res["magic_link"])

    def delete_data(
        self,
        *,
        access_grant_keys: Optional[List[str]] = None,
        booking_keys: Optional[List[str]] = None,
        building_keys: Optional[List[str]] = None,
        common_area_keys: Optional[List[str]] = None,
        customer_keys: Optional[List[str]] = None,
        facility_keys: Optional[List[str]] = None,
        guest_keys: Optional[List[str]] = None,
        listing_keys: Optional[List[str]] = None,
        property_keys: Optional[List[str]] = None,
        property_listing_keys: Optional[List[str]] = None,
        reservation_keys: Optional[List[str]] = None,
        resident_keys: Optional[List[str]] = None,
        room_keys: Optional[List[str]] = None,
        space_keys: Optional[List[str]] = None,
        tenant_keys: Optional[List[str]] = None,
        unit_keys: Optional[List[str]] = None,
        user_identity_keys: Optional[List[str]] = None,
        user_keys: Optional[List[str]] = None
    ) -> None:
        json_payload = {}

        if access_grant_keys is not None:
            json_payload["access_grant_keys"] = access_grant_keys
        if booking_keys is not None:
            json_payload["booking_keys"] = booking_keys
        if building_keys is not None:
            json_payload["building_keys"] = building_keys
        if common_area_keys is not None:
            json_payload["common_area_keys"] = common_area_keys
        if customer_keys is not None:
            json_payload["customer_keys"] = customer_keys
        if facility_keys is not None:
            json_payload["facility_keys"] = facility_keys
        if guest_keys is not None:
            json_payload["guest_keys"] = guest_keys
        if listing_keys is not None:
            json_payload["listing_keys"] = listing_keys
        if property_keys is not None:
            json_payload["property_keys"] = property_keys
        if property_listing_keys is not None:
            json_payload["property_listing_keys"] = property_listing_keys
        if reservation_keys is not None:
            json_payload["reservation_keys"] = reservation_keys
        if resident_keys is not None:
            json_payload["resident_keys"] = resident_keys
        if room_keys is not None:
            json_payload["room_keys"] = room_keys
        if space_keys is not None:
            json_payload["space_keys"] = space_keys
        if tenant_keys is not None:
            json_payload["tenant_keys"] = tenant_keys
        if unit_keys is not None:
            json_payload["unit_keys"] = unit_keys
        if user_identity_keys is not None:
            json_payload["user_identity_keys"] = user_identity_keys
        if user_keys is not None:
            json_payload["user_keys"] = user_keys

        self.client.post("/customers/delete_data", json=json_payload)

        return None

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
