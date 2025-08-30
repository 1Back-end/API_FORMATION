from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum


class Vehicle(Base):
    __tablename__="vehicles"

    uuid = Column(String,primary_key=True,index=True)
    
    name = Column(String,unique=True,index=True,nullable=False)

    description = Column(Text,nullable=True)

    vehicle_brand_uuid = Column(String,ForeignKey("vehicle_brands.uuid"),nullable=False)
    vehicle_brand = relationship("VehicleBrand",foreign_keys=[vehicle_brand_uuid],backref="vehicles")


    vehicle_fuel_uuid = Column(String,ForeignKey("vehicle_fuels.uuid"),nullable=False)
    vehicle_fuel = relationship("VehicleFuel",foreign_keys=[vehicle_fuel_uuid],backref="vehicles")


    added_by = Column(String,ForeignKey("users.uuid"),nullable=False)
    creator = relationship("User",foreign_keys=[added_by],backref="vehicles")
                      

    is_active = Column(Boolean,default=True)
    is_deleted=Column(Boolean,default=False)
    created_at = Column(DateTime, default=func.now())  # Account creation timestamp
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Last update timestamp
     
