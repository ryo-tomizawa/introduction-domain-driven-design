from icircle_repository import ICircleRepository
from circle import Circle

class CircleService:
    def __init__(self, circle_repository: ICircleRepository) -> None:
        self.circle_repository = circle_repository

    def exists(self, circle: Circle) -> bool:
        duplicated = self.circle_repository.find_by_name(circle.name)
        return duplicated is not None


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
    from circle_id import CircleId
    from circle_name import CircleName

    circle_repository = ICircleRepository()
    circle_service = CircleService(circle_repository)

    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_a = User(UserId('222-333-444'), UserName('john smith'))
    member_b = User(UserId('333-444-555'), UserName('james bond'))

    members =[member_a, member_b]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    now = datetime.now()

    circle = Circle(circle_id, circle_name, owner, members, now)

    print(circle_service.exists(circle))