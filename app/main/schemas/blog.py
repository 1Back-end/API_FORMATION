from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class Blog(BaseModel):
    uuid: str
    name: str


class BlogCreate(BaseModel):
    pass


class BlogUpdate(BaseModel):
    uuid: str
    name: str


class BlogDelete(BaseModel):
    uuid: str


class BlogResponse(BaseModel):
    uuid: str
    name: str
    create_at: str
    updated_at: Optional[str]
    model_config = ConfigDict(from_attributes=True)
