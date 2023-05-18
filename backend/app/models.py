import uuid
from sqlalchemy import UUID, Column, String
from app.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String)
    description = Column(String)
    demo_link = Column(String)
    video_link = Column(String)
    journal_link = Column(String)
    author = Column(String)
