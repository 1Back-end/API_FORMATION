import math
import bcrypt
from fastapi import HTTPException
from sqlalchemy import or_
import re
from typing import List, Optional, Union
import uuid
from app.main.core.i18n import __
from sqlalchemy.orm import Session
from app.main.crud.base import CRUDBase
from app.main import models, schemas

class CRUDProduct(CRUDBase[models.Product,schemas.ProductCreate,schemas.ProductUpdate]):
    
    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.Product).filter(models.Product.uuid==uuid,models.Product.is_deleted==False).first()
    
    @classmethod
    def get_by_name(cls,db:Session,name:str):
        return db.query(models.Product).filter(models.product.name == name,models.Product.is_deleted==False).first()
    
    @classmethod
    def delete(cls, db: Session, uuid: str):
        db_obj = cls.get_by_uuid(db=db, uuid=uuid)
        if not db_obj:
            raise HTTPException(
                status_code=404, detail="Product not find")
        db.delete(db_obj)
        db.commit()

    @classmethod
    def soft_delete(cls, db: Session, uuid: str):
        db_obj = cls.get_by_uuid(db=db, uuid=uuid)
        if not db_obj:
            raise HTTPException(
                status_code=404, detail="product not find")
        db_obj.is_deleted = True
        db.commit()

    @classmethod
    def create(cls, db: Session, obj_in: schemas.ProductCreate):
        db_obj = models.Product(
            uuid=str(uuid.uuid4),
            name=obj_in.name,
            description=obj_in.description,
            pu = obj_in.pu,
            pa = obj_in.pa,
            qty = obj_in.qty
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def update(cls, db: Session, obj_in: schemas.ProductUpdate):
        db_obj = cls.get_by_uuid(db=db, uuid=obj_in.uuid)
        if not db_obj:
            raise HTTPException(
                status_code=404, detail="PRODUCT NOT FOUND")
        db_obj.name = obj_in.name if obj_in.name else db_obj.name
        db_obj.description = obj_in.description if obj_in.description else db.description
        db_obj.qty = obj_in.qty if obj_in.qty else db.qty
        db_obj.pa = obj_in.pa if obj_in.pa else db.pa
        db_obj.pu = obj_in.pu if obj_in.pu else db.pu
        db.commit()
        db.refresh(db_obj)
        return db_obj

product= CRUDProduct(models.product)
        