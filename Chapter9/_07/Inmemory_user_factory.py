from user_id import UserId
from user_name import UserName
from user import User

class InMemoryUserFactory:
    def __init__(self) -> None:
        self.current_id = 0

    def create(self, name: UserName) -> User:
        self.current_id += 1

        return User(UserId(str(self.current_id)), name)
    

if __name__ == '__main__':
    user_factory = InMemoryUserFactory()

    name_a = UserName('tanaka taro')
    name_b = UserName('john smith')

    user_a = user_factory.create(name_a)
    print(user_a.id.value, user_a.name.value)

    print('*'*100)

    user_b = user_factory.create(name_b)
    print(user_b.id.value, user_b.name.value)