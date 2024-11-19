from asyncio import run

from core.crawler import WebSiteCrawler

if __name__ == "__main__":
    run(WebSiteCrawler().start_parsing())
