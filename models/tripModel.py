# -*- coding: utf-8 -*-
"""
File Name: tripModel.py
Description: This script defines the Trip model for representing and managing
 trip data in the application.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from sqlmodel import Field, Relationship, SQLModel


class Trip(SQLModel, table=True):
  """
  Trip model for representing and managing trip data in the application.

  Attributes:
    id (int): The unique identifier for the trip.
    start (int): The starting Km of the trip.
    end (int): The ending Km of the trip.
    description (str): A description of the trip.
    carId (int): The unique identifier for the car.
    car (Car): The car associated with the trip.
  """
  id: int | None = Field(
      None,
      primary_key=True,
      description="The unique identifier for the trip",
  )
  start: int = Field(..., description="The starting Km of the trip")
  end: int = Field(..., description="The ending Km of the trip")
  description: str = Field(..., description="A description of the trip")
  carId: int = Field(foreign_key="car.id",
                     description="The unique identifier for the car")
  car: "Car" = Relationship(back_populates="trips")


from .carModel import Car
