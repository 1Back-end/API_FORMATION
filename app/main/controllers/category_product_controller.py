from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/category_product", tags=["category_product"])


@router.post('/create', response_model=schemas.Msg, status_code=201)
async def create_category_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.CategoryProductCreate,
):

    exist_name = crud.category_product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409, detail="This-Name-Already-Exist")
    crud.category_product.create(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="categoryproduct-created-successfully"))


@router.put('/update', response_model=schemas.Msg, status_code=200)
async def update_category_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.CategoryProductUpdate
):

    exist_name = crud.category_product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409, detail="This-Name-Already-Exist")
    crud.category_product.update(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="categoryproduct-update-successfully"))


@router.delete('/delete', response_model=schemas.Msg, status_code=200)
async def category_product_delete(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.CategoryProductDelete,
):
    crud.category_product.delete(db=db, uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="categoryproduct-deleted-successfully"))


@router.put('/soft_delete', response_model=schemas.Msg, status_code=200)
async def soft_category_product_delete(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.CategoryProductDelete,
):
    crud.category_product.soft_delete(db=db, uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="categoryproduct-deleted-successfully"))
