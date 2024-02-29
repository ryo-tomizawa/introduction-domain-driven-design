from inmemory_user_repository import InMemoryUserRepository
from user import User
from user_name import UserName

class Program:
    def main(self):
        user_repository = InMemoryUserRepository()


        # 本来存在しないテストデータ作成フェイズ 開始
        # テストデータ作成
        user1 = User("Tanaka", 1)
        user2 = User("Sato", 2)

        # ユーザーを保存
        user_repository.save(user1)
        user_repository.save(user2)
        # 本来存在しないテストデータ作成フェイズ 終了

        user = user_repository.find('Tanaka')
        print(f'before name value:{user.name}')

        # ここでインスタンスをそのままリポジトリに保存してしまうと
        user_repository.save(user)

        # インスタンスの操作がリポジトリに保存したインスタンスにまで影響する
        user.change_name(UserName('tanaka'))
        print(f'after name value:{user.name.value}')


if __name__ == '__main__':
    # main処理実行
    program = Program()
    program.main()