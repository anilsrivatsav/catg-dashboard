from pydantic import BaseModel
from typing import Optional

class StationBase(BaseModel):
    station_code: str
    station_name: str
    division: str
    zone: str
    section: Optional[str] = None
    cmi: Optional[str] = None
    den: Optional[str] = None
    sr_den: Optional[str] = None
    categorisation: Optional[str] = None
    earnings_range: Optional[str] = None
    passenger_range: Optional[str] = None
    passenger_footfall: Optional[int] = None
    platforms: Optional[str] = None
    number_of_platforms: Optional[int] = None
    platform_type: Optional[str] = None
    parking: Optional[bool] = None
    pay_and_use: Optional[bool] = None

class StationCreate(StationBase):
    pass

class Station(StationBase):
    id: int

    class Config:
        orm_mode = True
