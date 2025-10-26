#!/usr/bin/python3
"""Update the State object with id=2 to 'New Mexico' (Task 12)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, dbname):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the obj first using filter()
    state = session.query(State).filter(State.id == 2).first()
    if state:
        # Update the obj attribute
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
