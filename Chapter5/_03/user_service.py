from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def exists(self, user: User)-> bool:
        found = self.user_repository.find(user.name.value)
        return found is not None


if __name__ == '__main__':
    from user_name import UserName

    user = User(UserName('Kato'))
    user_service = UserService(IUserRepository())
    
    print(user_service.exists(user))