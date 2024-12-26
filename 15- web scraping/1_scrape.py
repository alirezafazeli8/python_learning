import requests

virgool = requests.get("https://virgool.io")

print(virgool.content.index("name"))
