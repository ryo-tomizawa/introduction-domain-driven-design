from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, iuser_repository: IUserRepository) -> None:
        self.user_repository = iuser_repository

    def exists(self, user: User) -> bool:
        found = self.user_repository.find(user.name.value)
        return found 


if __name__ == '__main__':
    from user_name import UserName
    from ef_user_repository import EFUserRepository
    from mydb_context import MyDbContext
    user_name = UserName('Tanaka')
    user = User(None, user_name)

    mydb_context = MyDbContext()
    user_repository =  EFUserRepository(mydb_context)

    user_service = UserService(user_repository)

    print(user_service.exists(user))
