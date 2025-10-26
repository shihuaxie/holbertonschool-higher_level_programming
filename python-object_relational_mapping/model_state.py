#!/usr/bin/python3
"""SQLAlchemy model definition of State and Base instance"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base class for all ORM models
Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table 'states'"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
