from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

# from sqlalchemy.ext.declarative import declarative_base

my_metadata = MetaData()

Base = declarative_base(metadata=my_metadata)


class DeclarativeBase(Base):  # type: ignore
    """Base class for declarative ORM mapping."""

    __abstract__ = True
    __table_args__ = {'extend_existing': True}
