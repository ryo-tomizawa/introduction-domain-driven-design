import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Circles'))
circle_invitation_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/CircleInvitations'))
user_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Users'))
circle_create_dir = os.path.abspath(os.path.join(current_dir, './Create'))
circle_join_dir = os.path.abspath(os.path.join(current_dir, './Join'))
circle_update_dir = os.path.abspath(os.path.join(current_dir, './Update'))
app_user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

sys.path.append(circle_model_dir)
sys.path.append(circle_invitation_dir)
sys.path.append(user_model_dir)
sys.path.append(circle_create_dir)
sys.path.append(circle_join_dir)
sys.path.append(circle_update_dir)
sys.path.append(app_user_dir)

from icircle_factory import ICircleFactory
from icircle_repository import ICircleRepository
from circle_service import CircleService
from iuser_repository import IUserRepository
from circle_create_command import CircleCreateCommand
from user_id import UserId
from user_not_found_exception import UserNotFoundException
from can_not_register_user_exception import CanNotRegisterCircleException
from circle_name import CircleName
from circle_join_command import CircleJoinCommand
from circle_update_command import CircleUpdateCommand
from circle_id import CircleId
from circle_not_found_exception import CircleNotFoundException
from circle_full_exception import CircleFullException

class CircleApplicationService:
    def __init__(self,
                 circle_factory: ICircleFactory,
                 circle_repository: ICircleRepository,
                 circle_service: CircleService,
                 user_repository: IUserRepository) -> None:

        self.circle_factory = circle_factory
        self.circle_repository = circle_repository
        self.circle_service = circle_service
        self.user_repository = user_repository

    def join(self, command: CircleJoinCommand):
        circle_id = CircleId(command.circle_id)
        circle = self.circle_repository.find(circle_id)

        users = self.user_repository.find_all_members(circle.members)
        # サークルに所属しているプレミアムユーザの人数により上限が変わる
        premium_user_number = sum(user.is_premium for user in users)
        circle_upper_limit = 30 if premium_user_number < 10 else 50

        if len(circle.members) >= circle_upper_limit:
            raise CircleFullException(circle_id)
        
        member_id = UserId(command.user_id)
        member = self.user_repository.find(member_id)
        if member is None:
            raise UserNotFoundException(member_id, 'ユーザが見つかりませんでした。')
                
        circle.members.append(member)
        self.circle_repository.save(circle)
        

if __name__ == '__main__':
    from circle import Circle
    from user_name import UserName
    from user import User
    from typing import Optional, List

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
        
    class MockCircleRepository(ICircleRepository):
        def save(self, circle: Circle) -> None:
            pass

        def find(self, id: CircleId) -> Circle:
            return Circle(CircleId('1111'), 
                          CircleName('sample cirrcle'), 
                          User(UserId('111-222-333'), UserName('tanaka taro')), 
                          [User(UserId('222-333-444'), UserName('john smith'))]
                          )

        def find_by_name(self, name: CircleName) -> Circle:
            pass

    circle_factory = ICircleFactory()
    circle_repository = MockCircleRepository()
    circle_service = CircleService(circle_repository)
    user_repository = MockUserRepository()

    circle_application_service = CircleApplicationService(
        circle_factory, 
        circle_repository, 
        circle_service, 
        user_repository
        )

    circle_join_command = CircleJoinCommand('111-222-333', '1111')

    circle_application_service.join(circle_join_command)