from azure.identity import InteractiveBrowserCredential
from msgraph import GraphServiceClient
import asyncio
import configparser

# Load secrets from config.cfg
config = configparser.ConfigParser()
config.read("config.cfg")
client_id = config["azure"]["clientId"]
tenant_id = config["azure"]["tenantId"]



async def main():
    credential = InteractiveBrowserCredential(
        client_id=client_id,
        tenant_id=tenant_id
    )

    graph = GraphServiceClient(credential)

    me = await graph.me.get()
    print("Logged in as:", me.display_name)

asyncio.run(main())

