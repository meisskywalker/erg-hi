from pydantic import BaseModel


class ProductRequest(BaseModel):
    title: str
    description: str
    demo_link: str
    video_link: str
    journal_link: str
    author: str
