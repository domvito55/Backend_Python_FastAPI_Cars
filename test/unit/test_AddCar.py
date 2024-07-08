# -*- coding: utf-8 -*-
"""
File Name: test_AddCar.py
Description: This script tests the addCar f8unction of the car sharing API. This
 function adds a car to the database. It tests the logic of the endpoint.
"""

### Imports ###
from unittest.mock import Mock
from routers.cars import addCar
from schemas import CarSchema, UserSchema
from models import Car


# In general, all the testing an endpoint is a integration test because it
# tests the interaction between the different components of the application.
# But the following test is a unit test because it tests the logic of the
# endpoint.
def testDatabaseOperation():
  """
  Test the addCar function of the car sharing API.
  """
  # Mocking the session object, so we don't have to connect to the database.
  # We are testing the logic of the endpoint, not the database.
  # We are testing if the endpoint is calling the right methods of the session
  # object.
  mockSession = Mock()
  inputCar = CarSchema(size="s",
                       fuel="gasoline",
                       doors=5,
                       transmission="automatic")
  user = UserSchema(username="test", password="test")
  result = addCar(inputCar, mockSession, user)

  mockSession.add.assert_called_once()
  mockSession.commit.assert_called_once()
  mockSession.refresh.assert_called_once()
  assert result.code == 200
  assert isinstance(result.message, Car)
  assert result.message.size == "s"
  assert result.message.fuel == "gasoline"
  assert result.message.doors == 5
  assert result.message.transmission == "automatic"
