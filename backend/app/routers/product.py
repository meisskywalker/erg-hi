from typing import List
from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import oauth2
from app import Tf_idf

from ..handlers import product
from .. import db, schemas, models

product_model = models.Product

get_db = db.get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", status_code=status.HTTP_200_OK)
def index(db: Session = Depends(get_db)):
    return product.show_products(db)


@router.get("/get-titles", status_code=status.HTTP_200_OK)
def title_only(
    query: str = "the intelligence lazy to? jumped fox The brown fox is a cunning animal known for its intelligence and speed. It is often hunted for its fur and meat",
    db: Session = Depends(get_db),
):
    corpus = {a.id:a.title for a in product.show_products(db)}
    df = Tf_idf.Tf_Idf(corpus)
    tfidf = df.val_tfidf

    # print(list(tfidf.T.columns))

    keywords = df.clean_w(query)
    match_w = list(filter(lambda w: w in list(tfidf.T.columns), keywords))
    found = tfidf.T.loc[:, match_w]
    return found.T.sum().to_dict()


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
