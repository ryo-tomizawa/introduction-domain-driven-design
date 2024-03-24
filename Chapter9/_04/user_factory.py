import sqlite3
from typing import Optional

from iuser_factory import IUserFactory
from user_id import UserId
from user_name import UserName
from user import User

class UserFactory(IUserFactory):
    def create(self, name: UserName) -> Optional[User]:
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        # 後続処理を動かすために、usersテーブルを作成・レコード追加
        create_query = "create table users(id integer, name text);"
        cursor.execute(create_query)
        insert_query = "insert into users values('1111', 'Kato');"
        cursor.execute(insert_query)
        # テスト用コード終了

        # 現在のidで最大の値を取得
        select_query = "select max(id) from users;"
        cursor.execute(select_query)

        select_list = cursor.fetchone()
        if select_list[0] is None: raise Exception

        max_id = select_list[0] + 1

        user_id = UserId(str(max_id))
        return User(user_id, name)



if __name__ == '__main__':
    user_factory = UserFactory()
    user = user_factory.create(UserName('tanaka taro'))

    print(user.id.value, user.name.value)