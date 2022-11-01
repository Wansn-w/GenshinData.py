from urllib.parse import urlparse, urljoin
from pathlib import Path
from os.path import join
from io import FileIO

import asyncfile
import httpx


class Loader(object):
    def __call__(self, path: str):
        ...

    def __truediv__(self, other):  # /
        ...


class HttpLoader(Loader):
    def __init__(self, base: str):
        self.client = httpx.AsyncClient(base_url=base)

    async def __call__(self, path: str, *args, **kwargs):
        __resp = await self.client.get(path, *args, **kwargs)
        return __resp


class Provider:
    def __init__(self, base_url: str, cache: bool = True):
        self.parsed = urlparse(base_url)
        self.use_cache = cache

        if self.parsed.scheme in ['http', 'https']:
            async with httpx.AsyncClient() as client:
                __resp = await client.get(self.url)
                self.content = __resp.content
