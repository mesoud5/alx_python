"""
in this module we will do some sql alchemy projects
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
"""
this is instance of base class  holding declarative base function
"""
class State(Base):
    """Class representing the 'states' table in the database.

    Attributes:
        id (int): Auto-generated unique integer, primary key.
        name (str): String with a maximum of 128 characters, cannot be null.
    """
    __tablename__ = 'states'
    """
    creating table name
    """
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
