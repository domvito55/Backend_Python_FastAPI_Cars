# -*- coding: utf-8 -*-
"""
File Name: cars.py
Description: This script defines the routers for managing cars in the car
 sharing service.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from typing import Union
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from core.database import carsDb
from schemas import CarSchema, DetailedCarSchema, ResponseSchema, DetailedResponseSchema
from models import Car
from utils import sizeQuery, doorsQuery, tripQuery, idPath

### Router Initialization ###
router = APIRouter()


# CRUD Operations for Cars
# Create
@router.post("/", summary="Add new car", response_model=ResponseSchema)
def addCar(
    car: CarSchema, session: Session = Depends(carsDb.getSession)
) -> ResponseSchema:
  """
  Add a new car to the database.

  Args:
    car (CarSchema): The car to add.

  Returns:
    ResponseSchema: A dictionary containing a success message and HTTP code.

  Raises:
    HTTPException: If the car data is invalid or there is an error adding the car to the database.
  """
  try:
    # Validate the car data
    carToAdd = Car.model_validate(car)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))

  try:
    # Add the car to the session
    session.add(carToAdd)
    # Save to the database
    session.commit()
    # Refresh the carToAdd object to get the ID generated by the database
    # This is necessary to get the updated state of the object, including any
    # changes made by the database
    session.refresh(carToAdd)
  except Exception as e:
    session.rollback()
    raise HTTPException(status_code=500,
                        detail=f"Failed to add car to the database: {e}")

  return ResponseSchema(message=carToAdd, code=200)


# Read "All" filtered by size and doors
@router.get(
    "/",
    summary="Get cars filtered by size and number of doors",
    response_model=Union[ResponseSchema, DetailedResponseSchema],
)
def getCars(
    size: str | None = sizeQuery,
    doors: int | None = doorsQuery,
    includeTrips: bool | None = tripQuery,
    session: Session = Depends(carsDb.getSession)
) -> ResponseSchema | DetailedResponseSchema:
  """
  Retrieve cars filtered by size and number of doors.

  Args:
    size (str, optional): The size to filter cars by (s, m, l).
    doors (int, optional): The number of doors to filter cars by.

  Returns:
    ResponseSchema: A dictionary containing the list of cars filtered by size and number of doors.

  Raises:
    HTTPException: If there is an error retrieving cars from the database.
  """
  try:
    query = select(Car)
    if size:
      query = query.where(Car.size == size)
    if doors:
      query = query.where(Car.doors == doors)
    # Execute the query and return the results
    # The .all() method converts the result into a list of all the results.
    # If .all() is not used, an iterator is returned which is not directly usable.
    # Using .all() ensures we get a list that can be easily returned and manipulated.
    filteredCars = session.exec(query).all()
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to retrieve cars: {e}")

  if includeTrips:
    detailed_cars = [
        DetailedCarSchema.model_validate(car) for car in filteredCars
    ]
    return DetailedResponseSchema(message=detailed_cars, code=200)
  return ResponseSchema(message=filteredCars, code=200)


# Read one by ID
@router.get(
    "/{id}",
    summary="Get car by ID",
    response_model=ResponseSchema,
)
def getCarById(
    id: int = idPath,
    session: Session = Depends(carsDb.getSession)
) -> ResponseSchema:
  """
  Retrieve a car by its ID.

  Args:
    id (int): The ID of the car to retrieve.

  Returns:
    ResponseSchema: A dictionary containing the car details if found, otherwise a message indicating it was not found.

  Raises:
    HTTPException: If the car with the given ID is not found or there is an error retrieving the car.
  """
  try:
    # get() looks for the object by its primary key and returns None if not found
    car = session.get(Car, id)
  except Exception as e:
    raise HTTPException(status_code=500,
                        detail=f"Failed to retrieve car by ID: {e}")

  if not car:
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")

  return ResponseSchema(message=car, code=200)


# Update
@router.put("/{id}", summary="Update car by ID", response_model=ResponseSchema)
def updateCar(
    car: CarSchema,
    id: int = idPath,
    session: Session = Depends(carsDb.getSession)
) -> ResponseSchema:
  """
  Update a car in the database by its ID.

  Args:
    id (int): The ID of the car to update.
    car (CarSchema): The updated car data.

  Returns:
    ResponseSchema: A dictionary containing the updated car details if found, otherwise a message indicating it was not found.

  Raises:
    HTTPException: If the car with the given ID is not found or there is an error updating the car in the database.
  """
  try:
    # get() looks for the object by its primary key and returns None if not found
    carToUpdate = session.get(Car, id)
  except Exception as e:
    raise HTTPException(status_code=500,
                        detail=f"Failed to retrieve car by ID: {e}")

  if not carToUpdate:
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")

  try:
    # Update the car attributes with the new values
    updatedCar = carToUpdate.update(car).model_dump()
    # Save the updated car to the database
    session.commit()
  except Exception as e:
    session.rollback()
    raise HTTPException(status_code=500, detail=f"Failed to update car: {e}")

  return ResponseSchema(message=updatedCar, code=200)


# Delete
@router.delete("/{id}",
               summary="Delete car by ID",
               response_model=ResponseSchema)
def deleteCar(
    id: int = idPath,
    session: Session = Depends(carsDb.getSession)
) -> ResponseSchema:
  """
  Delete a car from the database by its ID.

  Args:
    id (int): The ID of the car to delete.

  Returns:
    ResponseSchema: A dictionary containing a success message if the car was deleted, otherwise a message indicating it was not found.

  Raises:
    HTTPException: If the car with the given ID is not found or there is an error deleting the car from the database.
  """
  try:
    # get() looks for the object by its primary key and returns None if not found
    car = session.get(Car, id)
  except Exception as e:
    raise HTTPException(status_code=500,
                        detail=f"Failed to retrieve car by ID: {e}")

  if not car:
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")

  try:
    session.delete(car)
    # Save the changes to the database
    session.commit()
  except Exception as e:
    session.rollback()
    raise HTTPException(status_code=500, detail=f"Failed to delete car: {e}")

  return ResponseSchema(message=f"Car with ID {id} deleted successfully.",
                        code=200)