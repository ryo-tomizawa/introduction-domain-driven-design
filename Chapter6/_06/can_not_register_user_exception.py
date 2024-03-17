from typing import Union

from user_name import UserName
from user import User

class CanNotRegisterUserException(Exception):
    def __init__(self, user: Union[User, UserName], message):
        super().__init__(message)
        if isinstance(user, User):
            self.id = user.id.value
            self.name = user.name.value
        elif isinstance(user, UserName):
            self.id = None
            self.name = user.value
        else:
            self.id = None
            self.name = None

    @property
    def Id(self):
        return self.id

    @property
    def Name(self):
        return self.name


if __name__ == '__main__':
    from user_id import UserId

    user = User(UserId('111-222-333'), UserName('tanaka taro'))

    try:
        raise CanNotRegisterUserException(user, 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.Id}')
        print(f'User Name: {e.Name}')
    

    try:
        raise CanNotRegisterUserException(UserName('john smith'), 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.Id}')
        print(f'User Name: {e.Name}')