from user_application_service import UserApplicationService
from user_name import UserName

class Client:
    def __init__(self, user_application_service: UserApplicationService) -> None:
        self.user_application_service = user_application_service

    def change_name(self, id: str, name: str):
        target = self.user_application_service.get(id)
        new_name = UserName(name)

        target.change_name(new_name)

        #for test
        print(target.id.value, target.name.value)



if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName
    from user import User

    class MockUserApplicationService:
        def get(self, id: str):
            return User(UserId(id), UserName('tanaka taro'))
        
    application_service = MockUserApplicationService()

    client = Client(application_service)

    client.change_name('111-222-333', 'john smith')