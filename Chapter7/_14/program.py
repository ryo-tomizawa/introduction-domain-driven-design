from inmemory_user_repository import InMemoryUserRepository
from user_application_service import UserApplicationService

class Program:
    def main(self):
        user_repository = InMemoryUserRepository()
        user_application_service = UserApplicationService(user_repository)


if __name__ == '__main__':
    program = Program()
    # 具体的な処理は特に実装されてないため、何も帰ってこない
    program.main()