from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, iuser_repository: IUserRepository) -> None:
        self.user_repository = iuser_repository

    def exists(self, user: User) -> bool:
        found = self.user_repository.find(user.name.value)
        return found is not None 


if __name__ == '__main__':
    from user_name import UserName
    user_name = UserName('Tanaka')
    user = User(None, user_name)

    user_repository =  IUserRepository()

    user_service = UserService(user_repository)

    print(user_service.exists(user))
