from iuser_repository import IUserRepository
from user import User
from user_name import UserName
from user_service import UserService

class Program:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, user_name: str) -> None:
        user = User(None, UserName(user_name))

        user_service = UserService(self.user_repository)
        if user_service.exists(user):
            raise ValueError(f'{user_name}は既に存在しています')

        self.user_repository.save(user)
        print('登録に成功しました')


if __name__ == '__main__':
    from ef_user_repository import EFUserRepository
    from mydb_context import MyDbContext
    
    mydb_context = MyDbContext()
    user_repository = EFUserRepository(mydb_context)

    program = Program(user_repository)

    try:
        # 1回目は正常に登録できることを期待
        program.create_user('Tanaka')

        # 同じ名前を登録してエラーが発生することを期待
        program.create_user('Tanaka')
    except ValueError as e:
        print('登録時にエラーが発生しました')
        print(e)