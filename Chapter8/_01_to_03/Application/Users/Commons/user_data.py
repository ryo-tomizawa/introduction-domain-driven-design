from injector import Inject
import os
import sys

current_dir = os.path.dirname(__file__)
user_dir =os.path.abspath(os.path.join(current_dir, '../../../Models/Users'))
sys.path.append(user_dir)

from user import User

class UserData:
    def __init__(self, user: User) -> None:
        self._id = user.id.value
        self._name = user.name.value

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

    user = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_data = UserData(user)

    print(user_data.id, user_data.name)