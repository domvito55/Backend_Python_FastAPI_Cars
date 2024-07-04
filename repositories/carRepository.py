# -*- coding: utf-8 -*-
"""
File Name: carRepository.py
Description: This script defines a repository class for interacting with the car
  database (JSON file).
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.2
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
import json
from fastapi import HTTPException
from pydantic import ValidationError
from models.carModel import CarModel
from schemas.carSchema import CarSchema


class CarRepository:
  """
  A repository class for managing car data stored in a JSON file.

  Attributes:
    file (str): The path to the JSON file containing the car data.
    cars (list[CarModel]): The list of CarModel objects loaded from the JSON file.

  Methods:
    importCarsDb: Imports and validates car data from a JSON file.
    addCar: Adds a new car to the database.
    findCarById: Finds a car by its ID.
    removeCar: Removes a car from the database.
    saveCarDb: Saves the updated data to the JSON file.
  """

  def __init__(self, file: str):
    """
    Initializes the CarRepository with the path to the JSON file.

    Args:
      file (str): The path to the JSON file containing the car data.
    """
    self.file = file
    self.cars = self.importCarsDb()

  def importCarsDb(self) -> list[CarModel]:
    """
    Imports a list of cars from a JSON file and validates them using the Car model.

    Returns:
      list[CarModel]: A list of CarModel objects validated against the Car model.

    Raises:
      HTTPException: If the file is not found, the JSON data is invalid, or validation fails.
    """
    try:
      with open(self.file, "r") as f:
        return [CarModel.model_validate(obj) for obj in json.load(f)]
    except FileNotFoundError:
      raise HTTPException(status_code=500, detail="Database file not found")
    except json.JSONDecodeError:
      raise HTTPException(status_code=500,
                          detail="Error decoding JSON from database file")
    except ValidationError as e:
      raise HTTPException(status_code=500, detail=f"Validation error: {e}")

  def addCar(self, car: CarSchema) -> CarModel:
    """
    Adds a new car to the database.

    Args:
      car (CarSchema): The car to add.

    Returns:
      CarModel: The added CarModel object.
    """
    # Convert CarSchema object to dictionary
    carData = car.model_dump()

    # Add the id field to the dictionary
    carData['id'] = len(self.cars) + 1

    # Create a CarModel object using the dictionary
    carToAdd = CarModel(**carData)

    # Add the car to the repository
    self.cars.append(carToAdd)

    return carToAdd

  def findCarById(self, carId: int) -> CarModel:
    """
    Finds a car by its ID.

    Args:
      carId (int): The ID of the car to find.

    Returns:
      CarModel: The car with the specified ID.

    Raises:
      HTTPException: If the car with the specified ID is not found.
    """
    for car in self.cars:
      if car.id == carId:
        return car
    raise HTTPException(status_code=404, detail=f"Car not found. ID: {carId}")

  def removeCar(self, car: CarModel) -> CarModel:
    """
    Removes a car from the database.

    Args:
      car (CarModel): The car to remove.

    Returns:
      CarModel: The removed CarModel object.
    """
    self.cars.remove(car)
    return car

  def saveCarDb(self) -> None:
    """
    Saves the updated data to the JSON file.

    Raises:
      HTTPException: If there is an error saving to the database file.
    """
    try:
      with open(self.file, "w") as f:
        json.dump([car.model_dump() for car in self.cars], f, indent=4)
    except Exception as e:
      raise HTTPException(status_code=500,
                          detail=f"Error saving to database file: {e}")
