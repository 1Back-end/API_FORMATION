from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/product", tags=["product"])


@router.post('/create', response_model=schemas.Msg, status_code=201)
async def create_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.ProductCreate,
    current_user: models.User = Depends(
        TokenRequired(roles=["SUPER_ADMIN", "ADMIN"]))

):
    exist_name = crud.product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409, detail="product-already-exist")

    category = crud.category_product.get_by_uuid(
        db=db, uuid=obj_in.category_product_uuid)
    if not category:
        raise HTTPException(
            status_code=404, detail="category-product-not-found")

    unit = crud.unit_product.get_by_uuid(db=db, uuid=obj_in.unit_product_uuid)
    if not unit:
        raise HTTPException(status_code=409, detail="unit-product-not-found")
    crud.product.create(
        db=db,
        obj_in=obj_in,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="product-create-successfully"))


@router.put('/update', response_model=schemas.Msg, status_code=200)
async def update_product(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.ProductUpdate,
    current_user: models.User = Depends(
        TokenRequired(roles=["SUPER_ADMIN", "ADMIN"]))
):
    exist_name = crud.product.get_by_name(db=db, name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409, detail="this-name-already-exist")

    category = crud.category_product.get_by_uuid(
        db=db, uuid=obj_in.category_product_uuid)
    if not category:
        raise HTTPException(
            status_code=404, detail="category-product-not-found")

    unit = crud.unit_product.get_by_uuid(db=db, uuid=obj_in.unit_product_uuid)
    if not unit:
        raise HTTPException(status_code=409, detail="unit-product-not-found")
    crud.product.update(
        db=db,
        obj_in=obj_in,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="product-update-successfully"))


@router.delete('/delete', response_model=schemas.Msg, status_code=200)
async def product_delete(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.ProductDelete,
    current_user: models.User = Depends(
        TokenRequired(roles=["SUPER_ADMIN", "ADMIN"]))
):
    crud.product.delete(
        db=db,
        uuid=obj_in.uuid,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="product-deleted-successfully"))


@router.put('/soft_delete', response_model=schemas.Msg, status_code=200)
async def soft_product_delete(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.ProductDelete,
    current_user: models.User = Depends(
        TokenRequired(roles=["SUPER_ADMIN", "ADMIN"]))
):
    crud.category_product.soft_delete(
        db=db,
        uuid=obj_in.uuid,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="product-deleted-successfully"))


@router.get('/get_by_uuid', response_model=schemas.Product, status_code=200)
async def get_product_by_uuid(
    *,
    db: Session = Depends(get_db),
    uuid: str,
    current_user: models.User = Depends(
        TokenRequired(roles=["SUPER_ADMIN", "ADMIN"]))

):
    obj_in = crud.product_crud.get_by_uuid(
        db=db,
        uuid=uuid,
        added_by=current_user.uuid
    )
    if not obj_in:
        raise HTTPException(status_code=404, detail="product-not-found")
    return obj_in
