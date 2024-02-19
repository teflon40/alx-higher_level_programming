#!/usr/bin/python3
""" Adds a new state obj representing a row in the db table. The values
of this object are mapped to the columns of the corresponding table. """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from model_state import Base, State

    conn_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        new_state = State(name="Louisiana")  # new table row
        session.add(new_state)
        session.commit()
        print(new_state.id)
