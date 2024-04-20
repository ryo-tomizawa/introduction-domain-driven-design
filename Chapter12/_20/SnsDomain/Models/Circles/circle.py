import os
import sys
from typing import List

current_dir = os.path.dirname(__file__)
user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
sys.path.append(user_dir)

from circle_id import CircleId
from circle_name import CircleName
from circle_full_exception import CircleFullException
from user_id import UserId
from user_name import UserName
from user import User

class Circle:
    def __init__(self,
                 id: CircleId,
                 name: CircleName,
                 owner: User,
                 members: List[UserId]
                 ) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        if owner is None: raise ValueError(f'incorrect value: {owner}')
        if members is None: raise ValueError(f'incorrect value: {members}')

        self._id = id
        self._name = name
        self._owner = owner
        self._members = members

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def members(self):
        return self._members

    def is_full(self) -> bool:
        return len(self._members) >= 29

    def join(self, user: User):
        if user is None: raise ValueError(f'incorrect value: {user}')

        if (self.is_full()):
            raise CircleFullException(self._id)
        self._members.append(user.id)

    def change_name(self, name: CircleName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')
        self.name = name


if __name__ == '__main__':
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_1 = User(UserId('userid1'), UserName('username1'))
    member_2 = User(UserId('userid2'), UserName('username2'))
    member_3 = User(UserId('userid3'), UserName('username3'))
    member_4 = User(UserId('userid4'), UserName('username4'))
    member_5 = User(UserId('userid5'), UserName('username5'))
    member_6 = User(UserId('userid6'), UserName('username6'))
    member_7 = User(UserId('userid7'), UserName('username7'))
    member_8 = User(UserId('userid8'), UserName('username8'))
    member_9 = User(UserId('userid9'), UserName('username9'))
    member_10 = User(UserId('userid10'), UserName('username10'))
    member_11 = User(UserId('userid11'), UserName('username11'))
    member_12 = User(UserId('userid12'), UserName('username12'))
    member_13 = User(UserId('userid13'), UserName('username13'))
    member_14 = User(UserId('userid14'), UserName('username14'))
    member_15 = User(UserId('userid15'), UserName('username15'))
    member_16 = User(UserId('userid16'), UserName('username16'))
    member_17 = User(UserId('userid17'), UserName('username17'))
    member_18 = User(UserId('userid18'), UserName('username18'))
    member_19 = User(UserId('userid19'), UserName('username19'))
    member_20 = User(UserId('userid20'), UserName('username20'))
    member_21 = User(UserId('userid21'), UserName('username21'))
    member_22 = User(UserId('userid22'), UserName('username22'))
    member_23 = User(UserId('userid23'), UserName('username23'))
    member_24 = User(UserId('userid24'), UserName('username24'))
    member_25 = User(UserId('userid25'), UserName('username25'))
    member_26 = User(UserId('userid26'), UserName('username26'))
    member_27 = User(UserId('userid27'), UserName('username27'))
    member_28 = User(UserId('userid28'), UserName('username28'))
    member_29 = User(UserId('userid29'), UserName('username29'))

    members =[member_1.id,member_2.id,member_3.id,member_4.id,member_5.id,
              member_6.id,member_7.id,member_8.id,member_9.id,member_10.id,
              member_11.id,member_12.id,member_13.id,member_14.id,member_15.id,
              member_16.id,member_17.id,member_18.id,member_19.id,member_20.id,
              member_21.id,member_22.id,member_23.id,member_24.id,member_25.id,
              member_26.id,member_27.id,member_28.id]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    circle = Circle(circle_id, circle_name, owner, members)

    print(f'circle id is {circle.id.value}')
    print(f'circle name is {circle.name.value}')
    print(f'owner id is {circle.owner.id.value}, owner name is {circle.owner.name.value}')

    print('*'*100)
    circle.join(member_29)


    for member in circle.members:
        print(member.value)

    print('*'*100)

    # 30人目のサークルメンバーのため、CircleFullExceptionとなる
    member_30 = User(UserId('userid30'), UserName('username30'))
    circle.join(member_30.id)