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
from app.main import models,schemas



class CrudVehicleFuel(CRUDBase[models.VehicleFuel,schemas.VehicleFuelCreate,schemas.VehicleFuelUpdate]):


    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.VehicleFuel).filter(models.VehicleFuel.uuid==uuid,models.VehicleFuel.is_deleted==False).first()
    

    @classmethod
    def get_by_name(cls,db:Session,name:str):
        return db.query(models.VehicleFuel).filter(models.VehicleFuel.name==name,models.VehicleFuel.is_deleted==False).first()
    

   
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail=__(key="vehicle-fuel-not-found"))
        db.delete(db_obj)
        db.commit()


    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="vehicle-fuel-not-found")
        db_obj.is_deleted=True
        db.commit()


    @classmethod
    def create(cls,db:Session, obj_in:schemas.VehicleFuelCreate):

        db_obj = models.VehicleFuel(
            uuid = str(uuid.uuid4()),
            name = obj_in.name,
            description = obj_in.description

        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    



    @classmethod
    def update(cls,db:Session,obj_in:schemas.VehicleFuelUpdate):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="Vehicle-Fuel-not-found")
        db_obj.name = obj_in.name if obj_in.name else db_obj.name
        db_obj.description = obj_in.description if obj_in.description else db_obj.description
        db.commit()
        db.refresh(db_obj)
        return db_obj
    

    @classmethod
    def get_many(
        cls,
        db: Session,
        page: int = 1,
        per_page: int = 25,
    ):
        record_query = db.query(models.VehicleFuel).filter( models.VehicleFuel.is_deleted == False)

        total = record_query.count()

        record_query = record_query.offset((page - 1) * per_page).limit(per_page)

        return schemas.VehiculeFuelResponseList(
            total=total,
            pages=math.ceil(total / per_page),
            per_page=per_page,
            current_page=page,
            data=record_query,
        )
    
    


vehicle_fuel= CrudVehicleFuel(models.VehicleFuel) 