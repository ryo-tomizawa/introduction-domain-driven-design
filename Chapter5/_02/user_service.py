from user import User
import sqlite3

class UserService:
    def exists(self, user: User)-> bool:

        # sql処理が実行できるための下準備(usersテーブルの作成)
        # DBコネクション作成
        connection = sqlite3.connect(':memory:')
        # カーソル取得
        cursor = connection.cursor()

        # 後続処理を動かすために、usersテーブルを作成・レコード追加
        create_query = "create table users(id integer, name text);"
        cursor.execute(create_query)
        insert_query = "insert into users values('1111', 'Kato');"
        cursor.execute(insert_query)
        

        # select実行
        query = f"select * from users where name = '{user.name.value}';"
        cursor.execute(query)

        exist = cursor.fetchall()
        return exist


if __name__ == '__main__':
    from user_name import UserName

    user = User(UserName('Kato'))
    user_service = UserService()
    
    print(user_service.exists(user))