from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    Represents a user object with an optional id, name, and email.
    """

    id: Optional[int] = None
    username: str
    email: str
    password: Optional[str] = None
