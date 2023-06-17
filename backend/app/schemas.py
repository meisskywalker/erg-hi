from fastapi import File, UploadFile
from pydantic import UUID4, BaseModel, EmailStr, Field


class ProductRequest(BaseModel):
    title: str = Field(min_length=6)
    description: str = Field(min_length=12)
    filename: str
    demo_link: str
    video_link: str
    journal_link: str
    author: str


class ProductResponse(ProductRequest):
    class Config:
        orm_mode = True


class ProductTitleOnly(BaseModel):
    title: str

    class Config:
        orm_mode = True


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID4
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
