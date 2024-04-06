import sys
import os

current_dir = os.path.dirname(__file__)
models_users_dir = os.path.abspath(os.path.join(current_dir,'../../SnsDomain/Models/Users'))
sys.path.append(models_users_dir)

from user_id import UserId

class UserNotFoundException(Exception):
    def __init__(self, user_id: UserId, message):
            super().__init__(message)
            self._user_id = user_id.value

    @property
    def user_id(self):
        return self._user_id


if __name__ == '__main__':
    user_id = UserId('111-222-333')

    try:
        raise UserNotFoundException(user_id, 'User not found.')
    except UserNotFoundException as e:
        print(f'Error: {e}')
        print(f'User ID: {e.user_id}')
