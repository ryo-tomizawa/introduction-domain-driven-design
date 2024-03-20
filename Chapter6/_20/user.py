﻿import uuid
# C言語のGuidに対応するモジュールのimport
# Guidの具体的な説明は↓
# https://webbibouroku.com/Blog/Article/cs-guid

from mail_address import MailAddress
from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')
        
        if id is None:
            self._id = UserId(str(uuid.uuid4()))
        else:
            self._id = id
        self._name = name
        self._mail_address = None

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def mail_address(self):
        return self._mail_address

    def change_name(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._name = name

if __name__ == '__main__':
    user_name = UserName('Tanaka')
    user = User(None, user_name)

    print(user.id.value, user.name.value)

    print('*'*100)

    new_name = UserName('john smith')

    user.change_name(new_name)

    print(user.id.value, user.name.value)