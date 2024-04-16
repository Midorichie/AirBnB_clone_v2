#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class PlaceAmenity(Base):
    __tablename__ = 'place_amenity'

    place_id = Column(
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
            )
    amenity_id = Column(
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
            )
