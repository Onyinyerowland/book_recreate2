from uuid import UUID, uuid4
from typing import Optional
from database import book
from schemas.user import UserCreate, UserUpdate, User


class UserService:

    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        return next((user for user in users if user.id == user_id), None)

    def create_user(self, user_in:UserCreate) -> User:
        new_user = User(
            id=uuid4(),
            name=user_in.name,
            email=user_in.email,
            age=user_in.age
        )
        users.append(new_user)
        return new_user

    def update_user(self, user_id: UUID, user_in: UserUpdate) -> Optional[UnicodeTranslateError]:
        user = self.get_user_by_id(user_id)
        if not user:
            return None

        if user_in.name is not None:
            user.name = user_in.name
        if user_in.email is not None:
            user.email = user_in.email
        if user_in.age is not None:
            user.age = user_in.age

        return user

    def delete_user(self, user_id: UUID) -> bool:
        global users
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        users.remove(user)
        return True

# services/user.py
users = []

def reset_data():
    users.clear()


# Expose a single service instance
user_service = UserService()
