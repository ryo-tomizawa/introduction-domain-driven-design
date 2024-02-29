from inmemory_user_repository import InMemoryUserRepository
from program import Program

class EntryPoint:
    def main(self):
        user_repository = InMemoryUserRepository()
        program = Program(user_repository)
        program.create_user('tanaka')

        # データを取り出して確認
        heads = user_repository.store.values()
        for head in heads:
            print(head.name.value)


if __name__ == '__main__':
    entry_point = EntryPoint()
    entry_point.main() 