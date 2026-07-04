from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient
import asyncio
import configparser

# Load secrets from config.cfg
config = configparser.ConfigParser()
config.read("config.cfg")
CLIENT_ID = config["azure"]["clientId"]
CLIENT_SECRET = config["azure"]["clientSecret"]
TENANT_ID = config["azure"]["tenantId"]



async def main():
    credential = DeviceCodeCredential(
        client_id=CLIENT_ID,
        tenant_id=TENANT_ID
    )

    graph = GraphServiceClient(credential)

    # Await the Graph call
    users = await graph.users.get()

    for u in users.value:
        print(u.display_name)

asyncio.run(main())
