from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict, List


app: FastAPI = FastAPI()
# origins: List[str] = ["*"]
origins: List[str] = [
    # "*"
    "http://localhost:5173",  # localhost
    # "http://192.168.1.60:3000",  # Network
]

# Add middleware to handle Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    # TODO: Replace "localhost:3000" with the actual frontend URL or load it from a configuration file.
    allow_origins=origins,  # List of allowed origins (domains) that can interact with this API.
    allow_credentials=True,  # Allow sending cookies and other credentials in cross-origin requests.
    allow_methods=[
        "*"
    ],  # Specify the HTTP methods that are allowed in cross-origin requests.
    allow_headers=[
        "*"
    ],  # Specify the HTTP headers that can be included in cross-origin requests.
)


@app.get("/")
async def ping() -> Dict[str, str]:
    """
    Endpoint for health checks
    """
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # TODO: Get host and port from config?
