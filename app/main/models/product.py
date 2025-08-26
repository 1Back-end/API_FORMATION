from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean, Float
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum


class Product(Base):

    __tablename__ = "products"

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    qty = Column(Integer, nullable=False, default="0")
    pv = Column(Float, nullable=False)
    pa = Column(Float, nullable=False)
    stock_seal = Column(Integer, nullable=False, default="0")
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    description = Column(String, nullable=True)
    #foreignkey
    category_uuid = Column(String, ForeignKey( "category_product.uuid"), nullable=False) # foreign key
    category = relationship("CategoryProduct", backref="products")
    unit_uuid = Column(String,ForeignKey("unit_product.uuid"),nullable=False)
    unit = relationship("UnitProduct",backref="products")
    # Account creation timestamp
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(),
                        onupdate=func.now())  # Last update timestamp
