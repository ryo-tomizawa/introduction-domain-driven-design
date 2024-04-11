from typing import List
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
import sys

current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '../'))
user_data_dir = os.path.abspath(os.path.join(current_dir, '../Persistence/DataModels'))
sys.path.append(base_dir)
sys.path.append(user_data_dir)

from base import Base
from user_data_model import UserDataModel

class MyDbContext():
    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_user(self, user: UserDataModel):
        self.session.add(user)
        self.session.commit()

    def get_users(self) -> List:
        return self.session.query(UserDataModel).all()


if __name__ == '__main__':
    user_dir = os.path.abspath(os.path.join(current_dir, '../../SnsDomain/Models/Users'))
    sys.path.append(user_dir)
    from user_id import UserId
    from user_name import UserName

    context = MyDbContext()

    user1 = UserDataModel(id = '111-222-333', name = 'tanaka taro')
    user2 = UserDataModel(id = '222-333-444', name = 'john smith')

    context.add_user(user1)
    context.add_user(user2)

    context.session.commit()

    # Usersテーブルからデータを取得
    users = context.get_users()
    for user in users:
        print(user.id, user.name)