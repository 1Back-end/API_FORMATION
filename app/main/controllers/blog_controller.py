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


@router.post("/create",response_model=schemas.Msg,status_code=201)
async def create_blog(
    *,
    db: Session = Depends(get_db),
    obj_in : schemas.BlogCreate,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))
):
    exist_blog = crud.blog.get_by_name(db=db,name=obj_in.name)
    if exist_blog:
        raise HTTPException(status_code=409,detail=__(key="blog-already-exist"))
    
    category_blog = crud.category_blog.get_by_uuid(db=db,uuid=obj_in.category_uuid)
    if not category_blog:
        raise HTTPException(status_code=404,detail=__(key="category-blog-not-found"))
    crud.blog.create(
        db=db,
        obj_in=obj_in,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="blog-created-successfully"))