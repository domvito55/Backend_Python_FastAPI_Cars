# -*- config: utf-8 -*-
"""
File Name: test_home.py
Description: This script tests the home endpoint of the car sharing API. This is
 an home page that welcomes users to the API.
Author: MathTeixeira
Date: July 8, 2024
Version: 5.0.0
License: MIT License
Contact Information: mathteixeira55
"""


def testHome(client):
  """
  Test the home endpoint of the car sharing API.

  Args:
    client (TestClient): The FastAPI TestClient instance.

  Returns:
    None
  """
  response = client.get("/")
  assert response.status_code == 200
  assert "Welcome to Car Sharing API" in response.text
