from user_repository import UserRepository
from program import Program

class EntryPoint:
    def main(self):
        user_repository = UserRepository()
        program = Program(user_repository)
        program.create_user('Tanaka')


if __name__ == '__main__':
    from user_name import UserName

    entry_point = EntryPoint()
    entry_point.main()