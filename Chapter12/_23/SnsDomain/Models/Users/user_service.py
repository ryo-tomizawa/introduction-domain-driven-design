﻿from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, iuser_repository: IUserRepository) -> None:
        self.user_repository = iuser_repository

    def exists(self, user: User) -> bool:
        duplicated_user = self.user_repository.find_by_user_name(user.name)
        return duplicated_user is not None


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName
    
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    user = User(user_id, user_name)

    user_repository =  IUserRepository()

    user_service = UserService(user_repository)

    print(user_service.exists(user))
