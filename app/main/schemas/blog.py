from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.main.schemas.category_blog import CategoryBlogSlim
from app.main.schemas.user import AddedBySlim


class Blog(BaseModel):
    name:str
    category_uuid:str
    description:Optional[str]


class BlogCreate(Blog):
    pass 


class BlogUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    category_uuid : Optional[str]
    description: Optional[str]
    

class BlogDelete(BaseModel):
    uuid: str

class BlogUpdateStatus(BaseModel):
    uuid: Optional[str]
    status: str



class BlogResponse(BaseModel):
    uuid : str
    name: str
    description: Optional[str]
    category_blog : CategoryBlogSlim
    creator : AddedBySlim 
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)

class BlogResponseList(BaseModel):
    total: int
    pages: int
    per_page: int
    current_page: int
    data: list[BlogResponse]
    model_config = ConfigDict(from_attributes=True)




 
