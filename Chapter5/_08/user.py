import uuid
# C言語のGuidに対応するモジュールのimport
# Guidの具体的な説明は↓
# https://webbibouroku.com/Blog/Article/cs-guid

from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')
        self.id = UserId(uuid.uuid4())
        self.name = name
    

if __name__ == '__main__':
    user_name = UserName('Tanaka')
    user = User(user_name)

    print(user.id.value, user.name.value)