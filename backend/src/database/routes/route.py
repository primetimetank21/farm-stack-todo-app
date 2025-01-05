from fastapi import FastAPI, APIRouter
from ..models.todos import Todo, TodoPost
from contextlib import asynccontextmanager
from ..setup_database import connect_to_database
from pymongo.database import Collection

collection_name: Collection


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Server Startup
    global collection_name
    client, collection_name = await connect_to_database(health_check=True)

    yield

    # Server Shutdown
    client.close()


router: APIRouter = APIRouter(prefix="/todos")


@router.get("/", response_model=list[Todo])
async def get_all_todos() -> list[Todo]:
    return collection_name.find().to_list(length=None)


@router.post("/", response_model=TodoPost)
async def create_todo(todo: TodoPost) -> TodoPost:
    collection_name.insert_one(todo.model_dump())
    return todo
