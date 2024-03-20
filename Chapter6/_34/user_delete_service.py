from iuser_repository import IUserRepository
from user_delete_command import UserDeleteCommand
from user_id import UserId
from user_not_found_exception import UserNotFoundException
from user import User

class UserDeleteService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository
    
    def handle(self, command: UserDeleteCommand):
        user_id = UserId(command.id)
        user = self.user_repository.find(user_id)

        if user is None: raise UserNotFoundException(user, None)
        
        self.user_repository.delete(user)


if __name__ == '__main__':
    from user_name import UserName

    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None
        
        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def delete(self, user: User):
            if user.id.value in self.store:
                del self.store[user.id.value]

        def clone(self, user: User):
            return User(user.id, user.name)


    user_repository = MockUserRepository()
    user_delete_service = UserDeleteService(user_repository)

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))

    user_repository.save(user_a)

    user_delete_command = UserDeleteCommand('111-222-333')
    user_delete_service.handle(user_delete_command)

    print(f'登録状況: {user_repository.store}')