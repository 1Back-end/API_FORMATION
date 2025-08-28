from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/unit_product", tags=["unit_product"])


@router.post('/create', response_model=schemas.Msg, status_code=201)
async def create_unit_prodeuct(
    *,
    db: Session = Depends(get_db),
    obj_in=schemas.CategoryProductCreate
):
    exist_name = crud.unit_product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=401, detail="this-name-already-exist")
    crud.unit_product.create(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="unit-product-create-successfully"))


@router.put('/update', response_model=schemas.Msg, status_code=200)
async def update_unit_project(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.UnitProductUpdate
):
    exist_name = crud.unit_product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=401, detail="this-name-already-exist")
    crud.unit_product.update(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="unit-product-updated-successfully"))


@router.delete('/delete', response_model=schemas.Msg, status_code=200)
async def delete_unit_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.UnitProductDelete
):
    crud.unit_product.delete(db=db, uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="unitp-roduct-deleted-successfully"))


@router.put('/soft-delete', response_model=schemas.Msg, status_code=200)
async def soft_delete_unit_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.UnitProductDelete

):
    crud.unit_product.soft_delete(db=db, uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="unitproduct-deleted-successfully"))
