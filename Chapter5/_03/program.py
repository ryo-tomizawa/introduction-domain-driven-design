from iuser_repository import IUserRepository
from user import User
from user_name import UserName
from user_service import UserService

class Program:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, user_name: str):
        user = User(UserName(user_name))
        user_service = UserService(self.user_repository)

        if user_service.exists(user):
            raise ValueError(f'{user_name}は既に存在しています')
        
        self.user_repository.save(user)
        print(f'{user_name}の登録が完了しました')


if __name__ == '__main__':
    user_repository = IUserRepository()
    program = Program(user_repository)

    program.create_user('Tanaka')