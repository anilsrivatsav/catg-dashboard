from pydantic import BaseModel
from typing import Optional
from datetime import date

class StallBase(BaseModel):
    sl_no: Optional[int] = None
    unit_no: str
    type_of_unit: str
    station: str
    station_category: str
    old_category: Optional[str] = None
    pf_no: Optional[str] = None
    pegged_location: Optional[str] = None
    reservation_category: Optional[str] = None
    type_of_allotment: Optional[str] = None
    name_of_licensee: Optional[str] = None
    license_fee: Optional[float] = None
    contract_from: Optional[date] = None
    contract_to: Optional[date] = None
    license_fee_2: Optional[float] = None  # Remove if not needed
    unit_status: Optional[str] = None

class StallCreate(StallBase):
    pass

class Stall(StallBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {
            date: lambda v: v.isoformat() if isinstance(v, date) else v
        }
        json_decoders = {
            date: lambda v: date.fromisoformat(v) if isinstance(v, str) else v
        }