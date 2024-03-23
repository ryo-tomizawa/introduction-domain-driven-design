import os
import sys
from typing import Union

current_dir = os.path.dirname(__file__)
models_users_dir = os.path.abspath(os.path.join(current_dir,'../../Models/Users'))
sys.path.append(models_users_dir)

from user_name import UserName
from user import User

class CanNotRegisterUserException(Exception):
    def __init__(self, user: Union[User, UserName], message):
        super().__init__(message)
        if isinstance(user, User):
            self._id = user.id.value
            self._name = user.name.value
        elif isinstance(user, UserName):
            self._id = None
            self._name = user.value
        else:
            self._id = None
            self._name = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    from user_id import UserId

    user = User(UserId('111-222-333'), UserName('tanaka taro'))

    try:
        raise CanNotRegisterUserException(user, 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.id}')
        print(f'User Name: {e.name}')
    

    try:
        raise CanNotRegisterUserException(UserName('john smith'), 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.id}')
        print(f'User Name: {e.name}')