from userId import UserId
from userName import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if id is None:
            raise ValueError(f'incorrect UserId: {id}')
        if name is None:
            raise ValueError(f'incorrect UserName: {name}')
        self._id = id
        self.name = name

    @classmethod
    def exists(cls, user_left: 'User', user_right: 'User') -> bool:
        return user_left._id.value == user_right._id.value and user_left.name.value == user_right.name.value

if __name__ == '__main__':
    id_1 = UserId('111')
    name_1 = UserName('Tanaka')

    id_2 = UserId('111')
    name_2 = UserName('Tanaka')

    user_1 = User(id_1, name_1)
    user_2 = User(id_2, name_2)
    print(User.exists(user_1, user_2))

    id_3 = UserId('111')
    name_3 = UserName('Kato')
    user_3 = User(id_3, name_3)
    print(User.exists(user_1, user_3))