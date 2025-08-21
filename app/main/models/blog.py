from dataclasses import dataclass
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSONB
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy import event
from app.main.models.db.base_class import Base
from enum import Enum


class Blog(Base):
    __tablename__ = "blogs"
    uuid = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    category_uuid = Column(String, ForeignKey(
        "category_blog.uuid"), nullable=False)
    category = relationship("CategoryBlog", backref="blogs")
