from user import User
from user_name import UserName
from user_service import UserService

class Program:
    def create_user(user_name: str):
        user = User(UserName(user_name))

        user_service = UserService()
        if user_service.exists(user):
            raise ValueError(f'{user_name}はすでに存在しています')
        
        # 存在しないユーザ名だった場合、DBにレコードを登録する
        # con.execute_query(sql)