import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Circles'))
sys.path.append(circle_model_dir)

from circle import Circle

class CircleSummaryData:
    def __init__(self, circle: Circle) -> None:
        self._id = str(circle.id.value)
        self._name = str(circle.name.value)

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    

if __name__ == '__main__':
    user_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Users'))
    sys.path.append(user_model_dir)

    from circle_id import CircleId
    from circle_name import CircleName
    from user_id import UserId
    from user_name import UserName
    from user import User

    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member = User(UserId('userid1'), UserName('username1'))
    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    circle = Circle(circle_id, circle_name, owner, [member])

    circle_summary_data = CircleSummaryData(circle)

    print(circle_summary_data.id,
          circle_summary_data.name)
    