from fastapi import FastAPI
from api.routes.router import api_router
import uvicorn

app = FastAPI()

HOST = "127.0.0.1"
PORT = 8000

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("server:app",  host=HOST, port=PORT,  reload=True)
    print(f"Starting server at {HOST}:{PORT}")