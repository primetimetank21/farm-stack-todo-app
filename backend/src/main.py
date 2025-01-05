from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .database.routes.route import lifespan, router
from typing import cast
import os
import uvicorn

# Load env variables
load_dotenv()

app: FastAPI = FastAPI(lifespan=lifespan)

origins: list[str] = [
    # "http://localhost:5173",  # localhost
    cast(str, os.getenv("ALLOWED_ORIGIN"))
]

# Add middleware to handle Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins (domains) that can interact with this API.
    allow_credentials=True,  # Allow sending cookies and other credentials in cross-origin requests.
    allow_methods=[
        "*"
    ],  # Specify the HTTP methods that are allowed in cross-origin requests.
    allow_headers=[
        "*"
    ],  # Specify the HTTP headers that can be included in cross-origin requests.
)

app.include_router(router=router)


@app.get("/", tags=["Health Check"])
async def ping() -> dict[str, str]:
    """
    Endpoint for health checks
    """
    return {"ping": "pong"}


if __name__ == "__main__":
    try:
        uvicorn.run(
            app, host=cast(str, os.getenv("HOST")), port=cast(int, os.getenv("PORT"))
        )
    except Exception as e:
        print(e)
