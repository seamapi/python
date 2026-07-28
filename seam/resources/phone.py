from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Phone:
    """Represents an app user's mobile phone.

    :ivar created_at: Date and time at which the phone was created.
    :vartype created_at: str

    :ivar custom_metadata: Optional [custom metadata](https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device) for the phone.
    :vartype custom_metadata: Dict[str, Any]

    :ivar device_id: ID of the phone.
    :vartype device_id: str

    :ivar device_type: Type of the phone device, such as `ios_phone` or `android_phone`.
    :vartype device_type: str

    :ivar display_name: Display name of the phone. Defaults to `nickname` (if it is set) or `properties.appearance.name`, otherwise. Enables administrators and users to identify the phone easily, especially when there are numerous phones.
    :vartype display_name: str

    :ivar errors: Errors associated with the phone.
    :vartype errors: List[Dict[str, Any]]

    :ivar nickname: Optional nickname to describe the phone, settable through Seam.
    :vartype nickname: str

    :ivar properties: Properties of the phone.
    :vartype properties: Dict[str, Any]

    :ivar warnings: Warnings associated with the phone.
    :vartype warnings: List[Dict[str, Any]]

    :ivar workspace_id: ID of the workspace that contains the phone.
    :vartype workspace_id: str"""

    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_type: str
    display_name: str
    errors: List[Dict[str, Any]]
    nickname: str
    properties: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Phone(
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            nickname=d.get("nickname", None),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
