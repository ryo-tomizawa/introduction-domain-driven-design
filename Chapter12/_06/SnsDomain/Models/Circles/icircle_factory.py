import os
import sys
from circle_name import CircleName

current_dir = os.path.dirname(__file__)
user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
sys.path.append(user_dir)

from user import User

class ICircleFactory:
    def create(self, name: CircleName, owner: User):
        pass


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

    user = User(UserId('111-222-333'), UserName('tanaka taro'))
    circle_name = CircleName('sample circle')

    circle_factory = ICircleFactory()
    print(circle_factory.create(circle_name, user))