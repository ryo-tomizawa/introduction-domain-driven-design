import os
import sys
from typing import List

current_dir = os.path.dirname(__file__)
user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
sys.path.append(user_dir)

from circle_id import CircleId
from circle_name import CircleName
from user import User

class Circle:
    def __init__(self,
                 id: CircleId,
                 name: CircleName,
                 owner: User,
                 member: List[User]
                 ) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        if owner is None: raise ValueError(f'incorrect value: {owner}')
        if member is None: raise ValueError(f'incorrect value: {member}')

        self._id = id
        self._name = name
        self._owner = owner
        self._member = member

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner
    
    @property
    def member(self):
        return self._member
    
    @member.setter
    def member(self, new_member):
        self._member = new_member


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_a = User(UserId('222-333-444'), UserName('john smith'))
    member_b = User(UserId('333-444-555'), UserName('james bond'))

    members =[member_a, member_b]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    circle = Circle(circle_id, circle_name, owner, members)

    print(f'circle id is {circle.id.value}')
    print(f'circle name is {circle.name.value}')
    print(f'owner id is {circle.owner.id.value}, owner name is {circle.owner.name.value}')
    for member in circle.member:
        print(f'member id is {member.id.value}, member name is {member.name.value}')