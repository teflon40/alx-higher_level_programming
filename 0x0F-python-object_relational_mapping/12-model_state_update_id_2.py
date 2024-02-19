#!/usr/bin/python3
""" Retrieves a state with ID 2 from the 'states' table id the db and
updates the name of the retrieved state to "New Mexico. """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        target_id = session.get(State, 2)
        target_id.name = "New Mexico"
        session.commit()