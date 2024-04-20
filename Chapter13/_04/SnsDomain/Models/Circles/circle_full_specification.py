import os
import sys

current_dir = os.path.dirname(__file__)
user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
sys.path.append(user_model_dir)

from iuser_repository import IUserRepository
from circle import Circle

class CircleFullSpecification:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def is_satisfied_by(self, circle: Circle) -> bool:
        users = self.user_repository.find_all_members(circle.members)
        premium_user_number = sum(user.is_premium for user in users)
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        return circle.count_member() >= circle_upper_limit
    

if __name__ == '__main__':
    from typing import Optional, List

    from user_id import UserId
    from user_name import UserName
    from user import User
    from circle_id import CircleId
    from circle_name import CircleName

    class MockUserRepository(IUserRepository):
        def find(self, id: UserId) -> Optional[User]:
            return User(UserId('111-222-333'), UserName('tanaka taro'))

        def find_by_user_name(self, name: UserName) -> Optional[User]:
            pass

        def find_all(self) -> Optional[User]:
            pass

        def save(self, user: User) -> None:
            pass

        def delete(self, user: User) -> None:
            pass

        def find_all_members(self, circle_members: List[UserId]) -> List[User]:
            return [User(UserId('111-222-333'), UserName('tanaka taro'))]
        
    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_1 = User(UserId('userid1'), UserName('username1'))

    circle = Circle(circle_id, circle_name, owner, [member_1])

    user_repository = MockUserRepository()
    circle_full_specification = CircleFullSpecification(user_repository)
    print(circle_full_specification.is_satisfied_by(circle))