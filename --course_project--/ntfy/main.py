import requests
import time

time.sleep(30)

requests.post(
    "https://ntfy.sh/test",
    data="Arabs Are Mother Fucker (:".encode(encoding="utf-8"),
)
