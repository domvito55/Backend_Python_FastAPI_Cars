# -*- coding: utf-8 -*-
"""
File Name: trips.py
Description: This script defines the router for managing trips in the car
 sharing service.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from core.database import carsDb
from schemas import TripSchema, ResponseSchema
from models import Trip, Car

### Router Initialization ###
router = APIRouter()


# CRUD Operations for Trips
# Create
@router.post("/{carId}",
             summary="Add trip by car ID",
             response_model=ResponseSchema)
def addTrip(
    trip: TripSchema, carId: int,
    session: Session = Depends(carsDb.getSession)) -> ResponseSchema:
  """
  Add a trip to a car by its ID.

  Args:
    id (int): The ID of the car to add a trip to.
    trip (TripSchema): The trip data to add.

  Returns:
    ResponseSchema: A dictionary containing the updated car details with the added trip if found, otherwise a message indicating it was not found.

  Raises:
    HTTPException: If the car with the given ID is not found or there is an error adding the trip to the car.
  """
  try:
    # get() looks for the object by its primary key and returns None if not found
    carToUpdate = session.get(Car, carId)
  except Exception as e:
    raise HTTPException(status_code=500,
                        detail=f"Failed to retrieve car by ID: {e}")

  if not carToUpdate:
    raise HTTPException(status_code=404,
                        detail=f"Car with id {carId} not found")

  try:
    # Add the trip to the car's trips list
    tripModel = Trip.model_validate(trip, update={"carId": carId})
    carToUpdate.addTrip(tripModel)
    # Save the updated car to the database
    session.commit()
    # Refresh the carToUpdate object to get the updated state of the object, including any changes made by the database
    session.refresh(carToUpdate)
  except Exception as e:
    session.rollback()
    raise HTTPException(status_code=500,
                        detail=f"Failed to add trip to car: {e}")

  return ResponseSchema(message=carToUpdate, code=200)
