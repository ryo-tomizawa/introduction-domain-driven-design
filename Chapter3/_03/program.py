from my_program import MyProgram
from user import User
from user_change_name_request import UserChangeNameRequest

class Program:
    def main(self):
        program = MyProgram()
        user = User('test-user')
        request = UserChangeNameRequest('')
        program.main(user, request)


if __name__ == '__main__':
    program = Program()
    program.main()