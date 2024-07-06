# -*- config: utf-8 -*-
"""
File Name: auth.py
Description: This script defines the AuthHandler class for handling user
 authentication and authorization in the application.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel import Session, select
from starlette import status

from core.database import carsDb
from schemas import UserProtectedSchema
from models import User


class AuthHandler:
  """
  The AuthHandler class provides methods for handling user authentication and authorization.
  """

  def getCurrentUser(
      self,
      credentials: HTTPBasicCredentials = Depends(HTTPBasic()),
      session: Session = Depends(carsDb.getSession)
  ) -> UserProtectedSchema:
    """
        Get the current user from the database using the provided credentials.

        Args:
          credentials (HTTPBasicCredentials): The credentials for the current user.

        Returns:
          UserProtectedSchema: The current user from the database.
        """
    query = select(User).where(User.username == credentials.username)
    user = session.exec(query).first()

    if not user or not user.verifyPassword(credentials.password):
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                          detail="Invalid credentials")
    return UserProtectedSchema.model_validate(user)
