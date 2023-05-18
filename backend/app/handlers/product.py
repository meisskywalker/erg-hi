from fastapi import HTTPException, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import models, schemas

product_model = models.Product


def show_products(db: Session):
    return db.query(product_model).all()


def show_product(id: UUID4, db: Session):
    product = db.query(product_model).filter(product_model.id == id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} is not found",
        )

    return product


def create_product(request: schemas.ProductRequest, db: Session):
    new_product = models.Product(
        title=request.title,
        description=request.description,
        video_link=request.video_link,
        demo_link=request.demo_link,
        journal_link=request.journal_link,
        author=request.author,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def edit_product(id: UUID4, request: schemas.ProductRequest, db: Session):
    edited_product= request.dict(exclude_unset=True)
    product = db.query(product_model).filter(product_model.id == id)

    if not product.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} is not found",
        )

    product.update(edited_product, synchronize_session=False)
    db.commit()

    return {"detail": "Product was updated"}


def delete_product(id: UUID4, db: Session):
    product = db.query(product_model).filter(product_model.id == id)

    if not product.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} is not found",
        )

    product.delete(synchronize_session=False)
    db.commit()

    return {"detail": "Product was deleted"}
