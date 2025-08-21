from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/fournisseurs", tags=["fournisseurs"])


@router.post('/create',response_model=schemas.Msg,status_code=201)
async def create_fournisseur(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.QuinFourCreate
): 
    exist_phone_number1 = crud.fourisseur.get_by_phone_number1(db=db,phone_number1=obj_in.phone_number1)
    if exist_phone_number1:
        raise HTTPException(status_code=409,detail="phone-number-already-exist")
    
    if obj_in.phone_number2:
        exist_phone_number2 = crud.fourisseur.get_by_phone_number2(db=db,phone_number2=obj_in.phone_number2)
        if exist_phone_number2:
            raise HTTPException(status_code=409,detail="phone-number-already-exist")
        
    crud.fourisseur.create(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="fournisseur-created-successfully"))


@router.put('/update',response_model=schemas.Msg,status_code=200)
async def update_fournisseur(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.QuinFourUpdate

):
    exist_phone_number1 = crud.fourisseur.get_by_phone_number1(db=db,phone_number1=obj_in.phone_number1)
    if exist_phone_number1:
        raise HTTPException(status_code=409,detail="phone-number-already-exist")
    
    if obj_in.phone_number2:
        exist_phone_number2 = crud.fourisseur.get_by_phone_number2(db=db,phone_number2=obj_in.phone_number2)
        if exist_phone_number2:
            raise HTTPException(status_code=409,detail="phone-number-already-exist")
    crud.fourisseur.update(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="fournisseur-update-successfully"))

@router.delete('/delete',response_model=schemas.Msg,status_code=200)
async def delete_fournisseur(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.QuinFourDelete

):
    crud.fourisseur.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="fournisseur-deleted-successfully"))


@router.put('/soft_delete',response_model=schemas.Msg,status_code=200)
async def soft_delete_fournisseur(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.QuinFourDelete

):
    crud.fourisseur.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="fournisseur-deleted-successfully"))