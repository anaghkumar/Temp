import random
from locust import HttpUser, task, constant
import json
import enum_file

TOKEN = 'wrjx7znfupbab2mhj1q3tpu0qhtec9rf'
HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}


class MarketNews(HttpUser):
    wait_time = constant(5)

    def on_start(self):
        self.market_news_image = []
        self.application = []
        self.grades = []
        self.client.headers = HEADERS

    @task(5)
    def bookmark(self):
        self.client.get("/rest/V2/bookmark")

    @task(4)
    def market_news(self):
        self.client.get("/rest/V2/market/news")
        resp = self.client.get("/rest/V2/market/news")
        json_object = json.loads(resp.text)
        json_object = json.loads(json_object)
        image_data = json_object.get("data").get("news")

        for item in image_data:
            self.market_news_image.append(item["image"])

    @task(3)
    def load_image(self):
        for news_url in self.market_news_image:
            self.client.get(news_url, name="Images")

    @task(2)
    def data_sync(self):
        self.client.get("/rest/V2/sync/data")

    @task(1)
    def search_grades(self):
        fifty_grades = [random.choice(enum_file.GRADES) for i in range(3)]
        # fifty_applications = [random.choice(enum_file.APPLICATION) for i in range(3)]

        self.client.post("/rest/V2/price/search", json={
            "type": "grade",
            "grade": fifty_grades,
            "company": [""],
            "application": [""],
            "location": 1138,
            "price_type": ["1"],
            "date": "2022-05-13"
        })
