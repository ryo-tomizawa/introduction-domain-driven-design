import injector

from Application.Users.user_application_service import UserApplicationService
from Application.Users.Register.user_register_command import UserRegisterCommand

class Program:
    @injector.inject
    def main(self, user_application_service: UserApplicationService):
        while True:
            print('Input user name')
            print('>', end='')

            input_value = input()
            command = UserRegisterCommand(input_value)
            user_application_service.register(command)

            print('-------------------------')
            print('user created:')
            print('-------------------------')
            print('user name:')
            print(f'- {input_value}')
            print('-------------------------')
            print('continue? (y/n)')
            print('>', end='')
            yes_or_no = input()
            if yes_or_no == 'n':
                break

if __name__ == '__main__':
    from InMemoryInfrastructure.Users.inmemory_user_repository import InMemoryUserRepository
    from Models.Users.user_service import UserService

    user_repository = InMemoryUserRepository()
    user_service = UserService(user_repository)
    user_application_service = UserApplicationService(user_repository, user_service)

    program = Program()
    program.main(user_application_service)