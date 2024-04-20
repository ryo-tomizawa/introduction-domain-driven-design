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
circle_members_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/CircleMembers'))

sys.path.append(circle_model_dir)
sys.path.append(circle_invitation_dir)
sys.path.append(user_model_dir)
sys.path.append(circle_create_dir)
sys.path.append(circle_join_dir)
sys.path.append(circle_update_dir)
sys.path.append(app_user_dir)
sys.path.append(circle_members_dir)

from icircle_factory import ICircleFactory
from icircle_repository import ICircleRepository
from circle_service import CircleService
from iuser_repository import IUserRepository
from user_id import UserId
from user_not_found_exception import UserNotFoundException
from can_not_register_user_exception import CanNotRegisterCircleException
from circle_name import CircleName
from circle_join_command import CircleJoinCommand
from circle_id import CircleId
from circle_not_found_exception import CircleNotFoundException
from circle_full_exception import CircleFullException
from circle_members import CircleMembers
from circle_members_full_specification import CircleMembersFullSpecification

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

        owner = self.user_repository.find(circle.owner)
        members = self.user_repository.find_all_members(circle.members)
        circle_members = CircleMembers(circle.id, owner, members)
        circle_full_specification = CircleMembersFullSpecification()
        if circle_full_specification.is_satisfied_by(circle_members):
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