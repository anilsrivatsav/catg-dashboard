from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    sl_no = Column(Integer)
    date_of_receipt = Column(Date)
    unit_no = Column(String, ForeignKey("stalls.unit_no"))  # Foreign key to Stall
    stall = relationship("Stall", back_populates="payments")
    station = Column(String)
    pf_no = Column(String)
    name_of_licensee = Column(String)
    payment_head = Column(String)
    payment_sub_head = Column(String)
    period_from = Column(Date)
    period_to = Column(Date)
    amount = Column(Float)
    gst = Column(Float)
    mr_no = Column(String)
    mr_date = Column(Date)
    ua_case = Column(String)
    remarks = Column(String)
