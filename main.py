from hcoptcha import HCaptchaEnterpriseTask

api_key = "hcoptcha_api_key"
sitekey = "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2"
url = "https://accounts.hcaptcha.com/demo"
proxy = "user:pass@ip:port"
rqdata = None  # optional

hcaptcha_task = HCaptchaEnterpriseTask(api_key, sitekey, url, proxy, rqdata)
task_creation_response = hcaptcha_task.create_task()
print(task_creation_response)

task_result = hcaptcha_task.get_task_result()
print(task_result)
