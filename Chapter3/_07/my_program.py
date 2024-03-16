from user import User
from user_id import UserId

class MyProgram:
    def main(self):
        left = User(UserId('a'), 'left')
        right = User(UserId('b'), 'right')
        self.check(left, right)

    def check(self, left_user: User, right_user: User):
        if left_user == right_user:
            print(f'同一のユーザです')
        else:
            print(f'別のユーザです')


if __name__ == '__main__':
    my_program = MyProgram()
    my_program.main()