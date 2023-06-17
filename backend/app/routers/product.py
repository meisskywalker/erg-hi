import os
import uuid
from fastapi import APIRouter, Depends, File, HTTPException, status, UploadFile
from fastapi.responses import FileResponse
from pydantic import UUID4
from sqlalchemy.orm import Session

from app import oauth2

from ..handlers import product
from .. import db, schemas, models

product_model = models.Product

get_db = db.get_db

router = APIRouter(prefix="/products", tags=["Products"])

IMAGEDIR = "./images"

def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.isfile(file_path)


@router.post("/upload-file", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...)):
    os.makedirs(IMAGEDIR, exist_ok=True)

    _, ext = os.path.splitext(str(file.filename))
    file.filename = f"image-{uuid.uuid4()}{ext}"
    content = await file.read()

    with open(f"{IMAGEDIR}/{file.filename}", "wb") as buffer:
        buffer.write(content)

    return {"filename": file.filename}


@router.get("/get-file/{filename}")
async def get_file(filename: str):
    file_path = f"./images/{filename}"
    return FileResponse(file_path)


@router.delete("/delete-file/{filename}", status_code=status.HTTP_200_OK)
async def remove_file(
    filename: str,
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    if check_file_exists(IMAGEDIR, filename):
        os.remove(f"{IMAGEDIR}/{filename}")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File with name {filename} is not found",
        )

    return {"detail": "File was deleted"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.ProductRequest,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.create_product(request, db)


@router.get("/", status_code=status.HTTP_200_OK)
def index(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    return product.show_products(db, page, limit)


@router.get("/tfidf", status_code=status.HTTP_200_OK)
def show_tfidf(
    query: str = "",
    db: Session = Depends(get_db),
):
    return product.show_tf_idf(query, db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def show_by_id(id: UUID4, db: Session = Depends(get_db)):
    return product.show_product(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: UUID4,
    request: schemas.ProductRequest,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.edit_product(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy(
    id: UUID4,
    db: Session = Depends(get_db),
    current_user: schemas.UserRequest = Depends(oauth2.get_current_user),
):
    return product.delete_product(id, db)
