from sqlmodel import SQLModel
from database.connection import engine
from database.models.application import Application

def create_all_tables():
    SQLModel.metadata.create_all(engine)