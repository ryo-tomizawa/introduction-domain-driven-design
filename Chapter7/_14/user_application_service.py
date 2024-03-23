from iuser_repository import IUserRepository
from user_data import UserData
from user_id import UserId

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data
    

if __name__ == '__main__':
    from inmemory_user_repository import InMemoryUserRepository
    from user_name import UserName
    from user import User

    user_repository = InMemoryUserRepository()
    user_application_service = UserApplicationService(user_repository)

    user = User(UserId('111-222-333'), UserName('tanaka taro'))

    user_repository.save(user)

    get_user = user_application_service.get('111-222-333')
    print(get_user.id, get_user.name)