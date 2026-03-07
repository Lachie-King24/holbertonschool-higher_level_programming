#!/usr/bin/python3
"""Update the name of a State object in the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database)
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all states
    session.query(State).delete()

    session.commit()  # Save changes

    # Close the session
    session.close()
