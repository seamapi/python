from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


@dataclass
class InstantKey:
    """Represents a Seam Instant Key. For issuing Bluetooth mobile keys, Instant Keys are the fastest way to share access. With a single API call, you can create a mobile key and send it through text or email or embed it in your own app.

    There’s no app to install, nor account to create. Your user just taps a link and gets a lightweight, native-feeling experience using iOS App Clip or Instant Apps on Android. Further, Instant Keys work offline, so even in areas with poor cellular or Wi-Fi, like elevator banks or concrete-walled hallways, the Instant Keys still work.

    :ivar client_session_id: ID of the client session associated with the Instant Key.

    :ivar created_at: Date and time at which the Instant Key was created.

    :ivar customization: Customization applied to the Instant Key UI.

    :ivar customization_profile_id: ID of the customization profile associated with the Instant Key.

    :ivar expires_at: Date and time at which the Instant Key expires.

    :ivar instant_key_id: ID of the Instant Key.

    :ivar instant_key_url: Shareable URL for the Instant Key. Use the URL to deliver the Instant Key to your user through a link in a text message or email or by embedding it in your web app.

    :ivar user_identity_id: ID of the user identity associated with the Instant Key.

    :ivar workspace_id: ID of the workspace that contains the Instant Key."""

    @dataclass
    class Customization(ResourceMapping):
        """Customization applied to the Instant Key UI.

        :ivar logo_url: URL of the logo displayed on the Instant Key.

        :ivar primary_color: Primary color used in the Instant Key UI.

        :ivar secondary_color: Secondary color used in the Instant Key UI."""

        logo_url: Optional[str]
        primary_color: Optional[str]
        secondary_color: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                logo_url=d.get("logo_url", None),
                primary_color=d.get("primary_color", None),
                secondary_color=d.get("secondary_color", None),
            )

    client_session_id: str
    created_at: str
    customization: Optional[Customization]
    customization_profile_id: Optional[str]
    expires_at: str
    instant_key_id: str
    instant_key_url: str
    user_identity_id: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            client_session_id=d.get("client_session_id", None),
            created_at=d.get("created_at", None),
            customization=_object_from_dict(cls.Customization, d.get("customization")),
            customization_profile_id=d.get("customization_profile_id", None),
            expires_at=d.get("expires_at", None),
            instant_key_id=d.get("instant_key_id", None),
            instant_key_url=d.get("instant_key_url", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )
