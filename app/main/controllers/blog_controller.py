from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/blogs", tags=["blogs"])
@router.get("/create",response_model=schemas.Msg,status_code=201)
async def create_blog(
    *,
    db:Session = Depends(get_db),
    obj_in:schemas.BlogCreate
):
    exist_name = crud.blog.get_by_name(db=db,name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409,detail="Blog-Already-Exist")
    crud.blog.create(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="Blogs-Created-Successfully"))

@router.put("update",response_model=schemas.Msg,status_code=200)
async def update_blog(
    *,
    db:Session = Depends(get_db),
    obj_in :schemas.BlogUpdate
):
    exist_name = crud.blog.get_by_name(db=db,name=obj_in.name)
    if exist_name:
      raise HTTPException(status_code=409,detail="Blog-Already-exist")
    crud.blog.create(db=db,obj_in=obj_in)
    return schemas.Msg(message=__(key="blog-create-successfully"))


@router.delete('/delete',response_model=schemas.Msg,status_code=200)
async def delete_blog(
     *,
    db: Session = Depends(get_db),
    obj_in: schemas.BlogDelete
    
):
    crud.blog.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="blogs-deleted-successfully"))

@router.put('/soft_delete',response_model=schemas.Msg,status_code=200)
async def soft_delete_blog(
     *,
    db: Session = Depends(get_db),
    obj_in: schemas.BlogDelete
    
):
    crud.blog.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="blogs-deleted-successfully"))

@router.get('/get_by_uuid',response_model=schemas.BlogResponse,status_code=200)
async def get_blog_by_uuid(
   *,
   db:Session = Depends(get_db),
   uuid:str
):
    obj_in = crud.blog.get_by_uuid(db=db,uuid=uuid)
    if not obj_in:
     raise HTTPException(status_code=404,detail="blog-not-found")
    return obj_in

