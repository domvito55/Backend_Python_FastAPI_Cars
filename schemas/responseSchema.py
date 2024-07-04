# -*- coding: utf-8 -*-
"""
File Name: responseSchema.py
Description: This script defines the ResponseSchema using Pydantic for data
 validation and serialization. The ResponseSchema is used to structure the API
 responses.
Author: MathTeixeira
Date: June 29, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel
from typing import Union
from models.carModel import CarModel


### Response Schema ###
class ResponseSchema(BaseModel):
  """
  ResponseSchema for structuring API responses.

  Attributes:
    message (Union[str, list[CarModel], CarModel]): The message returned in the response.
      It can be a string, a list of CarModel objects, or a single CarModel object.
    code (int): The status code of the response.
  """
  message: Union[str, list[CarModel], CarModel]
  code: int
