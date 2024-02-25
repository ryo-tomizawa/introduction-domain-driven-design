from user_id import UserId
from user_name import UserName
from user_service import UserService
from user import User

class Program:
    def main(self):
        user_service = UserService()

        user_id = UserId('id')
        user_name = UserName('naruse')
        user = User(user_id, user_name)

        # ドメインサービスに問い合わせ
        duplicate_check_result = user_service.exist(user)
        print(duplicate_check_result)

if __name__ == '__main__':
    program = Program()
    program.main()