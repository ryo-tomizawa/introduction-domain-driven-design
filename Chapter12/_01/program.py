from user_id import UserId
from user_name import UserName
from user import User

class Program:
    def main(self):
        id = UserId('test-id')
        name = UserName('CurrentName')
        user = User(id, name)

        user_name = UserName('NewName')

        # NG
        # user.name = UserName

        # OK
        user.change_name(user_name)

        # for test
        print(user.id.value, user.name.value)


if __name__ == '__main__':
    program = Program()
    program.main()