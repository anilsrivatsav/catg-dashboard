from typing import Optional
from sqlalchemy.orm import Session
from app.models.stalls import Stall
from app.schemas.stalls import StallCreate

def get_stalls(db: Session):
    return db.query(Stall).all()

def create_stall(db: Session, stall: StallCreate):
    db_stall = Stall(**stall.dict())
    db.add(db_stall)
    db.commit()
    db.refresh(db_stall)
    return db_stall

def get_stall(db: Session, stall_id: int) -> Optional[Stall]:
    return db.query(Stall).filter(Stall.id == stall_id).first()

def update_stall(db: Session, stall_id: int, stall: StallCreate) -> bool:
    db_stall = get_stall(db=db, stall_id=stall_id)
    if db_stall is None:
        return False
    for key, value in stall.dict().items():
        setattr(db_stall, key, value)
    db.commit()
    return True

def delete_stall(db: Session, stall_id: int) -> bool:
    db_stall = get_stall(db=db, stall_id=stall_id)
    if db_stall is None:
        return False
    db.delete(db_stall)
    db.commit()
    return True

def get_stall_by_unit_no(db: Session, unit_no: str) -> Optional[Stall]:
    return db.query(Stall).filter(Stall.unit_no == unit_no).first()

def get_stalls_by_station(db: Session, station: str):
    return db.query(Stall).filter(Stall.station == station).all()

def get_stalls_by_station_category(db: Session, station_category: str):
    return db.query(Stall).filter(Stall.station_category == station_category).all()

def get_stalls_by_old_category(db: Session, old_category: str):
    return db.query(Stall).filter(Stall.old_category == old_category).all()

def get_stalls_by_pf_no(db: Session, pf_no: str):
    return db.query(Stall).filter(Stall.pf_no == pf_no).all()

def get_stalls_by_pegged_location(db: Session, pegged_location: str):
    return db.query(Stall).filter(Stall.pegged_location == pegged_location).all()

def get_stalls_by_reservation_category(db: Session, reservation_category: str):
    return db.query(Stall).filter(Stall.reservation_category == reservation_category).all()

def get_stalls_by_type_of_allotment(db: Session, type_of_allotment: str):
    return db.query(Stall).filter(Stall.type_of_allotment == type_of_allotment).all()

def get_stalls_by_name_of_licensee(db: Session, name_of_licensee: str):
    return db.query(Stall).filter(Stall.name_of_licensee == name_of_licensee).all()

def get_stalls_by_license_fee(db: Session, license_fee: float):
    return db.query(Stall).filter(Stall.license_fee == license_fee).all()

def get_stalls_by_contract_from(db: Session, contract_from: str):
    return db.query(Stall).filter(Stall.contract_from == contract_from).all()

def get_stalls_by_contract_to(db: Session, contract_to: str):
    return db.query(Stall).filter(Stall.contract_to == contract_to).all()

def get_stalls_by_license_fee_2(db: Session, license_fee_2: float):
    return db.query(Stall).filter(Stall.license_fee_2 == license_fee_2).all()

def get_stalls_by_unit_status(db: Session, unit_status: str):
    return db.query(Stall).filter(Stall.unit_status == unit_status).all()
