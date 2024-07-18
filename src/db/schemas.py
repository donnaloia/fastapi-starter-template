from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class CategoryBase(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True

class CreateCategory(CategoryBase):
    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    id: UUID
    content: str
    title: str
    published: bool
    created_at: datetime
    category_id: UUID

    class Config:
        orm_mode = True

# this modifies the payload response to include a nested Category resource rather than just the uuid
class ItemDetailed(ItemBase):
    category: CategoryBase
        
    class Config:
        exclude = ['category_id']
    


class CreateItem(ItemBase):
    id: Optional[UUID] = None
    
    class Config:
        orm_mode = True
