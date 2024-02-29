from iuser_repository import IUserRepository
from user import User

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.store = {}

    def find(self, user_name: str):
        target = next((user for user in self.store.values() if user_name == user.name.value), None)
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
        return User(user.name, user.id)


if __name__ == '__main__':
    from user_name import UserName
    user1 = User(UserName("Alice"), 1)
    user2 = User(UserName("Bob"), 2)
    repository = InMemoryUserRepository()

    # ユーザーを保存
    repository.save(user1)
    repository.save(user2)

    # ユーザーを検索して表示
    found_user = repository.find("Alice")
    print(found_user.name)