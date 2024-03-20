from user_data import UserData
from user_id import UserId
from user_repository import UserRepository

class UserApplicationService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data