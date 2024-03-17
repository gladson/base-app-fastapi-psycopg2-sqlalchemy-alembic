from typing import List, Optional

from apps.user.model import User as UserModel
from apps.user.schema import User as UserSchema
from core.database import Database
from core.settings import Settings


class UserRepository:
    """
    Repository class to perform CRUD operations for users.
    """

    def __init__(self):
        self.settings = Settings()
        self.db = Database()

    def get_user_by_id(
        self,
        user_id: int,
    ) -> Optional[UserSchema]:
        """
        Retrieves a user by its ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[UserSchema]: The user with the specified ID, if found;
            None otherwise.
        """
        with self.db.Session() as session:
            user = (
                session.query(UserSchema)
                .filter(
                    UserSchema.id == user_id,
                )
                .first()
            )
            return user

    def create_user(self, user: UserModel) -> UserSchema:
        """
        Creates a new user.

        Args:
            user (UserModel): The user object to create.

        Returns:
            UserSchema: The created user object.
        """
        with self.db.Session() as session:
            user_dict = user.model_dump()
            db_user = UserSchema(**user_dict)
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            return db_user

    def update_user(
        self, user_id: int, new_user_data: UserModel
    ) -> Optional[UserSchema]:
        """
        Updates an existing user.

        Args:
            db (Session): SQLAlchemy database session.
            user_id (int): The ID of the user to update.
            new_user_data (UserModel): The new user data.

        Returns:
            Optional[UserSchema]: The updated user object,
            if the user was found;
            None otherwise.
        """
        # Obter o usuário dentro da sessão atual
        with self.db.Session() as session:
            db_user = (
                session.query(UserSchema)
                .filter(
                    UserSchema.id == user_id,
                )
                .first()
            )

            if db_user:
                for field, value in new_user_data.model_dump().items():
                    setattr(db_user, field, value)
                session.commit()
                session.refresh(db_user)
                return db_user
            return None

    def delete_user(self, user_id: int) -> Optional[UserSchema]:
        """
        Deletes a user by its ID.

        Args:
            db (Session): SQLAlchemy database session.
            user_id (int): The ID of the user to delete.

        Returns:
            Optional[UserSchema]: The deleted user object,
            if the user was found;
            None otherwise.
        """
        with self.db.Session() as session:
            db_user = self.get_user_by_id(user_id=user_id)
            if db_user:
                session.delete(db_user)
                session.commit()
                return db_user
            return None

    def get_all_users(self) -> List[UserSchema]:
        """
        Retrieves all users.

        Args:
            db (Session): SQLAlchemy database session.

        Returns:
            List[UserSchema]: A list containing all users.
        """
        with self.db.Session() as session:
            return session.query(UserSchema).all()
