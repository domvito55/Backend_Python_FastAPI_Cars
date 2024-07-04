# -*- coding: utf-8 -*-
"""
File Name: docDetails.py
Description: This script defines query parameters for the Car Sharing API,
 providing Swagger documentation.
Author: MathTeixeira
Date: June 28, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from fastapi import Query, Path

### Query Parameters ###
# Query is used to define query parameters for the API endpoints.
# These definitions also provide Swagger documentation for the query parameters.

sizeQuery: str | None = Query(None,
                              description="Filter cars by size (s, m, l)",
                              example="s")
doorsQuery: int | None = Query(None,
                               description="Filter cars by number of doors",
                               example=5)
### Path Parameters ###
# Path is used to define path parameters for the API endpoints.
idPath: int = Path(..., description="ID of the car to retrieve", example=5)
