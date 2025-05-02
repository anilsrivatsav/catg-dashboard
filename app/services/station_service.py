from sqlalchemy.orm import Session
from app.models.stations import Station
from app.schemas.stations import StationCreate

def get_stations(db: Session):
    return db.query(Station).all()

def create_station(db: Session, station: StationCreate):
    db_station = Station(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

def get_station(db: Session, station_id: int):
    return db.query(Station).filter(Station.id == station_id).first()
def update_station(db: Session, station_id: int, station: StationCreate):
    update = Station(**station.dict())
    print("updating")
    db_station = get_station(db, station_id)
    for key in update.__dict__:
        if not hasattr(db_station, key) or getattr(db_station, key) != getattr(update, key):
            setattr(db_station, key, getattr(update, key))
    db.commit()
    db.refresh(db_station)
    return db_station
def delete_station(db: Session, station_id: int):
    db_station = get_station(db, station_id)
    if db_station:
        db.delete(db_station)
        db.commit()
        return True
    return False
def get_station_by_code(db: Session, station_code: str):
    return db.query(Station).filter(Station.station_code == station_code).first()
def get_stations_by_division(db: Session, division: str):
    return db.query(Station).filter(Station.division == division).all()
def get_stations_by_zone(db: Session, zone: str):
    return db.query(Station).filter(Station.zone == zone).all()
def get_stations_by_section(db: Session, section: str):
    return db.query(Station).filter(Station.section == section).all()
def get_stations_by_cmi(db: Session, cmi: str):
    return db.query(Station).filter(Station.cmi == cmi).all()
def get_stations_by_den(db: Session, den: str):
    return db.query(Station).filter(Station.den == den).all()
def get_stations_by_sr_den(db: Session, sr_den: str):
    return db.query(Station).filter(Station.sr_den == sr_den).all()
def get_stations_by_categorisation(db: Session, categorisation: str):
    return db.query(Station).filter(Station.categorisation == categorisation).all()
def get_stations_by_earnings_range(db: Session, earnings_range: str):
    return db.query(Station).filter(Station.earnings_range == earnings_range).all()
def get_stations_by_passenger_range(db: Session, passenger_range: str):
    return db.query(Station).filter(Station.passenger_range == passenger_range).all()