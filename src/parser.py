import hashlib
import json
import os

import aiohttp
import asyncio
from lxml import html
from bs4 import BeautifulSoup
import requests

from CRUD.films import create_film, get_films


class Parser:
    def __init__(self):
        self.xpath_selectors = {
            "name": "//h1//text()",
            "description": "//p//text()",
            "picture_path": "//div[@data-testid='hero-media__poster']//img/@src",
            "rating": "//div[@data-testid='hero-rating-bar__aggregate-rating__score']//text()",
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
            "/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        self.pics_path = "static/pics"

    async def fetch_page(self, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                print(response.status)
                content = await response.text()
                return content

    def download_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image_hash = hashlib.md5(image_data).hexdigest()
            filename = f"{image_hash}.png"
            save_path = os.path.join(self.pics_path, filename)
            with open(save_path, "wb") as f:
                f.write(image_data)
            print(filename)
            return filename

    def get_data(self, content):
        data = {}
        for k, v in self.xpath_selectors.items():
            data[k] = str(content.xpath(v)[0])
        data["rating"] = float(data["rating"])
        data["picture_path"] = self.download_image(data["picture_path"])
        return data

    async def get_film_data(self, url):
        content = await self.fetch_page(url)
        content = html.fromstring(content)
        data = self.get_data(content)
        return data

    def get_urls(self, page_content):
        urls = []
        soup = BeautifulSoup(page_content, "html.parser")
        scripts = soup.find_all("script", type="application/ld+json")

        for script in scripts:
            try:
                data = json.loads(script.string)
                for item in data["itemListElement"]:
                    urls.append(item["item"]["url"])
                return urls[:10]
            except json.JSONDecodeError:
                continue

    async def run(self, session):
        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        page_content = await self.fetch_page(url)
        links = self.get_urls(page_content)
        for link in links:
            data = await self.get_film_data(link)
            print(data)
            await create_film(data=data)
        films = await get_films(session)
        return films


if __name__ == "__main__":
    parser = Parser()
    asyncio.run(parser.run())
