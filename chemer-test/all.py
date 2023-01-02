from locust import HttpUser, task,  constant


TOKEN = 'wrjx7znfupbab2mhj1q3tpu0qhtec9rf'
HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}


class Script(HttpUser):
    # def on_start(self):
    # self.client.headers = HEADERS

    # @task
    # def customers_me(self):
    #     self.client("/rest/V1/customers/me")

    @task
    def recent_search(self):
        # self.client("/rest/V2/recent/price/search")
        # self.client("/addon/product/onepage/?industry=6539")
        # self.client("/addon/product/onepage/?industry=6458")
        # self.client("/customer/account/login/referer/aHR0cHM6Ly9zd")
        # self.client("/addon/manufacture/index?req=37")
        # self.client("/addon/manufacture/index?req=59")
        # self.client("/addon/product/onepage/?industry=6008")
        self.client("/addon/product/onepage/?features=6272&industr")
