# -*- coding: utf-8 -*-
"""
File Name: config.py
Description: This script handles loading environment variables and other configurations.
Author: MathTeixeira
Date: July 4, 2024
Version: 2.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from dotenv import load_dotenv
import os


class Config:
  """
  Config class to load environment variables and provide configuration values.

  Attributes:
    DB_USERNAME (str): Database username.
    DB_PASSWORD (str): Database password.
    DB_HOST (str): Database host.
    DB_PORT (str): Database port.
    DB_NAME (str): Database name.
  """

  def __init__(self):
    """
    Initialize the Config class and load environment variables from a .env file.
    """
    load_dotenv()
    self.DB_USERNAME = os.getenv("DB_USERNAME")
    self.DB_PASSWORD = os.getenv("DB_PASSWORD")
    self.DB_HOST = os.getenv("DB_HOST")
    self.DB_PORT = os.getenv("DB_PORT")
    self.DB_NAME = os.getenv("DB_NAME")
