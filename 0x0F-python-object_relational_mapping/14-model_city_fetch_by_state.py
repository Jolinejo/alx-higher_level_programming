#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306
    query = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(name, pwd, host, port, db)
    engine = create_engine(query, pool_pre_ping=True)
    session = Session(engine)
    for c, s in session.query(City, State) \
            .filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
