from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, Text, DateTime, Boolean,Integer, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from app.main.models.db.base_class import Base

class VehicleBrand(Base):

    __tablename__="vehicle_brands"

    uuid=Column(String,primary_key=True,index=True)
    name=Column(String,unique=True,nullable=False)
    description=Column(Text,nullable=True)
    is_deleted=Column(Boolean,default=False)
    is_active  = Column(Boolean,default=True)
    created_at = Column(DateTime, default=func.now())  # Account creation timestamp
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Last update timestamp
     