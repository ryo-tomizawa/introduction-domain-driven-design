from user_name import UserName
from user import User

class CanNotRegisterUserException(Exception):
    def __init__(self, user: User, message):
        super().__init__(message)
        if isinstance(user, User):
            self._id = user.id.value
            self._name = user.name.value
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