from fastapi import FastAPI
from routers.book import book_router
from routers.user import user_router
from typing import Annotated
from fastapi.testclient import TestClient




app = FastAPI()

client = TestClient(app)

app.include_router(book_router, tags=["Books"], prefix="/books")
app.include_router(user_router, tags=["User"], prefix="/user")

@app.get("/")
async def read_main ():
    return {"message": "Hello from the books API"}
