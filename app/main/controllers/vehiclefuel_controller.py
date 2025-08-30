from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/vehicle_fuel", tags=["vehicle_fuel"])


@router.post('/create',response_model=schemas.Msg,status_code=201)
async def create_vehicle_fuel(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleFuelCreate
): 
    exist_name=crud.vehicle_fuel.get_by_name(db=db,name=obj_in.name)
    if exist_name:
        raise HTTPException(status_code=409,detail="this name already exist")
    
    crud.vehicle_fuel.create(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="vehiclefuel-created-successfully"))


@router.put('/update',response_model=schemas.Msg,status_code=200)
async def update_vehicle_fuel(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleFuelUpdate

):
    crud.vehicle_fuel.update(db=db, obj_in=obj_in)
    return schemas.Msg(message=__(key="vehiclefuel-update-successfully"))

@router.delete('/delete',response_model=schemas.Msg,status_code=200)
async def delete_vehicle_fuel(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleFuelDelete

):
    crud.vehicle_fuel.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="vehiclefuel-deleted-successfully"))

@router.put('/soft_delete',response_model=schemas.Msg,status_code=200)
async def soft_delete_vehicle_fuel(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleFuelDelete

):
    crud.vehicle_fuel.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="vehiclefuel-deleted-successfully"))


@router.get('/get_by_uuid',response_model=schemas.VehicleFuelResponse,status_code=200)
async def get_vehicle_fuel_by_uuid(
    *,
    db: Session = Depends(get_db),
    uuid:str

):
    obj_in = crud.vehicle_fuel.get_by_uuid(db=db,uuid=uuid)
    if not obj_in:
        raise HTTPException(status_code=404,detail=__(key="vehicle_fuel-not-found"))
    return obj_in


@router.get("/get_many", response_model=None)
def get(
    *,
    db: Session = Depends(get_db),
    page: int = 1,
    per_page: int = 25,
):
    return crud.vehicle_fuel.get_many(
        db, 
        page, 
        per_page, 
    )