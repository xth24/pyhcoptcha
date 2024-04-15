import time
import requests
from hcoptcha import exceptions


class Task:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def post_request(self, endpoint: str, data: dict):
        response = requests.post(endpoint, json=data)
        body = response.json()

        if body.get('error'):
            error_message = body.get('message', 'unknown error')
            raise exceptions.SolverException(error_message)

        return body


class HCaptchaEnterpriseTask(Task):
    def __init__(self, api_key: str, sitekey: str, url: str, proxy: str, rqdata: str = None):
        super().__init__(api_key)
        self.task_id = ""
        self.params = {
            "task_type": "hcaptchaEnterprise",
            "api_key": self.api_key,
            "data": {
                "sitekey": sitekey,
                "url": url,
                "proxy": proxy
            }
        }
        if rqdata:
            self.params["data"]["rqdata"] = rqdata

    def create_task(self):
        endpoint = "https://api.hcoptcha.online/api/createTask"
        response = self.post_request(endpoint, self.params)
        self.task_id = response['task_id']
        return self.task_id

    def get_task_result(self, retry_interval=3, max_retries=10):
        endpoint = "https://api.hcoptcha.online/api/getTaskData"
        data = {
            "api_key": self.api_key,
            "task_id": self.task_id
        }

        for _ in range(max_retries):
            response = self.post_request(endpoint, data)
            task_state = response['task']['state']

            if task_state == "completed":
                return response['task']['captcha_key']
            elif task_state == "error":
                error_message = response['task'].get('message', 'unknown error')
                raise exceptions.SolverException(error_message)

            time.sleep(retry_interval)

        raise exceptions.SolverException("Max retries exceeded without completion.")
