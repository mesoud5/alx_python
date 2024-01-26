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
state = session.query(State).first()
if state:
    print(f"{state.id}: {state.name}")
else:
    print("nothing\n")




session.close()