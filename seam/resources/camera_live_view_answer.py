from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class CameraLiveViewAnswer:
    """Represents the WebRTC SDP answer that starts streaming video from a camera for a live view session.

    :ivar sdp_answer: WebRTC SDP answer for the offer, limited to 64 KiB of UTF-8 data.
    """

    sdp_answer: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            sdp_answer=d.get("sdp_answer", None),
        )
