import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from user import User
from user_id import UserId
from user_name import UserName

class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.connection = sqlite3.connect(':memory:')

    def save(self, user: User):
        cursor = self.connection.cursor()

        query = f"""
                INSERT INTO users(
                    id,
                    name
                )
                values(
                    '{user.id.value}',
                    '{user.name.value}'
                )
                on conflict(id)
                do update
                    set
                    name = '{user.name.value}'
                """
        cursor.execute(query)

    # 静的型付けを用いて返り値をOptional型で定義
    def find(self, user_name: UserName) -> Optional[User]:
        cursor = self.connection.cursor()
        query = f"SELECT * FROM users WHERE name = '{user_name.value}'"
        
        cursor.execute(query)
        exist = cursor.fetchall()
        # existに値が存在する場合は以下のように値を受け取る
        # [(1111, 'Kato')]

        if len(exist) > 0:
            id = exist[0][0]
            name = exist[0][1]
            return User(UserName(name), UserId(id))
        else:
            return None


if __name__ == '__main__':
    user_repository=IUserRepository()

    user_name = UserName('Tanaka')
    user = User(user_name)

    print(user_repository.save(user))
    print(user_repository.find(user_name))