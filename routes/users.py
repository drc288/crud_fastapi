from os import name
from fastapi import APIRouter, Response, status
from config.db import connection
from config.encode import encode
from models.users import users
from schemas.users import User
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()


@user.get("/users", response_model=list[User], tags=["Users"])
def get_users():
    return connection.execute(users.select()).fetchall()


@user.post("/users", response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email
    }

    # Encrypt password
    new_user["password"] = encode(user.password.encode("utf-8"))

    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users{id}", response_model=User, tags=["Users"])
def get_user_id(id: str):
    return connection.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str):
    result = connection.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users{id}", response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    connection.execute(users.update().values(
        name=user.name, email=user.email, password=encode(user.password.encode("utf-8"))).where(users.c.id == id))
    return connection.execute(users.select().where(users.c.id == id)).first()
