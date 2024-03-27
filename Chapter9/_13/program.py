from circle_name import CircleName
from circle import Circle
from user_id import UserId
from user_name import UserName
from user import User

class Program:
    def main(self):
        user = User(UserId('test-id'), UserName('test-name'))
        circle = Circle(user.id, CircleName('my circle'))

        # for test
        print(circle.owner_id.value, circle.name.value)



if __name__ == '__main__':
    program = Program()
    program.main()