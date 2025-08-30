from datetime import timedelta, datetime
from typing import Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from app.main.core.dependencies import TokenRequired

router = APIRouter(prefix="/vehicles", tags=["vehicles"])


@router.post("/create",response_model=schemas.Msg,status_code=201)
async def create_vehicle(
    *,
    db: Session = Depends(get_db),
    obj_in : schemas.VehicleCreate,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))
):
    exist_vehicle = crud.vehicle.get_by_name(db=db,name=obj_in.name)
    if exist_vehicle:
        raise HTTPException(status_code=409,detail=__(key="vehicle-already-exist"))
    
    vehicle_brand = crud.vehicle_brand.get_by_uuid(db=db,uuid=obj_in.vehicle_brand_uuid)
    if not vehicle_brand:
        raise HTTPException(status_code=404,detail=__(key="vehicle-brand-not-found"))
    
    vehicle_fuel = crud.vehicle_fuel.get_by_uuid(db=db,uuid=obj_in.vehicle_fuel_uuid)
    if not vehicle_fuel:
        raise HTTPException(status_code=404,detail=__(key="vehicle-fuel-not-found"))
    
    crud.vehicle.create(
        db=db,
        obj_in=obj_in,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="vehicle-created-successfully"))



@router.put("/update",response_model=schemas.Msg,status_code=201)
async def create_vehicle(
    *,
    db: Session = Depends(get_db),
    obj_in : schemas.VehicleCreate,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))
):
    exist_vehicle = crud.vehicle.get_by_name(db=db,name=obj_in.name)
    if exist_vehicle:
        raise HTTPException(status_code=409,detail=__(key="vehicle-already-exist"))
    
    vehicle_brand = crud.vehicle_brand.get_by_uuid(db=db,uuid=obj_in.vehicle_brand_uuid)
    if not vehicle_brand:
        raise HTTPException(status_code=404,detail=__(key="vehicle-brand-not-found"))
    
    vehicle_fuel = crud.vehicle_fuel.get_by_uuid(db=db,uuid=obj_in.vehicle_fuel_uuid)
    if not vehicle_fuel:
        raise HTTPException(status_code=404,detail=__(key="vehicle-fuel-not-found"))
    
    crud.vehicle.update(
        db=db,
        obj_in=obj_in,
        added_by=current_user.uuid
    )
    return schemas.Msg(message=__(key="vehicle-updated-successfully"))



@router.delete('/delete',response_model=schemas.Msg,status_code=200)
async def delete_vehicle(
     *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleDelete,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))

):
    crud.vehicle.delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="vehicule-deleted-successfully"))

@router.put('/soft_delete',response_model=schemas.Msg,status_code=200)
async def soft_delete_vehicle_brand(
    *,
    db: Session = Depends(get_db),
    obj_in:schemas.VehicleDelete,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))

):
    crud.vehicle.soft_delete(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message=__(key="vehicle-deleted-successfully"))


@router.get('/get_by_uuid',response_model=schemas.VehicleResponse,status_code=200)
async def get_vehicle_brand_by_uuid(
    *,
    db: Session = Depends(get_db),
    uuid:str,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))

):
    obj_in = crud.vehicle.get_by_uuid(db=db,uuid=uuid)
    if not obj_in:
        raise HTTPException(status_code=404,detail=__(key="vehicle_brand-not-found"))
    return obj_in



@router.get("/get_many", response_model=None)
def get(
    *,
    db: Session = Depends(get_db),
    page: int = 1,
    per_page: int = 25,
    current_user: models.User = Depends(TokenRequired(roles=["SUPER_ADMIN"]))
):
    return crud.vehicle.get_many(
        db, 
        page, 
        per_page, 
    )