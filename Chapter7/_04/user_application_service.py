from iuser_repository import IUserRepository
from user_data import UserData
from user_id import UserId
from user_name import UserName
from user import User

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data


if __name__ == '__main__':
    # モックオブジェクトやスタブの作成
    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def save(self, user: User) -> None:
            self.store[user.id.value] = self.clone(user)
            print(f"ユーザー {user.name.value}を保存しました。")

        def clone(self, user: User):
            return User(user.id, user.name)

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None


    user_repository = MockUserRepository()
    user_application_service = UserApplicationService(user_repository)

    # ユーザー登録のテスト
    user_name_a = 'tanaka taro'
    user_repository.save(User(None, UserName(user_name_a)))

    user_id_b = '222-333-444'
    user_name_b = 'kato taro'
    user_b = User(UserId(user_id_b), UserName(user_name_b))
    user_repository.save(user_b)

    print('*'*100)

    get_user_data = user_application_service.get('222-333-444')
    print(get_user_data.id, get_user_data.name)