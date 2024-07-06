# -*- coding: utf-8 -*-
"""
Package Name: schemas
Description: This package contains the Pydantic schemas for data validation and
 serialization in the car sharing service, including CarSchema, TripSchema, and ResponseSchema.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from .carSchema import CarSchema
from .detailedCarSchema import DetailedCarSchema
from .tripSchema import TripSchema
from .responseSchema import ResponseSchema
from .detailedResponseSchema import DetailedResponseSchema
