from complex_exception import ComplexException
from iuser_register_service import IUserRegisterService
from user_register_command import UserRegisterCommand

class EcxeptionkUserResiterService(IUserRegisterService):
    def handle(self, command: UserRegisterCommand):
        raise ComplexException()


if __name__ == '__main__':
    user_register_command = UserRegisterCommand('tanaka taro')
    user_register_service = EcxeptionkUserResiterService()
    
    user_register_service.handle(user_register_command)