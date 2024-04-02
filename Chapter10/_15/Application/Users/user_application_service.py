import os
import sys
from typing import Optional

current_dir = os.path.dirname(__file__)
models_users_dir = os.path.abspath(os.path.join(current_dir, '../../Models/Users'))
user_data_dir = os.path.abspath(os.path.join(current_dir, './Commons'))
delete_dir = os.path.abspath(os.path.join(current_dir, './Delete'))
get_dir = os.path.abspath(os.path.join(current_dir, './Get'))
get_all_dir = os.path.abspath(os.path.join(current_dir, './GetAll'))
register_dir = os.path.abspath(os.path.join(current_dir, './Register'))
update_dir = os.path.abspath(os.path.join(current_dir, './Update'))
shared_dir = os.path.abspath(os.path.join(current_dir, '../../Domain/Shared'))
sys.path.append(current_dir)
sys.path.append(models_users_dir)
sys.path.append(user_data_dir)
sys.path.append(delete_dir)
sys.path.append(get_dir)
sys.path.append(get_all_dir)
sys.path.append(register_dir)
sys.path.append(update_dir)
sys.path.append(shared_dir)

from can_not_register_user_exception import CanNotRegisterUserException
from user_delete_command import UserDeleteCommand
from user_get_command import UserGetCommand
from user_get_result import UserGetResult
from user_get_all_result import UserGetAllResult
from user_register_command import UserRegisterCommand
from iuser_repository import IUserRepository
from iuser_factory import IUserFactory
from user_data import UserData
from user_id import UserId
from user_name import UserName
from user_not_found_exception import UserNotFoundException
from user_service import UserService
from user_update_command import UserUpdateCommand
from user import User
from iunit_of_work import IUnitOfWork

class UserApplicationService:
    def __init__(self, 
                 unit_of_work: IUnitOfWork,
                 user_factory: IUserFactory,
                 user_repository: IUserRepository, 
                 user_service: UserService) -> None:
        self.unit_of_work = unit_of_work
        self.user_factory = user_factory
        self.user_repository = user_repository
        self.user_service = user_service

    def get(self, command: UserGetCommand) -> Optional[UserGetResult]:
        target_id = UserId(command.id)
        user = self.unit_of_work.user_repository.find(target_id)
        if user is None: UserNotFoundException(id, 'ユーザが見つかりませんでした。')

        user_data = UserData(user)
        return UserGetResult(user_data)
    
    def get_all(self) -> Optional[UserGetAllResult]:
        users = self.unit_of_work.user_repository.find_all()
        user_model = [UserData(x) for x in users]
        return UserGetAllResult(user_model)

    def register(self, command: UserRegisterCommand) -> None:
        name = UserName(command.name)
        user = self.user_factory.create(name)

        if self.user_service.exists(user):
            raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
    
        self.unit_of_work.user_repository.save(user)
        self.unit_of_work.commit()


    def update(self, command:UserUpdateCommand) -> None:
        id = UserId(command.id)
        user = self.user_repository.find(id)

        if user is None: raise UserNotFoundException(id, None)

        if command.name is not None:
            name = UserName(command.name)
            user.change_name(name)

            if self.user_service.exists(user):
                raise CanNotRegisterUserException(user, 'ユーザは既に存在しています。')
        
        self.unit_of_work.user_repository.save(user)
        self.unit_of_work.commit()

    def delete(self, command: UserDeleteCommand) -> None:
        id = UserId(command.id)
        user = self.user_repository.find(id)
        if user is None: return

        self.unit_of_work.user_repository.delete(user)
        self.unit_of_work.commit()
    

if __name__ == '__main__':
    import sqlite3

    # モックオブジェクトやスタブの作成
    class MockFactory(IUserFactory):
        def __init__(self) -> None:
            self.num = 1111

        def create(self, name: UserName):
            self.num += 1
            return User(UserId(str(self.num)), name)

    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None
            
        def find_by_user_name(self, name: UserName):
            for elem in self.store.values():
                if elem.name.value == name.value:
                    return self.clone(elem)
            return None
        
        def find_all(self):
            return_list = []
            for elem in self.store.values():
                return_list.append(self.clone(elem))

            return return_list

        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def delete(self, user: User):
            if user.id.value in self.store:
                del self.store[user.id.value]

        def clone(self, user: User):
            return User(user.id, user.name)
        
    
    class MockUnitOfWork(IUnitOfWork):
        def __init__(self):
            self._user_repository = None

        @property
        def user_repository(self):
            if not self._user_repository:
                self._user_repository = MockUserRepository()
            return self._user_repository
        
        @user_repository.setter
        def user_repository(self, value):
            self._user_repository = value
        
        def commit(self):
            pass

    user_factory = MockFactory()
    user_repository = MockUserRepository()
    unit_of_work = MockUnitOfWork()
    unit_of_work.user_repository = user_repository
    user_service = UserService(user_repository)
    user_application_service = UserApplicationService(unit_of_work, user_factory, user_repository, user_service)

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_b = User(UserId('222-333-444'), UserName('john smith'))

    user_repository.save(user_a)
    user_repository.save(user_b)

    get_user = user_application_service.get(UserGetCommand('111-222-333'))
    print(get_user.user.id, get_user.user.name)

    # print('*'*100)

    # get_users = user_application_service.get_all()
    # for user in get_users.users:
    #     print(user.id, user.name)

    # print('*'*100)

    # register_command = UserRegisterCommand('kato taro')
    # user_application_service.register(register_command)
    # get_users = user_application_service.get_all()
    # for user in get_users.users:
    #     print(user.id, user.name)

    # print('*'*100)

    # update_command = UserUpdateCommand('222-333-444', 'james bond')
    # user_application_service.update(update_command)
    # get_users = user_application_service.get_all()
    # for user in get_users.users:
    #     print(user.id, user.name)

    # print('*'*100)

    # delete_command = UserDeleteCommand('222-333-444')
    # user_application_service.delete(delete_command)
    # get_users = user_application_service.get_all()
    # for user in get_users.users:
    #     print(user.id, user.name)