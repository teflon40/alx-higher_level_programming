#!/usr/bin/python3
""" Defines a SQLAlchemy model for the 'states' table in a database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A class representing the 'states' table in the database.
    Attributes:
        id (int): auto-generated, unique integer serving as the primary key.
        name (str): name of the state, 128 characters only, and cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
