from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Product(BaseModel):
    name:str
    pu:float
    pa:float
    qte:int
    stock_seuil:int
    description :Optional[str]
  


class ProductCreate(Product):
    pass 


class ProductUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    pu: Optional[float]
    pa: Optional[float]
    qte: Optional[int]
    stock_seuil: Optional[int]
    description: Optional[str]
    

class ProductDelete(BaseModel):
    uuid: str


class ProductResponse(BaseModel):
    uuid: str
    name: str
    description: Optional[str]
    pu: float
    pa: float
    qte: int
    stock_seuil: int
    created_at:datetime
    updated_at: Optional[datetime]
