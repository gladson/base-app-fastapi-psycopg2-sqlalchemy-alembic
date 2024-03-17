from typing import List, Optional

from apps.user.model import User as UserModel
from apps.user.repository import UserRepository
from apps.user.schema import User as UserSchema
from core.utils.gpass import GPass


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> Optional[UserSchema]:
        return self.user_repository.get_user_by_id(user_id)

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
    ) -> Optional[UserSchema]:
        user = UserModel(
            username=username,
            email=email,
            password=GPass.get_password_hash(password),
            id=None,
        )
        return self.user_repository.create_user(user)

    def update_user(
        self,
        user_id: int,
        username: str,
        email: str,
        password: Optional[str],
    ) -> Optional[UserSchema]:
        existing_user = self.user_repository.get_user_by_id(user_id)
        if existing_user:
            existing_user.username = username
            existing_user.email = email
            if password:
                existing_user.password = GPass.get_password_hash(password)
            return self.user_repository.update_user(
                user_id,
                new_user_data=UserModel(**existing_user.__dict__),
            )
        return None

    def delete_user(self, user_id: int) -> Optional[UserSchema]:
        return self.user_repository.delete_user(user_id)

    def get_all_users(self) -> List[UserSchema]:
        return self.user_repository.get_all_users()
