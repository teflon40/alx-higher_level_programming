#!/usr/bin/python3
""" Using sqlachemy(orm), Connects to a MySQL database and retrieves
information(state id and names) from the 'states' table. """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for state in session.query(State).order_by(State.id).all():
            if 'Y' in state.name:
                print(f"{state.id}: {state.name}")
