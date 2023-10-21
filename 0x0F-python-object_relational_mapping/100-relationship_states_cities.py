#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    Base.metadata.create_all(engine)
    session = Session(engine)
    newS = State(name="California")
    newC = City(name="San Francisco")
    newS.cities.append(newC)
    session.add(newS)
    session.commit()
