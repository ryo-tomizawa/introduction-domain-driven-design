import uuid
# C言語のGuidに対応するモジュールのimport
# Guidの具体的な説明は↓
# https://webbibouroku.com/Blog/Article/cs-guid

from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, name: UserName, id=None) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')
        
        if id is None:
            self.id = UserId(str(uuid.uuid4()))
        else:
            self.id = id
        self.name = name

    def change_name(self, name: UserName):
        if name is None: raise ValueError(f'incorrect value: {name}')

        self.name = name
    

if __name__ == '__main__':
    user_name = UserName('Tanaka')
    user = User(user_name)

    print(user.id.value, user.name.value)

    print('*'*100)

    user_id = UserId('11111-000')
    user_name = UserName('Watanabe')
    user = User(user_name, user_id)
    print(user.id.value, user.name.value)