from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.stalls import Stall, StallCreate
from app.services.stall_service import (
    get_stalls, create_stall, get_stall, update_stall, delete_stall,
    get_stall_by_unit_no, get_stalls_by_station, get_stalls_by_station_category,
    get_stalls_by_old_category, get_stalls_by_pf_no, get_stalls_by_pegged_location,
    get_stalls_by_reservation_category, get_stalls_by_type_of_allotment,
    get_stalls_by_name_of_licensee, get_stalls_by_license_fee,
    get_stalls_by_contract_from, get_stalls_by_contract_to,
    get_stalls_by_license_fee_2, get_stalls_by_unit_status
)
from app.models.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Endpoints

@router.get("/", response_model=List[Stall])
def read_stalls(db: Session = Depends(get_db)):
    return get_stalls(db)

@router.post("/", response_model=Stall, status_code=status.HTTP_201_CREATED)
def add_stall(stall: StallCreate, db: Session = Depends(get_db)):
    db_stall = create_stall(db, stall)
    return db_stall

@router.get("/{stall_id}", response_model=Stall)
def read_stall(stall_id: int, db: Session = Depends(get_db)):
    db_stall = get_stall(db, stall_id)
    if db_stall is None:
        raise HTTPException(status_code=404, detail="Stall not found")
    return db_stall

@router.put("/{stall_id}", response_model=bool)
def update_stall_endpoint(stall_id: int, stall: StallCreate, db: Session = Depends(get_db)):
    updated = update_stall(db, stall_id, stall)
    if not updated:
        raise HTTPException(status_code=404, detail="Stall not found")
    return updated

@router.delete("/{stall_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stall_endpoint(stall_id: int, db: Session = Depends(get_db)):
    deleted = delete_stall(db, stall_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Stall not found")
    return

# Custom Filter Endpoints

@router.get("/unit_no/{unit_no}", response_model=Stall)
def read_stall_by_unit_no(unit_no: str, db: Session = Depends(get_db)):
    db_stall = get_stall_by_unit_no(db, unit_no)
    if db_stall is None:
        raise HTTPException(status_code=404, detail="Stall not found")
    return db_stall

@router.get("/station/{station}", response_model=List[Stall])
def read_stalls_by_station(station: str, db: Session = Depends(get_db)):
    return get_stalls_by_station(db, station)

@router.get("/station_category/{station_category}", response_model=List[Stall])
def read_stalls_by_station_category(station_category: str, db: Session = Depends(get_db)):
    return get_stalls_by_station_category(db, station_category)

@router.get("/old_category/{old_category}", response_model=List[Stall])
def read_stalls_by_old_category(old_category: str, db: Session = Depends(get_db)):
    return get_stalls_by_old_category(db, old_category)

@router.get("/pf_no/{pf_no}", response_model=List[Stall])
def read_stalls_by_pf_no(pf_no: str, db: Session = Depends(get_db)):
    return get_stalls_by_pf_no(db, pf_no)

@router.get("/pegged_location/{pegged_location}", response_model=List[Stall])
def read_stalls_by_pegged_location(pegged_location: str, db: Session = Depends(get_db)):
    return get_stalls_by_pegged_location(db, pegged_location)

@router.get("/reservation_category/{reservation_category}", response_model=List[Stall])
def read_stalls_by_reservation_category(reservation_category: str, db: Session = Depends(get_db)):
    return get_stalls_by_reservation_category(db, reservation_category)

@router.get("/type_of_allotment/{type_of_allotment}", response_model=List[Stall])
def read_stalls_by_type_of_allotment(type_of_allotment: str, db: Session = Depends(get_db)):
    return get_stalls_by_type_of_allotment(db, type_of_allotment)

@router.get("/name_of_licensee/{name_of_licensee}", response_model=List[Stall])
def read_stalls_by_name_of_licensee(name_of_licensee: str, db: Session = Depends(get_db)):
    return get_stalls_by_name_of_licensee(db, name_of_licensee)

@router.get("/license_fee/{license_fee}", response_model=List[Stall])
def read_stalls_by_license_fee(license_fee: float, db: Session = Depends(get_db)):
    return get_stalls_by_license_fee(db, license_fee)

@router.get("/contract_from/{contract_from}", response_model=List[Stall])
def read_stalls_by_contract_from(contract_from: str, db: Session = Depends(get_db)):
    return get_stalls_by_contract_from(db, contract_from)

@router.get("/contract_to/{contract_to}", response_model=List[Stall])
def read_stalls_by_contract_to(contract_to: str, db: Session = Depends(get_db)):
    return get_stalls_by_contract_to(db, contract_to)

@router.get("/license_fee_2/{license_fee_2}", response_model=List[Stall])
def read_stalls_by_license_fee_2(license_fee_2: float, db: Session = Depends(get_db)):
    return get_stalls_by_license_fee_2(db, license_fee_2)

@router.get("/unit_status/{unit_status}", response_model=List[Stall])
def read_stalls_by_unit_status(unit_status: str, db: Session = Depends(get_db)):
    return get_stalls_by_unit_status(db, unit_status)
