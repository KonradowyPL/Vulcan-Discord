from vulcan import Keystore, Account
import asyncio
import json


async def main():
    token = input("insert token:")
    symbol = input("insert symbol:")
    pin = input("insert pin:")
    webhook = input("insert wiscord webhook:")

    keystore = await Keystore.create(device_model="Vulcan API")

    account = await Account.register(keystore, token, symbol, pin)

    # store for later use
    jsonObj = {
        "keystore": keystore.as_dict,
        "account": account.as_dict,
        "url": webhook,
    }

    with open("secrets.json", "w") as f:
        json.dump(jsonObj, f)


asyncio.run(main())
