import random
from locust import HttpUser, task
import json

TOKEN = 'wrjx7znfupbab2mhj1q3tpu0qhtec9rf'
HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}


class MarketNews(HttpUser):

    def on_start(self):
        self.market_news_image = []
        self.client.headers = HEADERS

    @task(1)
    def market_news(self):
        self.client.get("/rest/V2/market/news")
        resp = self.client.get("/rest/V2/market/news")
        json_object = json.loads(resp.text)
        json_object = json.loads(json_object)
        image_data = json_object.get("data").get("news")

        for item in image_data:
            self.market_news_image.append(item["image"])

    @task
    def load_image(self):
        for news_url in self.market_news_image:
            # self.client.get(news_url, name="/pub/media/news/file/")
            self.client.get(news_url)
            response = self.client.get(news_url)
            print("Response status code:", response.status_code)
