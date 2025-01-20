# app/models.py

from sqlalchemy import Column, Integer, Float, String
from .database import Base

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    housing_median_age = Column(Integer)
    total_rooms = Column(Integer)
    total_bedrooms = Column(Integer)
    population = Column(Integer)
    households = Column(Integer)
    median_income = Column(Float)
    median_house_value = Column(Float)
    ocean_proximity = Column(String)  # Choix restreint possible, mais on laisse String pour simplifier

