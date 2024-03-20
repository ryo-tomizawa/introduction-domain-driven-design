from inmemory_user_repository import InMemoryUserRepository
from user_data import UserData
from user_id import UserId
from user_name import UserName
from user import User

class UserApplicationService:
    def __init__(self) -> None:
        self.user_repository = InMemoryUserRepository()

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data


if __name__ == '__main__':
    user_application_service = UserApplicationService()

    # ユーザー登録のテスト
    user_name_a = 'tanaka taro'
    user_application_service.user_repository.save(User(None, UserName(user_name_a)))

    user_id_b = '222-333-444'
    user_name_b = 'kato taro'
    user_b = User(UserId(user_id_b), UserName(user_name_b))
    user_application_service.user_repository.save(user_b)

    print('*'*100)

    get_user_data = user_application_service.get('222-333-444')
    print(get_user_data.id, get_user_data.name)