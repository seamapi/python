from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Batch:
    """A batch of workspace resources.

    :ivar access_codes: Represents a smart lock [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly. Using the Seam Access Code API, you can easily generate access codes on the hundreds of door lock models with which we integrate.

    Seam supports programming two types of access codes: [ongoing](https://docs.seam.co/low-level-apis/smart-locks/access-codes#ongoing-access-codes) and [time-bound](https://docs.seam.co/low-level-apis/smart-locks/access-codes#time-bound-access-codes). To differentiate between the two, refer to the `type` property of the access code. Ongoing codes display as `ongoing`, whereas time-bound codes are labeled `time_bound`. An ongoing access code is active, until it has been removed from the device. To specify an ongoing access code, leave both `starts_at` and `ends_at` empty. A time-bound access code will be programmed at the `starts_at` time and removed at the `ends_at` time.

    In addition, for certain devices, Seam also supports [offline access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes#offline-access-codes). Offline access (PIN) codes are designed for door locks that might not always maintain an internet connection. For this type of access code, the device manufacturer uses encryption keys (tokens) to create server-based registries of algorithmically-generated offline PIN codes. Because the tokens remain synchronized with the managed devices, the locks do not require an active internet connection—and you do not need to be near the locks—to create an offline access code. Then, owners or managers can share these offline codes with users through a variety of mechanisms, such as messaging applications. That is, lock users do not need to install a smartphone application to receive an offline access code.

    For granting a person access to a space, [Access Grants](https://docs.seam.co/use-cases/granting-access) are the default and recommended approach and work across both standalone smart locks and access systems. Use the lower-level Access Codes API directly only when you specifically need to manage individual PIN codes.
    :vartype access_codes: List[Dict[str, Any]]

    :ivar access_grants: Represents an Access Grant. Access Grants enable you to grant a user identity access to spaces, entrances, and devices through one or more access methods, such as mobile keys, plastic cards, and PIN codes. You can create an Access Grant for an existing user identity, or you can create a new user identity *while* creating the new Access Grant.
    :vartype access_grants: List[Dict[str, Any]]

    :ivar access_methods: Represents an access method for an Access Grant. Access methods describe the modes of access, such as PIN codes, plastic cards, and mobile keys. For a mobile key, the access method also stores the URL for the associated Instant Key.
    :vartype access_methods: List[Dict[str, Any]]

    :ivar acs_access_groups: Group that defines the entrances to which a set of users has access and, in some cases, the access schedule for these entrances and users.

    Some access control systems use [access group](https://docs.seam.co/low-level-apis/access-systems/user-management/assigning-users-to-access-groups), which are sets of users, combined with sets of permissions. These permissions include both the set of areas or assets that the users can access and the schedule during which the users can access these areas or assets. Instead of assigning access rights individually to each access control system user, which can be time-consuming and error-prone, administrators can assign users to an access group, thereby ensuring that the users inherit all the permissions associated with the access group. Using access groups streamlines the process of managing large numbers of access control system users, especially in bigger organizations or complexes.

    To learn whether your access control system supports access groups, see the corresponding [system integration guide](https://docs.seam.co/device-and-system-integration-guides#access-control-systems).
    :vartype acs_access_groups: List[Dict[str, Any]]

    :ivar acs_credentials: Means by which an [access control system user](https://docs.seam.co/low-level-apis/access-systems/user-management) gains access at an [entrance](https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details). The `acs_credential` object represents a [credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) that provides an ACS user access within an [access control system](https://docs.seam.co/low-level-apis/access-systems).

    An access control system generally uses digital means of access to authorize a user trying to get through a specific entrance. Examples of credentials include plastic key cards, mobile keys, biometric identifiers, and PIN codes. The electronic nature of these credentials, as well as the fact that access is centralized, enables both the rapid provisioning and rescinding of access and the ability to compile access audit logs.

    For each `acs_credential`, you define the access method. You can also specify additional properties, such as a PIN code, depending on the credential type.

    For granting a person access to a space, [Access Grants](https://docs.seam.co/use-cases/granting-access) are the default and recommended approach. Use the lower-level ACS credential API directly only when you specifically need to manage individual credentials.
    :vartype acs_credentials: List[Dict[str, Any]]

    :ivar acs_encoders: Represents a hardware device that encodes [credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) data onto physical cards within an [access control system](https://docs.seam.co/low-level-apis/access-systems).

    Some access control systems require credentials to be encoded onto plastic key cards using a card encoder. This process involves the following two key steps:

    1. Credential creation
       Configure the access parameters for the credential.
    2. Card encoding
       Write the credential data onto the card using a compatible card encoder.

    Separately, the Seam API also supports card scanning, which enables you to scan and read the encoded data on a card. You can use this action to confirm consistency with access control system records or diagnose discrepancies if needed.

    See [Working with Card Encoders and Scanners](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

    To verify if your access control system requires a card encoder, see the corresponding [system integration guide](https://docs.seam.co/device-and-system-integration-guides#access-control-systems).
    :vartype acs_encoders: List[Dict[str, Any]]

    :ivar acs_entrances: Represents an [entrance](https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details) within an [access control system](https://docs.seam.co/low-level-apis/access-systems).

    In an access control system, an entrance is a secured door, gate, zone, or other method of entry. You can list details for all the `acs_entrance` resources in your workspace or get these details for a specific `acs_entrance`. You can also list all entrances associated with a specific credential, and you can list all credentials associated with a specific entrance.
    :vartype acs_entrances: List[Dict[str, Any]]

    :ivar acs_systems: Represents an [access control system](https://docs.seam.co/low-level-apis/access-systems).

    Within an `acs_system`, create [`acs_user`s](https://docs.seam.co/api/acs/users/object) and [`acs_credential`s](https://docs.seam.co/api/acs/credentials/object) to grant access to the `acs_user`s.

    For details about the resources associated with an access control system, see the [access control systems namespace](https://docs.seam.co/api/acs).
    :vartype acs_systems: List[Dict[str, Any]]

    :ivar acs_users: Represents a [user](https://docs.seam.co/low-level-apis/access-systems/user-management) in an [access system](https://docs.seam.co/low-level-apis/access-systems).

    An access system user typically refers to an individual who requires access, like an employee or resident. Each user can possess multiple credentials that serve as their keys or identifiers for access. The type of credential can vary widely. For example, in the Salto system, a user can have a PIN code, a mobile app account, and a fob. In other platforms, it is not uncommon for a user to have more than one of the same credential type, such as multiple key cards. Additionally, these credentials can have a schedule or validity period.

    For details about how to configure users in your access system, see the corresponding [system integration guide](https://docs.seam.co/device-and-system-integration-guides#access-control-systems).
    :vartype acs_users: List[Dict[str, Any]]

    :ivar action_attempts: Represents an action attempt that enables you to keep track of the progress of your action that affects a physical device or system.actions against a device. Action attempts are useful because the physical world is intrinsically asynchronous.

    When you request for a device to perform an action, the Seam API immediately returns an action attempt object. In the background, the Seam API performs the action.

    See also [Action Attempts](https://docs.seam.co/core-concepts/action-attempts).
    :vartype action_attempts: List[Dict[str, Any]]

    :ivar client_sessions: Represents a [client session](https://docs.seam.co/core-concepts/authentication/client-session-tokens). If you want to restrict your users' access to their own devices, use client sessions.

    You create each client session with a custom `user_identifier_key`. Normally, the `user_identifier_key` is a user ID that your application provides.

    When calling the Seam API from your backend using an API key, you can pass the `user_identifier_key` as a parameter to limit results to the associated client session. For example, `/devices/list?user_identifier_key=123` only returns devices associated with the client session created with the `user_identifier_key` `123`.

    A client session has a token that you can use with the Seam JavaScript SDK to make requests from the client (browser) directly to the Seam API. The token restricts the user's access to only the devices that they own.

    See also [Get Started with React](https://docs.seam.co/ui-components/overview/getting-started-with-seam-components/get-started-with-react-components-and-client-session-tokens).
    :vartype client_sessions: List[Dict[str, Any]]

    :ivar connect_webviews: Represents a [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews).

    Connect Webviews are fully-embedded client-side components that you add to your app. Your users interact with your embedded Connect Webviews to link their IoT device or system accounts to Seam. That is, Connect Webviews walk your users through the process of logging in to their device or system accounts. Seam handles all the authentication steps, and—once your user has completed the authorization through your app—you can access and control their devices or systems using the Seam API.

    Connect Webviews perform credential validation, multifactor authentication (when applicable), and error handling for each brand that Seam supports. Further, Connect Webviews work across all modern browsers and platforms, including Chrome, Safari, and Firefox.

    To enable a user to connect their device or system account to Seam through your app, first create a `connect_webview`. Once created, this `connect_webview` includes a URL that you can use to open an [iframe](https://www.w3schools.com/html/html_iframe.asp) or new window containing the Connect Webview for your user.

    When you create a Connect Webview, specify the desired provider category key in the `provider_category` parameter. Alternately, to specify a list of providers explicitly, use the `accepted_providers` parameter with a list of device provider keys.

    To list all providers within a category, use `/devices/list_device_providers` with the desired `provider_category` filter. To list all provider keys, use `/devices/list_device_providers` with no filters.
    :vartype connect_webviews: List[Dict[str, Any]]

    :ivar connected_accounts: Represents a [connected account](https://docs.seam.co/core-concepts/connected-accounts). A connected account is an external third-party account to which your user has authorized Seam to get access, for example, an August account with a list of door locks.
    :vartype connected_accounts: List[Dict[str, Any]]

    :ivar devices: Represents a [device](https://docs.seam.co/core-concepts/devices) that has been connected to Seam.
    :vartype devices: List[Dict[str, Any]]

    :ivar events: Represents an event. Events let you know when something interesting happens in your workspace. For example, when a lock is unlocked, Seam creates a `lock.unlocked` event. When a device's battery level is low, Seam creates a `device.battery_low` event.

    As with other API resources, you can retrieve an individual event or a list of events. Seam also provides a separate webhook system for sending the event objects directly to an endpoint on your sever. Manage webhooks through [Seam Console](https://console.seam.co). You can also use the webhooks sandbox in Seam Console to see the different payloads for each event and test them against your own endpoints.
    :vartype events: List[Dict[str, Any]]

    :ivar instant_keys: Represents a Seam Instant Key. For issuing Bluetooth mobile keys, Instant Keys are the fastest way to share access. With a single API call, you can create a mobile key and send it through text or email or embed it in your own app.

    There’s no app to install, nor account to create. Your user just taps a link and gets a lightweight, native-feeling experience using iOS App Clip or Instant Apps on Android. Further, Instant Keys work offline, so even in areas with poor cellular or Wi-Fi, like elevator banks or concrete-walled hallways, the Instant Keys still work.
    :vartype instant_keys: List[Dict[str, Any]]

    :ivar noise_thresholds: Represents a [noise threshold](https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings) for a [noise sensor](https://docs.seam.co/capability-guides/noise-sensors). Thresholds represent the limits of noise tolerated at a property, which can be customized for each hour of the day. Each device has its own default thresholds, but you can use the Seam API to modify them.
    :vartype noise_thresholds: List[Dict[str, Any]]

    :ivar spaces: Represents a space that is a logical grouping of devices and entrances. You can assign access to an entire space, thereby making granting access more efficient.
    :vartype spaces: List[Dict[str, Any]]

    :ivar thermostat_daily_programs: Represents a thermostat daily program, consisting of a set of periods, each of which has a starting time and the key that identifies the climate preset to apply at the starting time.
    :vartype thermostat_daily_programs: List[Dict[str, Any]]

    :ivar thermostat_schedules: Represents a [thermostat schedule](https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules) that activates a configured [climate preset](https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets) on a [thermostat](https://docs.seam.co/capability-guides/thermostats) at a specified starting time and deactivates the climate preset at a specified ending time.
    :vartype thermostat_schedules: List[Dict[str, Any]]

    :ivar unmanaged_access_codes: Represents an [unmanaged smart lock access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes).

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly.

    When you create an access code on a device in Seam, it is created as a managed access code. Access codes that exist on a device that were not created through Seam are considered unmanaged codes. We strictly limit the operations that can be performed on unmanaged codes.

    Prior to using Seam to manage your devices, you may have used another lock management system to manage the access codes on your devices. Where possible, we help you keep any existing access codes on devices and transition those codes to ones managed by your Seam workspace.

    Not all providers support unmanaged access codes. The following providers do not support unmanaged access codes:

    - [Kwikset](https://docs.seam.co/device-and-system-integration-guides/kwikset-locks)
    :vartype unmanaged_access_codes: List[Dict[str, Any]]

    :ivar unmanaged_devices: Represents an [unmanaged device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices). An unmanaged device has a limited set of visible properties and a subset of supported events. You cannot control an unmanaged device. Any [access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes) on an unmanaged device are unmanaged. To control an unmanaged device with Seam, [convert it to a managed device](https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices#convert-an-unmanaged-device-to-managed).
    :vartype unmanaged_devices: List[Dict[str, Any]]

    :ivar user_identities: Represents a [user identity](https://docs.seam.co/capability-guides/mobile-access/managing-mobile-app-user-accounts-with-user-identities#what-is-a-user-identity) associated with an application user account.
    :vartype user_identities: List[Dict[str, Any]]

    :ivar workspaces: Represents a Seam [workspace](https://docs.seam.co/core-concepts/workspaces). A workspace is a top-level entity that encompasses all other resources below it, such as devices, connected accounts, and Connect Webviews. Seam provides two types of workspaces. A [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces) is a special type of workspace designed for testing code. Sandbox workspaces offer test device accounts and virtual devices that you can connect and control. This ability to work with virtual devices is quite handy because it removes the need to own physical devices from multiple brands. To connect real devices and systems to Seam, use a [production workspace](https://docs.seam.co/core-concepts/workspaces#production-workspaces).
    :vartype workspaces: List[Dict[str, Any]]"""

    access_codes: List[Dict[str, Any]]
    access_grants: List[Dict[str, Any]]
    access_methods: List[Dict[str, Any]]
    acs_access_groups: List[Dict[str, Any]]
    acs_credentials: List[Dict[str, Any]]
    acs_encoders: List[Dict[str, Any]]
    acs_entrances: List[Dict[str, Any]]
    acs_systems: List[Dict[str, Any]]
    acs_users: List[Dict[str, Any]]
    action_attempts: List[Dict[str, Any]]
    client_sessions: List[Dict[str, Any]]
    connect_webviews: List[Dict[str, Any]]
    connected_accounts: List[Dict[str, Any]]
    devices: List[Dict[str, Any]]
    events: List[Dict[str, Any]]
    instant_keys: List[Dict[str, Any]]
    noise_thresholds: List[Dict[str, Any]]
    spaces: List[Dict[str, Any]]
    thermostat_daily_programs: List[Dict[str, Any]]
    thermostat_schedules: List[Dict[str, Any]]
    unmanaged_access_codes: List[Dict[str, Any]]
    unmanaged_devices: List[Dict[str, Any]]
    user_identities: List[Dict[str, Any]]
    workspaces: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Batch(
            access_codes=d.get("access_codes", None),
            access_grants=d.get("access_grants", None),
            access_methods=d.get("access_methods", None),
            acs_access_groups=d.get("acs_access_groups", None),
            acs_credentials=d.get("acs_credentials", None),
            acs_encoders=d.get("acs_encoders", None),
            acs_entrances=d.get("acs_entrances", None),
            acs_systems=d.get("acs_systems", None),
            acs_users=d.get("acs_users", None),
            action_attempts=d.get("action_attempts", None),
            client_sessions=d.get("client_sessions", None),
            connect_webviews=d.get("connect_webviews", None),
            connected_accounts=d.get("connected_accounts", None),
            devices=d.get("devices", None),
            events=d.get("events", None),
            instant_keys=d.get("instant_keys", None),
            noise_thresholds=d.get("noise_thresholds", None),
            spaces=d.get("spaces", None),
            thermostat_daily_programs=d.get("thermostat_daily_programs", None),
            thermostat_schedules=d.get("thermostat_schedules", None),
            unmanaged_access_codes=d.get("unmanaged_access_codes", None),
            unmanaged_devices=d.get("unmanaged_devices", None),
            user_identities=d.get("user_identities", None),
            workspaces=d.get("workspaces", None),
        )
