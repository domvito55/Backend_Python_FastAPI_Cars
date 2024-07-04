# -*- coding: utf-8 -*-
"""
File Name: carsharing.py
Description: This script initializes a FastAPI web application for a car sharing
 service. It provides endpoints for welcoming users, retrieving a list of
 available cars filtered by size and number of doors, and adding new cars to the
 database.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from fastapi import FastAPI, HTTPException
from repositories.carRepository import CarRepository
from schemas.carSchema import CarSchema
from schemas.tripSchema import TripSchema
from schemas.responseSchema import ResponseSchema
from models.carModel import CarModel
from models.tripModel import TripModel
from utils.docDetails import sizeQuery, doorsQuery, idPath

# Initialize the repository
carRepository = CarRepository("./database/carsDb.json")

### Initialize FastAPI App ###
app = FastAPI(title="Car Sharing API", version="1.0.0")


### API Endpoints ###
# Health Check Endpoint
@app.get("/",
         tags=["Health Check"],
         summary="Health Check",
         response_model=ResponseSchema)
def welcome() -> ResponseSchema:
  """
  Welcome endpoint for the Car Sharing API.

  Returns:
    ResponseSchema: A dictionary containing a welcome message.
  """
  return ResponseSchema(message="Welcome to the Car Sharing API!", code=200)


# CRUD Operations for Cars
# Create
@app.post("/api/cars",
          tags=["Cars"],
          summary="Add new car",
          response_model=ResponseSchema)
def addCar(car: CarSchema) -> ResponseSchema:
  """
  Add a new car to the database.

  Args:
    car (CarSchema): The car to add.

  Returns:
    ResponseSchema: A dictionary containing a success message and the added car's ID.
  """
  # Add the car to the repository
  addedCar = carRepository.addCar(car)

  # Save the updated repository to the database
  carRepository.saveCarDb()

  return ResponseSchema(message=addedCar, code=200)


# Read "All" filtered by size and doors
@app.get(
    "/api/cars",
    tags=["Cars"],
    summary="Get cars filtered by size and number of doors",
    response_model=ResponseSchema,
)
def getCars(size: str | None = sizeQuery,
            doors: int | None = doorsQuery) -> ResponseSchema:
  """
  Retrieve cars filtered by size and number of doors.

  Args:
    size (str, optional): The size to filter cars by (s, m, l).
    doors (int, optional): The number of doors to filter cars by.

  Returns:
    ResponseSchema: A dictionary containing the list of cars filtered by size and number of doors.

  Raises:
    HTTPException: If no cars are available in the database.
  """
  if not carRepository.cars:
    raise HTTPException(status_code=404,
                        detail="No cars available in the database")

  filteredCars = carRepository.cars
  if size:
    filteredCars = [car for car in filteredCars if car.size == size]
  if doors:
    filteredCars = [car for car in filteredCars if car.doors == doors]

  return ResponseSchema(message=filteredCars, code=200)


# Read one by ID
@app.get(
    "/api/cars/{id}",
    tags=["Cars"],
    summary="Get car by ID",
    response_model=ResponseSchema,
)
def getCarById(id: int = idPath) -> ResponseSchema:
  """
  Retrieve a car by its ID.

  Args:
    id (int): The ID of the car to retrieve.

  Returns:
    ResponseSchema: A dictionary containing the car details if found, otherwise a message indicating it was not found.
  """
  car = carRepository.findCarById(id)
  return ResponseSchema(message=car, code=200)


# Update
@app.put("/api/cars/{id}",
         tags=["Cars"],
         summary="Update car by ID",
         response_model=ResponseSchema)
def updateCar(id: int = idPath, car: CarSchema = None) -> ResponseSchema:
  """
  Update a car in the database by its ID.

  Args:
    id (int): The ID of the car to update.
    car (CarSchema): The updated car data.

  Returns:
    ResponseSchema: A dictionary containing the updated car details if found, otherwise a message indicating it was not found.
  """
  # Find the car to update by its ID
  carToUpdate = carRepository.findCarById(id)

  # Update the car object in the repository with the new data
  updatedCar = carToUpdate.update(car)

  # Save the updated repository to the database
  carRepository.saveCarDb()
  return ResponseSchema(message=updatedCar, code=200)


@app.put("/api/cars/{id}/trips",
         tags=["Cars"],
         summary="Add trip to car by ID",
         response_model=ResponseSchema)
def addTrip(id: int = idPath, trip: TripSchema = None) -> ResponseSchema:
  """
  Add a trip to a car by its ID.

  Args:
    id (int): The ID of the car to add a trip to.
    trip (TripSchema): The trip data to add.

  Returns:
    ResponseSchema: A dictionary containing the updated car details with the added trip if found, otherwise a message indicating it was not found.
  """
  # Find the car to update by its ID
  carToUpdate = carRepository.findCarById(id)

  # Add the trip to the car's trips list
  carToUpdate.addTrip(trip)

  # Save the updated repository to the database
  carRepository.saveCarDb()
  return ResponseSchema(message=carToUpdate, code=200)


# Delete
@app.delete("/api/cars/{id}",
            tags=["Cars"],
            summary="Delete car by ID",
            response_model=ResponseSchema)
def deleteCar(id: int = idPath) -> ResponseSchema:
  """
  Delete a car from the database by its ID.

  Args:
    id (int): The ID of the car to delete.

  Returns:
    ResponseSchema: A dictionary containing a success message if the car was deleted, otherwise a message indicating it was not found.
  """
  # Find the car to delete by its ID
  car = carRepository.findCarById(id)

  # Remove the car from the list
  carRepository.cars.remove(car)

  # Save the updated list to the database
  carRepository.saveCarDb()
  return ResponseSchema(message=f"Car with ID {id} deleted successfully.",
                        code=200)


if __name__ == "__main__":
  import uvicorn

  uvicorn.run("carsharing:app", host="0.0.0.0", port=8000, reload=True)
