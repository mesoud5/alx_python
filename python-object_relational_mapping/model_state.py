"""This module defines a SQLAlchemy State class representing a 'states' table in the database."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# MySQL database connection parameters
username = "mesoud"
password = "aymen123"
database = "hbtn_0e_6_usa"

# Create the connection path
path = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
engine = create_engine(path)
connection = engine.connect()

# Create a base class for declarative models
Base = declarative_base()

class State(Base):
    """Class representing the 'states' table in the database.

    Attributes:
        id (int): Auto-generated unique integer, primary key.
        name (str): String with a maximum of 128 characters, cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Create the 'states' table in the database
Base.metadata.create_all(bind=engine)

# Close the connection
connection.close()
