from typing import List

from circle_id import CircleId
from circle_name import CircleName
from circle import Circle

from datetime import datetime

class ICircleRepository:
    def save(self, circle: Circle) -> None:
        pass

    def find(self, id: CircleId) -> Circle:
        pass

    def find_by_name(self, name: CircleName) -> Circle:
        pass

    def find_recommended(self, now: datetime) -> List[Circle]:
        pass


if __name__ == '__main__':
    import os
    import sys

    current_dir = os.path.dirname(__file__)
    user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
    sys.path.append(user_dir)

    from datetime import datetime
    from user_id import UserId
    from user_name import UserName
    from user import User

    circle_repository = ICircleRepository()

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_a = User(UserId('222-333-444'), UserName('john smith'))
    member_b = User(UserId('333-444-555'), UserName('james bond'))
    members =[member_a, member_b]
    now = datetime.now()

    circle = Circle(circle_id, circle_name, owner, members, now)

    print(circle_repository.save(circle))
    print(circle_repository.find(circle_id))
    print(circle_repository.find_by_name(circle_name))
    print(circle_repository.find_recommended(datetime.now()))