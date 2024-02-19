#!/usr/bin/python3
""" Using SQLAlchemy, connects to db, retrieves the ID of a state by name,
and prints the ID or "Not found" if the state doesn't exist."""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        name = session.query(State).filter(State.name == argv[4])
        print(name.first().id if name.first() else "Not found")
