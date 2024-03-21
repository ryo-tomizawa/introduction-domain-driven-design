from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User

class InMemoryUserRepository(IUserRepository):
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


if __name__ == '__main__':
    user1 = User(UserId('111-222-333'), UserName('tanaka taro'))
    user2 = User(UserId('222-333-444'), UserName('john smith'))
    repository = InMemoryUserRepository()

    # ユーザーを保存
    repository.save(user1)
    repository.save(user2)

    # ユーザーを検索して表示
    found_user = repository.find(UserId('111-222-333'))
    print(found_user.id.value, found_user.name.value)