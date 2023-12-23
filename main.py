import hcoptcha

client = hcoptcha.Client(
    api_key="api_key"
)

captcha_key = client.solve(
    site_key="472b4c9f-f2b7-4382-8135-c983f5496eb9",
    url="https://discord.com/channels/@me",
    proxy=f"proxy"
)

print(captcha_key)