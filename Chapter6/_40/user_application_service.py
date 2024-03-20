from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from mail_utility import MailUtility
from user_id import UserId
from user_register_command import UserRegisterCommand
from user_service import UserService
from user_name import UserName
from user import User

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository, user_service: UserService) -> None:
        self.user_repository = user_repository
        self.user_service = user_service
        self.send_mail = False

    def change_send_mail_setting(self, is_send: bool):
        self.send_mail = is_send

    def register(self, command: UserRegisterCommand) -> None:
        user = User(None, UserName(command.name))

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, "ユーザは既に存在しています。")

        self.user_repository.save(user)

        if self.send_mail:
            MailUtility().send('user registered')


if __name__ == '__main__':
    # モックオブジェクトやスタブの作成
    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None
            
        def find_by_user_name(self, name: UserName):
            for elem in self.store.values():
                if elem.name.value == name.value:
                    return self.clone(elem)
            return None

        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def delete(self, user: User):
            if user.id.value in self.store:
                del self.store[user.id.value]

        def clone(self, user: User):
            return User(user.id, user.name)

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

    user_name_b = 'kato taro'
    command_b = UserRegisterCommand(user_name_b)

    user_application_service.change_send_mail_setting(True)
    user_application_service.register(command_b)
    print(f"{user_name_b} の登録が完了しました。")
