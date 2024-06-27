#!/usr/bin/python3
"""
Delete states with a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()

    for state in ses.query(State):
        if "a" in state.name:
            ses.delete(state)
    ses.commit()
