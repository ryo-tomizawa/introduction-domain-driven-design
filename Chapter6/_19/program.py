from inmemory_user_repository import InMemoryUserRepository
from user_application_service import UserApplicationService
from user_id import UserId
from user_name import UserName
from user_service import UserService
from user_update_command import UserUpdateCommand
from user import User

class Program:
    def main(self):
        repository = InMemoryUserRepository()
        user_service = UserService(repository)
        user_application_service = UserApplicationService(repository, user_service)

        id = '111-222-333'
        user = User(UserId(id), UserName('tanaka taro'))
        repository.save(user)


        # ユーザ名変更だけを行うように
        update__name_command = UserUpdateCommand(id)
        update__name_command.name = 'john smith'
        user_application_service.update(update__name_command)

        # メールアドレス変更だけを行うように
        update_mail_address_command = UserUpdateCommand(id)
        update_mail_address_command.mail_address = "xxxx@example.com"
        user_application_service.update(update_mail_address_command)


if __name__ == '__main__':
    program = Program()
    program.main()