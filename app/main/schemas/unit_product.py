from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UnitProduct(BaseModel):
    name: str
    description: Optional[str]


class UnitProductCreate(UnitProduct):
    pass


class UnitProductUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    description: Optional[str]


class UnitProductDelete(BaseModel):
    uuid: str


class UnitProductResponse(BaseModel):
    uuid: str
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)
    
class UnitProductSlim(BaseModel):
    uuid:str
    name:str
    model_config = ConfigDict(from_attributes=True)
