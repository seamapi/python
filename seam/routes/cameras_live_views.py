from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import CameraLiveViewSession, CameraLiveViewAnswer
from ..response import unwrap


class AbstractCamerasLiveViews(abc.ABC):

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        duration_seconds: Optional[int] = None,
        include_audio: Optional[bool] = None,
    ) -> CameraLiveViewSession:
        """Creates a short-lived live view session for a single camera. Pass the returned session ID and token to ``/cameras/live_views/offer`` to start a WebRTC stream, and to ``/cameras/live_views/stop`` to end the session.

        Camera live view is in beta. To enable it for your workspace, contact Seam support. To check whether a camera supports live view, use ``device.can_stream_live_video``.

        :param device_id: ID of the camera to view.

        :param duration_seconds: Number of seconds for which the live view session is valid, up to 600.

        :param include_audio: Indicates whether to include the camera's audio.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def offer(
        self, *, camera_live_view_session_id: str, sdp_offer: str, token: str
    ) -> CameraLiveViewAnswer:
        """Exchanges a WebRTC SDP offer for an SDP answer that starts streaming video from the camera, for a live view session that you created using ``/cameras/live_views/create``.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param sdp_offer: WebRTC SDP offer from the viewer, limited to 64 KiB of UTF-8 data.

        :param token: Token returned when the camera live view session was created.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def stop(self, *, camera_live_view_session_id: str, token: str) -> None:
        """Stops a camera live view session that the current client session owns.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param token: Token returned when the camera live view session was created."""
        raise NotImplementedError()


class AbstractAsyncCamerasLiveViews(abc.ABC):

    @abc.abstractmethod
    async def create(
        self,
        *,
        device_id: str,
        duration_seconds: Optional[int] = None,
        include_audio: Optional[bool] = None,
    ) -> CameraLiveViewSession:
        """Creates a short-lived live view session for a single camera. Pass the returned session ID and token to ``/cameras/live_views/offer`` to start a WebRTC stream, and to ``/cameras/live_views/stop`` to end the session.

        Camera live view is in beta. To enable it for your workspace, contact Seam support. To check whether a camera supports live view, use ``device.can_stream_live_video``.

        :param device_id: ID of the camera to view.

        :param duration_seconds: Number of seconds for which the live view session is valid, up to 600.

        :param include_audio: Indicates whether to include the camera's audio.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def offer(
        self, *, camera_live_view_session_id: str, sdp_offer: str, token: str
    ) -> CameraLiveViewAnswer:
        """Exchanges a WebRTC SDP offer for an SDP answer that starts streaming video from the camera, for a live view session that you created using ``/cameras/live_views/create``.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param sdp_offer: WebRTC SDP offer from the viewer, limited to 64 KiB of UTF-8 data.

        :param token: Token returned when the camera live view session was created.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def stop(self, *, camera_live_view_session_id: str, token: str) -> None:
        """Stops a camera live view session that the current client session owns.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param token: Token returned when the camera live view session was created."""
        raise NotImplementedError()


class CamerasLiveViews(AbstractCamerasLiveViews):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/cameras/live_views/create",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def create(
        self,
        *,
        device_id: str,
        duration_seconds: Optional[int] = None,
        include_audio: Optional[bool] = None,
    ) -> CameraLiveViewSession:
        """Creates a short-lived live view session for a single camera. Pass the returned session ID and token to ``/cameras/live_views/offer`` to start a WebRTC stream, and to ``/cameras/live_views/stop`` to end the session.

        Camera live view is in beta. To enable it for your workspace, contact Seam support. To check whether a camera supports live view, use ``device.can_stream_live_video``.

        :param device_id: ID of the camera to view.

        :param duration_seconds: Number of seconds for which the live view session is valid, up to 600.

        :param include_audio: Indicates whether to include the camera's audio.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if duration_seconds is not None:
            json_payload["duration_seconds"] = duration_seconds
        if include_audio is not None:
            json_payload["include_audio"] = include_audio

        res = self.client.post("/cameras/live_views/create", json=json_payload)

        return CameraLiveViewSession.from_dict(
            unwrap(res, "camera_live_view_session", "/cameras/live_views/create")
        )

    @route_metadata(
        path="/cameras/live_views/offer",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def offer(
        self, *, camera_live_view_session_id: str, sdp_offer: str, token: str
    ) -> CameraLiveViewAnswer:
        """Exchanges a WebRTC SDP offer for an SDP answer that starts streaming video from the camera, for a live view session that you created using ``/cameras/live_views/create``.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param sdp_offer: WebRTC SDP offer from the viewer, limited to 64 KiB of UTF-8 data.

        :param token: Token returned when the camera live view session was created.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if camera_live_view_session_id is not None:
            json_payload["camera_live_view_session_id"] = camera_live_view_session_id
        if sdp_offer is not None:
            json_payload["sdp_offer"] = sdp_offer
        if token is not None:
            json_payload["token"] = token

        res = self.client.post("/cameras/live_views/offer", json=json_payload)

        return CameraLiveViewAnswer.from_dict(
            unwrap(res, "camera_live_view_answer", "/cameras/live_views/offer")
        )

    @route_metadata(
        path="/cameras/live_views/stop",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def stop(self, *, camera_live_view_session_id: str, token: str) -> None:
        """Stops a camera live view session that the current client session owns.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param token: Token returned when the camera live view session was created."""
        json_payload: Dict[str, Any] = {}

        if camera_live_view_session_id is not None:
            json_payload["camera_live_view_session_id"] = camera_live_view_session_id
        if token is not None:
            json_payload["token"] = token

        self.client.post("/cameras/live_views/stop", json=json_payload)

        return None


class AsyncCamerasLiveViews(AbstractAsyncCamerasLiveViews):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/cameras/live_views/create",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def create(
        self,
        *,
        device_id: str,
        duration_seconds: Optional[int] = None,
        include_audio: Optional[bool] = None,
    ) -> CameraLiveViewSession:
        """Creates a short-lived live view session for a single camera. Pass the returned session ID and token to ``/cameras/live_views/offer`` to start a WebRTC stream, and to ``/cameras/live_views/stop`` to end the session.

        Camera live view is in beta. To enable it for your workspace, contact Seam support. To check whether a camera supports live view, use ``device.can_stream_live_video``.

        :param device_id: ID of the camera to view.

        :param duration_seconds: Number of seconds for which the live view session is valid, up to 600.

        :param include_audio: Indicates whether to include the camera's audio.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if duration_seconds is not None:
            json_payload["duration_seconds"] = duration_seconds
        if include_audio is not None:
            json_payload["include_audio"] = include_audio

        res = await self.client.post("/cameras/live_views/create", json=json_payload)

        return CameraLiveViewSession.from_dict(
            unwrap(res, "camera_live_view_session", "/cameras/live_views/create")
        )

    @route_metadata(
        path="/cameras/live_views/offer",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def offer(
        self, *, camera_live_view_session_id: str, sdp_offer: str, token: str
    ) -> CameraLiveViewAnswer:
        """Exchanges a WebRTC SDP offer for an SDP answer that starts streaming video from the camera, for a live view session that you created using ``/cameras/live_views/create``.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param sdp_offer: WebRTC SDP offer from the viewer, limited to 64 KiB of UTF-8 data.

        :param token: Token returned when the camera live view session was created.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if camera_live_view_session_id is not None:
            json_payload["camera_live_view_session_id"] = camera_live_view_session_id
        if sdp_offer is not None:
            json_payload["sdp_offer"] = sdp_offer
        if token is not None:
            json_payload["token"] = token

        res = await self.client.post("/cameras/live_views/offer", json=json_payload)

        return CameraLiveViewAnswer.from_dict(
            unwrap(res, "camera_live_view_answer", "/cameras/live_views/offer")
        )

    @route_metadata(
        path="/cameras/live_views/stop",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def stop(self, *, camera_live_view_session_id: str, token: str) -> None:
        """Stops a camera live view session that the current client session owns.

        Camera live view is in beta. To enable it for your workspace, contact Seam support.

        :param camera_live_view_session_id: ID of the camera live view session.

        :param token: Token returned when the camera live view session was created."""
        json_payload: Dict[str, Any] = {}

        if camera_live_view_session_id is not None:
            json_payload["camera_live_view_session_id"] = camera_live_view_session_id
        if token is not None:
            json_payload["token"] = token

        await self.client.post("/cameras/live_views/stop", json=json_payload)

        return None
