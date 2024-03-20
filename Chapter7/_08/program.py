from inmemory_user_repository import InMemoryUserRepository
from service_locator import ServiceLocator
from user_application_service import UserApplicationService

class Program:
    def main(self):
        service_locator = ServiceLocator()
        service_locator.register('IUserRepository', InMemoryUserRepository())

        user_application_service = UserApplicationService(service_locator)
        retult = user_application_service.get('111-222-333')


if __name__ == '__main__':
    program = Program()
    #処理結果None
    program.main()