from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime




class QuinFou(BaseModel):
    frist_name:str
    las_name:str
    phone_number1:int
    phone_number2:Optional[int]
    country:str
    city:str
    

class QuinFourCreate(QuinFour):
    pass 


class QuinFourUpdate(BaseModel):
    uuid: str
    frist_name: Optional[str]
    las_name: Optional[str]
    phone_number1: Optional[int]
    phone_number2: Optional[int]
    country: Optional[str]
    city: Optional[str]

    
class QuinFourDelete(BaseModel):
    uuid: str


class QuinFourResponse(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    phone_number1: int
    phone_number2: Optional[int]
    country: Optional[str]
    city: Optional[str]
    created_at:datetime
    updated_at: Optional[datetime]