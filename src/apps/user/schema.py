from sqlalchemy.orm import Mapped, mapped_column

from core.schema import DeclarativeBase


class User(DeclarativeBase):
    """User class for mapping to the 'users_tb' table."""

    __tablename__ = 'users_tb'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    """Attributes for user data such as id, username, email and password."""
