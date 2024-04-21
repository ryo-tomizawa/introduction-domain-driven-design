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
circle_recommend_dir = os.path.abspath(os.path.join(current_dir, './GetRecommend'))

sys.path.append(circle_model_dir)
sys.path.append(circle_invitation_dir)
sys.path.append(user_model_dir)
sys.path.append(circle_create_dir)
sys.path.append(circle_join_dir)
sys.path.append(circle_update_dir)
sys.path.append(app_user_dir)
sys.path.append(circle_recommend_dir)

from datetime import datetime
from icircle_factory import ICircleFactory
from icircle_repository import ICircleRepository
from circle_service import CircleService
from iuser_repository import IUserRepository
from user_id import UserId
from circle_name import CircleName
from circle_join_command import CircleJoinCommand
from circle_id import CircleId
from circle_get_recommend_request import CircleGetRecommendRequest
from circle_get_recommend_result import CircleGetRecommendResult

class CircleApplicationService:
    def __init__(self,
                 circle_factory: ICircleFactory,
                 circle_repository: ICircleRepository,
                 circle_service: CircleService,
                 user_repository: IUserRepository,
                 now: datetime) -> None:

        self.circle_factory = circle_factory
        self.circle_repository = circle_repository
        self.circle_service = circle_service
        self.user_repository = user_repository
        self.now = now

    def get_recommended(self, request: CircleGetRecommendRequest) -> CircleGetRecommendResult:
        recommeded_circles = self.circle_repository.find_recommended(self.now)
        return CircleGetRecommendResult(recommeded_circles)
        

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

        def find_recommended(self, now: datetime) -> List[Circle]:
            circle_1 = Circle(CircleId('1111'), 
                        CircleName('sample cirrcle'), 
                        User(UserId('111-222-333'), UserName('tanaka taro')), 
                        [User(UserId('222-333-444'), UserName('john smith'))]
                        )
            circle_2 = Circle(CircleId('2222'), 
                        CircleName('test cirrcle'), 
                        User(UserId('333-444-555'), UserName('owner_2')), 
                        [User(UserId('666-777-888'), UserName('member_2'))]
                        )
            return [circle_1, circle_2]

    circle_factory = ICircleFactory()
    circle_repository = MockCircleRepository()
    circle_service = CircleService(circle_repository)
    user_repository = MockUserRepository()
    now = datetime.now()

    circle_application_service = CircleApplicationService(
        circle_factory, 
        circle_repository, 
        circle_service, 
        user_repository,
        now
        )
    
    recommend_circles = circle_application_service.get_recommended('')
    for circle in recommend_circles.summaries:
        print(f'circle id is {circle.id}')
        print(f'circle name is {circle.name}')