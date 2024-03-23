import injector

from inmemory_user_repository import InMemoryUserRepository
from user_application_service import UserApplicationService


class Configration(injector.Module):
    def configure(self, binder):
        binder.bind(UserApplicationService, to=injector.InstanceProvider(UserApplicationService(InMemoryUserRepository())))

class Program:
    @injector.inject
    def main(self, user_application_service: UserApplicationService):
        pass

if __name__ == '__main__':
    injector_instance = injector.Injector(Configration)
    program = injector_instance.get(Program)
    user_application_service = injector_instance.get(UserApplicationService)
    program.main(user_application_service)