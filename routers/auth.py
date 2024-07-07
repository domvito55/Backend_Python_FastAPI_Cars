# -*- coding: utf-8 -*-
"""
File Name: auth.py
Description: This script defines the routers for user authentication in the car
 sharing service.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from starlette import status

from core.database import carsDb
from models import User

router = APIRouter()


@router.post("/token")
async def login(formData: OAuth2PasswordRequestForm = Depends(),
                session: Session = Depends(carsDb.getSession)) -> dict:
  """
  Get the authentication token for the user.

  Args:
    formData (OAuth2PasswordRequestForm): The user's login credentials.
    session (Session): The database session.

  Returns:
    dict: The user's authentication token.
  """
  query = select(User).where(User.username == formData.username)
  user = session.exec(query).first()

  if not user or not user.verifyPassword(formData.password):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Invalid credentials",
                        headers={"WWW-Authenticate": "Bearer"})
  # ########## NOTE: FOR SIMPLICITY, IN THIS SMALL PROJECT, TOKEN CONTAINS THE
  # USERNAME ONLY; BEFORE SENDING TO PRODUCTION THIS SHOULD BE ENHANCED.
  # ##########
  return {"access_token": user.username, "token_type": "bearer"}
