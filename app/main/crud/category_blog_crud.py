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



class CrudCategoryBlog(CRUDBase[models.CategoryBlog,schemas.CategoryBlogCreate,schemas.CategoryBlogUpdate]):


    @classmethod
    def get_by_uuid(cls,db:Session,uuid:str):
        return db.query(models.CategoryBlog).filter(models.CategoryBlog.uuid==uuid).first()
    

    @classmethod
    def get_by_name(cls,db:Session,name:str):
        return db.query(models.CategoryBlog).filter(models.CategoryBlog.name==name).first()
    
    @classmethod
    def delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail=__(key="category-blog-not-found"))
        db.delete(db_obj)
        db.commit()


    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="categoryblog not find")
        db_obj.is_deleted=True
        db.commit()

  
    @classmethod
    def create(cls,db:Session, obj_in:schemas.CategoryBlogCreate):

        db_obj = models.CategoryBlog(
            uuid = str(uuid.uuid4()),
            name = obj_in.name,
            description = obj_in.description

        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    



    @classmethod
    def update(cls,db:Session,obj_in:schemas.CategoryBlogUpdate):
        db_obj = cls.get_by_uuid(db=db,uuid=obj_in.uuid) 
        if not db_obj:
            raise HTTPException(status_code=404,detail="CategoryBlog not found")
        db_obj.name = obj_in.name if obj_in.name else db_obj.name
        db_obj.description = obj_in.description if obj_in.description else db_obj.description
        db.commit()
        db.refresh(db_obj)
        return db_obj
    


category_blog = CrudCategoryBlog(models.CategoryBlog)