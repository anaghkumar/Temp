import random
from locust import HttpUser, task,  constant
import json
import enum_file


TOKEN = 'wrjx7znfupbab2mhj1q3tpu0qhtec9rf'
HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}


class SearchByAppAndGrade(HttpUser):
    # wait_time = constant(5)

    def on_start(self):
        self.application = []
        self.grades = []
        self.client.headers = HEADERS

    # @task(1)
    @task
    def data_sync(self):
        self.client.get("/rest/V2/sync/data")
        resp = self.client.get("/rest/V2/sync/data")
        json_object = json.loads(resp.text)
        json_object = json.loads(json_object)
        grades_data = json_object.get("data").get("grades")
        application_data = json_object.get("data").get("applications")
        print("Response status code:", resp.status_code)

        for obj in grades_data:
            self.grades.append(obj.get("name"))

        for obj in application_data:
            self.application.append(obj.get("name"))

    @task
    def search_grades(self):
        fifty_grades = [random.choice(enum_file.GRADES) for i in range(50)]

        self.client.post("/rest/V2/price/search", json={
            "type": "grade",
            "grade": fifty_grades,
            "company": [""],
            "application": [""],
            "location": 1138,
            "price_type": ["1"],
            "date": "2022-05-13"
        })

        resp = self.client.post("/rest/V2/price/search", json={
            "type": "grade",
            "grade": fifty_grades,
            "company": [""],
            "application": [""],
            "location": 1138,
            "price_type": ["1"],
            "date": "2022-05-13"
        })

        print("Response status code:", resp.status_code)

    # @task
    # def search_application(self):
    #     fifty_applications = [random.choice(
    #         self.application) for i in range(50)]

    #     self.client.post("/rest/V2/price/search", json={
    #         "type": "application",
    #         "grade": [""],
    #         "company": ["3"],
    #         "application": fifty_applications,
    #         "location": 827,
    #         "price_type": ["1"],
    #         "date": "2022-06-29"
    #     })
