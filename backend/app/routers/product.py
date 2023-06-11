from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import oauth2

from ..handlers import product
from .. import db, schemas, models

product_model = models.Product

get_db = db.get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", status_code=status.HTTP_200_OK)
def index(db: Session = Depends(get_db)):
    return product.show_products(db)


@router.get("/tfidf", status_code=status.HTTP_200_OK)
def show_tfidf(
    query: str = "",
    db: Session = Depends(get_db),
):
    return product.show_tf_idf(query, db)

@router.get("/{id}", status_code=status.HTTP_200_OK)
def show_by_id(id: UUID4, db: Session = Depends(get_db)):
    return product.show_product(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.ProductRequest,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.create_product(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: UUID4,
    request: schemas.ProductRequest,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.edit_product(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def destroy(
    id: UUID4,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.delete_product(id, db)
