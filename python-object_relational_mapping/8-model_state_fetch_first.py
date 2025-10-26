#!/usr/bin/python3
"""Print the first State object from the database (Task 8)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username: str, password: str, dbname: str) -> None:
    # 1: create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    # 2: create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3: Search & sort - using first()
    try:
        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    print_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
