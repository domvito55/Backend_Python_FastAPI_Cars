# -*- coding: utf-8 -*-
"""
File Name: detailedResponseSchema.py
Description: This script defines the DetailedResponseSchema for data validation
 and serialization. The ResponseSchema is used to structure the API responses.
Author: MathTeixeira
Date: July 6, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from pydantic import BaseModel
from .detailedCarSchema import DetailedCarSchema


### Detailed Response Schema ###
class DetailedResponseSchema(BaseModel):
  """
  ResponseSchema for structuring API responses.

  Attributes:
    message (Union[str, list[Car], Car]): The message returned in the response.
      It can be a string, a list of Car objects, or a single Car object.
    code (int): The status code of the response.
  """
  message: list[DetailedCarSchema]
  code: int
