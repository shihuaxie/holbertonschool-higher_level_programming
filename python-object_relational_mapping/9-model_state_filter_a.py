#!/usr/bin/python3
"""Lists all State objects that contain the letter a (Task 9)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username: str, password: str, dbname: str) -> None:
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query = session.query(State)
        query = query.filter(State.name.like('%a%'))
        query = query.order_by(State.id)
        states = query.all()

        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
