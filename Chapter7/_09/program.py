from service_locator import ServiceLocator
from user_application_service import UserApplicationService
from user_repository import UserRepository

class Program:
    def main(self):
        service_locator = ServiceLocator()
        service_locator.register('IUserRepository', UserRepository())

        user_application_service = UserApplicationService(service_locator)
        retult = user_application_service.get('111-222-333')


if __name__ == '__main__':
    program = Program()
    # 検索対象テーブルが存在しないため、エラーとなる
    program.main()