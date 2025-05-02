from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.stations import Station, StationCreate
from app.services.station_service import (
    get_stations, create_station, get_station, update_station, delete_station,
    get_station_by_code, get_stations_by_division, get_stations_by_zone,
    get_stations_by_section, get_stations_by_cmi, get_stations_by_den,
    get_stations_by_sr_den, get_stations_by_categorisation,
    get_stations_by_earnings_range, get_stations_by_passenger_range,
)
from app.models.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Station])
def read_stations(db: Session = Depends(get_db)):
    return get_stations(db)

@router.post("/", response_model=Station, status_code=status.HTTP_201_CREATED)
def add_station(station: StationCreate, db: Session = Depends(get_db)):
    db_station = create_station(db, station)
    return db_station

@router.get("/{station_id}", response_model=Station)
def read_station(station_id: int, db: Session = Depends(get_db)):
    db_station = get_station(db, station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station

@router.put("/{station_id}", response_model=Station)
def update_station_endpoint(station_id: int, station: StationCreate, db: Session = Depends(get_db)):
    db_station = update_station(db, station_id, station)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station

@router.delete("/{station_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_station_endpoint(station_id: int, db: Session = Depends(get_db)):
    success = delete_station(db, station_id)
    if not success:
        raise HTTPException(status_code=404, detail="Station not found")
    return

@router.get("/code/{station_code}", response_model=Station)
def read_station_by_code(station_code: str, db: Session = Depends(get_db)):
    db_station = get_station_by_code(db, station_code)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station

@router.get("/division/{division}", response_model=List[Station])
def read_stations_by_division(division: str, db: Session = Depends(get_db)):
    return get_stations_by_division(db, division)

@router.get("/zone/{zone}", response_model=List[Station])
def read_stations_by_zone(zone: str, db: Session = Depends(get_db)):
    return get_stations_by_zone(db, zone)

@router.get("/section/{section}", response_model=List[Station])
def read_stations_by_section(section: str, db: Session = Depends(get_db)):
    return get_stations_by_section(db, section)

@router.get("/cmi/{cmi}", response_model=List[Station])
def read_stations_by_cmi(cmi: str, db: Session = Depends(get_db)):
    return get_stations_by_cmi(db, cmi)

@router.get("/den/{den}", response_model=List[Station])
def read_stations_by_den(den: str, db: Session = Depends(get_db)):
    return get_stations_by_den(db, den)

@router.get("/srden/{sr_den}", response_model=List[Station])
def read_stations_by_sr_den(sr_den: str, db: Session = Depends(get_db)):
    return get_stations_by_sr_den(db, sr_den)

@router.get("/categorisation/{categorisation}", response_model=List[Station])
def read_stations_by_categorisation(categorisation: str, db: Session = Depends(get_db)):
    return get_stations_by_categorisation(db, categorisation)

@router.get("/earnings-range/{earnings_range}", response_model=List[Station])
def read_stations_by_earnings_range(earnings_range: str, db: Session = Depends(get_db)):
    return get_stations_by_earnings_range(db, earnings_range)

@router.get("/passenger-range/{passenger_range}", response_model=List[Station])
def read_stations_by_passenger_range(passenger_range: str, db: Session = Depends(get_db)):
    return get_stations_by_passenger_range(db, passenger_range)
