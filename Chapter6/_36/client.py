from iuser_register_service import IUserRegisterService
from user_register_command import UserRegisterCommand

class Client:
    def __init__(self, user_register_service: IUserRegisterService) -> None:
        self. user_register_serivice = user_register_service

    def register(self, name: str):
        command = UserRegisterCommand(name)
        self.user_register_serivice.handle(command)


if __name__ == '__main__':
    user_register_service = IUserRegisterService()
    client = Client(user_register_service)

    client.register('tanaka taro')