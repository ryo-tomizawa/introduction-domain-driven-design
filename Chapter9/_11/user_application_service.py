from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from user_id import UserId
from user_register_command import UserRegisterCommand
from user_service import UserService
from user_name import UserName
from user import User

class UserApplicationService:
    def __init__(self, 
                 user_repository: IUserRepository,
                 user_service: UserService
                 ) -> None:
        self.user_repository = user_repository
        self.user_service = user_service

    def register(self, command: UserRegisterCommand) -> None:
        user_name = UserName(command.name)
        user = User(
            self.user_repository.next_identity(),
            user_name
        )

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, "ユーザは既に存在しています。")

        self.user_repository.save(user)

if __name__ == '__main__':
    # モックオブジェクトやスタブの作成
    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}
            self.current_id = 0

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None

        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def clone(self, user: User):
            return User(user.id, user.name)
        
        def next_identity(self) -> UserId:
            self.current_id += 1
            return UserId(str(self.current_id))

    class MockUserService(UserService):
        def exists(self, user: User) -> bool:
            # ここでは常にFalseを返すことで、どんなユーザーも存在しないとする
            # Trueにすることで、エラーパターンのテストも可能
            return False

    user_repository = MockUserRepository()
    user_service = MockUserService(user_repository)
    user_application_service = UserApplicationService(user_repository, user_service)

    # ユーザー登録のテスト
    user_name_a = 'tanaka taro'
    command_a = UserRegisterCommand(user_name_a)
    user_application_service.register(command_a)
    print(f"{user_name_a} の登録が完了しました。")

