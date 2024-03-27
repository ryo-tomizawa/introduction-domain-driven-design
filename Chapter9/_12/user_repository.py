import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from numbering_api import NumberingApi
from user_id import UserId
from user import User

class UserRepository(IUserRepository):
    def __init__(self, numbering_api: NumberingApi) -> None:
        self.numbering_api = numbering_api

        connection = sqlite3.connect(':memory:')
        self.cursor = connection.cursor()
        # for test

        create_query = "create table users(id text primary key, name text);"
        self.cursor.execute(create_query)
        insert_query = "insert into users values('1111', 'Kato');"
        self.cursor.execute(insert_query)
        # テスト用コード終了

    def save(self, user: User) -> None:
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
        self.cursor.execute(query)

    # リレーショナルデータベースを利用しているが
    def find(self, id: UserId) -> Optional[User]:
        query = f"SELECT * FROM users"
        
        self.cursor.execute(query)
        exist = self.cursor.fetchall()

        if len(exist) > 0:
            fecht_id = exist[0][0]
            fecth_name = exist[0][1]
            return User(UserId(fecht_id), UserId(fecth_name))
        else:
            return None

    # 採番処理はリレーショナルデータベースを利用していない
    def next_identity(self) -> UserId:
        response = self.numbering_api.request()
        return UserId(response.next_id())


if __name__ == '__main__':
    from user_name import UserName

    numbering_api = NumberingApi()
    user_repository = UserRepository(numbering_api)
    
    user = User(UserId('111-222-333'), UserName('tanaka taro'))
    user_repository.save(user)
    print(f'id:{user.id.value}, name:{user.name.value} regist complete')

    print('*'*100)

    get_user = user_repository.find(UserId('111-222-333'))
    print(f'id:{get_user.id.value}, name:{get_user.name.value}')

    print('*'*100)
    first_identify_id = user_repository.next_identity()
    print(f'next_identify method`s first return value: {first_identify_id.value}')