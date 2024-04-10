import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Circles'))
circle_invitation_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/CircleInvitations'))
user_model_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Users'))
circle_create_dir = os.path.abspath(os.path.join(current_dir, './Create'))
circle_join_dir = os.path.abspath(os.path.join(current_dir, './Join'))
app_user_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

sys.path.append(circle_model_dir)
sys.path.append(circle_invitation_dir)
sys.path.append(user_model_dir)
sys.path.append(circle_create_dir)
sys.path.append(circle_join_dir)
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

    def create(self, command: CircleCreateCommand) -> None:
        owner_id = UserId(command.user_id)
        owner = self.user_repository.find(owner_id)
        if owner is None:
            raise UserNotFoundException(owner_id, 'サークルのオーナーとなるユーザが見つかりませんでした。')
        
        name = CircleName(command.name)
        circle = self.circle_factory.create(name, owner)
        if self.circle_service.exists(circle):
            raise CanNotRegisterCircleException(circle, 'サークルは既に存在しています。')

        self.circle_repository.save(circle)

    def join(self, command: CircleJoinCommand):
        member_id = UserId(command.user_id)
        member = self.user_repository.find(member_id)
        if member is None:
            raise UserNotFoundException(member_id, 'ユーザが見つかりませんでした。')
        
        id = CircleId(command.id)
        circle = self.circle_repository(id)
        if circle is None:
            raise CircleNotFoundException(id, 'ユーザが見つかりませんでした。')
        
        if circle.is_full():
            raise CircleFullException(id)
        
        circle.member.append(member)
        self.circle_repository.save(circle)

if __name__ == '__main__':
    from circle import Circle
    from user_name import UserName
    from user import User

    circle_factory = ICircleFactory()
    circle_repository = ICircleRepository()
    circle_service = CircleService(circle_repository)
    user_repository = IUserRepository()

    circle_application_service = CircleApplicationService(
        circle_factory, 
        circle_repository, 
        circle_service, 
        user_repository
        )

    circle_create_command = CircleCreateCommand('111-222-333', 'sample circle')
    circle_application_service.create(circle_create_command)

    circle_join_command = CircleJoinCommand('222-333-444', '1111')
    circle_application_service.join(circle_join_command)