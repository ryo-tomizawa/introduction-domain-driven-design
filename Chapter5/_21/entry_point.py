from ef_user_repository import EFUserRepository
from mydb_context import MyDbContext
from program import Program
from user_service import UserService

class EntryPoint:
    def main(self):
        context = MyDbContext()
        user_repository = EFUserRepository(context)
        program = Program(user_repository)
        program.create_user('tanaka')

        # データを取り出して確認
        head = context.users().first()
        return head.name == 'tanaka'
    

if __name__ == '__main__':
    entry_point = EntryPoint()
    result = entry_point.main()
    print(result)