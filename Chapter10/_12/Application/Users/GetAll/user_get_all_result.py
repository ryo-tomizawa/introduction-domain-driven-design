import os
import sys
from typing import List

current_dir = os.path.dirname(__file__)
user_dir =os.path.abspath(os.path.join(current_dir, '../Commons'))
sys.path.append(user_dir)

from user_data import UserData

class UserGetAllResult:
    def __init__(self, users: List[UserData]) -> None:
        self._users = users

    @property
    def users(self):
        return self._users


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName
    from user import User

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_b = User(UserId('222-333-444'), UserName('john smith'))

    user_data_a = UserData(user_a)
    user_data_b = UserData(user_b)

    users = [user_data_a, user_data_b]

    user_get_result = UserGetAllResult(users)
    all_users = user_get_result.users

    for user in all_users:
        print(user.id, user.name)