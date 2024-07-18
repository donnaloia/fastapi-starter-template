from sqlalchemy import (
    Column, 
    Integer, 
    UUID,
    String, 
    Boolean, 
    TIMESTAMP, 
    text,
    ForeignKey
)
import uuid

from src.db.database import Base
from sqlalchemy.orm import relationship



class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
    category = relationship("Category")