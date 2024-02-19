#!/usr/bin/python3
""" connects to a MySQL database, retrieves information about cities and
their associated states, and prints the results."""

if __name__ == "__main__":
    from sys import argv
    from model_city import City
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import joinedload

    conn_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

    engine = create_engine(conn_url)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        fetched_objs = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
        for city, state in fetched_objs:
            print(f"{state.name}: ({city.id}) {city.name}")
