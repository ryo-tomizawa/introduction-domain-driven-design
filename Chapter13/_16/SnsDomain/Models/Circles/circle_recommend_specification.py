import os
import sys
current_dir = os.path.dirname(__file__)
user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))
library_dir = os.path.abspath(os.path.join(current_dir, '../../Library/Specifications'))
sys.path.append(user_model_dir)
sys.path.append(library_dir)

from datetime import datetime, timedelta

from ispecification import ISpecification
from circle import Circle

class CircleRecommendSpecification(ISpecification):
    def __init__(self, execute_datetime: datetime) -> None:
        self.execute_datetime = execute_datetime

    def is_satisfied_by(self, circle: Circle) -> bool:
        if circle.count_member() < 10:
            return False

        return circle.created > self.execute_datetime - timedelta(days=30)
    

if __name__ == '__main__':


    from circle_id import CircleId
    from circle_name import CircleName
    from user_id import UserId
    from user_name import UserName
    from user import User

    now = datetime.now()
    circle_recommend_specification = CircleRecommendSpecification(now)

    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_1 = User(UserId('userid1'), UserName('username1'))
    member_2 = User(UserId('userid2'), UserName('username2'))
    member_3 = User(UserId('userid3'), UserName('username3'))
    member_4 = User(UserId('userid4'), UserName('username4'))
    member_5 = User(UserId('userid5'), UserName('username5'))
    member_6 = User(UserId('userid6'), UserName('username6'))
    member_7 = User(UserId('userid7'), UserName('username7'))
    member_8 = User(UserId('userid8'), UserName('username8'))
    member_9 = User(UserId('userid9'), UserName('username9'))
    member_10 = User(UserId('userid10'), UserName('username10'))
    member_11 = User(UserId('userid11'), UserName('username11'))
    members =[member_1.id,member_2.id,member_3.id,member_4.id,member_5.id,
              member_6.id,member_7.id,member_8.id,member_9.id,member_10.id]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')

    satisfied_circle = Circle(circle_id, circle_name, owner, members, now)

    print(circle_recommend_specification.is_satisfied_by(satisfied_circle))

    print('*'*100)

    before_one_month = now - timedelta(days= 40)
    not_satisfied_circle = Circle(circle_id, circle_name, owner, members, before_one_month)
    print(circle_recommend_specification.is_satisfied_by(not_satisfied_circle))