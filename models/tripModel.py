# -*- coding: utf-8 -*-
"""
File Name: tripModel.py
Description: This script defines the TripModel for representing and managing
 trip data in the application. It extends the TripSchema used for data
 validation and serialization.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.2
License: MIT License
Contact Information: mathteixeira55
"""

# ### Imports ###
from sqlmodel import Field, Relationship
from schemas.tripSchema import TripSchema


class TripModel2(TripSchema, table=True):
  """
  TripModel for representing and managing trip data in the application.

  Attributes:
    id (int): The unique identifier for the trip.
    start (int): The starting Km of the trip.
    end (int): The ending Km of the trip.
    description (str): A description of the trip.
  """
  id: int | None = Field(
      None,
      primary_key=True,
      description="The unique identifier for the trip",
  )
  carId: int = Field(foreign_key="carmodel2.id",
                     description="The unique identifier for the car")
  car: "CarModel2" = Relationship(back_populates="trips")


class TripModel(TripSchema):
  """
  TripModel for representing and managing trip data in the application.

  Attributes:
    id (int): The unique identifier for the trip.
    start (int): The starting Km of the trip.
    end (int): The ending Km of the trip.
    description (str): A description of the trip.
  """
  id: int | None = Field(None, description="The unique identifier for the trip")


from .carModel import CarModel2
