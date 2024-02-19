#!/usr/bin/python3
""" using SQLAlchemy, retrieves states with the letter 'a' in their names,
and prints their IDs and names. """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for state in session.query(State).order_by(State.id).all():
            if 'a' in state.name:
                print(f"{state.id}: {state.name}")
