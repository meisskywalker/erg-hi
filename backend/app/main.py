from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app import models
from app.db import engine
from .routers import product

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(product.router)
