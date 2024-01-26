import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


path = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database)

engine = create_engine(path)

Session = sessionmaker(bind=engine)
session = Session()
a_states = session.query(State).filter(State.name.like('%a%')).all()
for state in a_states:
    print(f"{state.id}: {state.name}")






session.close()