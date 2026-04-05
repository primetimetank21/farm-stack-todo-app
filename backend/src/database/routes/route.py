from typing import Any
from fastapi import FastAPI, APIRouter, status, HTTPException
from ..models.todos import Todo, TodoPost
from contextlib import asynccontextmanager
from ..setup_database import connect_to_database
from pymongo.database import Collection
from bson import ObjectId

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
    try:
        return collection_name.find().to_list(length=None)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str) -> Todo:
    try:
        todo_request: dict[str, Any] | None = collection_name.find_one(
            {"_id": ObjectId(todo_id)}
        )

        if not todo_request:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
            )

        todo: Todo = Todo.model_validate(todo_request)
        return todo

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/", response_model=TodoPost, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoPost) -> TodoPost:
    try:
        collection_name.insert_one(todo.model_dump())
        return todo

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{todo_id}", response_model=TodoPost)
async def update_todo(todo_id: str, todo: TodoPost) -> TodoPost:
    try:
        update_result: Any | None = collection_name.find_one_and_update(
            {"_id": ObjectId(todo_id)}, {"$set": todo.model_dump()}
        )

        if not update_result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
            )

        return todo

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str) -> None:
    delete_result: Any | None = collection_name.find_one_and_delete(
        {"_id": ObjectId(todo_id)}
    )

    if not delete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
