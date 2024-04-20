from typing import List
import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../Circles'))
user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

sys.path.append(circle_model_dir)
sys.path.append(user_model_dir)

from circle_id import CircleId
from circle_name import CircleName
from user import User

class CircleMembers:
    def __init__(self, id: CircleId, owner: User, members: List[User]) -> None:
        self._id = id
        self._owner = owner
        self._members = members

    @property
    def id(self) -> None:
        return self._id
    
    def count_members(self) -> int:
        return len(self._members) + 1
    
    def count_premium_members(self, contains_owner: bool = True):
        premium_user_number = sum(user.is_premium for user in self._members)
        if contains_owner:
            return premium_user_number + 1 if self._owner.is_premium else 0
        else:
            return premium_user_number


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

    circle_id = CircleId('1111')
    owner = User(UserId('111-222-333'), UserName('tanaka taro'), True)
    member_1 = User(UserId('userid1'), UserName('username1'), True)
    member_2 = User(UserId('userid2'), UserName('username2'), True)
    member_3 = User(UserId('userid3'), UserName('username3'), True)
    member_4 = User(UserId('userid4'), UserName('username4'), True)
    member_5 = User(UserId('userid5'), UserName('username5'), True)
    members = [member_1, member_2, member_3, member_4, member_5]

    circle_members = CircleMembers(circle_id, owner, members)
    print(f'members count is {circle_members.count_members()}')

    print('*'*100)

    print(f'premium members count is {circle_members.count_premium_members(False)}')