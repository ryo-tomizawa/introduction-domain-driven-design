from iuser_repository import IUserRepository
from typing import Dict
from user import User
from user_id import UserId

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.store = {}

    def find(self, user_name: str):
        target = next((user for user in self.store.values() if user_name == user.name), None)
        if target:
            # インスタンスを直接返さずディープコピーを行う
            return self.clone(target)
        else:
            return None

    def save(self, user: User):
        # 保存時もディープコピーを行う
        self.store[user.id] = self.clone(user)

    # ディープコピーを行うメソッド
    def clone(self, user: User):
        return User(user.id, user.name)


if __name__ == '__main__':
    # ユーザーとリポジトリを作成
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    repository = InMemoryUserRepository()

    # ユーザーを保存
    repository.save(user1)
    repository.save(user2)

    # ユーザーを検索して表示
    found_user = repository.find("Alice")
    print(found_user)