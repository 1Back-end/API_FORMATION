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

class CRUDBlog(CRUDBase[models.Blog,schemas.BlogCreate,schemas.BlogUpdate]):


    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.Blog).filter(models.Blog.uuid==uuid,models.Blog.is_deleted==False).first()
    

    @classmethod
    def get_by_name(cls,db:Session,name:str):
        return db.query(models.Blog).filter(models.Blog.name==name,models.Blog.is_deleted==False).first()
    
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid)  
        if not db_obj:
             raise HTTPException(status_code=404,detail=__(key="blog-not-found"))
        db.delete(db_obj)
        db.commit()


    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="blog not find")
        db_obj.is_deleted=True
        db.commit()


    @classmethod
    def create(cls,db:Session, obj_in:schemas.BlogCreate,added_by:str):
        db_obj = models.Blog(
            uuid = str(uuid.uuid4()),
            name = obj_in.name,
            description = obj_in.description,
            category_uuid = obj_in.category_uuid,
            added_by = added_by
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    

    @classmethod
    def update(cls,db:Session,obj_in:schemas.BlogUpdate,added_by:str):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="Blog not found")
        db_obj.name = obj_in.name if obj_in.name else db_obj.name
        db_obj.description = obj_in.description if obj_in.description else db_obj.description
        db_obj.category_uuid  = obj_in.category_uuid if obj_in.category_uuid else db_obj.category_uuid
        db_obj.added_by = added_by
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def by_many(
        cls,
        db: Session,
        page: int = 1,
        per_page: int = 42,
    ):
        
        record_query = db.query(models.blog).filter(models.blog. is_deleted == False)
        total= record_query.count()
        record_query = record_query. offset((page - 1 ) * per_page). limit(per_page)
        return schemas.BlogResponseList(
            total= total,
            pages= math.ceil(total / per_page),
            per_page=per_page,
            current_page= page,
            data= record_query,

        )



blog = CRUDBlog(models.Blog)
