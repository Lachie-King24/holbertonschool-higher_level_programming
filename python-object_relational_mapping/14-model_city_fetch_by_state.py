#!/usr/bin/python3
"""Fetch all City objects from the database and print them by state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get MySQL credentials and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with their states, ordered by city id
    cities = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
