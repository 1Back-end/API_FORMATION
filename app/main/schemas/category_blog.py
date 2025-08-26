from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime




class CategoryBlog(BaseModel):
    name:str
    description :Optional[str]
  


class CategoryBlogCreate(CategoryBlog):
    pass 


class CategoryBlogUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    description: Optional[str]
    

class CategoryBlogDelete(BaseModel):
    uuid: str


class CategoryBlogResponse(BaseModel):
    uuid: str
    name: str
    description: Optional[str]
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)

