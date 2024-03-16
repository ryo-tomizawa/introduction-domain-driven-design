from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from user_data_model import UserDataModel

class MyDbContext:
    def __init__(self):
        self.engine = create_engine('sqlite:///example.db', echo=True)
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create(self):
        return self

    def users(self):
        return self.session.query(UserDataModel)


if __name__ == '__main__':
    # MyDbContextをインスタンス化
    context = MyDbContext()

    # テストデータをセットアップ
    user1 = UserDataModel(id='11-22-33', name='tanaka taro')
    user2 = UserDataModel(id='000-999-888', name='john smith')
    context.session.add(user1)
    context.session.add(user2)
    context.session.commit()

    # Usersテーブルからデータを取得
    users = context.users().all()
    for user in users:
        print(user.id, user.name)