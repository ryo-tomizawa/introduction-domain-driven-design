from service_locator import ServiceLocator
from user_data import UserData
from user_id import UserId

class UserApplicationService:
    def __init__(self, service_locator: ServiceLocator) -> None:
        self.user_repository = service_locator.resolve('IUserRepository')

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user)
        return user_data
    

if __name__ == '__main__':
    from iuser_repository import IUserRepository

    service_locator = ServiceLocator()
    service_locator.register('IUserRepository', IUserRepository())

    user_application_service = UserApplicationService(service_locator)

    # IuserRepositoryに具体的な処理は何も記載がないため、何も帰ってこない
    get_user = user_application_service.get('111-222-333')