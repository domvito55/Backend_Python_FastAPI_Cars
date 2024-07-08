# -*- config: utf-8 -*-
"""
File Name: test_postCars.py
Description: This script tests the postCars endpoint of the car sharing API.
Author: MathTeixeira
Date: July 8, 2024
Version: 5.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
import pytest


# both arguments are fixtures coming from conftest.py
def testPostCars(client, auth_token):
  """
  Test the postCars endpoint of the car sharing API.

  Args:
    client (TestClient): A TestClient instance from the FastAPI test client.
    auth_token (str): A JWT token for authenticating the user.
  """
  response = client.post("/api/cars",
                         json={
                             "size": "s",
                             "fuel": "gasoline",
                             "doors": 5,
                             "transmission": "automatic"
                         },
                         headers={"Authorization": f"Bearer {auth_token}"})
  # Check if the response status code is 200
  assert response.status_code == 200

  # Check if the car was created successfully
  responseJson = response.json()
  car = responseJson["message"]
  assert car["size"] == "s"
  assert car["fuel"] == "gasoline"
  assert car["doors"] == 5
  assert car["transmission"] == "automatic"
