from sqlalchemy import Column, Integer, String, Boolean
from app.models.database import Base
from sqlalchemy.orm import relationship
class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer,  index=True)
    station_code = Column(String, unique=True, primary_key=True, index=True)
    station_name = Column(String)
    division = Column(String)
    zone = Column(String)
    section = Column(String, nullable=True)
    cmi = Column(String, nullable=True)
    den = Column(String, nullable=True)
    sr_den = Column(String, nullable=True)
    categorisation = Column(String, nullable=True)
    earnings_range = Column(String, nullable=True)
    passenger_range = Column(String, nullable=True)
    passenger_footfall = Column(Integer, nullable=True)
    platforms = Column(String, nullable=True)
    number_of_platforms = Column(Integer, nullable=True)
    platform_type = Column(String, nullable=True)
    parking = Column(Boolean, nullable=True)
    pay_and_use = Column(Boolean, nullable=True)
    stalls = relationship("Stall", back_populates="station")