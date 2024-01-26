"""
in this code we will use sql alcehmy
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


username = "mesoud"
password = "aymen123"
database = "hbtn_0e_6_usa"

path = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
database = create_engine(path)
connection = database.connect()

Base = declarative_base()
Session = sessionmaker(bind=database) 
class State(Base):
    """Class representing the 'states' table in the database.

        Attributes:
        id (int): Auto-generated unique integer, primary key.
        name (str): String with a maximum of 128 characters, cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128), nullable=False)
    Base.metadata.create_all(bind=database)
# Creating a session
#session = Session()

# Adding a new state to the database
#new_state = State(name='New York')
#session.add(new_state)
#session.commit()

# Querying the states from the database
#states = session.query(State).all()
#for state in states:
    #print(state.id, state.name)

# Closing the session
#session.close()
