from typing import List
import os
import sys

current_dir = os.path.dirname(__file__)
user_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Users'))
db_context_dir = os.path.abspath(os.path.join(current_dir, '../../Contexts'))
data_model_dir = os.path.abspath(os.path.join(current_dir, '../DataModels'))
sys.path.append(user_model_dir)
sys.path.append(db_context_dir)
sys.path.append(data_model_dir)

from my_db_context import MyDbContext
from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User
from user_data_model import UserDataModel

class EFUserRepository(IUserRepository):
    def __init__(self, context: MyDbContext) -> None:
        self.context = context

    def find(self, id: UserId) -> User:
        raise NotImplementedError()
    
    def find_by_user_name(self, name: UserName) -> User:
        raise NotImplementedError()

    def find_all(self) -> List[User]:
        raise NotImplementedError()
    
    def save(self, user: User) -> None:
        user_data_model = UserDataModel(id=user.id.value, name=user.name.value)
        self.context.add_user(user_data_model)

    def delete(self, user: User) -> None:
        raise NotImplementedError()


if __name__ == '__main__':
    context = MyDbContext()
    user_repository = EFUserRepository(context)
    
    user = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_repository.save(user)

    users = context.get_users()
    for user in users:
        print(user.id, user.name)