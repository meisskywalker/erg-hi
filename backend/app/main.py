from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app import models
from app.db import engine
from .routers import product, user, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(user.router)
