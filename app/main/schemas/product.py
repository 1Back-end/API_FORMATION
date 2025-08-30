from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.main.schemas.category_product import CategoryProductSlim
from app.main.schemas.unit_product import UnitProductSlim


class Product(BaseModel):
    name: str
    qty: int
    description: str
    pv: float
    pa: float
    stock_seal: int
    category_product_uuid:str
    unit_product_uuid:str


class ProductCreate(Product):
    pass


class ProductUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    price: Optional[int]
    qty: Optional[int]
    description: Optional[str]
    pv: Optional[float]
    pa: Optional[float]
    unit_product_uuid:Optional[str]
    category_product_uuid:Optional[str]    


class ProductDelete(BaseModel):
    uuid: str


class ProductResponse(BaseModel):
    uuid: str
    name: str
    qty: int
    price: float
    description: str
    pv: float
    pa: float
    stock_seal: int
    created_at: datetime
    updated_at: Optional[datetime]
    category:CategoryProductSlim
    unit:UnitProductSlim
    model_config = ConfigDict(from_attributes=True)

class ProductResponseList(BaseModel):
    total :int
    per_page: int
    pages:int
    current_page:int
    data:list[ProductResponse]
    model_config = ConfigDict(from_attributes=True)