from loguru import logger
from httpx import Response
from bs4 import BeautifulSoup, ResultSet


class WebSiteParser:

    @classmethod
    async def parse_adv(cls, response: Response) -> list[dict[str, str]]:
        logger.info(f'Sent request to host {response.url}')
        await response.aread()
        parser: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        cards: ResultSet = parser.find_all('a', class_='decoration-none')
        ads_list: list[dict[str, str]] = cls.parse_data(cards)
        return ads_list

    @classmethod
    def parse_data(cls, cards: list) -> list[dict[str, str]] | None:
        ads_list: list[dict[str, str]] = []
        for card in cards:
            try:
                link: str = card['href']
                title: str = card.find('div', class_='bloc_title').text
            except (KeyError, AttributeError):
                logger.error(f'Failed to parse card {card}')
                continue
            if link and title:
                ads_list.append({'Title': title, 'Link': link})
        return ads_list
