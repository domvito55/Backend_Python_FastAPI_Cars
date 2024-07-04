# database.py
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os


class Database:

  def __init__(self):
    load_dotenv()
    self.DB_USERNAME = os.getenv("DB_USERNAME")
    self.DB_PASSWORD = os.getenv("DB_PASSWORD")
    self.DB_HOST = os.getenv("DB_HOST")
    self.DB_PORT = os.getenv("DB_PORT")
    self.DB_NAME = os.getenv("DB_NAME")

    self.DATABASE_URL = f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    self.engine = create_engine(self.DATABASE_URL)

  def init(self):
    # FastAPI will call this method to create the database tables
    SQLModel.metadata.create_all(self.engine)

  def getSession(self):
    # Session wraps the database connection and transaction, ensuring that the
    # changes are committed to the database at once, if no errors occur.
    # No partial changes are committed to the database.
    with Session(self.engine) as session:
      yield session
