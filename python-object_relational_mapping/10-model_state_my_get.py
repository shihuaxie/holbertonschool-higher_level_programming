#!/usr/bin/python3
"""Prints the State object with the name passed as argument (Task 10)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name(username, password, dbname, state_name):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")
    finally:
        session.close()


if __name__ == "__main__":
    get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
