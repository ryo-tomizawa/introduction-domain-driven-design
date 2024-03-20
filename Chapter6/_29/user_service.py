from iuser_repository import IUserRepository
from user import User

class UserService:
    def __init__(self, iuser_repository: IUserRepository) -> None:
        self.user_repository = iuser_repository

    def exists(self, user: User) -> bool:
        # 重複のルールをユーザ名からメールアドレスに変更
        # found = self.user_repository.find_by_user_name(user.name)
        duplicated_user = self.user_repository.find_by_mail_address(user.mail_address)
        return duplicated_user is not None


if __name__ == '__main__':
    from mail_address import MailAddress
    from user_name import UserName

    user_name = UserName('Tanaka')
    mail_address = MailAddress('test@example.com')
    user = User(None, user_name, mail_address)

    user_repository =  IUserRepository()

    user_service = UserService(user_repository)

    print(user_service.exists(user))
