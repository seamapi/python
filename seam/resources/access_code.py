from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class AccessCode:
    """Represents a smart lock [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly. Using the Seam Access Code API, you can easily generate access codes on the hundreds of door lock models with which we integrate.

    Seam supports programming two types of access codes: [ongoing](https://docs.seam.co/low-level-apis/smart-locks/access-codes#ongoing-access-codes) and [time-bound](https://docs.seam.co/low-level-apis/smart-locks/access-codes#time-bound-access-codes). To differentiate between the two, refer to the `type` property of the access code. Ongoing codes display as `ongoing`, whereas time-bound codes are labeled `time_bound`. An ongoing access code is active, until it has been removed from the device. To specify an ongoing access code, leave both `starts_at` and `ends_at` empty. A time-bound access code will be programmed at the `starts_at` time and removed at the `ends_at` time.

    In addition, for certain devices, Seam also supports [offline access codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes#offline-access-codes). Offline access (PIN) codes are designed for door locks that might not always maintain an internet connection. For this type of access code, the device manufacturer uses encryption keys (tokens) to create server-based registries of algorithmically-generated offline PIN codes. Because the tokens remain synchronized with the managed devices, the locks do not require an active internet connection—and you do not need to be near the locks—to create an offline access code. Then, owners or managers can share these offline codes with users through a variety of mechanisms, such as messaging applications. That is, lock users do not need to install a smartphone application to receive an offline access code.

    For granting a person access to a space, [Access Grants](https://docs.seam.co/use-cases/granting-access) are the default and recommended approach and work across both standalone smart locks and access systems. Use the lower-level Access Codes API directly only when you specifically need to manage individual PIN codes.

    :ivar access_code_id: Unique identifier for the access code.
    :vartype access_code_id: str

    :ivar code: Code used for access. Typically, a numeric or alphanumeric string.
    :vartype code: str

    :ivar common_code_key: Unique identifier for a group of access codes that share the same code.
    :vartype common_code_key: str

    :ivar created_at: Date and time at which the access code was created.
    :vartype created_at: str

    :ivar device_id: Unique identifier for the device associated with the access code.
    :vartype device_id: str

    :ivar dormakaba_oracode_metadata: Metadata for a dormakaba Oracode managed access code. Only present for access codes from dormakaba Oracode devices.
    :vartype dormakaba_oracode_metadata: Dict[str, Any]

    :ivar ends_at: Date and time after which the time-bound access code becomes inactive.
    :vartype ends_at: str

    :ivar errors: Errors associated with the [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).
    :vartype errors: List[Dict[str, Any]]

    :ivar is_backup: Indicates whether the access code is a backup code.
    :vartype is_backup: bool

    :ivar is_backup_access_code_available: Indicates whether a backup access code is available for use if the primary access code is lost or compromised.
    :vartype is_backup_access_code_available: bool

    :ivar is_external_modification_allowed: Indicates whether changes to the access code from external sources are permitted.
    :vartype is_external_modification_allowed: bool

    :ivar is_managed: Indicates whether Seam manages the access code.
    :vartype is_managed: bool

    :ivar is_offline_access_code: Indicates whether the access code is intended for use in offline scenarios. If `true`, this code can be created on a device without a network connection.
    :vartype is_offline_access_code: bool

    :ivar is_one_time_use: Indicates whether the access code can only be used once. If `true`, the code becomes invalid after the first use.
    :vartype is_one_time_use: bool

    :ivar is_scheduled_on_device: Indicates whether the code is set on the device according to a preconfigured schedule.
    :vartype is_scheduled_on_device: bool

    :ivar is_waiting_for_code_assignment: Indicates whether the access code is waiting for a code assignment.
    :vartype is_waiting_for_code_assignment: bool

    :ivar name: Name of the access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes. Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as `first_name` and `last_name`. To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints. To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called `appearance`. This is an object with a `name` property and, optionally, `first_name` and `last_name` properties (for providers that break down a name into components).
    :vartype name: str

    :ivar pending_mutations: Collection of pending mutations for the access code. Indicates changes that Seam is in the process of pushing to the device.
    :vartype pending_mutations: List[Dict[str, Any]]

    :ivar pulled_backup_access_code_id: Identifier of the pulled backup access code. Used to associate the pulled backup access code with the original access code.
    :vartype pulled_backup_access_code_id: str

    :ivar starts_at: Date and time at which the time-bound access code becomes active.
    :vartype starts_at: str

    :ivar status: Current status of the access code within the operational lifecycle. Values are `setting`, a transitional phase that indicates that the code is being configured or activated; `set`, which indicates that the code is active and operational; `unset`, which indicates a deactivated or unused state, either before activation or after deliberate deactivation; `removing`, which indicates a transitional period in which the code is being deleted or made inactive; and `unknown`, which indicates an indeterminate state, due to reasons such as system errors or incomplete data, that highlights a potential need for system review or troubleshooting. See also [Lifecycle of Access Codes](https://docs.seam.co/low-level-apis/smart-locks/access-codes/lifecycle-of-access-codes).
    :vartype status: str

    :ivar type: Type of the access code. `ongoing` access codes are active continuously until deactivated manually. `time_bound` access codes have a specific duration.
    :vartype type: str

    :ivar warnings: Warnings associated with the [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).
    :vartype warnings: List[Dict[str, Any]]

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the access code.
    :vartype workspace_id: str"""

    access_code_id: str
    code: str
    common_code_key: str
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Dict[str, Any]
    ends_at: str
    errors: List[Dict[str, Any]]
    is_backup: bool
    is_backup_access_code_available: bool
    is_external_modification_allowed: bool
    is_managed: bool
    is_offline_access_code: bool
    is_one_time_use: bool
    is_scheduled_on_device: bool
    is_waiting_for_code_assignment: bool
    name: str
    pending_mutations: List[Dict[str, Any]]
    pulled_backup_access_code_id: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return AccessCode(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            common_code_key=d.get("common_code_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=DeepAttrDict(
                d.get("dormakaba_oracode_metadata", None)
            ),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_backup=d.get("is_backup", None),
            is_backup_access_code_available=d.get(
                "is_backup_access_code_available", None
            ),
            is_external_modification_allowed=d.get(
                "is_external_modification_allowed", None
            ),
            is_managed=d.get("is_managed", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            is_waiting_for_code_assignment=d.get(
                "is_waiting_for_code_assignment", None
            ),
            name=d.get("name", None),
            pending_mutations=d.get("pending_mutations", None),
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
