import requests
import time

time.sleep(30)

requests.post(
    "https://ntfy.sh/test",
    data="Noting ".encode(encoding="utf-8"),
)
