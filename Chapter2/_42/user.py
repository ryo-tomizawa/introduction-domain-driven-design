from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        self._id = id
        self._name = name
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @id.setter
    def id(self, value: UserId):
        self._id = value

    @name.setter
    def name(self, value: UserName):
        self._name = value



if __name__ == '__main__':
    user_id = UserId('1-2-3')
    user_name = UserName('tanaka taro')

    user = User(user_id, user_name)
    print(user.id.value, user.name.value)

    print('*'*100)

    user.id = UserId('9-8-7')
    user.name = UserName('kato taro')

    print(user.id.value, user.name.value)