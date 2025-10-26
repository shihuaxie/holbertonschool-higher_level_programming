#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database (Task 11)."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(username, password, dbname):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # 1: create the new object - Louisian
    new_state = State(name="Louisiana")
    # 2: Register the new obj to session
    session.add(new_state)
    # 3: submit session
    session.commit()

    # 4: get new id
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    add_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
