from typing import Optional, List
import os
import sys

current_dir = os.path.dirname(__file__)
domain_dir = os.path.abspath(os.path.join(current_dir, './Domain/Models/Users'))
sys.path.append(domain_dir)

from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.creates = {}
        self.updates = {}
        self.deletes = {}
        self.db = {}

    @property
    def data(self):
        data_dict = {**self.db, **self.creates, **self.updates}
        
        if self.deletes:
            for k in self.deletes.keys():
                del data_dict[k]
        return data_dict

    def find_all(self) -> Optional[User]:
        return [self._clone(user) for user in self.data.values()]

    def save(self, user) -> None:
        raw_user_id = user.id.value
        target_map = self.updates if raw_user_id in self.data else self.creates
        target_map[raw_user_id] = self._clone(user)

    def remove(self, user) -> None:
        self.deletes[user.id.value] = self._clone(user)

    def commit(self) -> None:
        self.db = self.data
        self.creates.clear()
        self.updates.clear()
        self.deletes.clear()

    def find(self, id: UserId) -> Optional[User]:
        target = self.data.get(id)
        return self._clone(target) if target else None

    def find_by_name(self, name: UserName) -> Optional[User]:
        target = next((user for user in self.data.values() if user.name == name), None)
        return self._clone(target) if target else None

    def delete(self, user: User) -> None:
        self.remove(user)

    def _clone(self, user: User) -> User:
        return User(user.id, user.name)
    

if __name__ == '__main__':
    from inmemory_unit_of_work import InMemoryUnitOfWork

    unit_of_work = InMemoryUnitOfWork()

    user1 = User(UserId('111-222-333'), UserName("tanaka taro"))
    user2 = User(UserId('222-333-444'), UserName("john smith"))
    unit_of_work.user_repository.save(user1)
    unit_of_work.user_repository.save(user2)

    get_user = unit_of_work.user_repository.find('111-222-333')
    if get_user:
        print("Found user by ID:", get_user.id.value, get_user.name.value)

    print('*'*100)

    get_user = unit_of_work.user_repository.find_by_name(UserName("john smith"))
    if get_user:
        print("Found user by name:", get_user.id.value, get_user.name.value)

    print('*'*100)

    unit_of_work.user_repository.delete(user1)

    unit_of_work.commit()

    # Display all users
    all_users = unit_of_work.user_repository.find_all()
    print("All users after of delete action:")
    for user in all_users:
        print(user.id.value, user.name.value)