import sqlite3

from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')
        
        if id is None:
            connection = sqlite3.connect(':memory:')
            cursor = connection.cursor()

            # 後続処理を動かすために、usersテーブルを作成・レコード追加
            create_query = "create table users(id integer, name text);"
            cursor.execute(create_query)
            insert_query = "insert into users values('1111', 'Kato');"
            cursor.execute(insert_query)

            # 現在のidで最大の値を取得
            select_query = "select max(id) from users;"
            cursor.execute(select_query)

            select_list = cursor.fetchone()
            if select_list[0] is None: raise Exception

            max_id = select_list[0] + 1
            self._id = UserId(str(max_id))
        else:
            self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def change_name(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._name = name


if __name__ == '__main__':
    user_name = UserName('tanaka taro')
    user = User(None, user_name)

    print(user.id.value, user.name.value)

    print('*'*100)

    new_name = UserName('john smith')

    user.change_name(new_name)

    print(user.id.value, user.name.value)