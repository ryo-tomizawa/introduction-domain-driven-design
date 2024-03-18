from user_id import UserId

class UserNotFoundException(Exception):
    def __init__(self, user_id: UserId, message):
            super().__init__(message)
            self._user_id = user_id.value

    @property
    def user_id(self):
        return self._user_id


if __name__ == '__main__':
    from user_name import UserName
    from user import User

    user_id = UserId('111-222-333')

    try:
        raise UserNotFoundException(user_id, 'User not found.')
    except UserNotFoundException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.user_id}')
