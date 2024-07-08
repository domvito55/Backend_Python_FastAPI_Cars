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
sizeQuery: str | None = Query(
    None,
    description="Filter cars by size (s, m, l)",
    openapi_examples={"small": {
        "summary": "Small car",
        "value": "s"
    }})

doorsQuery: int | None = Query(
    None,
    description="Filter cars by number of doors",
    openapi_examples={"5 doors": {
        "summary": "5 doors",
        "value": 5
    }})

tripQuery: bool = Query(False,
                        description="include trips in the response",
                        openapi_examples={
                            "Retrieve trips": {
                                "summary": "Retrieve trips",
                                "value": False
                            }
                        })

### Path Parameters ###
# Path is used to define path parameters for the API endpoints.
idPath: int = Path(
    ...,
    description="ID of the car to retrieve",
    openapi_examples={"Car ID": {
        "summary": "Car ID",
        "value": 5
    }})
