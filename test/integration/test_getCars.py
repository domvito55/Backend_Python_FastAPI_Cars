# -*- config: utf-8 -*-
"""
File Name: test_getCars.py
Description: This script tests the getCars endpoint of the car sharing API.
Author: MathTeixeira
Date: July 8, 2024
Version: 5.0.0
License: MIT License
Contact Information: mathteixeira55
"""


# client is a fixture coming from conftest.py
def testGetCars(client):
  """
  Test the getCars endpoint of the car sharing API.

  Args:
    client (TestClient): The FastAPI TestClient instance.

  Returns:
    None
  """
  response = client.get("/api/cars")
  assert response.status_code == 200

  # Check if the cars were retrieved successfully
  responseJson = response.json()
  carList = responseJson["message"]
  assert all(["size" in car for car in carList])
  assert all(["doors" in car for car in carList])
