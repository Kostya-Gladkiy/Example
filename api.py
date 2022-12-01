import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

# from db import add_user, get_user
import db


app = FastAPI()


@app.get("/get_user/{id}")
async def _get_user(id: int):
    user = db.get_user(id)
    if user:
        return user
    else:
        return {"message": "Користувача з даним id не існує"}


class User(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    email: str = Field(min_length=3)
    age: int = Field(default=1, ge=14)


@app.post("/add_user/")
async def _add_user(user: User):
    user = user.dict()
    db.add_user(user)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
