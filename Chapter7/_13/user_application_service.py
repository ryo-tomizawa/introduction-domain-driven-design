
from service_locator import ServiceLocator
from user_data import UserData
from user_id import UserId

class UserApplicationService:
    def __init__(self, service_locator: ServiceLocator) -> None:
        self.user_repository = service_locator.resolve('IUserRepository')
        self.foo_repository = service_locator.resolve('IFooRepository')

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data
    

if __name__ == '__main__':
    from inmemory_user_repository import InMemoryUserRepository
    from ifoo_repository import IFooRepository

    service_locator = ServiceLocator()
    service_locator.register('IUserRepository', InMemoryUserRepository())
    service_locator.register('IFooRepository', IFooRepository())

    user_application_service = UserApplicationService(service_locator)

    # 事前にレコードの登録がないので、取得内容はNone
    get_user = user_application_service.get('111-222-333')