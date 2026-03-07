#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments: mysql username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database)
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects, ordered by id
    state = session.query(State).filter(
        State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not Found")

    # Close the session
    session.close()
