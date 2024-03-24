import sqlite3

from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        

        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    def change_name(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._name = name


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    user = User(user_id, user_name)

    print(user.id.value, user.name.value)