# -*- coding: utf-8 -*-
"""
File Name: carsharing.py
Description: This script initializes a FastAPI web application for a car sharing
 service. It provides endpoints for welcoming users, and includes routers for
 managing cars and trips.
Author: MathTeixeira
Date: July 6, 2024
Version: 4.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.database import carsDb
from schemas import ResponseSchema
from routers import cars, trips, web, users


### Lifespan Events ###
@asynccontextmanager
async def lifespan(app: FastAPI):
  print("Starting up...")
  carsDb.init()
  yield
  print("Shutting down...")


### Initialize FastAPI App ###
app = FastAPI(title="Car Sharing API", version="3.0.0", lifespan=lifespan)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

### Include Routers ###
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(cars.router, prefix="/api/cars", tags=["Cars"])
app.include_router(trips.router, prefix="/api/trips", tags=["Trips"])
app.include_router(web.router, tags=["Web"])


### set Middlewares ###
@app.middleware("http")
async def add_process_time_header(request: Request, callNext):
  visitCount = 0
  if "visitCountCookie" in request.cookies:
    # Check if the cookie exists
    visitCount = int(request.cookies.get("visitCountCookie"))
    # Increment the visit count if the cookie exists
    visitCount += 1

  response = await callNext(request)
  response.set_cookie(key="visitCountCookie", value=visitCount)
  return response


origins = [
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


### API Endpoints ###
# Health Check Endpoint
@app.get("/check",
         tags=["Health Check"],
         summary="Health Check",
         response_model=ResponseSchema)
def welcome() -> ResponseSchema:
  """
  Welcome endpoint for the Car Sharing API.

  Returns:
    ResponseSchema: A dictionary containing a welcome message.
  """
  return ResponseSchema(message="Welcome to the Car Sharing API!", code=200)


### Main ###
if __name__ == "__main__":
  import uvicorn

  uvicorn.run("carsharing:app", host="0.0.0.0", port=8000, reload=True)
