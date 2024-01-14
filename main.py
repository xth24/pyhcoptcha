import secrets

import hcoptcha

client = hcoptcha.Client(
    api_key=""
)

captcha_key = client.solve(
    site_key="a9b5fb07-92ff-493f-86fe-352a2803b3df",
    url="https://discord.com/channels/@me",
    proxy="proxy"
)

print(captcha_key)
