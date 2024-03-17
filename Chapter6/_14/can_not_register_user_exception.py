from typing import Union

from user_name import UserName
from user import User

class CanNotRegisterUserException(Exception):
    def __init__(self, user: Union[User, UserName], message):
        super().__init__(message)
        if isinstance(user, User):
            self._id = user.id.value
            self._name = user.name.value
            self._mail_address = user.mail_address.value
        elif isinstance(user, UserName):
            self._id = None
            self._name = user.value
            self._mail_address = None
        else:
            self._id = None
            self._name = None
            self._mail_address = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def mail_address(self):
        return self._mail_address


if __name__ == '__main__':
    from mail_address import MailAddress
    from user_id import UserId

    user = User(UserId('111-222-333'), UserName('tanaka taro'), MailAddress('test@example.com'))

    try:
        raise CanNotRegisterUserException(user, 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.id}')
        print(f'User Name: {e.name}')
        print(f'User MailAddress: {e.mail_address}')
    

    try:
        raise CanNotRegisterUserException(UserName('john smith'), 'Registration failed.')
    except CanNotRegisterUserException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.id}')
        print(f'User Name: {e.name}')
        print(f'User MailAddress: {e.mail_address}')