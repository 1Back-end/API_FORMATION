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


class CRUDQuinFour(CRUDBase[models.QuinFour, schemas.QuinFourCreate,schemas.QuinFourUpdate]):


    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.QuinFour).filter(models.QuinFour.uuid==uuid,models.QuinFour.is_deleted==False).first()
    
    @classmethod
    def get_by_first_name(cls,db:Session,first_name:str):
        return db.query(models.Product).filter(models.QuinFour.first_name==first_name,models.QuinFour.is_==False).first()
    
    @classmethod
    def get_by_last_name(cls,db:Session,last_name:str):
        return db.query(models.Product).filter(models.QuinFour.last_name==last_name,models.QuinFour.is_==False).first()
    




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
              db_obj= models.QuinFour(
                  uuid=str(uuid.uuid4()),
                  first_name=obj_in.first_name,
                  last_name=obj_in.last_name
                  phone_number1=obj_in.phone_number1
                  phone_number2=obj_in.phone_number2
                  country=obj_in.country
                  city=obj_in.city
    
                  
              )
              db.add(db_obj)
              db.commit()
              db.refresh(db_obj)
              return db_obj
        
        @classmethod
        def update(cls,db:Session,obj_in:schemas.QuinFour):
                db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid) 
                if not db_obj:
                    raise HTTPException(status_code=404, detail="QuinFour not find")
                db_obj.first_name=obj_in.first_name if obj_in.first_name else db_obj.first_name
                db_obj.last_name=obj_in.last_name if obj_in.last_name else db_obj.last_name
                
                db.commit()
                db.refresh(db_obj)
                return db_obj

product=CRUDQuinFour(models.QuinFour)


        








                  