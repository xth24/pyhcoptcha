import requests

from . import exceptions


class Task:
    def __init__(self, task_type: str, url: str, site_key: str, api_key: str, proxy: str):
        self.requests = requests.Session()
        self.proxy = proxy
        self.api_key = api_key
        self.task_type = task_type
        self.url = url
        self.site_key = site_key
        self.task_id = None
        self.task_response = None
        self.task_error = None
        self.task_state = None

    def create_task(self):
        data = {
            "task_type": self.task_type,
            "api_key": self.api_key,
            "data": {
                "sitekey": self.site_key,
                "url": self.url,
                "proxy": self.proxy,
            }
        }

        response = self.requests.post('https://api.hcoptcha.online/api/createTask', json=data)
        body = response.json()
        if response.status_code != 200:
            raise exceptions.ClientException(f"create_task: failed to create task: {body.get('message')}")
        if body.get('error'):
            raise exceptions.ClientException(f"create_task: failed to create task: {body.get('message')}")

        self.task_id = body['task_id']

    def get_task_data(self) -> [str, str]:
        data = {
            "api_key": self.api_key,
            "task_id": self.task_id
        }

        response = self.requests.post('https://api.hcoptcha.online/api/getTaskData', json=data)
        body = response.json()
        if response.status_code != 200:
            raise exceptions.ClientException(f"get_task_data: failed to get task: {body.get('message')}")
        if body.get('error'):
            raise exceptions.ClientException(f"get_task_data: failed to get task: {body.get('message')}")

        self.task_response = body['task']['captcha_key']
        self.task_state = body['task']['state']
