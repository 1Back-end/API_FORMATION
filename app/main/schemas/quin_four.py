from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class QuinFou(BaseModel):
    frist_name:str
    last_name:str
    phone_number1:str
    phone_number2:Optional[str]
    country:str
    city:str
    

class QuinFourCreate(QuinFou):
    pass 


class QuinFourUpdate(BaseModel):
    uuid: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number1: Optional[str]
    phone_number2: Optional[str]
    country: Optional[str]
    city: Optional[str]

    
class QuinFourDelete(BaseModel):
    uuid: str


class QuinFourResponse(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    phone_number1: int
    phone_number2: Optional[str]
    country: Optional[str]
    city: Optional[str]
    created_at:datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)