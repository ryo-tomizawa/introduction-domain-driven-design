import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Circles'))
sys.path.append(circle_model_dir)

from circle import Circle
from circle_id import CircleId

class CircleNotFoundException(Exception):
    def __init__(self, id: CircleId, message: str = ''):
        super().__init__(message)
        self._id = id.value

    @property
    def id(self):
        return self._id

if __name__ == '__main__':
    from circle_name import CircleName

    user_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Users'))
    sys.path.append(user_model_dir)

    from user_id import UserId
    from user_name import UserName
    from user import User

    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_a = User(UserId('222-333-444'), UserName('john smith'))
    member_b = User(UserId('333-444-555'), UserName('james bond'))

    members =[member_a, member_b]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    circle = Circle(circle_id, circle_name, owner, members)

    try:
        raise CircleNotFoundException(circle_id, 'Registration failed.')
    except CircleNotFoundException as e:
        print(f'Error: {e}')
        print(f'Circle ID: {e.id}')