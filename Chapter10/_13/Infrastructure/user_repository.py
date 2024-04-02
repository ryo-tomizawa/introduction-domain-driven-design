import os
import sqlite3
import sys
from typing import Optional, List

current_dir = os.path.dirname(__file__)
user_dir =os.path.abspath(os.path.join(current_dir, '../Domain/Models/Users'))
sys.path.append(user_dir)

from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User

class UserRepository(IUserRepository):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def find(self, id: UserId) -> Optional[User]:
        with self.connection:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM users WHERE id = ?"
            cursor.execute(query, (id.value,))
            row = cursor.fetchone()

            if row:
                return self._read_user(row)
            else:
                return None
    
    def find_by_name(self, name: UserName) -> Optional[User]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name = ?", (name.value,))
            row = cursor.fetchone()
            if row:
                return self._read_user(row)
            else:
                return None

    def find_all(self) -> Optional[List[User]]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return [self._read_user(row) for row in rows]

    def save(self, user: User) -> None:
        with self.connection:
            self.connection.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user.id.value, user.name.value))

    def delete(self, id: UserId) -> None:
        with self.connection:
            self.connection.execute("DELETE FROM users WHERE id = ?", (id.value,))

    def _read_user(self, row):
        return User(UserId(row[0]), UserName(row[1]))

if __name__ == '__main__':
    from unit_of_work import UnitOfWork

    connection = sqlite3.connect('example.db')
    unit_of_work = UnitOfWork(connection)
    user_repository = unit_of_work.user_repository

    delete_query = 'DELETE FROM users'
    connection.execute(delete_query)

    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_b = User(UserId('222-333-444'), UserName('john smith'))
    user_repository.save(user_a)
    user_repository.save(user_b)

    get_user = user_repository.find(UserId('111-222-333'))
    print(get_user.id.value, get_user.name.value)

    print('*'*100)

    get_user = user_repository.find_by_name(UserName('john smith'))
    print(get_user.id.value, get_user.name.value)

    print('*'*100)

    users = user_repository.find_all()
    for user in users:
        print(user.id.value, user.name.value)

    print('*'*100)

    user_repository.delete(UserId('111-222-333'))
    users = user_repository.find_all()
    for user in users:
        print(user.id.value, user.name.value)

