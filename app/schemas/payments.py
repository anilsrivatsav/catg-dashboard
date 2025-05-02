from pydantic import BaseModel
from typing import Optional
from datetime import date

class PaymentBase(BaseModel):
    sl_no: Optional[int] = None
    date_of_receipt: date
    unit_no: str  # Foreign key to Stall
    station: str
    pf_no: Optional[str] = None
    name_of_licensee: Optional[str] = None
    payment_head: Optional[str] = None
    payment_sub_head: Optional[str] = None
    period_from: Optional[date] = None
    period_to: Optional[date] = None
    amount: Optional[float] = None
    gst: Optional[float] = None
    mr_no: Optional[str] = None
    mr_date: Optional[date] = None
    ua_case: Optional[str] = None
    remarks: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True
