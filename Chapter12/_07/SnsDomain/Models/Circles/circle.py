import os
import sys
from typing import List

current_dir = os.path.dirname(__file__)
user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
sys.path.append(user_dir)

from circle_full_exception import CircleFullException
from circle_id import CircleId
from circle_name import CircleName
from user import User

class Circle:
    def __init__(self,
                 id: CircleId,
                 name: CircleName,
                 owner: User,
                 members: List[User]
                 ) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        if owner is None: raise ValueError(f'incorrect value: {owner}')
        if members is None: raise ValueError(f'incorrect value: {members}')

        self._id = id
        self._name = name
        self._owner = owner
        self._members = members

    def is_full(self) -> bool:
        return len(self._members) >= 29
    
    def join(self, user: User) -> None:
        if user is None: raise ValueError(f'incorrect value: {user}')
        if self.is_full(): raise CircleFullException(self._id)
        
        self._members.append(user)

if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

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

    members =[member_1,member_2,member_3,member_4,member_5,member_6,member_7,member_8,member_9,member_10,
              member_11,member_12,member_13,member_14,member_15,member_16,member_17,member_18,member_19,member_20,
              member_21,member_22,member_23,member_24,member_25,member_26,member_27,member_28]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    circle = Circle(circle_id, circle_name, owner, members)

    print(f'circle id is {circle._id.value}')
    print(f'circle name is {circle._name.value}')
    print(f'owner id is {circle._owner.id.value}, owner name is {circle._owner.name.value}')
    print(f'circle is_full method: {circle.is_full()}')

    print('*'*100)

    # 29人目のサークルメンバーを追加したため、is_full()の結果がtrue   
    circle.join(member_29)
    print(f'circle is_full method: {circle.is_full()}')