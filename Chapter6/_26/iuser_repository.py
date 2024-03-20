from abc import ABC
from typing import Optional

from mail_address import MailAddress
from user import User
from user_id import UserId
from user_name import UserName

class IUserRepository(ABC):
    def find(self, id: UserId) -> Optional[User]:
        pass

    def find_by_user_name(self, name: UserName) -> Optional[User]:
        pass

    def find_by_mail_address(self, mail_address: MailAddress) -> Optional[User]:
        pass

    def save(self, user: User):
        pass

    def delete(self, user: User):
        pass


if __name__ == '__main__':
    from user_id import UserId

    user_repository=IUserRepository()
    
    user_id = UserId('11-22-33')
    user_name = UserName('Tanaka')
    user_mail_address = MailAddress('test@example.com')
    user = User(user_id, user_name, user_mail_address)

    # 具体的な処理が何も書かれていないため、全てNoneが返される
    print(user_repository.save(user))
    print(user_repository.delete(user))
    print(user_repository.find(user_id))
    print(user_repository.find_by_user_name(user_name))
    print(user_repository.find_by_mail_address(user_mail_address))