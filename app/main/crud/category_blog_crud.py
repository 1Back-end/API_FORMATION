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



class CRUDcategoryblog(CRUDBase[models.CategoryBlog,schemas.CategoryBlogCreate,schemas.CategoryBlogUpdate]):


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
            raise HTTPException(status_code=404,detail="categoryblog not find")
        db.delete(db_obj)
        db.commit()


    @classmethod
    def soft_delete(cls,db:Session,uuid:str):
        db_obj = cls.get_by_uuid(db=db,uuid=uuid)
        if not db_obj:
            raise HTTPException(status_code=404,detail="categoryblog not find")
        db_obj.is_deleted=True
        db.commit()
