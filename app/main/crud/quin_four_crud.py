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


class CRUDQuinFour(CRUDBase[models.Fournisseur, schemas.QuinFourCreate,schemas.QuinFourUpdate]):


    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.Fournisseur).filter(models.Fournisseur.uuid==uuid,models.Fournisseur.is_deleted==False).first()
    
    @classmethod
    def get_by_phone_number1(cls,db:Session,phone_number1):
        return db.query(models.Fournisseur).filter(models.Fournisseur.phone_number1==phone_number1,models.Fournisseur.is_deleted==False).first()
    
    @classmethod
    def get_by_phone_number2(cls,db:Session,phone_number2):
        return db.query(models.Fournisseur).filter(models.Fournisseur.phone_number2==phone_number2,models.Fournisseur.is_deleted==False).first()

    
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db, uuid=uuid)
        if not db_obj:
            raise  HTTPException(status_code=404,detail="QuinFort not find")
        db.delete(db_obj)
        db.commit()

    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db==db, uuid==uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="QuinFour not find")
        db_obj.is_deleted=True
        db.commit()
            

    @classmethod
    def create(cls,db:Session,obj_in:schemas.QuinFourCreate):
        db_obj = models.Fournisseur(
            uuid=str(uuid.uuid4()),
            frist_name=obj_in.frist_name,
            last_name=obj_in.last_name,
            phone_number1=obj_in.phone_number1,
            phone_number2=obj_in.phone_number2,
            country=obj_in.country,
            city=obj_in.city   
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
            
        
    @classmethod
    def update(cls,db:Session,obj_in:schemas.QuinFourUpdate):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="fourniseur-not-found")
        db_obj.first_name = obj_in.first_name if obj_in.first_name else db_obj.first_name
        db_obj.last_name = obj_in.last_name if obj_in.last_name else db_obj.last_name
        db_obj.phone_number1 = obj_in.phone_number1 if obj_in.phone_number1 else db_obj.phone_number1
        db_obj.phone_number2 = obj_in.phone_number2 if obj_in.phone_number2 else db_obj.phone_number2
        db_obj.country = obj_in.country if obj_in.country else db_obj.country
        db_obj.city = obj_in.city if obj_in.city else db_obj.city
        db.commit()
        db.refresh(db_obj)
        return db_obj
            

fourisseur=CRUDQuinFour(models.Fournisseur)


        








                  