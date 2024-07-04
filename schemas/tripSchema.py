# -*- coding: utf-8 -*-
"""
File Name: tripSchema.py
Description: This script defines the TripSchema for data validation and
 serialization of trip data in the application. The schema includes fields for
 the start and end kilometers of the trip and a description of the trip.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.2
License: MIT License
Contact Information: mathteixeira55
"""

# ### Imports ###
from pydantic import Field
from sqlmodel import SQLModel


class TripSchema(SQLModel):
  """
  TripSchema model for data validation and serialization.

  Attributes:
    start (int): The starting Km of the trip.
    end (int): The ending Km of the trip.
    description (str): A description of the trip.
  """
  start: int = Field(..., description="The starting Km of the trip", example=0)
  end: int = Field(..., description="The ending Km of the trip", example=5)
  description: str = Field(...,
                           description="A description of the trip",
                           example="From store to home")
