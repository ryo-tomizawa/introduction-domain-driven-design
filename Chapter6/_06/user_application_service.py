from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from user_id import UserId
from user_service import UserService
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

    def get(self, user_id: str):
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)

        return user


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
    user_application_service.register(user_name)
    print(f"{user_name} の登録が完了しました。")

    print('*'*100)

    get_user = user_application_service.get('222-333-444')
    print(get_user.id.value, get_user.name.value)