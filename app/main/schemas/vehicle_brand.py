from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class VehicleBrand(BaseModel):
    name:str
    description :Optional[str]
  

class VehicleBrandCreate(VehicleBrand):
    pass 


class VehicleBrandUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    description :Optional[str]



class VehicleBrandDelete(BaseModel):
    uuid: str


class VehicleBrandResponse(BaseModel):
    uuid: str
    name: str   
    description :Optional[str]
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)


class VehicleBrandSlim(BaseModel):
    uuid: str
    name: str
    model_config = ConfigDict(from_attributes=True)



class VehiculeBrandResponseList(BaseModel):
    total: int
    pages: int
    per_page: int
    current_page:int
    data: list[VehicleBrandResponse]