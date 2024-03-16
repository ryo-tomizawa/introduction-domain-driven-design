from mydb_context import MyDbContext
from user_data_model import UserDataModel
from user_id import UserId
from user_name import UserName
from user import User

class EFUserRepository:
    def __init__(self, context: MyDbContext):
        self.context = context

    def find(self, name: str):
        target = self.context.session.query(UserDataModel).filter(UserDataModel.name == name).first()
        if target is None:
            return None
        return self.to_model(target)

    def save(self, user: User):
        found = self.context.session.query(UserDataModel).get(user.id.value)

        if found is None:
            data = self.to_data_model(user)
            self.context.session.add(data)
        else:
            # SQLAlchemy は変更を追跡し、コミット時にデータベースに反映してくれる
            found.id = user.id.value
            found.name = user.name.value

        self.context.session.commit()

    def to_model(self, from_data):
        return User(UserId(from_data.id), UserName(from_data.name))

    def to_data_model(self, from_user: User):
        return UserDataModel(id=from_user.id.value, name=from_user.name.value)
    

if __name__ == '__main__':
    mydb_context = MyDbContext()
    ef_user_repository = EFUserRepository(mydb_context)

    # テストデータをセットアップ
    user1 = UserDataModel(id='11-22-33', name='tanaka taro')
    user2 = UserDataModel(id='000-999-888', name='john smith')
    mydb_context.session.add(user1)
    mydb_context.session.add(user2)
    mydb_context.session.commit()

    # name='tanaka taro'のレコードが登録されていることを確認
    find_user = ef_user_repository.find('tanaka taro')
    print(find_user.id.value, find_user.name.value)

    # user1と同一idで、異なった名前を登録する
    user3 = User(UserId('11-22-33'), UserName('kato taro'))
    ef_user_repository.save(user3)

    print('*'*100)
    # user_1の情報が取得できないことを確認する
    # user_3の情報が取得できることを確認する
    missing_user = ef_user_repository.find('tanaka taro')
    print(f'missing_userデータ型：{type(missing_user)}')
    print('*'*100)
    
    find_user = ef_user_repository.find('kato taro')
    print(find_user.id.value, find_user.name.value)