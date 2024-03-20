from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from user_name import UserName
from user_register_command import UserRegisterCommand
from user_service import UserService
from user import User

class UserRegisterService:
    def __init__(self, user_repository: IUserRepository, user_service: UserService) -> None:
        self.user_repository = user_repository
        self.user_service = user_service
    
    def handle(self, command: UserRegisterCommand):
        user_name = UserName(command.name)
        user = User(None, user_name)

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
        
        self.user_repository.save(user)


if __name__ == '__main__':
    from user_id import UserId

    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def find_by_user_name(self, name: UserName):
            for elem in self.store.values():
                print(elem)
                if elem.name.value == name.value:
                    return self.clone(elem)
            return None
        
        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def clone(self, user: User):
            return User(user.id, user.name)


    user_repository = MockUserRepository()
    user_service = UserService(user_repository)
    user_register_service = UserRegisterService(user_repository, user_service)

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))

    user_repository.save(user_a)

    user_registory_command = UserRegisterCommand('john smith')
    user_register_service.handle(user_registory_command)

    print(f'登録状況: {user_repository.store}')