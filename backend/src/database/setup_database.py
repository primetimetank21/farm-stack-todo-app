from pymongo import MongoClient
from pymongo.database import Database, Collection
from dotenv import load_dotenv
import os


def create_client(health_check: bool = False) -> MongoClient:
    load_dotenv()

    uri: str | None = os.getenv("MONGODB_CONNECTION_STRING")

    if not uri:
        raise ValueError("MONGODB_CONNECTION_STRING is not set in the .env file")

    # Create new client and connect
    client: MongoClient = MongoClient(uri)

    # Send a ping to confirm a successful connection
    if health_check:
        try:
            client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    return client


async def connect_to_database(
    collection_str: str = "todo_collection", health_check: bool = False
) -> tuple[MongoClient, Collection]:  # -> Generator[Collection, Any, None]:
    client: MongoClient = create_client(health_check=health_check)

    db: Database = client.farm_todo_db
    collection_name: Collection = db[collection_str]

    return (client, collection_name)
