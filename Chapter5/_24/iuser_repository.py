from abc import ABC
from typing import Optional

from address import Address
from email import Email
from user import User
from user_id import UserId
from user_name import UserName

class IUserRepository(ABC):
    def save(self, user: User):
        pass

    def update_name(self, id: UserId, name: UserName):
        pass

    def update_email(self, id: UserId, mail: Email):
        pass

    def update_address(self, id: UserId, address: Address):
        pass

    def delete(self, user: User):
        pass

    def find(self, id=None, user_name=None) -> Optional[User]:
        pass


if __name__ == '__main__':
    from user_id import UserId

    user_repository=IUserRepository()
    
    user_id = UserId('11-22-33')
    user_name = UserName('Tanaka')
    address = Address('東京都港区1-1-1')
    email = Email('abc@gmail.com')
    user = User(user_id, user_name)

    # 具体的な処理が何も書かれていないため、全てNoneが返される
    print(user_repository.save(user))
    print(user_repository.update_name(UserId('22-33'), UserName('Kato')))
    print(user_repository.update_email(user_id, Email('abcdef@gmail.com')))
    print(user_repository.update_address(user_id, Address('東京都港区2-2-2')))
    print(user_repository.delete(user))
    print(user_repository.find(user_id))
    print(user_repository.find(user_name))