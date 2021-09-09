from fastapi import FastAPI
from routes.users import user

app = FastAPI(
    title="Users API",
    description="Users CRUD integration",
    version="0.0.1",
    openapi_tags=[{
        "name": "Users",
        "description": "users api"
    }]
)

app.include_router(user)

