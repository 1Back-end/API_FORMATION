from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class CategoryProduct(BaseModel):
    name: str
    description: Optional[str]


class CategoryProductCreate(CategoryProduct):
    pass


class CategoryProductUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    description: Optional[str]


class CategoryProductDelete(BaseModel):
    uuid: str


class CategoryProductResponse(BaseModel):
    uuid: str
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    

class CategoryProductSlim(BaseModel):
    uuid:str
    name:str 
    model_config = ConfigDict(from_attributes=True)
    
    