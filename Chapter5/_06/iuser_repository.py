from abc import ABC

from user import User
from user_name import UserName

class IUserRepository(ABC):
    def save(self, user: User):
        pass

    def find(self, user_name: UserName):
        pass

    def exists(self, user: User):
        pass


if __name__ == '__main__':
    user_repository=IUserRepository()

    user_name = UserName('Tanaka')
    user = User(user_name)

    # 具体的な処理が何も書かれていないため、両方ともNoneが返される
    print(user_repository.save(user))
    print(user_repository.find(user_name))
    print(user_repository.exists(user))