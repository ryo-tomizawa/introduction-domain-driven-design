import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User

class UserRepository(IUserRepository):
    def __init__(self, connection: object) -> None:
        self.connection = connection
        # for test
        cursor = self.connection.cursor()
        create_query = "create table users(id text primary key, name text);"
        cursor.execute(create_query)
        # テスト用コード終了

    def find(self, id: UserId) -> Optional[User]:
        cursor = self.connection.cursor()

        query = f"SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (id.value,))
        row = cursor.fetchone()

        if row:
            return self._read_user(row)
        else:
            return None

    def find_by_name(self, name: UserName) -> Optional[User]:
        cursor = self.connection.cursor()

        query = f"SELECT * FROM users WHERE name = ?"
        cursor.execute(query, (name.value,))
        row = cursor.fetchone()

        if row:
            return self._read_user(row)
        else:
            return None

    def find_all(self) -> Optional[User]:
        cursor = self.connection.cursor()

        query = f"SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()

        return [self._read_user(row) for row in rows]

    def save(self, user: User) -> None:
        cursor = self.connection.cursor()

        query = "INSERT OR REPLACE INTO users (id, name) VALUES (?, ?)"
        cursor.execute(query, (user.id.value, user.name.value))
        self.connection.commit()

    def delete(self, id: UserId) -> None:
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE id = ?"
        cursor.execute(query, (id.value,))


    def _read_user(self, row) -> User:
        return User(UserId(row[0]), UserName(row[1]))


if __name__ == '__main__':
    connection = sqlite3.connect(':memory:')
    user_repository = UserRepository(connection)
    
    user_a = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_b = User(UserId('222-333-444'), UserName('john smith'))
    user_repository.save(user_a)
    print(f'id:{user_a.id.value}, name:{user_a.name.value} regist complete')
    user_repository.save(user_b)
    print(f'id:{user_b.id.value}, name:{user_b.name.value} regist complete')

    print('*'*100)

    get_user = user_repository.find(UserId('111-222-333'))
    print(f'id:{get_user.id.value}, name:{get_user.name.value}')

    print('*'*100)

    get_user = user_repository.find_by_name(UserName('john smith'))
    print(f'id:{get_user.id.value}, name:{get_user.name.value}')

    print('*'*100)

    get_users = user_repository.find_all()
    for user in get_users:
        print(f'id:{user.id.value}, name:{user.name.value}')

    print('*'*100)

    user_repository.delete(UserId('222-333-444'))
    get_users = user_repository.find_all()
    for user in get_users:
        print(f'id:{user.id.value}, name:{user.name.value}')