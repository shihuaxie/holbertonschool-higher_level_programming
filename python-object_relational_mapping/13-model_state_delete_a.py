#!/usr/bin/python3
"""Delete all State objects whose name contains 'a' (Task 13)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, dbname):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Find all states that contains 'a' in the name
        victims = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
        )

        # Delete one by one
        for state in victims:
            session.delete(state)

        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
