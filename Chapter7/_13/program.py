from inmemory_user_repository import InMemoryUserRepository
from service_locator import ServiceLocator
from user_application_service import UserApplicationService

class Program:
    def main(self):
        service_locator = ServiceLocator()
        service_locator.register('IUserRepository', InMemoryUserRepository())

        user_application_service = UserApplicationService(service_locator)


if __name__ == '__main__':
    program = Program()
    # 具体的な処理は特に実装されてないため、何も帰ってこない
    program.main()