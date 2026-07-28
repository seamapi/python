from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class InstantKey:
    """Represents a Seam Instant Key. For issuing Bluetooth mobile keys, Instant Keys are the fastest way to share access. With a single API call, you can create a mobile key and send it through text or email or embed it in your own app.

    There’s no app to install, nor account to create. Your user just taps a link and gets a lightweight, native-feeling experience using iOS App Clip or Instant Apps on Android. Further, Instant Keys work offline, so even in areas with poor cellular or Wi-Fi, like elevator banks or concrete-walled hallways, the Instant Keys still work.

    :ivar client_session_id: ID of the client session associated with the Instant Key.
    :vartype client_session_id: str

    :ivar created_at: Date and time at which the Instant Key was created.
    :vartype created_at: str

    :ivar customization: Customization applied to the Instant Key UI.
    :vartype customization: Dict[str, Any]

    :ivar customization_profile_id: ID of the customization profile associated with the Instant Key.
    :vartype customization_profile_id: str

    :ivar expires_at: Date and time at which the Instant Key expires.
    :vartype expires_at: str

    :ivar instant_key_id: ID of the Instant Key.
    :vartype instant_key_id: str

    :ivar instant_key_url: Shareable URL for the Instant Key. Use the URL to deliver the Instant Key to your user through a link in a text message or email or by embedding it in your web app.
    :vartype instant_key_url: str

    :ivar user_identity_id: ID of the user identity associated with the Instant Key.
    :vartype user_identity_id: str

    :ivar workspace_id: ID of the workspace that contains the Instant Key.
    :vartype workspace_id: str"""

    client_session_id: str
    created_at: str
    customization: Dict[str, Any]
    customization_profile_id: str
    expires_at: str
    instant_key_id: str
    instant_key_url: str
    user_identity_id: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return InstantKey(
            client_session_id=d.get("client_session_id", None),
            created_at=d.get("created_at", None),
            customization=DeepAttrDict(d.get("customization", None)),
            customization_profile_id=d.get("customization_profile_id", None),
            expires_at=d.get("expires_at", None),
            instant_key_id=d.get("instant_key_id", None),
            instant_key_url=d.get("instant_key_url", None),
            user_identity_id=d.get("user_identity_id", None),
            workspace_id=d.get("workspace_id", None),
        )
