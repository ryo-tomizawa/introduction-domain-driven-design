import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from user_id import UserId
from user_name import UserName
from user import User

class UserRepository(IUserRepository):
    def __init__(self) -> None:
        connection = sqlite3.connect(':memory:')
        self.cursor = connection.cursor()

    def find(self, id: UserId) -> Optional[User]:
        sql = 'SELECT * FROM users WHERE id = ?'
        self.cursor.execute(sql, (id.value,))

        row = self.cursor.fetchone()

        if row is None: return None

        user_id, user_name = row
        return User(UserId(user_id), UserName(user_name))
    

if __name__ == '__main__':
    user_repository = UserRepository()
    
    create_query = "create table users(id integer, name text);"
    user_repository.cursor.execute(create_query)
    insert_query = "insert into users values('111-222-333', 'tanaka taro');"
    user_repository.cursor.execute(insert_query)

    get_user = user_repository.find(UserId('111-222-333'))
    print(get_user.id.value, get_user.name.value)