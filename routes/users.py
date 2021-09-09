from fastapi import APIRouter
from config.db import connection
from models.users import users
from schemas.users import User
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get("/users")
def get_users():
    return connection.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email
    }

    # Encrypt password
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))

    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users{id}")
def get_user_id(id: str):
    return connection.execute(users.select().where(users.c.id == id)).first()

@user.delete("/users{id}")
def delete_user(id: str):
    result = connection.execute(users.delete().where(users.c.id == id))
    return {"status": "complete"}


@user.get("/users")
def get_user():
    return {"hello": "user"}