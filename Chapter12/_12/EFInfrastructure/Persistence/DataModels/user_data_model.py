import os
import sys

current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(base_dir)

from base import Base
from sqlalchemy import Column, String


class UserDataModel(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)


if __name__ == '__main__':
    user_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Users'))
    sys.path.append(user_dir)
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

    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    user_data_model_instance = UserDataModel(id=user_id.value, name=user_name.value)
    session.add(user_data_model_instance)
    session.commit()

    # ユーザーデータをクエリしてみる
    user = session.query(UserDataModel).filter_by(id='111-222-333').first()
    print(f'Queried user: ID={user.id}, Name={user.name}')

    # セッションを閉じる
    session.close()