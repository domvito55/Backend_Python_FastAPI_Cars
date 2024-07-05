# -*- coding: utf-8 -*-
"""
File Name: database.py
Description: This script sets up the connection to a PostgreSQL database using SQLModel.
 It includes a Database class to manage the database connection and session.
Author: MathTeixeira
Date: July 4, 2024
Version: 2.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from sqlmodel import SQLModel, Session, create_engine


class Database:
  """
  Database class to manage the connection to the PostgreSQL database and provide
  methods to initialize the database and get a session.

  Attributes:
    userName (str): Database username.
    password (str): Database password.
    host (str): Database host.
    port (str): Database port.
    dbName (str): Database name.
    DATABASE_URL (str): Full database URL.
    engine (Engine): SQLAlchemy engine connected to the PostgreSQL database.
  """

  def __init__(self, userName, password, host, port, dbName):
    """
    Initialize the Database class with the provided configuration values.

    Args:
      userName (str): Database username.
      password (str): Database password.
      host (str): Database host.
      port (str): Database port.
      dbName (str): Database name.
    """
    self.userName = userName
    self.password = password
    self.host = host
    self.port = port
    self.dbName = dbName

    self.DATABASE_URL = f"postgresql://{self.userName}:{self.password}@{self.host}:{self.port}/{self.dbName}"
    self.engine = create_engine(self.DATABASE_URL)

  def init(self):
    """
    Initialize the database by creating all the tables defined in the SQLModel metadata.
    FastAPI will call this method to create the database tables.
    """
    SQLModel.metadata.create_all(self.engine)

  def getSession(self):
    """
    Provide a database session. This method is used as a dependency in FastAPI to ensure
    that each request has its own database session.

    Yields:
      session (Session): The database session.
    """
    # Session wraps the database connection and transaction, ensuring that the
    # changes are committed to the database at once, if no errors occur.
    # No partial changes are committed to the database.
    with Session(self.engine) as session:
      yield session
