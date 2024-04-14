import os
import sys

current_dir = os.path.dirname(__file__)
user_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Users'))
user_data_model_dir = os.path.abspath(os.path.join(current_dir, '../DataModels'))
sys.path.append(user_model_dir)
sys.path.append(user_data_model_dir)

from iuser_notification import IUserNotification
from user_data_model import UserDataModel
from user_id import UserId
from user_name import UserName

class UserDataModelBuilder(IUserNotification):
    def build(self) -> UserDataModel:
        return UserDataModel(id=self._id.value, name=self._name.value)


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')

    user_data_model_builder = UserDataModelBuilder()
    user_data_model_builder.id = user_id
    user_data_model_builder.name = user_name

    user_data_model = user_data_model_builder.build()
    print(user_data_model.id, user_data_model.name)