from ifoo_repository import IFooRepository
from inmemory_user_repository import InMemoryUserRepository
from user_application_service import UserApplicationService

class Program:
    def main(self):
        user_repository = InMemoryUserRepository()
        # 第2引数にIFooRepositoryの実体が渡されていないためコンパイルエラーとなる
        # user_application_service = UserApplicationService(user_repository)

        # 正しいのはこちら
        foo_repository = IFooRepository()
        user_application_service = UserApplicationService(user_repository, foo_repository)


if __name__ == '__main__':
    program = Program()
    # 具体的な処理は特に実装されてないため、何も帰ってこない
    program.main()