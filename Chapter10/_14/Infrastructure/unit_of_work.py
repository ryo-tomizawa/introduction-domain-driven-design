import os
import sqlite3
import sys

current_dir = os.path.dirname(__file__)
user_dir =os.path.abspath(os.path.join(current_dir, '../Domain/Models/Users'))
shared_dir = os.path.abspath(os.path.join(current_dir, '../Domain/Shared'))
sys.path.append(user_dir)
sys.path.append(shared_dir)

from user_repository import UserRepository
from iunit_of_work import IUnitOfWork

class UnitOfWork(IUnitOfWork):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self._user_repository = None

    @property
    def user_repository(self):
        if not self._user_repository:
            self._user_repository = UserRepository(self.connection)
        return self._user_repository


if __name__ == '__main__':
    connection = sqlite3.Connection('example.db')
    unit_of_work = UnitOfWork(connection)
    print(unit_of_work.user_repository)