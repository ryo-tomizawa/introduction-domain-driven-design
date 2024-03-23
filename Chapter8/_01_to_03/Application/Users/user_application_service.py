from injector import Inject
import os
import sys

current_dir = os.path.dirname(__file__)
models_users_dir = os.path.abspath(os.path.join(current_dir, '../../Models/Users'))
user_data_dir = os.path.abspath(os.path.join(current_dir, './Commons'))
delete_dir = os.path.abspath(os.path.join(current_dir, './Delete'))
get_all_dir = os.path.abspath(os.path.join(current_dir, './GetAll'))
register_dir = os.path.abspath(os.path.join(current_dir, './Register'))
update_dir = os.path.abspath(os.path.join(current_dir, './Update'))
inmemory_repository_dir = os.path.abspath(os.path.join(current_dir, '../../InMemoryInfrastructure/Users'))
sys.path.append(current_dir)
sys.path.append(models_users_dir)
sys.path.append(user_data_dir)
sys.path.append(delete_dir)
sys.path.append(get_all_dir)
sys.path.append(register_dir)
sys.path.append(update_dir)
sys.path.append(inmemory_repository_dir)

from can_not_register_user_exception import CanNotRegisterUserException
from user_delete_command import UserDeleteCommand
from user_get_all_result import UserGetAllResult
from user_register_command import UserRegisterCommand
from iuser_repository import IUserRepository
from user_data import UserData
from user_id import UserId
from user_name import UserName
from user_not_found_exception import UserNotFoundException
from user_service import UserService
from user_update_command import UserUpdateCommand
from user import User

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository, user_service: UserService) -> None:
        self.user_repository = user_repository
        self.user_service = user_service

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data
    
    def get_all(self):
        users = self.user_repository.find_all()
        user_model = [UserData(x) for x in users]
        return UserGetAllResult(user_model)

    def register(self, command: UserRegisterCommand):
        name = UserName(command.name)
        user = User(None, name)

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
        
        self.user_repository.save(user)

    def update(self, command:UserUpdateCommand):
        id = UserId(command.id)
        user = self.user_repository.find(id)

        if user is None: raise UserNotFoundException(id, None)

        if command.name is not None:
            name = UserName(command.name)
            user.change_name(name)

            if self.user_service.exists(user):
                raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
        
        self.user_repository.save(user)

    def delete(self, command: UserDeleteCommand):
        id = UserId(command.id)
        user = self.user_repository.find(id)
        if user is None: return

        self.user_repository.delete(user)
    

if __name__ == '__main__':
    from inmemory_user_repository import InMemoryUserRepository

    user_repository = InMemoryUserRepository()
    user_service = UserService(user_repository)
    user_application_service = UserApplicationService(user_repository, user_service)

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_b = User(UserId('222-333-444'), UserName('john smith'))

    user_repository.save(user_a)
    user_repository.save(user_b)

    get_user = user_application_service.get('111-222-333')
    print(get_user.id, get_user.name)

    print('*'*100)

    get_users = user_application_service.get_all()
    for user in get_users.users:
        print(user.id, user.name)

    print('*'*100)

    register_command = UserRegisterCommand('kato taro')
    user_application_service.register(register_command)
    get_users = user_application_service.get_all()
    for user in get_users.users:
        print(user.id, user.name)

    print('*'*100)

    update_command = UserUpdateCommand('222-333-444', 'james bond')
    user_application_service.update(update_command)
    get_users = user_application_service.get_all()
    for user in get_users.users:
        print(user.id, user.name)

    print('*'*100)

    delete_command = UserDeleteCommand('222-333-444')
    user_application_service.delete(delete_command)
    get_users = user_application_service.get_all()
    for user in get_users.users:
        print(user.id, user.name)