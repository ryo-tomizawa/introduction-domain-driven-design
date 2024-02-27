from abc import ABC
from typing import Optional

from user import User
from user_name import UserName

class IUserRepository(ABC):
    def save(self, user: User):
        pass

    # 静的型付けを用いて返り値をOptional型で定義
    def find(self, user_name: UserName) -> Optional[User]:
        pass


if __name__ == '__main__':
    user_repository=IUserRepository()

    user_name = UserName('Tanaka')
    user = User(user_name)

    # 具体的な処理が何も書かれていないため、両方ともNoneが返される
    print(user_repository.save(user))
    print(user_repository.find(user_name))