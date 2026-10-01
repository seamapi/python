from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import Media as MediaResource
from ..response import unwrap


class AbstractMedia(abc.ABC):

    @abc.abstractmethod
    def get(
        self, *, media_id: str, format: Optional[Literal["json", "redirect"]] = None
    ) -> MediaResource:
        """Returns a specified piece of media, such as a video clip or thumbnail image captured for a camera event, with a short-lived URL from which you can download it. Camera events list their media in ``media_ids``. This endpoint is in beta.

        :param media_id: ID of the media that you want to get.

        :param format: Response format. ``json`` returns the media object. ``redirect`` responds with a ``302`` redirect to the media's download URL, so you can use this endpoint directly as the source of an image or video.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncMedia(abc.ABC):

    @abc.abstractmethod
    async def get(
        self, *, media_id: str, format: Optional[Literal["json", "redirect"]] = None
    ) -> MediaResource:
        """Returns a specified piece of media, such as a video clip or thumbnail image captured for a camera event, with a short-lived URL from which you can download it. Camera events list their media in ``media_ids``. This endpoint is in beta.

        :param media_id: ID of the media that you want to get.

        :param format: Response format. ``json`` returns the media object. ``redirect`` responds with a ``302`` redirect to the media's download URL, so you can use this endpoint directly as the source of an image or video.

        :returns: OK"""
        raise NotImplementedError()


class Media(AbstractMedia):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/media/get", at_least_one_parameter_names=(), has_pagination=False
    )
    def get(
        self, *, media_id: str, format: Optional[Literal["json", "redirect"]] = None
    ) -> MediaResource:
        """Returns a specified piece of media, such as a video clip or thumbnail image captured for a camera event, with a short-lived URL from which you can download it. Camera events list their media in ``media_ids``. This endpoint is in beta.

        :param media_id: ID of the media that you want to get.

        :param format: Response format. ``json`` returns the media object. ``redirect`` responds with a ``302`` redirect to the media's download URL, so you can use this endpoint directly as the source of an image or video.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if media_id is not None:
            params["media_id"] = media_id
        if format is not None:
            params["format"] = format

        res = self.client.get("/media/get", params=params)

        return MediaResource.from_dict(unwrap(res, "media", "/media/get"))


class AsyncMedia(AbstractAsyncMedia):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/media/get", at_least_one_parameter_names=(), has_pagination=False
    )
    async def get(
        self, *, media_id: str, format: Optional[Literal["json", "redirect"]] = None
    ) -> MediaResource:
        """Returns a specified piece of media, such as a video clip or thumbnail image captured for a camera event, with a short-lived URL from which you can download it. Camera events list their media in ``media_ids``. This endpoint is in beta.

        :param media_id: ID of the media that you want to get.

        :param format: Response format. ``json`` returns the media object. ``redirect`` responds with a ``302`` redirect to the media's download URL, so you can use this endpoint directly as the source of an image or video.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if media_id is not None:
            params["media_id"] = media_id
        if format is not None:
            params["format"] = format

        res = await self.client.get("/media/get", params=params)

        return MediaResource.from_dict(unwrap(res, "media", "/media/get"))
