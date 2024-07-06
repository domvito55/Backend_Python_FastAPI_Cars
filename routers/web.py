# -*- coding: utf-8 -*-
"""
File Name: web.py
Description: This script provides a router for the Car Sharing API to welcome
 users.
Author: MathTeixeira
Date: July 6, 2024
Version: 3.0.0
License: MIT License
Contact Information: mathteixeira55
"""

### Imports ###
from fastapi import APIRouter, Cookie, Depends, Query, Request
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from core.database import carsDb
from starlette.responses import HTMLResponse

from routers.cars import getCars

### Router Initialization ###
router = APIRouter()

templates = Jinja2Templates(directory="templates")


### Router Endpoints ###
@router.get("/", response_class=HTMLResponse)
def index(request: Request, visitCountCookie: int = Cookie(0)):
  print(f"This client has being here for {visitCountCookie} times.")
  return templates.TemplateResponse("index.html", {"request": request})


# To allow bookmarking and results sharing, it is best to use get requests,
# instead of post requests; therefore, we need to use Query parameters; if we
# used post requests, we would have to use Form parameters.
@router.get("/search", response_class=HTMLResponse)
# * is used to indicate that all the parameters that follow are keyword-only
# parameters and will not be used positionally, allowing us to call the function
# passing parameters without default values in any order.
def search(*,
           size: str | None = Query(None),
           doors: int | None = Query(None),
           request: Request,
           session: Session = Depends(carsDb.getSession)):
  res = getCars(size, doors, False, session)
  cars = res.message
  return templates.TemplateResponse("searchResults.html", {
      "request": request,
      "cars": cars
  })
