#!/usr/bin/python3
"""List all State objects via SQLAlchemy (Task 7)."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def list_states(username: str, password: str, dbname: str) -> None:
    # 1) Create Engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True,
    )

    # 2) Create Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3) Search & Sort
    try:
        states = session.query(State).order_by(State.id).all()

        # 4) print as the format
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()

if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
