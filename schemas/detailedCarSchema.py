# -*- coding: utf-8 -*-
"""
File Name: carSchema.py
Description: This script defines the CarSchema for data validation and
 serialization using Pydantic.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel, ConfigDict, Field
from .tripSchema import TripSchema


class DetailedCarSchema(BaseModel):
  """
  CarSchema model for data validation and serialization.

  Attributes:
    size (str, optional): The size of the car (e.g., s, m, l).
    fuel (str, optional): The type of fuel the car uses (e.g., gasoline, diesel, electric).
    doors (int, optional): The number of doors the car has.
    transmission (str, optional): The type of transmission (e.g., manual, automatic).
  """
  id: int | None = Field(None,
                         description="The unique identifier for the car",
                         json_schema_extra={"example": 5})
  size: str | None = Field(None,
                           description="The size of the car (e.g., s, m, l)",
                           json_schema_extra={"example": "s"})
  fuel: str | None = Field(
      None,
      description=
      "The type of fuel the car uses (e.g., gasoline, diesel, electric)",
      json_schema_extra={"example": "gasoline"})
  doors: int | None = Field(None,
                            description="The number of doors the car has",
                            json_schema_extra={"example": 5})
  transmission: str | None = Field(
      None,
      description="The type of transmission (e.g., manual, automatic)",
      json_schema_extra={"example": "automatic"})
  trips: list[TripSchema] = Field(
      [],
      description="A list of trip associated with the car",
      json_schema_extra={
          "example": [{
              "start": 0,
              "end": 5,
              "description": "From store to home"
          }]
      })

  model_config = ConfigDict(from_attributes=True)
