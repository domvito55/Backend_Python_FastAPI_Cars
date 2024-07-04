# -*- coding: utf-8 -*-
"""
File Name: carSchema.py
Description: This script defines the CarSchema for data validation and serialization using Pydantic.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.2
License: MIT License
Contact Information: mathteixeira55
"""

# ### Imports ###
from sqlmodel import SQLModel
from pydantic import Field


class CarSchema(SQLModel):
  """
  CarSchema model for data validation and serialization.

  Attributes:
    size (str, optional): The size of the car (e.g., s, m, l).
    fuel (str): The type of fuel the car uses (e.g., gasoline, diesel, electric).
    doors (int): The number of doors the car has.
    transmission (str): The type of transmission (e.g., manual, automatic).
  """
  size: str | None = Field(None,
                           description="The size of the car (e.g., s, m, l)",
                           example="m")
  fuel: str = Field(
      ...,
      description=
      "The type of fuel the car uses (e.g., gasoline, diesel, electric)",
      example="gasoline")
  doors: int = Field(...,
                     description="The number of doors the car has",
                     example=5)
  transmission: str = Field(
      ...,
      description="The type of transmission (e.g., manual, automatic)",
      example="automatic")
