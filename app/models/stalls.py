from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from app.models.database import Base
from sqlalchemy.orm import relationship
class Stall(Base):
    __tablename__ = "stalls"
    id = Column(Integer, index=True)
    sl_no = Column(Integer, nullable=True)
    unit_no = Column(String, unique=True, primary_key=True,index=True)
    type_of_unit = Column(String)
    station = Column(String, ForeignKey("stations.station_code"))
    station_category = Column(String)
    old_category = Column(String, nullable=True)
    pf_no = Column(String, nullable=True)
    pegged_location = Column(String, nullable=True)
    reservation_category = Column(String, nullable=True)
    type_of_allotment = Column(String, nullable=True)
    name_of_licensee = Column(String, nullable=True)
    license_fee = Column(Float, nullable=True)
    contract_from = Column(Date, nullable=True)
    contract_to = Column(Date, nullable=True)
    license_fee_2 = Column(Float, nullable=True)
    unit_status = Column(String, nullable=True)
    # Add any additional fields as needed
    payments = relationship("Payment", back_populates="stall")
    station_rel = relationship("Station", back_populates="stalls")