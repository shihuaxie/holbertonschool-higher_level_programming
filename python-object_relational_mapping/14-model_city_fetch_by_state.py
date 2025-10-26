#!/usr/bin/python3
"""Print all City objects with their State name, ordered by cities.id."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_cities_with_state(username, password, dbname):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # JOIN + ORDER BY cities.id
        query = session.query(State.name, City.id, City.name)
        query = query.join(City, City.state_id == State.id)
        query = query.order_by(City.id)
        rows = query.all()

        for state_name, city_id, city_name in rows:
            print(f"{state_name}: ({city_id}) {city_name}")
    finally:
        session.close()


if __name__ == "__main__":
    list_cities_with_state(sys.argv[1], sys.argv[2], sys.argv[3])
