# -*- coding: utf-8 -*-
"""
File Name: tripSchema.py
Description: This script defines the TripSchema for data validation and
 serialization of trip data in the application. The schema includes fields for
 the start and end kilometers of the trip and a description of the trip.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel, Field


class TripSchema(BaseModel):
  """
  TripSchema model for data validation and serialization.

  Attributes:
    start (int): The starting Km of the trip.
    end (int): The ending Km of the trip.
    description (str): A description of the trip.
  """
  start: int | None = Field(None,
                            description="The starting Km of the trip",
                            example=0)
  end: int | None = Field(None,
                          description="The ending Km of the trip",
                          example=5)
  description: str | None = Field(None,
                                  description="A description of the trip",
                                  example="From store to home")

  class Config:
    from_attributes = True
