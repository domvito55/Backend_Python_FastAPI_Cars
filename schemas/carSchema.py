# -*- coding: utf-8 -*-
"""
File Name: carSchema.py
Description: This script defines the CarSchema for data validation and\
 serialization using Pydantic.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel, Field


class CarSchema(BaseModel):
  """
  CarSchema model for data validation and serialization.

  Attributes:
    size (str, optional): The size of the car (e.g., s, m, l).
    fuel (str, optional): The type of fuel the car uses (e.g., gasoline, diesel, electric).
    doors (int, optional): The number of doors the car has.
    transmission (str, optional): The type of transmission (e.g., manual, automatic).
  """
  size: str | None = Field(None,
                           description="The size of the car (e.g., s, m, l)",
                           example="m")
  fuel: str | None = Field(
      None,
      description=
      "The type of fuel the car uses (e.g., gasoline, diesel, electric)",
      example="gasoline")
  doors: int | None = Field(None,
                            description="The number of doors the car has",
                            example=5)
  transmission: str | None = Field(
      None,
      description="The type of transmission (e.g., manual, automatic)",
      example="automatic")
