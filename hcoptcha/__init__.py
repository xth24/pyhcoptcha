import time

from .task import Task


class Client:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def solve(self, site_key: str, url: str, proxy: str):
        client = Task(
            site_key=site_key,
            url=url,
            proxy=proxy,
            task_type="hcaptchaEnterprise",
            api_key=self.api_key
        )

        client.create_task()
        client.get_task_data()

        while client.task_state == "processing":
            client.get_task_data()
            time.sleep(1)

        return client.task_response
