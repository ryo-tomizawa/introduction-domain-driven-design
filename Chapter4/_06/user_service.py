from user_name import UserName
from user import User

class UserService:
    def change_name(self, user: User, name: UserName):
        if user is None: raise ValueError(f'{user}')
        if name is None: raise ValueError(f'{name}')
        
        user.name = name


