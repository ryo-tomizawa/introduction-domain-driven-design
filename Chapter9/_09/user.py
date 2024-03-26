import sqlite3

from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, name: UserName) -> None:
        self._id = None
        self._name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    
    user = User(user_name)

    user.id = user_id

    print(user.id.value, user._name.value)