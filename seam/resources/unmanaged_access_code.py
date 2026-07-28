from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class UnmanagedAccessCode:
    """Represents an [unmanaged smart lock access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes).

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly.

    When you create an access code on a device in Seam, it is created as a managed access code. Access codes that exist on a device that were not created through Seam are considered unmanaged codes. We strictly limit the operations that can be performed on unmanaged codes.

    Prior to using Seam to manage your devices, you may have used another lock management system to manage the access codes on your devices. Where possible, we help you keep any existing access codes on devices and transition those codes to ones managed by your Seam workspace.

    Not all providers support unmanaged access codes. The following providers do not support unmanaged access codes:

    - [Kwikset](https://docs.seam.co/device-and-system-integration-guides/kwikset-locks)

    :ivar access_code_id: Unique identifier for the access code.
    :vartype access_code_id: str

    :ivar cannot_be_managed: Indicates that Seam cannot convert this unmanaged access code to a managed access code. Some providers do not support management of unmanaged access codes through API integrations.
    :vartype cannot_be_managed: bool

    :ivar cannot_delete_unmanaged_access_code: Indicates that Seam cannot delete this unmanaged access code through the provider. If this access code needs to be deleted, it will only be possible from the manufacturer app.
    :vartype cannot_delete_unmanaged_access_code: bool

    :ivar code: Code used for access. Typically, a numeric or alphanumeric string.
    :vartype code: str

    :ivar created_at: Date and time at which the access code was created.
    :vartype created_at: str

    :ivar device_id: Unique identifier for the device associated with the access code.
    :vartype device_id: str

    :ivar dormakaba_oracode_metadata: Metadata for a dormakaba Oracode unmanaged access code. Only present for unmanaged access codes from dormakaba Oracode devices.
    :vartype dormakaba_oracode_metadata: Dict[str, Any]

    :ivar ends_at: Date and time after which the time-bound access code becomes inactive.
    :vartype ends_at: str

    :ivar errors: Errors associated with the [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).
    :vartype errors: List[Dict[str, Any]]

    :ivar is_managed: Indicates that Seam does not manage the access code.
    :vartype is_managed: bool

    :ivar name: Name of the access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes. Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as `first_name` and `last_name`. To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints. To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called `appearance`. This is an object with a `name` property and, optionally, `first_name` and `last_name` properties (for providers that break down a name into components).
    :vartype name: str

    :ivar starts_at: Date and time at which the time-bound access code becomes active.
    :vartype starts_at: str

    :ivar status: Current status of the access code within the operational lifecycle. `set` indicates that the code is active and operational. `unset` indicates that the code exists on the provider but is not usable on the device.
    :vartype status: str

    :ivar type: Type of the access code. `ongoing` access codes are active continuously until deactivated manually. `time_bound` access codes have a specific duration.
    :vartype type: str

    :ivar warnings: Warnings associated with the [access code](https://docs.seam.co/low-level-apis/smart-locks/access-codes).
    :vartype warnings: List[Dict[str, Any]]

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the access code.
    :vartype workspace_id: str"""

    access_code_id: str
    cannot_be_managed: bool
    cannot_delete_unmanaged_access_code: bool
    code: str
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Dict[str, Any]
    ends_at: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    name: str
    starts_at: str
    status: str
    type: str
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return UnmanagedAccessCode(
            access_code_id=d.get("access_code_id", None),
            cannot_be_managed=d.get("cannot_be_managed", None),
            cannot_delete_unmanaged_access_code=d.get(
                "cannot_delete_unmanaged_access_code", None
            ),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=DeepAttrDict(
                d.get("dormakaba_oracode_metadata", None)
            ),
            ends_at=d.get("ends_at", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
