from time import time
from asyncio import gather
from typing import Coroutine

from loguru import logger
from httpx import Response, AsyncClient, Request

from core.consts import RETRY_TIMES
from core.tools import save_csv
from core.parser import WebSiteParser

from config import settings


class WebSiteCrawler:
    parser: WebSiteParser = WebSiteParser()

    def __init__(self):
        self.client: AsyncClient = AsyncClient(follow_redirects=True)
        self.ads: list[dict[str, str]] = []

    @staticmethod
    async def build_request_url(page: int) -> str:
        return settings.DOMAIN_URL + '?page=' + str(page)

    @staticmethod
    async def process_request(request: Request) -> None:
        logger.info(f'Sent request  {request.method} to host {request.url}')

    async def do_request(self, url: str) -> Response | None:
        for attempt in range(RETRY_TIMES):
            res: Response = await self.client.get(url=url, follow_redirects=True, timeout=10.0)
            if not res.is_success:
                logger.error(f'Failed to get response from {res.url} with status code {res.status_code}')
                continue
            logger.info(res.status_code)
            return res

    async def parse_data(self, page: int) -> None:
        response: Response = await self.do_request(url=await self.build_request_url(page))
        if not response:
            return
        await response.aread()
        ads: list[dict[str, str]] = await self.parser.parse_adv(response)
        if ads:
            self.ads.extend(ads)

    async def start_parsing(self) -> None:

        time_start: float = time()
        tasks: list[Coroutine] = [self.parse_data(page) for page in range(1, settings.NUM_PAGES + 1)]
        await gather(*tasks)
        save_csv(data_list=self.ads)
        logger.info(time() - time_start)

