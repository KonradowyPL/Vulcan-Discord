from discord_webhook import DiscordWebhook
import json

debug = True


# load webhook key
with open("secrets.json") as f:
    jsonObj = json.load(f)
    url = jsonObj["url"]

print(f"debug = {debug}")


def send(message: str) -> "requests.response":
    "sends message"

    if message == "":
        return 0

    print(f"Sending Discord message: {message}")

    if debug:
        return 0

    return DiscordWebhook(url=url, content=message).execute()
