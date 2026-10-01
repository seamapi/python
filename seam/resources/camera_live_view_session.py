from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class CameraLiveViewSession:
    """Represents a short-lived live view session for a single camera. Use the session ID and token to start a WebRTC stream and to stop the session.

    :ivar camera_live_view_session_id: ID of the camera live view session.

    :ivar device_id: ID of the camera.

    :ivar expires_at: Date and time at which the live view session expires.

    :ivar token: Token that authorizes the offer and stop requests for this session."""

    camera_live_view_session_id: str
    device_id: str
    expires_at: str
    token: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            camera_live_view_session_id=d.get("camera_live_view_session_id", None),
            device_id=d.get("device_id", None),
            expires_at=d.get("expires_at", None),
            token=d.get("token", None),
        )
