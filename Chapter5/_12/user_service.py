from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, iuser_repository: IUserRepository) -> None:
        self.user_repository = iuser_repository

    def exists(self, user: User) -> bool:
        found = self.user_repository.find(user)
        return found 

if __name__ == '__main__':
    user_id = UserId('1010')
    print(user_id.value)