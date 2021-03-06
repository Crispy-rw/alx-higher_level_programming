#!/usr/bin/python3
"""
Using the SQLAlchemy module, list all State objects from the
database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(City, State)\
                      .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
