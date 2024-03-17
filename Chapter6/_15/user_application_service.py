from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from mail_address import MailAddress
from user_data import UserData
from user_id import UserId
from user_service import UserService
from user_not_found_exception import UserNotFoundException
from user_name import UserName
from user import User

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository, user_service: UserService) -> None:
        self.user_repository = user_repository
        self.user_service = user_service

    def register(self, name: str) -> None:
        user = User(None, UserName(name))

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
        
        self.user_repository.save(user)

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user.id.value, user.name.value)
        return user_data
    
    def update(self, user_id: str, name: str) -> None:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: raise UserNotFoundException(target_id)

        new_user_name = UserName(name)
        user.change_name(new_user_name)
        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')

        self.user_repository.save(user)


if __name__ == '__main__':
    # モックオブジェクトやスタブの作成
    class MockUserRepository(IUserRepository):
        def save(self, user: User) -> None:
            print(f"ユーザー {user.name.value} を保存しました。")

        def find(self, id: UserId) -> User:
            return User(id, UserName('john smith'))

    class MockUserService(UserService):
        def exists(self, user: User) -> bool:
            # ここでは常にFalseを返すことで、どんなユーザーも存在しないとする
            # Trueにすることで、エラーパターンのテストも可能
            return False

    user_repository = MockUserRepository()
    user_service = MockUserService(user_repository)
    user_application_service = UserApplicationService(user_repository, user_service)

    # ユーザー登録のテスト
    user_name = 'tanaka taro'
    mail_address = 'test@example.com'
    user_application_service.register(user_name)
    print(f"{user_name} の登録が完了しました。")

    print('*'*100)

    get_user_data = user_application_service.get('222-333-444')
    print(get_user_data.id, get_user_data.name)

    print('*'*100)

    user_application_service.update('222-333-444', 'john doe')
