from user_name import UserName
from user_id import UserId
from user import User

class Program:
    def create_user(self, name: UserName):
        user = User(UserId('1-2-3'), UserName('tanaka taro')) 
        # user.id = name # C言語だとコンパイルエラーになるがpythonだとならない
        return user


if __name__ == '__main__':
    user_name = UserName('kato taro')

    program = Program()
    user = program.create_user(user_name)
    print(user.id.value, user.name.value)