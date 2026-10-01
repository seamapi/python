from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from .cameras_live_views import (
    AbstractCamerasLiveViews,
    CamerasLiveViews,
    AbstractAsyncCamerasLiveViews,
    AsyncCamerasLiveViews,
)


class AbstractCameras(abc.ABC):

    @property
    @abc.abstractmethod
    def live_views(self) -> AbstractCamerasLiveViews:
        raise NotImplementedError()


class AbstractAsyncCameras(abc.ABC):

    @property
    @abc.abstractmethod
    def live_views(self) -> AbstractAsyncCamerasLiveViews:
        raise NotImplementedError()


class Cameras(AbstractCameras):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._live_views = CamerasLiveViews(client=client, defaults=defaults)

    @property
    def live_views(self) -> CamerasLiveViews:
        return self._live_views


class AsyncCameras(AbstractAsyncCameras):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._live_views = AsyncCamerasLiveViews(client=client, defaults=defaults)

    @property
    def live_views(self) -> AsyncCamerasLiveViews:
        return self._live_views
