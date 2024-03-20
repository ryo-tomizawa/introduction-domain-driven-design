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
    repository = InMemoryUserRepository()

    user_1 = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_2 = User(UserId('222-333-444'), UserName('john smith'))

    repository.save(user_1)
    repository.save(user_2)

    print(f'Find by ID "111-222-333":, {repository.find(UserId("111-222-333"))}')
    print(f'Find by ID "222-333-444":, {repository.find(UserId("222-333-444"))}')

    print(f'Find by Name "tanaka taro":, {repository.find_by_user_name(UserId("tanaka taro"))}')
    print(f'Find by Name "john smith":, {repository.find_by_user_name(UserId("john smith"))}')

    repository.delete(user_1)
    print(f'After deleting tanaka taro, find by ID "1":, {repository.find(UserId("111-222-333"))}')