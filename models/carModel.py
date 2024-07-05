# -*- coding: utf-8 -*-
"""
File Name: carModel.py
Description: This script defines the Car model for representing and managing car
 data in the application.
Author: MathTeixeira
Date: July 4, 2024
Version: 2.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from sqlmodel import SQLModel, Field, Relationship
from schemas import CarSchema


class Car(SQLModel, table=True):
  """
  Car model for representing and managing car data in the application.

  Attributes:
    id (int): The unique identifier for the car.
    size (str, optional): The size of the car (e.g., s, m, l).
    fuel (str, optional): The type of fuel the car uses (e.g., gasoline, diesel, electric).
    doors (int, optional): The number of doors the car has.
    transmission (str, optional): The type of transmission (e.g., manual, automatic).
    trips (list[Trip]): A list of trips associated with the car.
  """
  # None will allow the database to generate the ID
  id: int | None = Field(None, primary_key=True)
  size: str | None = Field(None,
                           description="The size of the car (e.g., s, m, l)")
  fuel: str | None = Field(
      None,
      description=
      "The type of fuel the car uses (e.g., gasoline, diesel, electric)")
  doors: int | None = Field(None, description="The number of doors the car has")
  transmission: str | None = Field(
      None, description="The type of transmission (e.g., manual, automatic)")
  trips: list["Trip"] = Relationship(back_populates="car")

  def update(self, car: CarSchema) -> "Car":
    """
    Update the car attributes with new values.

    Args:
      car (CarSchema): The new car data to update.

    Returns:
      Car: The updated Car object.
    """
    for key, value in vars(car).items():
      setattr(self, key, value)
    return self

  def addTrip(self, trip: "Trip"):
    """
    Add a trip to the car's list of trips.

    Args:
      trip (Trip): The trip data to add.

    Returns:
      Car: The updated Car object.
    """
    # Add the trip to the car's trips list
    self.trips.append(trip)
    return self


from .tripModel import Trip
