import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../Circles'))
user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

sys.path.append(circle_model_dir)
sys.path.append(user_model_dir)

from circle import Circle
from user import User

class CircleInvitation:
    def __init__(self, circle: Circle, from_user: User, invite_user: User) -> None:
        self._circle = circle
        self._from_user = from_user
        self._invite_user = invite_user

    @property
    def circle(self):
        return self._circle
    
    @property
    def from_user(self):
        return self._from_user
    
    @property
    def invite_user(self):
        return self._invite_user
    

if __name__ == '__main__':
    from circle_id import CircleId
    from circle_name import CircleName
    from user_id import UserId
    from user_name import UserName
    
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member = User(UserId('222-333-444'), UserName('john smith'))
    members =[member]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    circle = Circle(circle_id, circle_name, owner, members)

    print(f'circle id is {circle.id.value}')
    print(f'circle name is {circle.name.value}')
    print(f'owner id is {circle.owner.id.value}, owner name is {circle.owner.name.value}')
    for member in circle.member:
        print(f'member id is {member.id.value}, member name is {member.name.value}')

    print('*'*100)

    invite_user = User(UserId('333-444-555'), UserName('james bond'))

    circle_invitation = CircleInvitation(circle, owner, invite_user)
    print(f'circle name is {circle_invitation.circle.name.value}')
    print(f'from_user id is {circle_invitation.from_user.id.value}, from_user name is {circle_invitation.from_user.name.value}')
    print(f'invite_user id is {circle_invitation.invite_user.id.value}, invite_user name is {circle_invitation.invite_user.name.value}')