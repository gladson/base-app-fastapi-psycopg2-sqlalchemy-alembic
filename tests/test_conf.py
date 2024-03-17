import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.apps.user.schema import DeclarativeBase


@pytest.fixture
def session():
    """
    Fixture for creating a session object for testing purposes.
    """
    engine = create_engine('sqlite:///:memory:')
    """
    Create a SQLite database in memory and create a session object
    for testing purposes.
    """
    Session = sessionmaker(bind=engine)
    """
    Create a session object for testing purposes.
    """
    DeclarativeBase.metadata.create_all(engine)
    """
    Create the tables in the database.
    """
    yield Session()
    """
    Yield the session object.
    """
    DeclarativeBase.metadata.drop_all(engine)
