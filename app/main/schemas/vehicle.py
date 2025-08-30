from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.main.schemas.vehicle_brand import VehicleBrandSlim
from app.main.schemas.vehicle_fuel import VehicleFuelSlim
from app.main.schemas.user import AddedBySlim


class Vehicle(BaseModel):
    name:str
    vehicle_brand_uuid:str
    vehicle_fuel_uuid:str
    description:Optional[str]


class VehicleCreate(Vehicle):
    pass 


class VehicleUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    vehicle_brand_uuid : Optional[str]
    vehicle_fuel_uuid : Optional[str]
    description: Optional[str]
    

class VehicleDelete(BaseModel):
    uuid: str

class VehicleUpdateStatus(BaseModel):
    uuid: Optional[str]
    status: str



class VehicleResponse(BaseModel):
    uuid : str
    name: str
    description: Optional[str]
    vehicle_brand : VehicleBrandSlim
    vehicle_fuel : VehicleFuelSlim
    creator : AddedBySlim 
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)

class VehicleResponseList(BaseModel):
    total: int
    pages: int
    per_page: int
    current_page: int
    data: list[VehicleResponse]
    model_config = ConfigDict(from_attributes=True)