from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class Media:
    """Represents a piece of media, such as a video clip or a thumbnail image, that a device captured for an event. Media is in beta.

    :ivar content_type: MIME type of the media, such as ``video/mp4`` or ``image/jpeg``.

    :ivar created_at: Date and time at which the media was created.

    :ivar device_id: ID of the device that captured the media.

    :ivar event_id: ID of the event that the media belongs to.

    :ivar expires_at: Date and time at which the media stops being available. Null when Seam does not know when the media expires.

    :ivar media_id: ID of the media.

    :ivar media_type: Type of the media: a video clip or a still image.

    :ivar status: Status of the media. ``pending`` means that Seam is still retrieving the media. ``available`` means that ``url`` can be used to download it. ``unavailable`` means that no media exists for the event, and ``failed`` means that Seam could not retrieve it.

    :ivar url: Short-lived URL from which you can download the media. Null unless ``status`` is ``available``. The URL expires after about five minutes. Call ``/media/get`` again for a new URL.

    :ivar video_codec: Video codec used to encode the media. Only present for video media. ``hevc`` (H.265) playback support varies by browser and device, so check compatibility before assuming a clip plays inline.

    :ivar workspace_id: ID of the workspace that contains the media."""

    content_type: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_id: Optional[str]
    expires_at: Optional[str]
    media_id: str
    media_type: Literal["video", "image"]
    status: Literal["pending", "available", "unavailable", "failed"]
    url: Optional[str]
    video_codec: Optional[Literal["h264", "hevc"]]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            content_type=d.get("content_type", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_id=d.get("event_id", None),
            expires_at=d.get("expires_at", None),
            media_id=d.get("media_id", None),
            media_type=d.get("media_type", None),
            status=d.get("status", None),
            url=d.get("url", None),
            video_codec=d.get("video_codec", None),
            workspace_id=d.get("workspace_id", None),
        )
