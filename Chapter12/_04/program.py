import os
import sys

current_dir = os.path.dirname(__file__)
circle_dir = os.path.abspath(os.path.join(current_dir, './SnsDomain/Models/Circles'))
user_dir = os.path.abspath(os.path.join(current_dir, './SnsDomain/Models/Models'))
sys.path.append(circle_dir)
sys.path.append(user_dir)

from circle_id import CircleId
from circle_name import CircleName
from circle import Circle

from user_id import UserId
from user_name import UserName
from user import User

class Program:
    def main(self):
        circle_id = CircleId('test-circle-id')
        circle_name = CircleName('test-circle-name')
        owner = User(UserId('owner-user-id'), UserName('owner-user-name'))

        circle = Circle(circle_id, circle_name, owner, [])

        member = User(UserId('member-user-id'), UserName('member-user-name'))
        circle.join(member)


if __name__ == '__main__':
    program = Program()
    program.main()