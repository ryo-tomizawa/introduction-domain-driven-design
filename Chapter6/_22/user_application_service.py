from can_not_register_user_exception import CanNotRegisterUserException
from iuser_repository import IUserRepository
from mail_address import MailAddress
from user_data import UserData
from user_delete_command import UserDeleteCommand
from user_id import UserId
from user_service import UserService
from user_not_found_exception import UserNotFoundException
from user_name import UserName
from user_update_command import UserUpdateCommand
from user import User

class UserApplicationService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def register(self, name: str) -> None:
        user_name = UserName(name)

        # 重複確認を行うコード
        duplicated_user = self.user_repository.find(user_name)
        if duplicated_user is not None:
            raise CanNotRegisterUserException(user_name, 'ユーザは既に存在しています。')
        
        user = User(None, user_name)

        self.user_repository.save(user)

    def get(self, user_id: str) -> UserData:
        target_id = UserId(user_id)
        user = self.user_repository.find(target_id)
        if user is None: return None

        user_data = UserData(user.id.value, user.name.value)
        return user_data

    def update(self, command: UserUpdateCommand) -> None:
        target_id = UserId(command.id)
        user = self.user_repository.find(target_id)
        if user is None: raise UserNotFoundException(target_id)

        name = command.name
        if name is not None:
            new_user_name = UserName(name)
            # 重複確認を行うコード
            duplicated_user = self.user_repository.find(new_user_name)
            if duplicated_user is not None:
                raise CanNotRegisterUserException(new_user_name, 'ユーザは既に存在しています。')
            user.change_name(new_user_name)

        mail_address = command.mail_address
        if mail_address is not None:
            new_mail_address = MailAddress(mail_address)
            user.change_mail_address(new_mail_address)

        self.user_repository.save(user)

    def delete(self, command: UserDeleteCommand):
        target_id = UserId(command.id)
        user = self.user_repository.find(target_id)

        # 対象が見つからなかったため退会成功とする
        if user is None: return

        self.user_repository.delete(user)


if __name__ == '__main__':
    # モックオブジェクトやスタブの作成
    class MockUserRepository(IUserRepository):
        def __init__(self):
            self.store = {}

        def find(self, id: UserId):
            try:
                target = self.store[id.value]
                return self.clone(target)
            except KeyError:
                return None
            
        def find_by_user_name(self, name: UserName):
            for elem in self.store.values():
                if elem.name.value == name.value:
                    return self.clone(elem)
            return None

        def save(self, user: User):
            self.store[user.id.value] = self.clone(user)

        def delete(self, user: User):
            if user.id.value in self.store:
                del self.store[user.id.value]

        def clone(self, user: User):
            return User(user.id, user.name)

    class MockUserService(UserService):
        def exists(self, user: User) -> bool:
            # ここでは常にFalseを返すことで、どんなユーザーも存在しないとする
            # Trueにすることで、エラーパターンのテストも可能
            return False

    user_repository = MockUserRepository()
    user_service = MockUserService(user_repository)
    user_application_service = UserApplicationService(user_repository)

    # ユーザー登録のテスト
    user_name_a = 'tanaka taro'
    user_application_service.register(user_name_a)
    print(f"{user_name_a} の登録が完了しました。")

    user_id_b = '222-333-444'
    user_name_b = 'kato taro'
    user_b = User(UserId(user_id_b), UserName(user_name_b))
    user_repository.save(user_b)
    print(f"{user_name_b} の登録が完了しました。")

    print('*'*100)

    get_user_data = user_application_service.get('222-333-444')
    print(get_user_data.id, get_user_data.name)

    print('*'*100)

    command = UserUpdateCommand('222-333-444')
    command.name = 'john doe'
    command.mail_address = 'test@example.com'
    user_application_service.update(command)
    print(f"ID:{command.id}のユーザ名を{command.name}に、メールアドレスを{command.mail_address}に更新が完了しました。")

    print('*'*100)

    delete_command = UserDeleteCommand('222-333-444')
    user_application_service.delete(delete_command)
    print(f"ID:{delete_command.id}の削除が完了しました。")