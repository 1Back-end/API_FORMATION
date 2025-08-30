from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class VehicleFuel(BaseModel):
    name:str
    description :Optional[str]
  

class VehicleFuelCreate(VehicleFuel):
    pass 


class VehicleFuelUpdate(BaseModel):
    uuid: str
    name: Optional[str]
    description :Optional[str]
  
    

class VehicleFuelDelete(BaseModel):
    uuid: str


class VehicleFuelResponse(BaseModel):
    uuid: str
    name: str   
    description :Optional[str] 
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)


class VehicleFuelSlim(BaseModel):
    uuid: str
    name: str
    model_config = ConfigDict(from_attributes=True)



class VehiculeFuelResponseList(BaseModel):
    total: int
    pages: int
    per_page: int
    current_page:int
    data: list[VehicleFuelResponse]
    model_config = ConfigDict(from_attributes=True)