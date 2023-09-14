from vulcan import Keystore, Account
from vulcan import Vulcan
import json


async def load() -> Vulcan:
    """ loads client """

    with open("secrets.json") as f:
        jsonObj = json.load(f)
        keystore = Keystore.load(jsonObj["keystore"])
        account = Account.load(jsonObj["account"])
        client = Vulcan(keystore, account)

    await client.select_student()

    return client
