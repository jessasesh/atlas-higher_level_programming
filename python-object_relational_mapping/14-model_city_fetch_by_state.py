#!/usr/bin/python3
"""  
Prints all cities from specified database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import (sessionmaker)
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()

    item = sesh.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in item:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    sesh.close()