from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName, is_premium: bool = False) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        

        self._id = id
        self._name = name
        self._is_premium = is_premium

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def is_premium(self):
        return self._is_premium

    def change_name(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._name = name


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    user = User(user_id, user_name)

    print(user.id.value, user.name.value, user.is_premium)