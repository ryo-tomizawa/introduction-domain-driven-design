from user_data import UserData
from user_name import UserName
from user import User


class Program:
    def main(self):
        user = User(None, UserName('tanaka taro'))
        user_data = UserData(user)

        # for test
        print(user_data.id, user_data.name)


if __name__ == '__main__':
    program = Program()
    program.main()