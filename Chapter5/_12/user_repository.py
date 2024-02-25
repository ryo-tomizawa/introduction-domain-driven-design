import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from user import User
from user_id import UserId
from user_name import UserName

class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.connection = sqlite3.connect(':memory:')

        cursor = self.connection.cursor()

        # 後続処理を動かすために、usersテーブルを作成・レコード追加
        create_query = "create table users(id integer, name text PRIMARY KEY);"
        cursor.execute(create_query)

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
                on conflict(name)
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