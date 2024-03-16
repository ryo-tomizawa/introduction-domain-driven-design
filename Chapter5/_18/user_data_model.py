from sqlalchemy import Column, String

from base import Base

class UserDataModel(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    # sqlalchemyで文字数制約はできないため、データベース側の制約で設定する必要がある
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)



if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from user_data_model import Base

    # SQLiteメモリデータベースを使用するエンジンを作成
    engine = create_engine('sqlite:///:memory:', echo=True)

    # データのクリーンナップ
    Base.metadata.drop_all(engine)

    # テーブルを作成
    Base.metadata.create_all(engine)

    # セッションを作成
    Session = sessionmaker(bind=engine)
    session = Session()

    # ユーザーデータを追加してみる
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    # Userクラスのインスタンスはなく、ORMマッピングをするためUserDataModelクラスのインスタンスを作成する
    user_data_model_instance = UserDataModel(id=user_id.value, name=user_name.value)
    session.add(user_data_model_instance)
    session.commit()

    # ユーザーデータをクエリしてみる
    user = session.query(UserDataModel).filter_by(id='111-222-333').first()
    print(f'Queried user: ID={user.id}, Name={user.name}')

    # セッションを閉じる
    session.close()