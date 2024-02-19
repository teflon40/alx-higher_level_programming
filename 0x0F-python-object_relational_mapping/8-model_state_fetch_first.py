#!/usr/bin/python3
""" Using SQLAlchemy, Connects to db and retrieves the first entry from the
'states' table, prints its ID and name. prints "Nothing" If the table is empty
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        first_state = session.query(State).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
