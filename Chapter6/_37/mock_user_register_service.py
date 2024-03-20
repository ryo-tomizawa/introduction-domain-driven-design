from iuser_register_service import IUserRegisterService
from user_register_command import UserRegisterCommand

class MockUserResiterService(IUserRegisterService):
    def handle(self, command: UserRegisterCommand):
        pass
        # 以下にモックで実行したい内容を記載



if __name__ == '__main__':
    user_register_command = UserRegisterCommand('tanaka taro')
    user_register_service = MockUserResiterService()
    
    user_register_service.handle(user_register_command)