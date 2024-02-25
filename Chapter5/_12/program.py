﻿from iuser_repository import IUserRepository
from user import User
from user_name import UserName
from user_service import UserService

class Program:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, user_name: str) -> None:
        user = User(UserName(user_name))
        user_service = UserService(self.user_repository)

        if user_service.exists(user):
            raise ValueError(f'{user_name}は既に存在しています')
        
        self.user_repository.save(user)



if __name__ == '__main__':
    from user_repository import UserRepository

    user_repository = UserRepository()
    
    program = Program(user_repository)

    program.create_user('Tanaka')

    fetch_user = user_repository.find(UserName('Tanaka'))
    print(fetch_user.id.value, fetch_user.name.value)