from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum


class UnitProduct(Base):

    __tablename__="unit_product"

    uuid=Column(String,primary_key=True,index=True)
    name=Column(String,unique=True,nullable=False)
    description=Column(Text,nullable=True)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at = Column(DateTime, default=func.now())  # Account creation timestamp
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Last update timestamp
