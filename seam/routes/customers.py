from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import CustomerPortal


class AbstractCustomers(abc.ABC):

    @abc.abstractmethod
    def create_portal(
        self,
        *,
        customer_resources_filters: Optional[List[Dict[str, Any]]] = None,
        customization_profile_id: Optional[str] = None,
        deep_link: Optional[Dict[str, Any]] = None,
        exclude_locale_picker: Optional[bool] = None,
        features: Optional[Dict[str, Any]] = None,
        is_embedded: Optional[bool] = None,
        landing_page: Optional[Dict[str, Any]] = None,
        locale: Optional[str] = None,
        navigation_mode: Optional[str] = None,
        read_only: Optional[bool] = None,
        customer_data: Optional[Dict[str, Any]] = None,
    ) -> CustomerPortal:
        """Creates a new customer portal magic link with configurable features.

        :param customer_resources_filters: Filter configuration for resources based on their custom_metadata. Each filter specifies a field, operation, and value to match against resource custom_metadata.

        :param customization_profile_id: The ID of the customization profile to use for the portal.

        :param deep_link: Deep link target resource for initial redirect. When set, the portal will navigate directly to the specified resource.

        :param exclude_locale_picker: Whether to exclude the option to select a locale within the portal UI.

        :param features:

        :param is_embedded: Whether the portal is embedded in another application.

        :param landing_page: Configuration for the landing page when the portal loads.

        :param locale: The locale to use for the portal.

        :param navigation_mode: Navigation mode for the portal. 'restricted' tells frontend to hide navigation UI, typically used for embedded deep links.

        :param read_only: Whether the portal is read-only. When true, the customer can browse the portal but cannot perform any mutating action; write requests made with the portal's client session are rejected.

        :param customer_data:

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
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
        staff_member_keys: Optional[List[str]] = None,
        tenant_keys: Optional[List[str]] = None,
        unit_keys: Optional[List[str]] = None,
        user_identity_keys: Optional[List[str]] = None,
        user_keys: Optional[List[str]] = None,
    ) -> None:
        """Deletes customer data including resources like spaces, properties, rooms, users, etc.
        This will delete the partner resources and any related Seam resources (user identities, access grants, spaces).

        :param access_grant_keys: List of access grant keys to delete.

        :param booking_keys: List of booking keys to delete.

        :param building_keys: List of building keys to delete.

        :param common_area_keys: List of common area keys to delete.

        :param customer_keys: List of customer keys to delete all data for.

        :param facility_keys: List of facility keys to delete.

        :param guest_keys: List of guest keys to delete.

        :param listing_keys: List of listing keys to delete.

        :param property_keys: List of property keys to delete.

        :param property_listing_keys: List of property listing keys to delete.

        :param reservation_keys: List of reservation keys to delete.

        :param resident_keys: List of resident keys to delete.

        :param room_keys: List of room keys to delete.

        :param space_keys: List of space keys to delete.

        :param staff_member_keys: List of staff member keys to delete.

        :param tenant_keys: List of tenant keys to delete.

        :param unit_keys: List of unit keys to delete.

        :param user_identity_keys: List of user identity keys to delete.

        :param user_keys: List of user keys to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
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
        sites: Optional[List[Dict[str, Any]]] = None,
        spaces: Optional[List[Dict[str, Any]]] = None,
        staff_members: Optional[List[Dict[str, Any]]] = None,
        tenants: Optional[List[Dict[str, Any]]] = None,
        units: Optional[List[Dict[str, Any]]] = None,
        user_identities: Optional[List[Dict[str, Any]]] = None,
        users: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        """Pushes customer data including resources like spaces, properties, rooms, users, etc.

        :param customer_key: Your unique identifier for the customer.

        :param access_grants: List of access grants.

        :param bookings: List of bookings.

        :param buildings: List of buildings.

        :param common_areas: List of shared common areas.

        :param facilities: List of gym or fitness facilities.

        :param guests: List of guests.

        :param listings: List of property listings.

        :param properties: List of short-term rental properties.

        :param property_listings: List of property listings.

        :param reservations: List of reservations.

        :param residents: List of residents.

        :param rooms: List of hotel or hospitality rooms.

        :param sites: List of general sites or areas.

        :param spaces: List of general spaces or areas.

        :param staff_members: List of staff members.

        :param tenants: List of tenants.

        :param units: List of multi-family residential units.

        :param user_identities: List of user identities.

        :param users: List of users."""
        raise NotImplementedError()


class Customers(AbstractCustomers):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_portal(
        self,
        *,
        customer_resources_filters: Optional[List[Dict[str, Any]]] = None,
        customization_profile_id: Optional[str] = None,
        deep_link: Optional[Dict[str, Any]] = None,
        exclude_locale_picker: Optional[bool] = None,
        features: Optional[Dict[str, Any]] = None,
        is_embedded: Optional[bool] = None,
        landing_page: Optional[Dict[str, Any]] = None,
        locale: Optional[str] = None,
        navigation_mode: Optional[str] = None,
        read_only: Optional[bool] = None,
        customer_data: Optional[Dict[str, Any]] = None,
    ) -> CustomerPortal:
        """Creates a new customer portal magic link with configurable features.

        :param customer_resources_filters: Filter configuration for resources based on their custom_metadata. Each filter specifies a field, operation, and value to match against resource custom_metadata.

        :param customization_profile_id: The ID of the customization profile to use for the portal.

        :param deep_link: Deep link target resource for initial redirect. When set, the portal will navigate directly to the specified resource.

        :param exclude_locale_picker: Whether to exclude the option to select a locale within the portal UI.

        :param features:

        :param is_embedded: Whether the portal is embedded in another application.

        :param landing_page: Configuration for the landing page when the portal loads.

        :param locale: The locale to use for the portal.

        :param navigation_mode: Navigation mode for the portal. 'restricted' tells frontend to hide navigation UI, typically used for embedded deep links.

        :param read_only: Whether the portal is read-only. When true, the customer can browse the portal but cannot perform any mutating action; write requests made with the portal's client session are rejected.

        :param customer_data:

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if customer_resources_filters is not None:
            json_payload["customer_resources_filters"] = customer_resources_filters
        if customization_profile_id is not None:
            json_payload["customization_profile_id"] = customization_profile_id
        if deep_link is not None:
            json_payload["deep_link"] = deep_link
        if exclude_locale_picker is not None:
            json_payload["exclude_locale_picker"] = exclude_locale_picker
        if features is not None:
            json_payload["features"] = features
        if is_embedded is not None:
            json_payload["is_embedded"] = is_embedded
        if landing_page is not None:
            json_payload["landing_page"] = landing_page
        if locale is not None:
            json_payload["locale"] = locale
        if navigation_mode is not None:
            json_payload["navigation_mode"] = navigation_mode
        if read_only is not None:
            json_payload["read_only"] = read_only
        if customer_data is not None:
            json_payload["customer_data"] = customer_data

        res = self.client.post("/customers/create_portal", json=json_payload)

        return CustomerPortal.from_dict(res["customer_portal"])

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
        staff_member_keys: Optional[List[str]] = None,
        tenant_keys: Optional[List[str]] = None,
        unit_keys: Optional[List[str]] = None,
        user_identity_keys: Optional[List[str]] = None,
        user_keys: Optional[List[str]] = None,
    ) -> None:
        """Deletes customer data including resources like spaces, properties, rooms, users, etc.
        This will delete the partner resources and any related Seam resources (user identities, access grants, spaces).

        :param access_grant_keys: List of access grant keys to delete.

        :param booking_keys: List of booking keys to delete.

        :param building_keys: List of building keys to delete.

        :param common_area_keys: List of common area keys to delete.

        :param customer_keys: List of customer keys to delete all data for.

        :param facility_keys: List of facility keys to delete.

        :param guest_keys: List of guest keys to delete.

        :param listing_keys: List of listing keys to delete.

        :param property_keys: List of property keys to delete.

        :param property_listing_keys: List of property listing keys to delete.

        :param reservation_keys: List of reservation keys to delete.

        :param resident_keys: List of resident keys to delete.

        :param room_keys: List of room keys to delete.

        :param space_keys: List of space keys to delete.

        :param staff_member_keys: List of staff member keys to delete.

        :param tenant_keys: List of tenant keys to delete.

        :param unit_keys: List of unit keys to delete.

        :param user_identity_keys: List of user identity keys to delete.

        :param user_keys: List of user keys to delete."""
        json_payload: Dict[str, Any] = {}

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
        if staff_member_keys is not None:
            json_payload["staff_member_keys"] = staff_member_keys
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
        sites: Optional[List[Dict[str, Any]]] = None,
        spaces: Optional[List[Dict[str, Any]]] = None,
        staff_members: Optional[List[Dict[str, Any]]] = None,
        tenants: Optional[List[Dict[str, Any]]] = None,
        units: Optional[List[Dict[str, Any]]] = None,
        user_identities: Optional[List[Dict[str, Any]]] = None,
        users: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        """Pushes customer data including resources like spaces, properties, rooms, users, etc.

        :param customer_key: Your unique identifier for the customer.

        :param access_grants: List of access grants.

        :param bookings: List of bookings.

        :param buildings: List of buildings.

        :param common_areas: List of shared common areas.

        :param facilities: List of gym or fitness facilities.

        :param guests: List of guests.

        :param listings: List of property listings.

        :param properties: List of short-term rental properties.

        :param property_listings: List of property listings.

        :param reservations: List of reservations.

        :param residents: List of residents.

        :param rooms: List of hotel or hospitality rooms.

        :param sites: List of general sites or areas.

        :param spaces: List of general spaces or areas.

        :param staff_members: List of staff members.

        :param tenants: List of tenants.

        :param units: List of multi-family residential units.

        :param user_identities: List of user identities.

        :param users: List of users."""
        json_payload: Dict[str, Any] = {}

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
        if sites is not None:
            json_payload["sites"] = sites
        if spaces is not None:
            json_payload["spaces"] = spaces
        if staff_members is not None:
            json_payload["staff_members"] = staff_members
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
