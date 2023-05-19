from pydantic import UUID4, BaseModel, EmailStr


class ProductRequest(BaseModel):
    title: str
    description: str
    demo_link: str
    video_link: str
    journal_link: str
    author: str


class ProductResponse(ProductRequest):
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
