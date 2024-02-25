from user import User

class UserService:
    def exist(self, user: User):
        # 重複を確認する処理
        return True