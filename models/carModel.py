# -*- coding: utf-8 -*-
"""
File Name: carModel.py
Description: This script defines the CarModel for representing and managing car
  data in the application.
  It extends the CarSchema used for data validation and serialization.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.2
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import Field
from schemas.carSchema import CarSchema
from schemas.tripSchema import TripSchema
from .tripModel import TripModel


class CarModel(CarSchema):
  """
  CarModel for representing and managing car data in the application.

  Attributes:
    id (int): The unique identifier for the car.
    size (str, optional): The size of the car (e.g., s, m, l).
    fuel (str): The type of fuel the car uses (e.g., gasoline, diesel, electric).
    doors (int): The number of doors the car has.
    transmission (str): The type of transmission (e.g., manual, automatic).
    trips (list[TripModel]): A list of trips associated with the car.
  """
  id: int = Field(..., example=10)
  trips: list[TripModel] = Field(
      [], example=[TripModel(start=0, end=5, description="From store to home")])

  def update(self, car: CarSchema):
    """
    Update the car attributes with new values.

    Args:
      car (CarSchema): The new car data to update.

    Returns:
      CarModel: The updated CarModel object.
    """
    for key, value in vars(car).items():
      setattr(self, key, value)
    return self

  def addTrip(self, trip: TripSchema):
    """
    Add a trip to the car's list of trips.

    Args:
      trip (TripSchema): The trip data to add.

    Returns:
      CarModel: The updated CarModel object.
    """
    # Convert TripSchema object to dictionary
    tripData = trip.model_dump()

    # Assign a unique ID to the trip
    tripData['id'] = len(self.trips) + 1

    # Create a TripModel object using the dictionary
    tripToAdd = TripModel(**tripData)

    # Add the trip to the car's trips list
    self.trips.append(tripToAdd)

    return self
