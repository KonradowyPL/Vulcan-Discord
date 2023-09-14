from discord_webhook import DiscordWebhook
import json


# load webhook key
with open("secrets.json") as f:
    jsonObj = json.load(f)
    url = jsonObj["url"]


def send(message: str) -> "requests.response":
    "sends message"
    return DiscordWebhook(url=url, content=message).execute()
