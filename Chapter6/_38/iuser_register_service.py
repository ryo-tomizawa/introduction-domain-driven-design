from user_register_command import UserRegisterCommand

class IUserRegisterService:
    def handle(self, command: UserRegisterCommand):
        pass



if __name__ == '__main__':
    user_register_command = UserRegisterCommand('tanaka taro')
    user_register_service = IUserRegisterService()
    
    user_register_service.handle(user_register_command)