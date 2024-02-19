#!/usr/bin/python3
""" This is a python class definition of a city table in the database """

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """ Class representing the 'cities' table in the database.
    Attributes:
        id (int): The primary key of the City, automatically incremented.
        name (str): The name of the City, up to 128 characters.
        state_id (int): FK, referencing 'id' column of the 'states' table."""

    __tablename__ = "cities"
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
