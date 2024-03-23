import os
import sys

current_dir = os.path.dirname(__file__)
user_dir =os.path.abspath(os.path.join(current_dir, '../Commons'))
sys.path.append(user_dir)

from user_data import UserData

class UserGetResult:
    def __init__(self, user: UserData) -> None:
        self._user = user

    @property
    def user(self):
        return self._user


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName
    from user import User

    user = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_data = UserData(user)
    user_get_result = UserGetResult(user_data)

    print(
        user_get_result.user.id,
        user_get_result.user.name
          )
    